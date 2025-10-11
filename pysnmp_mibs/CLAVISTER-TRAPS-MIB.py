# SNMP MIB module (CLAVISTER-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/clavister/CLAVISTER-TRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:17:15 2025
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

(clavisterOSTrap,
 clavisterOSTrapInfo) = mibBuilder.importSymbols(
    "CLAVISTER-SMI",
    "clavisterOSTrap",
    "clavisterOSTrapInfo")

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

clavisterOSTrapMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 0)
)
if mibBuilder.loadTexts:
    clavisterOSTrapMibModule.setRevisions(
        ("2015-10-21 17:00",
         "2007-10-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ClavisterOSTrapVarSeverity_Type(Integer32):
    """Custom type clavisterOSTrapVarSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_ClavisterOSTrapVarSeverity_Type.__name__ = "Integer32"
_ClavisterOSTrapVarSeverity_Object = MibScalar
clavisterOSTrapVarSeverity = _ClavisterOSTrapVarSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 4),
    _ClavisterOSTrapVarSeverity_Type()
)
clavisterOSTrapVarSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarSeverity.setStatus("current")
_ClavisterOSTrapVarCategory_Type = DisplayString
_ClavisterOSTrapVarCategory_Object = MibScalar
clavisterOSTrapVarCategory = _ClavisterOSTrapVarCategory_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 5),
    _ClavisterOSTrapVarCategory_Type()
)
clavisterOSTrapVarCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarCategory.setStatus("current")
_ClavisterOSTrapVarID_Type = DisplayString
_ClavisterOSTrapVarID_Object = MibScalar
clavisterOSTrapVarID = _ClavisterOSTrapVarID_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 6),
    _ClavisterOSTrapVarID_Type()
)
clavisterOSTrapVarID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarID.setStatus("current")
_ClavisterOSTrapVarEvent_Type = DisplayString
_ClavisterOSTrapVarEvent_Object = MibScalar
clavisterOSTrapVarEvent = _ClavisterOSTrapVarEvent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 7),
    _ClavisterOSTrapVarEvent_Type()
)
clavisterOSTrapVarEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarEvent.setStatus("current")
_ClavisterOSTrapVarAction_Type = DisplayString
_ClavisterOSTrapVarAction_Object = MibScalar
clavisterOSTrapVarAction = _ClavisterOSTrapVarAction_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 8),
    _ClavisterOSTrapVarAction_Type()
)
clavisterOSTrapVarAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarAction.setStatus("current")
_ClavisterOSTrapVarTime_Type = DisplayString
_ClavisterOSTrapVarTime_Object = MibScalar
clavisterOSTrapVarTime = _ClavisterOSTrapVarTime_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 9),
    _ClavisterOSTrapVarTime_Type()
)
clavisterOSTrapVarTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarTime.setStatus("current")
_ClavisterOSTrapVarMessage_Type = DisplayString
_ClavisterOSTrapVarMessage_Object = MibScalar
clavisterOSTrapVarMessage = _ClavisterOSTrapVarMessage_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 10),
    _ClavisterOSTrapVarMessage_Type()
)
clavisterOSTrapVarMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarMessage.setStatus("current")

# Managed Objects groups

clavisterOSTrapGroupVar = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 2)
)
clavisterOSTrapGroupVar.setObjects(
      *(("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarSeverity"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarCategory"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarID"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarEvent"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarAction"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarTime"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarMessage"))
)
if mibBuilder.loadTexts:
    clavisterOSTrapGroupVar.setStatus("current")


# Notification objects

clavisterOSGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5089, 1, 0, 1)
)
clavisterOSGenericTrap.setObjects(
      *(("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarSeverity"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarCategory"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarID"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarEvent"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarAction"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarTime"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarMessage"))
)
if mibBuilder.loadTexts:
    clavisterOSGenericTrap.setStatus(
        "current"
    )


# Notifications groups

clavisterOSTrapGroupTrap = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 1)
)
clavisterOSTrapGroupTrap.setObjects(
    ("CLAVISTER-TRAPS-MIB", "clavisterOSGenericTrap")
)
if mibBuilder.loadTexts:
    clavisterOSTrapGroupTrap.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

clavisterOSTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 3)
)
clavisterOSTrapCompliance.setObjects(
      *(("CLAVISTER-TRAPS-MIB", "clavisterOSTrapGroupTrap"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapGroupVar"))
)
if mibBuilder.loadTexts:
    clavisterOSTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAVISTER-TRAPS-MIB",
    **{"clavisterOSGenericTrap": clavisterOSGenericTrap,
       "clavisterOSTrapMibModule": clavisterOSTrapMibModule,
       "clavisterOSTrapGroupTrap": clavisterOSTrapGroupTrap,
       "clavisterOSTrapGroupVar": clavisterOSTrapGroupVar,
       "clavisterOSTrapCompliance": clavisterOSTrapCompliance,
       "clavisterOSTrapVarSeverity": clavisterOSTrapVarSeverity,
       "clavisterOSTrapVarCategory": clavisterOSTrapVarCategory,
       "clavisterOSTrapVarID": clavisterOSTrapVarID,
       "clavisterOSTrapVarEvent": clavisterOSTrapVarEvent,
       "clavisterOSTrapVarAction": clavisterOSTrapVarAction,
       "clavisterOSTrapVarTime": clavisterOSTrapVarTime,
       "clavisterOSTrapVarMessage": clavisterOSTrapVarMessage}
)
