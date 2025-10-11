# SNMP MIB module (NEWTEC-ALARMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-ALARMS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:18 2025
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

ntcAlarms = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600)
)
if mibBuilder.loadTexts:
    ntcAlarms.setRevisions(
        ("2013-09-20 10:00",
         "2013-09-20 08:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcAlmsObjects_ObjectIdentity = ObjectIdentity
ntcAlmsObjects = _NtcAlmsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1)
)
if mibBuilder.loadTexts:
    ntcAlmsObjects.setStatus("current")
_NtcAlmsConfigTable_Object = MibTable
ntcAlmsConfigTable = _NtcAlmsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1, 1)
)
if mibBuilder.loadTexts:
    ntcAlmsConfigTable.setStatus("current")
_NtcAlmsConfigEntry_Object = MibTableRow
ntcAlmsConfigEntry = _NtcAlmsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1, 1, 1)
)
ntcAlmsConfigEntry.setIndexNames(
    (0, "NEWTEC-ALARMS-MIB", "ntcAlmsConfigName"),
)
if mibBuilder.loadTexts:
    ntcAlmsConfigEntry.setStatus("current")


class _NtcAlmsConfigName_Type(DisplayString):
    """Custom type ntcAlmsConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcAlmsConfigName_Type.__name__ = "DisplayString"
_NtcAlmsConfigName_Object = MibTableColumn
ntcAlmsConfigName = _NtcAlmsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1, 1, 1, 1),
    _NtcAlmsConfigName_Type()
)
ntcAlmsConfigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAlmsConfigName.setStatus("current")


class _NtcAlmsConfigMask_Type(Integer32):
    """Custom type ntcAlmsConfigMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcAlmsConfigMask_Type.__name__ = "Integer32"
_NtcAlmsConfigMask_Object = MibTableColumn
ntcAlmsConfigMask = _NtcAlmsConfigMask_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1, 1, 1, 2),
    _NtcAlmsConfigMask_Type()
)
ntcAlmsConfigMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAlmsConfigMask.setStatus("current")


class _NtcAlmsConfigGeneralInterface_Type(Integer32):
    """Custom type ntcAlmsConfigGeneralInterface based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcAlmsConfigGeneralInterface_Type.__name__ = "Integer32"
_NtcAlmsConfigGeneralInterface_Object = MibTableColumn
ntcAlmsConfigGeneralInterface = _NtcAlmsConfigGeneralInterface_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1, 1, 1, 3),
    _NtcAlmsConfigGeneralInterface_Type()
)
ntcAlmsConfigGeneralInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAlmsConfigGeneralInterface.setStatus("current")


class _NtcAlmsConfigGeneralDevice_Type(Integer32):
    """Custom type ntcAlmsConfigGeneralDevice based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcAlmsConfigGeneralDevice_Type.__name__ = "Integer32"
_NtcAlmsConfigGeneralDevice_Object = MibTableColumn
ntcAlmsConfigGeneralDevice = _NtcAlmsConfigGeneralDevice_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 1, 1, 1, 4),
    _NtcAlmsConfigGeneralDevice_Type()
)
ntcAlmsConfigGeneralDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAlmsConfigGeneralDevice.setStatus("current")
_NtcAlmsConformance_ObjectIdentity = ObjectIdentity
ntcAlmsConformance = _NtcAlmsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 2)
)
if mibBuilder.loadTexts:
    ntcAlmsConformance.setStatus("current")
_NtcAlmsConfCompliance_ObjectIdentity = ObjectIdentity
ntcAlmsConfCompliance = _NtcAlmsConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 2, 1)
)
if mibBuilder.loadTexts:
    ntcAlmsConfCompliance.setStatus("current")
_NtcAlmsConfGroup_ObjectIdentity = ObjectIdentity
ntcAlmsConfGroup = _NtcAlmsConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 2, 2)
)
if mibBuilder.loadTexts:
    ntcAlmsConfGroup.setStatus("current")

# Managed Objects groups

ntcAlmsConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 2, 2, 1)
)
ntcAlmsConfGrpV1Standard.setObjects(
      *(("NEWTEC-ALARMS-MIB", "ntcAlmsConfigMask"),
        ("NEWTEC-ALARMS-MIB", "ntcAlmsConfigGeneralInterface"),
        ("NEWTEC-ALARMS-MIB", "ntcAlmsConfigGeneralDevice"))
)
if mibBuilder.loadTexts:
    ntcAlmsConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcAlmsConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5600, 2, 1, 1)
)
ntcAlmsConfCompV1Standard.setObjects(
    ("NEWTEC-ALARMS-MIB", "ntcAlmsConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcAlmsConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-ALARMS-MIB",
    **{"ntcAlarms": ntcAlarms,
       "ntcAlmsObjects": ntcAlmsObjects,
       "ntcAlmsConfigTable": ntcAlmsConfigTable,
       "ntcAlmsConfigEntry": ntcAlmsConfigEntry,
       "ntcAlmsConfigName": ntcAlmsConfigName,
       "ntcAlmsConfigMask": ntcAlmsConfigMask,
       "ntcAlmsConfigGeneralInterface": ntcAlmsConfigGeneralInterface,
       "ntcAlmsConfigGeneralDevice": ntcAlmsConfigGeneralDevice,
       "ntcAlmsConformance": ntcAlmsConformance,
       "ntcAlmsConfCompliance": ntcAlmsConfCompliance,
       "ntcAlmsConfCompV1Standard": ntcAlmsConfCompV1Standard,
       "ntcAlmsConfGroup": ntcAlmsConfGroup,
       "ntcAlmsConfGrpV1Standard": ntcAlmsConfGrpV1Standard}
)
