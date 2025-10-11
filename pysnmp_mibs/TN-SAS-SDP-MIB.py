# SNMP MIB module (TN-SAS-SDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-SAS-SDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:02:16 2025
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

(sdpBindBaseStatsEntry,
 sdpBindEntry) = mibBuilder.importSymbols(
    "TN-SDP-MIB",
    "sdpBindBaseStatsEntry",
    "sdpBindEntry")

(tnSASModules,
 tnSASObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSASModules",
    "tnSASObjs")


# MODULE-IDENTITY

tnSASServicesSdpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tnSASServicesSdpMIBModule.setRevisions(
        ("2015-07-30 00:00",
         "2007-10-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnSASSdpObjs_ObjectIdentity = ObjectIdentity
tnSASSdpObjs = _TnSASSdpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 12)
)
_SdpBindExtnTable_Object = MibTable
sdpBindExtnTable = _SdpBindExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 12, 4)
)
if mibBuilder.loadTexts:
    sdpBindExtnTable.setStatus("current")
_SdpBindExtnEntry_Object = MibTableRow
sdpBindExtnEntry = _SdpBindExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 12, 4, 1)
)
if mibBuilder.loadTexts:
    sdpBindExtnEntry.setStatus("current")


class _SdpBindIngressExtraVlanTagDropCount_Type(TruthValue):
    """Custom type sdpBindIngressExtraVlanTagDropCount based on TruthValue"""
    defaultValue = 2


_SdpBindIngressExtraVlanTagDropCount_Type.__name__ = "TruthValue"
_SdpBindIngressExtraVlanTagDropCount_Object = MibTableColumn
sdpBindIngressExtraVlanTagDropCount = _SdpBindIngressExtraVlanTagDropCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 12, 4, 1, 1),
    _SdpBindIngressExtraVlanTagDropCount_Type()
)
sdpBindIngressExtraVlanTagDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressExtraVlanTagDropCount.setStatus("current")
_SdpBindBaseStatsExtnTable_Object = MibTable
sdpBindBaseStatsExtnTable = _SdpBindBaseStatsExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 12, 5)
)
if mibBuilder.loadTexts:
    sdpBindBaseStatsExtnTable.setStatus("current")
_SdpBindBaseStatsExtnEntry_Object = MibTableRow
sdpBindBaseStatsExtnEntry = _SdpBindBaseStatsExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 12, 5, 1)
)
if mibBuilder.loadTexts:
    sdpBindBaseStatsExtnEntry.setStatus("current")
_SdpBindIngressExtraVlanTagDroppedPackets_Type = Counter64
_SdpBindIngressExtraVlanTagDroppedPackets_Object = MibTableColumn
sdpBindIngressExtraVlanTagDroppedPackets = _SdpBindIngressExtraVlanTagDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 12, 5, 1, 1),
    _SdpBindIngressExtraVlanTagDroppedPackets_Type()
)
sdpBindIngressExtraVlanTagDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIngressExtraVlanTagDroppedPackets.setStatus("current")
_SdpBindIngressExtraVlanTagDroppedOctets_Type = Counter64
_SdpBindIngressExtraVlanTagDroppedOctets_Object = MibTableColumn
sdpBindIngressExtraVlanTagDroppedOctets = _SdpBindIngressExtraVlanTagDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 12, 5, 1, 2),
    _SdpBindIngressExtraVlanTagDroppedOctets_Type()
)
sdpBindIngressExtraVlanTagDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIngressExtraVlanTagDroppedOctets.setStatus("current")
sdpBindEntry.registerAugmentions(
    ("TN-SAS-SDP-MIB",
     "sdpBindExtnEntry")
)
sdpBindExtnEntry.setIndexNames(*sdpBindEntry.getIndexNames())
sdpBindBaseStatsEntry.registerAugmentions(
    ("TN-SAS-SDP-MIB",
     "sdpBindBaseStatsExtnEntry")
)
sdpBindBaseStatsExtnEntry.setIndexNames(*sdpBindBaseStatsEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SAS-SDP-MIB",
    **{"tnSASServicesSdpMIBModule": tnSASServicesSdpMIBModule,
       "tnSASSdpObjs": tnSASSdpObjs,
       "sdpBindExtnTable": sdpBindExtnTable,
       "sdpBindExtnEntry": sdpBindExtnEntry,
       "sdpBindIngressExtraVlanTagDropCount": sdpBindIngressExtraVlanTagDropCount,
       "sdpBindBaseStatsExtnTable": sdpBindBaseStatsExtnTable,
       "sdpBindBaseStatsExtnEntry": sdpBindBaseStatsExtnEntry,
       "sdpBindIngressExtraVlanTagDroppedPackets": sdpBindIngressExtraVlanTagDroppedPackets,
       "sdpBindIngressExtraVlanTagDroppedOctets": sdpBindIngressExtraVlanTagDroppedOctets}
)
