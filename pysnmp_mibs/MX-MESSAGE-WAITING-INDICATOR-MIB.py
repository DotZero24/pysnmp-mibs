# SNMP MIB module (MX-MESSAGE-WAITING-INDICATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-MESSAGE-WAITING-INDICATOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:26 2025
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

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxDigitMap,
 MxEnableState,
 MxSignalingAddress) = mibBuilder.importSymbols(
    "MX-TC",
    "MxDigitMap",
    "MxEnableState",
    "MxSignalingAddress")

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

messageWaitingIndicatorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100)
)
if mibBuilder.loadTexts:
    messageWaitingIndicatorMIB.setRevisions(
        ("2010-08-04 00:00",
         "1903-08-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwiMIBObjects_ObjectIdentity = ObjectIdentity
mwiMIBObjects = _MwiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 1)
)


class _MwiFetchDigitMap_Type(MxDigitMap):
    """Custom type mwiFetchDigitMap based on MxDigitMap"""
    defaultValue = OctetString("")


_MwiFetchDigitMap_Type.__name__ = "MxDigitMap"
_MwiFetchDigitMap_Object = MibScalar
mwiFetchDigitMap = _MwiFetchDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 10),
    _MwiFetchDigitMap_Type()
)
mwiFetchDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwiFetchDigitMap.setStatus("current")


class _MwiExpirationTime_Type(Unsigned32):
    """Custom type mwiExpirationTime based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 604800),
    )


_MwiExpirationTime_Type.__name__ = "Unsigned32"
_MwiExpirationTime_Object = MibScalar
mwiExpirationTime = _MwiExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 20),
    _MwiExpirationTime_Type()
)
mwiExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwiExpirationTime.setStatus("current")


class _MwiSubscriptionCmdRefresh_Type(Integer32):
    """Custom type mwiSubscriptionCmdRefresh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("refresh", 1))
    )


_MwiSubscriptionCmdRefresh_Type.__name__ = "Integer32"
_MwiSubscriptionCmdRefresh_Object = MibScalar
mwiSubscriptionCmdRefresh = _MwiSubscriptionCmdRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 30),
    _MwiSubscriptionCmdRefresh_Type()
)
mwiSubscriptionCmdRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwiSubscriptionCmdRefresh.setStatus("current")
_MwiIfConfigurationTable_Object = MibTable
mwiIfConfigurationTable = _MwiIfConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 40)
)
if mibBuilder.loadTexts:
    mwiIfConfigurationTable.setStatus("current")
_MwiIfConfigurationEntry_Object = MibTableRow
mwiIfConfigurationEntry = _MwiIfConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 40, 1)
)
mwiIfConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mwiIfConfigurationEntry.setStatus("current")


class _MwiConfigActivation_Type(MxEnableState):
    """Custom type mwiConfigActivation based on MxEnableState"""
    defaultValue = 0


_MwiConfigActivation_Type.__name__ = "MxEnableState"
_MwiConfigActivation_Object = MibTableColumn
mwiConfigActivation = _MwiConfigActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 40, 1, 5),
    _MwiConfigActivation_Type()
)
mwiConfigActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwiConfigActivation.setStatus("current")


class _MwiConfigUserSubscriptionAddress_Type(MxSignalingAddress):
    """Custom type mwiConfigUserSubscriptionAddress based on MxSignalingAddress"""
    defaultValue = OctetString("")


_MwiConfigUserSubscriptionAddress_Type.__name__ = "MxSignalingAddress"
_MwiConfigUserSubscriptionAddress_Object = MibTableColumn
mwiConfigUserSubscriptionAddress = _MwiConfigUserSubscriptionAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 40, 1, 10),
    _MwiConfigUserSubscriptionAddress_Type()
)
mwiConfigUserSubscriptionAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwiConfigUserSubscriptionAddress.setStatus("current")


class _MwiConfigFetchAddress_Type(MxSignalingAddress):
    """Custom type mwiConfigFetchAddress based on MxSignalingAddress"""
    defaultValue = OctetString("")


_MwiConfigFetchAddress_Type.__name__ = "MxSignalingAddress"
_MwiConfigFetchAddress_Object = MibTableColumn
mwiConfigFetchAddress = _MwiConfigFetchAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 40, 1, 15),
    _MwiConfigFetchAddress_Type()
)
mwiConfigFetchAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwiConfigFetchAddress.setStatus("current")


class _MwiConfigVoltageEnable_Type(MxEnableState):
    """Custom type mwiConfigVoltageEnable based on MxEnableState"""
    defaultValue = 0


_MwiConfigVoltageEnable_Type.__name__ = "MxEnableState"
_MwiConfigVoltageEnable_Object = MibScalar
mwiConfigVoltageEnable = _MwiConfigVoltageEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 40, 1, 20),
    _MwiConfigVoltageEnable_Type()
)
mwiConfigVoltageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwiConfigVoltageEnable.setStatus("current")
_MwiConformance_ObjectIdentity = ObjectIdentity
mwiConformance = _MwiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 10)
)
_MwiCompliances_ObjectIdentity = ObjectIdentity
mwiCompliances = _MwiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 10, 1)
)
_MwiGroups_ObjectIdentity = ObjectIdentity
mwiGroups = _MwiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 10, 5)
)

# Managed Objects groups

mwiIfConfigVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 10, 5, 3)
)
mwiIfConfigVer1.setObjects(
      *(("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiConfigActivation"),
        ("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiConfigUserSubscriptionAddress"),
        ("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiConfigFetchAddress"))
)
if mibBuilder.loadTexts:
    mwiIfConfigVer1.setStatus("current")

mwiConfigVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 10, 5, 6)
)
mwiConfigVer1.setObjects(
      *(("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiFetchDigitMap"),
        ("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiExpirationTime"))
)
if mibBuilder.loadTexts:
    mwiConfigVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mwiComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 100, 10, 1, 1)
)
mwiComplVer1.setObjects(
      *(("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiIfConfigVer1"),
        ("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiConfigVer1"))
)
if mibBuilder.loadTexts:
    mwiComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-MESSAGE-WAITING-INDICATOR-MIB",
    **{"messageWaitingIndicatorMIB": messageWaitingIndicatorMIB,
       "mwiMIBObjects": mwiMIBObjects,
       "mwiFetchDigitMap": mwiFetchDigitMap,
       "mwiExpirationTime": mwiExpirationTime,
       "mwiSubscriptionCmdRefresh": mwiSubscriptionCmdRefresh,
       "mwiIfConfigurationTable": mwiIfConfigurationTable,
       "mwiIfConfigurationEntry": mwiIfConfigurationEntry,
       "mwiConfigActivation": mwiConfigActivation,
       "mwiConfigUserSubscriptionAddress": mwiConfigUserSubscriptionAddress,
       "mwiConfigFetchAddress": mwiConfigFetchAddress,
       "mwiConfigVoltageEnable": mwiConfigVoltageEnable,
       "mwiConformance": mwiConformance,
       "mwiCompliances": mwiCompliances,
       "mwiComplVer1": mwiComplVer1,
       "mwiGroups": mwiGroups,
       "mwiIfConfigVer1": mwiIfConfigVer1,
       "mwiConfigVer1": mwiConfigVer1}
)
