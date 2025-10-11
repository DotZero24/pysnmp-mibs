# SNMP MIB module (DLINKPRIME-STP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-STP-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:31 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkPrimeStpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 18)
)
if mibBuilder.loadTexts:
    dlinkPrimeStpExtMIB.setRevisions(
        ("2014-06-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IEEE8021BridgePortNumber(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_DpStpExtMIBNotifications_ObjectIdentity = ObjectIdentity
dpStpExtMIBNotifications = _DpStpExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 0)
)
_DpStpExtMIBObjects_ObjectIdentity = ObjectIdentity
dpStpExtMIBObjects = _DpStpExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 1)
)
_DpStpExtGblMgmt_ObjectIdentity = ObjectIdentity
dpStpExtGblMgmt = _DpStpExtGblMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 1)
)
_DpStpExtStpGblStateEnabled_Type = TruthValue
_DpStpExtStpGblStateEnabled_Object = MibScalar
dpStpExtStpGblStateEnabled = _DpStpExtStpGblStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 1, 1),
    _DpStpExtStpGblStateEnabled_Type()
)
dpStpExtStpGblStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpStpExtStpGblStateEnabled.setStatus("current")


class _DpStpExtStpMode_Type(Integer32):
    """Custom type dpStpExtStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp", 1),
          ("rstp", 2))
    )


_DpStpExtStpMode_Type.__name__ = "Integer32"
_DpStpExtStpMode_Object = MibScalar
dpStpExtStpMode = _DpStpExtStpMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 1, 2),
    _DpStpExtStpMode_Type()
)
dpStpExtStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpStpExtStpMode.setStatus("current")


class _DpStpExtNotificationEnable_Type(Bits):
    """Custom type dpStpExtNotificationEnable based on Bits"""
    namedValues = NamedValues(
        *(("newRoot", 0),
          ("topologyChange", 1))
    )

_DpStpExtNotificationEnable_Type.__name__ = "Bits"
_DpStpExtNotificationEnable_Object = MibScalar
dpStpExtNotificationEnable = _DpStpExtNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 1, 3),
    _DpStpExtNotificationEnable_Type()
)
dpStpExtNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpStpExtNotificationEnable.setStatus("current")
_DpStpExtPortMgmt_ObjectIdentity = ObjectIdentity
dpStpExtPortMgmt = _DpStpExtPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 2)
)
_DpStpExtPortTable_Object = MibTable
dpStpExtPortTable = _DpStpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dpStpExtPortTable.setStatus("current")
_DpStpExtPortEntry_Object = MibTableRow
dpStpExtPortEntry = _DpStpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 2, 1, 1)
)
dpStpExtPortEntry.setIndexNames(
    (0, "DLINKPRIME-STP-EXT-MIB", "dpStpExtPortNumber"),
)
if mibBuilder.loadTexts:
    dpStpExtPortEntry.setStatus("current")
_DpStpExtPortNumber_Type = IEEE8021BridgePortNumber
_DpStpExtPortNumber_Object = MibTableColumn
dpStpExtPortNumber = _DpStpExtPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 2, 1, 1, 1),
    _DpStpExtPortNumber_Type()
)
dpStpExtPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpStpExtPortNumber.setStatus("current")


class _DpStpExtPortFast_Type(Integer32):
    """Custom type dpStpExtPortFast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("disabled", 2),
          ("edge", 3))
    )


_DpStpExtPortFast_Type.__name__ = "Integer32"
_DpStpExtPortFast_Object = MibTableColumn
dpStpExtPortFast = _DpStpExtPortFast_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 2, 1, 1, 2),
    _DpStpExtPortFast_Type()
)
dpStpExtPortFast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpStpExtPortFast.setStatus("current")


class _DpStpExtPortState_Type(Integer32):
    """Custom type dpStpExtPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("errDisabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6),
          ("nonStpForwarding", 7),
          ("nonStpOther", 8))
    )


_DpStpExtPortState_Type.__name__ = "Integer32"
_DpStpExtPortState_Object = MibTableColumn
dpStpExtPortState = _DpStpExtPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 2, 1, 1, 3),
    _DpStpExtPortState_Type()
)
dpStpExtPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpStpExtPortState.setStatus("current")
_DpStpExtMIBConformance_ObjectIdentity = ObjectIdentity
dpStpExtMIBConformance = _DpStpExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 2)
)
_DpStpExtMIBCompliances_ObjectIdentity = ObjectIdentity
dpStpExtMIBCompliances = _DpStpExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 2, 1)
)
_DpStpExtGroups_ObjectIdentity = ObjectIdentity
dpStpExtGroups = _DpStpExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 2, 1, 2)
)

# Managed Objects groups

dpStpExtBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 2, 1, 2, 1)
)
dpStpExtBasicGroup.setObjects(
      *(("DLINKPRIME-STP-EXT-MIB", "dpStpExtStpGblStateEnabled"),
        ("DLINKPRIME-STP-EXT-MIB", "dpStpExtPortState"),
        ("DLINKPRIME-STP-EXT-MIB", "dpStpExtNotificationEnable"))
)
if mibBuilder.loadTexts:
    dpStpExtBasicGroup.setStatus("current")

dpStpExtMstpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 2, 1, 2, 2)
)
dpStpExtMstpGroup.setObjects(
    ("DLINKPRIME-STP-EXT-MIB", "dpStpExtPortFast")
)
if mibBuilder.loadTexts:
    dpStpExtMstpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpStpExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 18, 2, 1, 1)
)
dpStpExtCompliance.setObjects(
      *(("DLINKPRIME-STP-EXT-MIB", "dpStpExtBasicGroup"),
        ("DLINKPRIME-STP-EXT-MIB", "dpStpExtMstpGroup"))
)
if mibBuilder.loadTexts:
    dpStpExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-STP-EXT-MIB",
    **{"IEEE8021BridgePortNumber": IEEE8021BridgePortNumber,
       "dlinkPrimeStpExtMIB": dlinkPrimeStpExtMIB,
       "dpStpExtMIBNotifications": dpStpExtMIBNotifications,
       "dpStpExtMIBObjects": dpStpExtMIBObjects,
       "dpStpExtGblMgmt": dpStpExtGblMgmt,
       "dpStpExtStpGblStateEnabled": dpStpExtStpGblStateEnabled,
       "dpStpExtStpMode": dpStpExtStpMode,
       "dpStpExtNotificationEnable": dpStpExtNotificationEnable,
       "dpStpExtPortMgmt": dpStpExtPortMgmt,
       "dpStpExtPortTable": dpStpExtPortTable,
       "dpStpExtPortEntry": dpStpExtPortEntry,
       "dpStpExtPortNumber": dpStpExtPortNumber,
       "dpStpExtPortFast": dpStpExtPortFast,
       "dpStpExtPortState": dpStpExtPortState,
       "dpStpExtMIBConformance": dpStpExtMIBConformance,
       "dpStpExtMIBCompliances": dpStpExtMIBCompliances,
       "dpStpExtCompliance": dpStpExtCompliance,
       "dpStpExtGroups": dpStpExtGroups,
       "dpStpExtBasicGroup": dpStpExtBasicGroup,
       "dpStpExtMstpGroup": dpStpExtMstpGroup}
)
