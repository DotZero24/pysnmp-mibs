# SNMP MIB module (DLINKPRIME-DDP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-DDP-CLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:48:00 2025
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

dlinkPrimeDdpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 2)
)
if mibBuilder.loadTexts:
    dlinkPrimeDdpClientMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpDdpClientNotifications_ObjectIdentity = ObjectIdentity
dpDdpClientNotifications = _DpDdpClientNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 2, 0)
)
_DpDdpClientObjects_ObjectIdentity = ObjectIdentity
dpDdpClientObjects = _DpDdpClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 2, 1)
)
_DpDdpClientCtrl_ObjectIdentity = ObjectIdentity
dpDdpClientCtrl = _DpDdpClientCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 2, 1, 1)
)


class _DpDdpClientGlobalState_Type(TruthValue):
    """Custom type dpDdpClientGlobalState based on TruthValue"""
    defaultValue = 1


_DpDdpClientGlobalState_Type.__name__ = "TruthValue"
_DpDdpClientGlobalState_Object = MibScalar
dpDdpClientGlobalState = _DpDdpClientGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 2, 1, 1, 1),
    _DpDdpClientGlobalState_Type()
)
dpDdpClientGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpDdpClientGlobalState.setStatus("current")


class _DpDdpClientReportTimer_Type(Unsigned32):
    """Custom type dpDdpClientReportTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(120, 120),
    )


_DpDdpClientReportTimer_Type.__name__ = "Unsigned32"
_DpDdpClientReportTimer_Object = MibScalar
dpDdpClientReportTimer = _DpDdpClientReportTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 2, 1, 1, 2),
    _DpDdpClientReportTimer_Type()
)
dpDdpClientReportTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpDdpClientReportTimer.setStatus("current")
if mibBuilder.loadTexts:
    dpDdpClientReportTimer.setUnits("second")
_DpDdpClientConformance_ObjectIdentity = ObjectIdentity
dpDdpClientConformance = _DpDdpClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 2, 2)
)
_DpDdpClientCompliances_ObjectIdentity = ObjectIdentity
dpDdpClientCompliances = _DpDdpClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 2, 2, 1)
)
_DpDdpClientGroups_ObjectIdentity = ObjectIdentity
dpDdpClientGroups = _DpDdpClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 2, 2, 2)
)

# Managed Objects groups

dpDdpClientControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 2, 2, 2, 1)
)
dpDdpClientControlGroup.setObjects(
    ("DLINKPRIME-DDP-CLIENT-MIB", "dpDdpClientGlobalState")
)
if mibBuilder.loadTexts:
    dpDdpClientControlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpDdpClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 2, 2, 1, 1)
)
dpDdpClientCompliance.setObjects(
      *(("DLINKPRIME-DDP-CLIENT-MIB", "dpDdpClientControlGroup"),
        ("DLINKPRIME-DDP-CLIENT-MIB", "dpDdpClientControlGroup"))
)
if mibBuilder.loadTexts:
    dpDdpClientCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-DDP-CLIENT-MIB",
    **{"dlinkPrimeDdpClientMIB": dlinkPrimeDdpClientMIB,
       "dpDdpClientNotifications": dpDdpClientNotifications,
       "dpDdpClientObjects": dpDdpClientObjects,
       "dpDdpClientCtrl": dpDdpClientCtrl,
       "dpDdpClientGlobalState": dpDdpClientGlobalState,
       "dpDdpClientReportTimer": dpDdpClientReportTimer,
       "dpDdpClientConformance": dpDdpClientConformance,
       "dpDdpClientCompliances": dpDdpClientCompliances,
       "dpDdpClientCompliance": dpDdpClientCompliance,
       "dpDdpClientGroups": dpDdpClientGroups,
       "dpDdpClientControlGroup": dpDdpClientControlGroup}
)
