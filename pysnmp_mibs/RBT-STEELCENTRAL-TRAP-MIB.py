# SNMP MIB module (RBT-STEELCENTRAL-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/riverbed/RBT-STEELCENTRAL-TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:16:12 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(products,
 rbtTrap,
 rbtTrapInfo) = mibBuilder.importSymbols(
    "RBT-MIB",
    "products",
    "rbtTrap",
    "rbtTrapInfo")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

steelcentralTrapModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1)
)
if mibBuilder.loadTexts:
    steelcentralTrapModule.setRevisions(
        ("2016-04-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SteelcentralTraps_ObjectIdentity = ObjectIdentity
steelcentralTraps = _SteelcentralTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 1)
)
_SteelcentralTrapInfo_ObjectIdentity = ObjectIdentity
steelcentralTrapInfo = _SteelcentralTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2)
)


class _AlertSeverity_Type(Integer32):
    """Custom type alertSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlertSeverity_Type.__name__ = "Integer32"
_AlertSeverity_Object = MibScalar
alertSeverity = _AlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2, 1),
    _AlertSeverity_Type()
)
alertSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertSeverity.setStatus("current")


class _AlertSeverityLevel_Type(Integer32):
    """Custom type alertSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("minor", 1),
          ("major", 2),
          ("critical", 3))
    )


_AlertSeverityLevel_Type.__name__ = "Integer32"
_AlertSeverityLevel_Object = MibScalar
alertSeverityLevel = _AlertSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2, 2),
    _AlertSeverityLevel_Type()
)
alertSeverityLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertSeverityLevel.setStatus("current")
_AlertPolicyName_Type = OctetString
_AlertPolicyName_Object = MibScalar
alertPolicyName = _AlertPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2, 3),
    _AlertPolicyName_Type()
)
alertPolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertPolicyName.setStatus("current")
_AlertPolicyDescription_Type = OctetString
_AlertPolicyDescription_Object = MibScalar
alertPolicyDescription = _AlertPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2, 4),
    _AlertPolicyDescription_Type()
)
alertPolicyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertPolicyDescription.setStatus("current")
_AlertPolicyID_Type = Integer32
_AlertPolicyID_Object = MibScalar
alertPolicyID = _AlertPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2, 5),
    _AlertPolicyID_Type()
)
alertPolicyID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertPolicyID.setStatus("current")


class _AlertPolicyType_Type(Integer32):
    """Custom type alertPolicyType based on Integer32"""
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
        *(("traffic", 1),
          ("storage", 2),
          ("watch", 3),
          ("pcap", 4),
          ("autobaseline", 5))
    )


_AlertPolicyType_Type.__name__ = "Integer32"
_AlertPolicyType_Object = MibScalar
alertPolicyType = _AlertPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2, 6),
    _AlertPolicyType_Type()
)
alertPolicyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertPolicyType.setStatus("current")
_AlertPolicyEvalPeriod_Type = Integer32
_AlertPolicyEvalPeriod_Object = MibScalar
alertPolicyEvalPeriod = _AlertPolicyEvalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2, 7),
    _AlertPolicyEvalPeriod_Type()
)
alertPolicyEvalPeriod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertPolicyEvalPeriod.setStatus("current")
_AlertID_Type = Integer32
_AlertID_Object = MibScalar
alertID = _AlertID_Object(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2, 8),
    _AlertID_Type()
)
alertID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertID.setStatus("current")
_AlertStart_Type = OctetString
_AlertStart_Object = MibScalar
alertStart = _AlertStart_Object(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2, 9),
    _AlertStart_Type()
)
alertStart.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertStart.setStatus("current")
_AlertURL_Type = OctetString
_AlertURL_Object = MibScalar
alertURL = _AlertURL_Object(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2, 10),
    _AlertURL_Type()
)
alertURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertURL.setStatus("current")
_AlertInfoURL_Type = OctetString
_AlertInfoURL_Object = MibScalar
alertInfoURL = _AlertInfoURL_Object(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2, 11),
    _AlertInfoURL_Type()
)
alertInfoURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertInfoURL.setStatus("current")
_AlertMessage_Type = OctetString
_AlertMessage_Object = MibScalar
alertMessage = _AlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 2, 12),
    _AlertMessage_Type()
)
alertMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertMessage.setStatus("current")

# Managed Objects groups


# Notification objects

testTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    testTrap.setStatus(
        "current"
    )

policyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 1, 2)
)
policyTrap.setObjects(
      *(("RBT-STEELCENTRAL-TRAP-MIB", "alertSeverity"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertSeverityLevel"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertPolicyName"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertPolicyDescription"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertPolicyID"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertPolicyType"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertPolicyEvalPeriod"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertID"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertStart"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertURL"))
)
if mibBuilder.loadTexts:
    policyTrap.setStatus(
        "current"
    )

hardwareTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 2, 1, 1, 3)
)
hardwareTrap.setObjects(
      *(("RBT-STEELCENTRAL-TRAP-MIB", "alertSeverity"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertSeverityLevel"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertPolicyName"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertPolicyDescription"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertPolicyID"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertPolicyType"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertPolicyEvalPeriod"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertID"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertStart"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertURL"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertInfoURL"),
        ("RBT-STEELCENTRAL-TRAP-MIB", "alertMessage"))
)
if mibBuilder.loadTexts:
    hardwareTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBT-STEELCENTRAL-TRAP-MIB",
    **{"steelcentralTrapModule": steelcentralTrapModule,
       "steelcentralTraps": steelcentralTraps,
       "testTrap": testTrap,
       "policyTrap": policyTrap,
       "hardwareTrap": hardwareTrap,
       "steelcentralTrapInfo": steelcentralTrapInfo,
       "alertSeverity": alertSeverity,
       "alertSeverityLevel": alertSeverityLevel,
       "alertPolicyName": alertPolicyName,
       "alertPolicyDescription": alertPolicyDescription,
       "alertPolicyID": alertPolicyID,
       "alertPolicyType": alertPolicyType,
       "alertPolicyEvalPeriod": alertPolicyEvalPeriod,
       "alertID": alertID,
       "alertStart": alertStart,
       "alertURL": alertURL,
       "alertInfoURL": alertInfoURL,
       "alertMessage": alertMessage}
)
