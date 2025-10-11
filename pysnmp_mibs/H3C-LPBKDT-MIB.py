# SNMP MIB module (H3C-LPBKDT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-LPBKDT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:21:01 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
    "ifIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cLpbkdt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95)
)
if mibBuilder.loadTexts:
    h3cLpbkdt.setRevisions(
        ("2014-07-26 15:18",
         "2009-03-30 17:41",
         "2008-09-27 15:04")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cLpbkdtActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("block", 2),
          ("nolearning", 3),
          ("shutdown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_H3cLpbkdtNotifications_ObjectIdentity = ObjectIdentity
h3cLpbkdtNotifications = _H3cLpbkdtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 1)
)
_H3cLpbkdtTrapPrefix_ObjectIdentity = ObjectIdentity
h3cLpbkdtTrapPrefix = _H3cLpbkdtTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 1, 0)
)
_H3cLpbkdtObjects_ObjectIdentity = ObjectIdentity
h3cLpbkdtObjects = _H3cLpbkdtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 2)
)
_H3cLpbkdtVlanID_Type = VlanId
_H3cLpbkdtVlanID_Object = MibScalar
h3cLpbkdtVlanID = _H3cLpbkdtVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 2, 1),
    _H3cLpbkdtVlanID_Type()
)
h3cLpbkdtVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLpbkdtVlanID.setStatus("current")


class _H3cLpbkdtVlanEnable_Type(OctetString):
    """Custom type h3cLpbkdtVlanEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_H3cLpbkdtVlanEnable_Type.__name__ = "OctetString"
_H3cLpbkdtVlanEnable_Object = MibScalar
h3cLpbkdtVlanEnable = _H3cLpbkdtVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 2, 2),
    _H3cLpbkdtVlanEnable_Type()
)
h3cLpbkdtVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLpbkdtVlanEnable.setStatus("current")


class _H3cLpbkdtAction_Type(H3cLpbkdtActionType):
    """Custom type h3cLpbkdtAction based on H3cLpbkdtActionType"""
    defaultValue = 1


_H3cLpbkdtAction_Type.__name__ = "H3cLpbkdtActionType"
_H3cLpbkdtAction_Object = MibScalar
h3cLpbkdtAction = _H3cLpbkdtAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 2, 3),
    _H3cLpbkdtAction_Type()
)
h3cLpbkdtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLpbkdtAction.setStatus("current")


class _H3cLpbkdtIntervalTime_Type(Integer32):
    """Custom type h3cLpbkdtIntervalTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_H3cLpbkdtIntervalTime_Type.__name__ = "Integer32"
_H3cLpbkdtIntervalTime_Object = MibScalar
h3cLpbkdtIntervalTime = _H3cLpbkdtIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 2, 4),
    _H3cLpbkdtIntervalTime_Type()
)
h3cLpbkdtIntervalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLpbkdtIntervalTime.setStatus("current")
_H3cLpbkdtPortTable_Object = MibTable
h3cLpbkdtPortTable = _H3cLpbkdtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 2, 5)
)
if mibBuilder.loadTexts:
    h3cLpbkdtPortTable.setStatus("current")
_H3cLpbkdtPortEntry_Object = MibTableRow
h3cLpbkdtPortEntry = _H3cLpbkdtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 2, 5, 1)
)
h3cLpbkdtPortEntry.setIndexNames(
    (0, "H3C-LPBKDT-MIB", "h3cLpbkdtPortIfIndex"),
)
if mibBuilder.loadTexts:
    h3cLpbkdtPortEntry.setStatus("current")
_H3cLpbkdtPortIfIndex_Type = InterfaceIndex
_H3cLpbkdtPortIfIndex_Object = MibTableColumn
h3cLpbkdtPortIfIndex = _H3cLpbkdtPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 2, 5, 1, 1),
    _H3cLpbkdtPortIfIndex_Type()
)
h3cLpbkdtPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cLpbkdtPortIfIndex.setStatus("current")


