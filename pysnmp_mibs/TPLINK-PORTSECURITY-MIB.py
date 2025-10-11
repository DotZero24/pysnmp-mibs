# SNMP MIB module (TPLINK-PORTSECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-PORTSECURITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:50 2025
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

tplinkPortSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 12)
)
if mibBuilder.loadTexts:
    tplinkPortSecurityMIB.setRevisions(
        ("2012-12-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkPortSecurityMIBObjects_ObjectIdentity = ObjectIdentity
tplinkPortSecurityMIBObjects = _TplinkPortSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 12, 1)
)
_TpPortSecurityTable_Object = MibTable
tpPortSecurityTable = _TpPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 12, 1, 1)
)
if mibBuilder.loadTexts:
    tpPortSecurityTable.setStatus("current")
_TpPortSecurityEntry_Object = MibTableRow
tpPortSecurityEntry = _TpPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 12, 1, 1, 1)
)
tpPortSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpPortSecurityEntry.setStatus("current")


class _TpPortSecurityPortIndex_Type(DisplayString):
    """Custom type tpPortSecurityPortIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpPortSecurityPortIndex_Type.__name__ = "DisplayString"
_TpPortSecurityPortIndex_Object = MibTableColumn
tpPortSecurityPortIndex = _TpPortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 12, 1, 1, 1, 1),
    _TpPortSecurityPortIndex_Type()
)
tpPortSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortSecurityPortIndex.setStatus("current")


class _TpPortSecurityMaxNum_Type(Integer32):
    """Custom type tpPortSecurityMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_TpPortSecurityMaxNum_Type.__name__ = "Integer32"
_TpPortSecurityMaxNum_Object = MibTableColumn
tpPortSecurityMaxNum = _TpPortSecurityMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 12, 1, 1, 1, 2),
    _TpPortSecurityMaxNum_Type()
)
tpPortSecurityMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortSecurityMaxNum.setStatus("current")
_TpPortSecurityLearnNum_Type = Integer32
_TpPortSecurityLearnNum_Object = MibTableColumn
tpPortSecurityLearnNum = _TpPortSecurityLearnNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 12, 1, 1, 1, 3),
    _TpPortSecurityLearnNum_Type()
)
tpPortSecurityLearnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortSecurityLearnNum.setStatus("current")


class _TpPortSecurityLearnMode_Type(Integer32):
    """Custom type tpPortSecurityLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1),
          ("permanent", 2))
    )


_TpPortSecurityLearnMode_Type.__name__ = "Integer32"
_TpPortSecurityLearnMode_Object = MibTableColumn
tpPortSecurityLearnMode = _TpPortSecurityLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 12, 1, 1, 1, 4),
    _TpPortSecurityLearnMode_Type()
)
tpPortSecurityLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortSecurityLearnMode.setStatus("current")


class _TpPortSecurityPortStatus_Type(Integer32):
    """Custom type tpPortSecurityPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("forward", 1),
          ("drop", 2))
    )


_TpPortSecurityPortStatus_Type.__name__ = "Integer32"
_TpPortSecurityPortStatus_Object = MibTableColumn
tpPortSecurityPortStatus = _TpPortSecurityPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 12, 1, 1, 1, 5),
    _TpPortSecurityPortStatus_Type()
)
tpPortSecurityPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortSecurityPortStatus.setStatus("current")
_TplinkPortSecurityNotifications_ObjectIdentity = ObjectIdentity
tplinkPortSecurityNotifications = _TplinkPortSecurityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 12, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-PORTSECURITY-MIB",
    **{"tplinkPortSecurityMIB": tplinkPortSecurityMIB,
       "tplinkPortSecurityMIBObjects": tplinkPortSecurityMIBObjects,
       "tpPortSecurityTable": tpPortSecurityTable,
       "tpPortSecurityEntry": tpPortSecurityEntry,
       "tpPortSecurityPortIndex": tpPortSecurityPortIndex,
       "tpPortSecurityMaxNum": tpPortSecurityMaxNum,
       "tpPortSecurityLearnNum": tpPortSecurityLearnNum,
       "tpPortSecurityLearnMode": tpPortSecurityLearnMode,
       "tpPortSecurityPortStatus": tpPortSecurityPortStatus,
       "tplinkPortSecurityNotifications": tplinkPortSecurityNotifications}
)
