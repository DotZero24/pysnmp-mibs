# SNMP MIB module (TPLINK-GVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-GVRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:56:33 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkGvrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20)
)
if mibBuilder.loadTexts:
    tplinkGvrpMIB.setRevisions(
        ("2012-12-06 09:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkGvrpMIBObjects_ObjectIdentity = ObjectIdentity
tplinkGvrpMIBObjects = _TplinkGvrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1)
)
_TpGvrpGlobalConfig_ObjectIdentity = ObjectIdentity
tpGvrpGlobalConfig = _TpGvrpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 1)
)


class _TpGvrpGlobalEnable_Type(Integer32):
    """Custom type tpGvrpGlobalEnable based on Integer32"""
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


_TpGvrpGlobalEnable_Type.__name__ = "Integer32"
_TpGvrpGlobalEnable_Object = MibScalar
tpGvrpGlobalEnable = _TpGvrpGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 1, 1),
    _TpGvrpGlobalEnable_Type()
)
tpGvrpGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpGvrpGlobalEnable.setStatus("current")
_TpGvrpPortConfig_ObjectIdentity = ObjectIdentity
tpGvrpPortConfig = _TpGvrpPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2)
)
_TpGvrpPortTable_Object = MibTable
tpGvrpPortTable = _TpGvrpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpGvrpPortTable.setStatus("current")
_TpGvrpPortEntry_Object = MibTableRow
tpGvrpPortEntry = _TpGvrpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1)
)
tpGvrpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpGvrpPortEntry.setStatus("current")


class _TpGvrpPortNumber_Type(OctetString):
    """Custom type tpGvrpPortNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpGvrpPortNumber_Type.__name__ = "OctetString"
_TpGvrpPortNumber_Object = MibTableColumn
tpGvrpPortNumber = _TpGvrpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 1),
    _TpGvrpPortNumber_Type()
)
tpGvrpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpGvrpPortNumber.setStatus("current")


class _TpGvrpPortEnable_Type(Integer32):
    """Custom type tpGvrpPortEnable based on Integer32"""
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


_TpGvrpPortEnable_Type.__name__ = "Integer32"
_TpGvrpPortEnable_Object = MibTableColumn
tpGvrpPortEnable = _TpGvrpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 2),
    _TpGvrpPortEnable_Type()
)
tpGvrpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpGvrpPortEnable.setStatus("current")


class _TpGvrpPortRegistration_Type(Integer32):
    """Custom type tpGvrpPortRegistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("fixed", 1),
          ("forbidden", 2))
    )


_TpGvrpPortRegistration_Type.__name__ = "Integer32"
_TpGvrpPortRegistration_Object = MibTableColumn
tpGvrpPortRegistration = _TpGvrpPortRegistration_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 3),
    _TpGvrpPortRegistration_Type()
)
tpGvrpPortRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpGvrpPortRegistration.setStatus("current")


class _TpGvrpLeaveAllTimer_Type(Integer32):
    """Custom type tpGvrpLeaveAllTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 30000),
    )


_TpGvrpLeaveAllTimer_Type.__name__ = "Integer32"
_TpGvrpLeaveAllTimer_Object = MibTableColumn
tpGvrpLeaveAllTimer = _TpGvrpLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 4),
    _TpGvrpLeaveAllTimer_Type()
)
tpGvrpLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpGvrpLeaveAllTimer.setStatus("current")


class _TpGvrpJoinTimer_Type(Integer32):
    """Custom type tpGvrpJoinTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_TpGvrpJoinTimer_Type.__name__ = "Integer32"
_TpGvrpJoinTimer_Object = MibTableColumn
tpGvrpJoinTimer = _TpGvrpJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 5),
    _TpGvrpJoinTimer_Type()
)
tpGvrpJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpGvrpJoinTimer.setStatus("current")


class _TpGvrpLeaveTimer_Type(Integer32):
    """Custom type tpGvrpLeaveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3000),
    )


_TpGvrpLeaveTimer_Type.__name__ = "Integer32"
_TpGvrpLeaveTimer_Object = MibTableColumn
tpGvrpLeaveTimer = _TpGvrpLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 6),
    _TpGvrpLeaveTimer_Type()
)
tpGvrpLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpGvrpLeaveTimer.setStatus("current")


class _TpGvrpPortLag_Type(OctetString):
    """Custom type tpGvrpPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpGvrpPortLag_Type.__name__ = "OctetString"
_TpGvrpPortLag_Object = MibTableColumn
tpGvrpPortLag = _TpGvrpPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 7),
    _TpGvrpPortLag_Type()
)
tpGvrpPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpGvrpPortLag.setStatus("current")
_TplinkGvrpNotifications_ObjectIdentity = ObjectIdentity
tplinkGvrpNotifications = _TplinkGvrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 20, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-GVRP-MIB",
    **{"tplinkGvrpMIB": tplinkGvrpMIB,
       "tplinkGvrpMIBObjects": tplinkGvrpMIBObjects,
       "tpGvrpGlobalConfig": tpGvrpGlobalConfig,
       "tpGvrpGlobalEnable": tpGvrpGlobalEnable,
       "tpGvrpPortConfig": tpGvrpPortConfig,
       "tpGvrpPortTable": tpGvrpPortTable,
       "tpGvrpPortEntry": tpGvrpPortEntry,
       "tpGvrpPortNumber": tpGvrpPortNumber,
       "tpGvrpPortEnable": tpGvrpPortEnable,
       "tpGvrpPortRegistration": tpGvrpPortRegistration,
       "tpGvrpLeaveAllTimer": tpGvrpLeaveAllTimer,
       "tpGvrpJoinTimer": tpGvrpJoinTimer,
       "tpGvrpLeaveTimer": tpGvrpLeaveTimer,
       "tpGvrpPortLag": tpGvrpPortLag,
       "tplinkGvrpNotifications": tplinkGvrpNotifications}
)
