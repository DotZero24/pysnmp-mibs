# SNMP MIB module (TPLINK-ARP-DETECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-ARP-DETECTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:07 2025
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

(tplinkArpInspectionMIBObjects,) = mibBuilder.importSymbols(
    "TPLINK-ARP-INSPECTION-MIB",
    "tplinkArpInspectionMIBObjects")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TpArpDetection_ObjectIdentity = ObjectIdentity
tpArpDetection = _TpArpDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1)
)
_TpArpDetectionConfig_ObjectIdentity = ObjectIdentity
tpArpDetectionConfig = _TpArpDetectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 1)
)


class _TpArpDetectionConfigEnable_Type(Integer32):
    """Custom type tpArpDetectionConfigEnable based on Integer32"""
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


_TpArpDetectionConfigEnable_Type.__name__ = "Integer32"
_TpArpDetectionConfigEnable_Object = MibScalar
tpArpDetectionConfigEnable = _TpArpDetectionConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 1, 1),
    _TpArpDetectionConfigEnable_Type()
)
tpArpDetectionConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpArpDetectionConfigEnable.setStatus("current")
_TpArpDetectionTrustPortTable_Object = MibTable
tpArpDetectionTrustPortTable = _TpArpDetectionTrustPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tpArpDetectionTrustPortTable.setStatus("current")
_TpArpDetectionTrustPortEntry_Object = MibTableRow
tpArpDetectionTrustPortEntry = _TpArpDetectionTrustPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 1, 2, 1)
)
tpArpDetectionTrustPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpArpDetectionTrustPortEntry.setStatus("current")
_TpArpDetectionTrustPort_Type = OctetString
_TpArpDetectionTrustPort_Object = MibTableColumn
tpArpDetectionTrustPort = _TpArpDetectionTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 1, 2, 1, 1),
    _TpArpDetectionTrustPort_Type()
)
tpArpDetectionTrustPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpArpDetectionTrustPort.setStatus("current")


class _TpArpDetectionTrustPortState_Type(Integer32):
    """Custom type tpArpDetectionTrustPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("untrusty", 0),
          ("trustful", 1))
    )


_TpArpDetectionTrustPortState_Type.__name__ = "Integer32"
_TpArpDetectionTrustPortState_Object = MibTableColumn
tpArpDetectionTrustPortState = _TpArpDetectionTrustPortState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 1, 2, 1, 2),
    _TpArpDetectionTrustPortState_Type()
)
tpArpDetectionTrustPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpArpDetectionTrustPortState.setStatus("current")


class _TpArpDetectionTrustPortLag_Type(OctetString):
    """Custom type tpArpDetectionTrustPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpArpDetectionTrustPortLag_Type.__name__ = "OctetString"
_TpArpDetectionTrustPortLag_Object = MibTableColumn
tpArpDetectionTrustPortLag = _TpArpDetectionTrustPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 1, 2, 1, 3),
    _TpArpDetectionTrustPortLag_Type()
)
tpArpDetectionTrustPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpArpDetectionTrustPortLag.setStatus("current")
_TpArpDetectionStat_ObjectIdentity = ObjectIdentity
tpArpDetectionStat = _TpArpDetectionStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 2)
)


class _TpArpDetectionStatReset_Type(Integer32):
    """Custom type tpArpDetectionStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notReset", 0),
          ("reset", 1))
    )


_TpArpDetectionStatReset_Type.__name__ = "Integer32"
_TpArpDetectionStatReset_Object = MibScalar
tpArpDetectionStatReset = _TpArpDetectionStatReset_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 2, 1),
    _TpArpDetectionStatReset_Type()
)
tpArpDetectionStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpArpDetectionStatReset.setStatus("current")
_TpArpDetectionStatTable_Object = MibTable
tpArpDetectionStatTable = _TpArpDetectionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tpArpDetectionStatTable.setStatus("current")
_TpArpDetectionStatEntry_Object = MibTableRow
tpArpDetectionStatEntry = _TpArpDetectionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 2, 2, 1)
)
tpArpDetectionStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpArpDetectionStatEntry.setStatus("current")


class _TpArpDetectionStatPort_Type(OctetString):
    """Custom type tpArpDetectionStatPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpArpDetectionStatPort_Type.__name__ = "OctetString"
_TpArpDetectionStatPort_Object = MibTableColumn
tpArpDetectionStatPort = _TpArpDetectionStatPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 2, 2, 1, 1),
    _TpArpDetectionStatPort_Type()
)
tpArpDetectionStatPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpArpDetectionStatPort.setStatus("current")


class _TpArpDetectionStatState_Type(Integer32):
    """Custom type tpArpDetectionStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("untrusty", 0),
          ("trustful", 1))
    )


_TpArpDetectionStatState_Type.__name__ = "Integer32"
_TpArpDetectionStatState_Object = MibTableColumn
tpArpDetectionStatState = _TpArpDetectionStatState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 2, 2, 1, 2),
    _TpArpDetectionStatState_Type()
)
tpArpDetectionStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpArpDetectionStatState.setStatus("current")
_TpArpDetectionStatNonLegalPkt_Type = Counter32
_TpArpDetectionStatNonLegalPkt_Object = MibTableColumn
tpArpDetectionStatNonLegalPkt = _TpArpDetectionStatNonLegalPkt_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 2, 2, 1, 3),
    _TpArpDetectionStatNonLegalPkt_Type()
)
tpArpDetectionStatNonLegalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpArpDetectionStatNonLegalPkt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ARP-DETECTION-MIB",
    **{"tpArpDetection": tpArpDetection,
       "tpArpDetectionConfig": tpArpDetectionConfig,
       "tpArpDetectionConfigEnable": tpArpDetectionConfigEnable,
       "tpArpDetectionTrustPortTable": tpArpDetectionTrustPortTable,
       "tpArpDetectionTrustPortEntry": tpArpDetectionTrustPortEntry,
       "tpArpDetectionTrustPort": tpArpDetectionTrustPort,
       "tpArpDetectionTrustPortState": tpArpDetectionTrustPortState,
       "tpArpDetectionTrustPortLag": tpArpDetectionTrustPortLag,
       "tpArpDetectionStat": tpArpDetectionStat,
       "tpArpDetectionStatReset": tpArpDetectionStatReset,
       "tpArpDetectionStatTable": tpArpDetectionStatTable,
       "tpArpDetectionStatEntry": tpArpDetectionStatEntry,
       "tpArpDetectionStatPort": tpArpDetectionStatPort,
       "tpArpDetectionStatState": tpArpDetectionStatState,
       "tpArpDetectionStatNonLegalPkt": tpArpDetectionStatNonLegalPkt}
)