class _H3cLpbkdtPortVlanEnable_Type(OctetString):
    """Custom type h3cLpbkdtPortVlanEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_H3cLpbkdtPortVlanEnable_Type.__name__ = "OctetString"
_H3cLpbkdtPortVlanEnable_Object = MibTableColumn
h3cLpbkdtPortVlanEnable = _H3cLpbkdtPortVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 2, 5, 1, 2),
    _H3cLpbkdtPortVlanEnable_Type()
)
h3cLpbkdtPortVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLpbkdtPortVlanEnable.setStatus("current")
_H3cLpbkdtPortAction_Type = H3cLpbkdtActionType
_H3cLpbkdtPortAction_Object = MibTableColumn
h3cLpbkdtPortAction = _H3cLpbkdtPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 2, 5, 1, 3),
    _H3cLpbkdtPortAction_Type()
)
h3cLpbkdtPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLpbkdtPortAction.setStatus("current")
_H3cLpbkdtPortLoopbacked_Type = TruthValue
_H3cLpbkdtPortLoopbacked_Object = MibTableColumn
h3cLpbkdtPortLoopbacked = _H3cLpbkdtPortLoopbacked_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 2, 5, 1, 4),
    _H3cLpbkdtPortLoopbacked_Type()
)
h3cLpbkdtPortLoopbacked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLpbkdtPortLoopbacked.setStatus("current")

# Managed Objects groups


# Notification objects

h3cLpbkdtTrapLoopbacked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 1, 0, 1)
)
h3cLpbkdtTrapLoopbacked.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cLpbkdtTrapLoopbacked.setStatus(
        "current"
    )

h3cLpbkdtTrapRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 1, 0, 2)
)
h3cLpbkdtTrapRecovered.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cLpbkdtTrapRecovered.setStatus(
        "current"
    )

h3cLpbkdtTrapPerVlanLoopbacked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 1, 0, 3)
)
h3cLpbkdtTrapPerVlanLoopbacked.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-LPBKDT-MIB", "h3cLpbkdtVlanID"))
)
if mibBuilder.loadTexts:
    h3cLpbkdtTrapPerVlanLoopbacked.setStatus(
        "current"
    )

h3cLpbkdtTrapPerVlanRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 95, 1, 0, 4)
)
h3cLpbkdtTrapPerVlanRecovered.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-LPBKDT-MIB", "h3cLpbkdtVlanID"))
)
if mibBuilder.loadTexts:
    h3cLpbkdtTrapPerVlanRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-LPBKDT-MIB",
    **{"H3cLpbkdtActionType": H3cLpbkdtActionType,
       "h3cLpbkdt": h3cLpbkdt,
       "h3cLpbkdtNotifications": h3cLpbkdtNotifications,
       "h3cLpbkdtTrapPrefix": h3cLpbkdtTrapPrefix,
       "h3cLpbkdtTrapLoopbacked": h3cLpbkdtTrapLoopbacked,
       "h3cLpbkdtTrapRecovered": h3cLpbkdtTrapRecovered,
       "h3cLpbkdtTrapPerVlanLoopbacked": h3cLpbkdtTrapPerVlanLoopbacked,
       "h3cLpbkdtTrapPerVlanRecovered": h3cLpbkdtTrapPerVlanRecovered,
       "h3cLpbkdtObjects": h3cLpbkdtObjects,
       "h3cLpbkdtVlanID": h3cLpbkdtVlanID,
       "h3cLpbkdtVlanEnable": h3cLpbkdtVlanEnable,
       "h3cLpbkdtAction": h3cLpbkdtAction,
       "h3cLpbkdtIntervalTime": h3cLpbkdtIntervalTime,
       "h3cLpbkdtPortTable": h3cLpbkdtPortTable,
       "h3cLpbkdtPortEntry": h3cLpbkdtPortEntry,
       "h3cLpbkdtPortIfIndex": h3cLpbkdtPortIfIndex,
       "h3cLpbkdtPortVlanEnable": h3cLpbkdtPortVlanEnable,
       "h3cLpbkdtPortAction": h3cLpbkdtPortAction,
       "h3cLpbkdtPortLoopbacked": h3cLpbkdtPortLoopbacked}
)
