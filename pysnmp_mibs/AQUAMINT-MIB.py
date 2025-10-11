# SNMP MIB module (AQUAMINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinet/AQUAMINT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:10 2025
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

(sysSerialNumber,
 sysTrapSequence) = mibBuilder.importSymbols(
    "AQUASYSTEM-MIB",
    "sysSerialNumber",
    "sysTrapSequence")

(wanflex,) = mibBuilder.importSymbols(
    "INFINET-MIB",
    "wanflex")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

aquamintMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5)
)
if mibBuilder.loadTexts:
    aquamintMIB.setRevisions(
        ("2016-04-04 07:35",
         "2015-08-25 06:54",
         "2015-08-17 06:02",
         "2010-01-28 09:37",
         "2009-02-04 05:48",
         "2008-12-04 07:18",
         "2008-07-21 05:40",
         "2008-05-22 04:04",
         "2008-05-21 13:36",
         "2008-05-04 11:41",
         "2006-10-26 12:25")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MintMIBObjects_ObjectIdentity = ObjectIdentity
mintMIBObjects = _MintMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1)
)
_Mint_ObjectIdentity = ObjectIdentity
mint = _Mint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1)
)
_MintNodesTable_Object = MibTable
mintNodesTable = _MintNodesTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mintNodesTable.setStatus("current")
_MintNodesEntry_Object = MibTableRow
mintNodesEntry = _MintNodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1)
)
mintNodesEntry.setIndexNames(
    (0, "AQUAMINT-MIB", "nodeInterfaceId"),
)
if mibBuilder.loadTexts:
    mintNodesEntry.setStatus("current")
_NetAddress_Type = MacAddress
_NetAddress_Object = MibTableColumn
netAddress = _NetAddress_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 1),
    _NetAddress_Type()
)
netAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAddress.setStatus("current")


class _NodeType_Type(Integer32):
    """Custom type nodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("mesh", 3))
    )


_NodeType_Type.__name__ = "Integer32"
_NodeType_Object = MibTableColumn
nodeType = _NodeType_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 2),
    _NodeType_Type()
)
nodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeType.setStatus("current")


class _NodeMode_Type(Integer32):
    """Custom type nodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("nomadic", 2),
          ("mobile", 3))
    )


_NodeMode_Type.__name__ = "Integer32"
_NodeMode_Object = MibTableColumn
nodeMode = _NodeMode_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 3),
    _NodeMode_Type()
)
nodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeMode.setStatus("current")
_LinksCount_Type = Integer32
_LinksCount_Object = MibTableColumn
linksCount = _LinksCount_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 4),
    _LinksCount_Type()
)
linksCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linksCount.setStatus("current")
_NodesCount_Type = Integer32
_NodesCount_Object = MibTableColumn
nodesCount = _NodesCount_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 5),
    _NodesCount_Type()
)
nodesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesCount.setStatus("current")


class _NodeInterfaceId_Type(Integer32):
    """Custom type nodeInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NodeInterfaceId_Type.__name__ = "Integer32"
_NodeInterfaceId_Object = MibTableColumn
nodeInterfaceId = _NodeInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 6),
    _NodeInterfaceId_Type()
)
nodeInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInterfaceId.setStatus("current")


class _ProtocolEnabled_Type(Integer32):
    """Custom type protocolEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ProtocolEnabled_Type.__name__ = "Integer32"
_ProtocolEnabled_Object = MibTableColumn
protocolEnabled = _ProtocolEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 7),
    _ProtocolEnabled_Type()
)
protocolEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolEnabled.setStatus("current")


class _NodeName_Type(DisplayString):
    """Custom type nodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_NodeName_Type.__name__ = "DisplayString"
_NodeName_Object = MibTableColumn
nodeName = _NodeName_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 8),
    _NodeName_Type()
)
nodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeName.setStatus("current")


class _AutoBitrateEnable_Type(Integer32):
    """Custom type autoBitrateEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_AutoBitrateEnable_Type.__name__ = "Integer32"
_AutoBitrateEnable_Object = MibTableColumn
autoBitrateEnable = _AutoBitrateEnable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 9),
    _AutoBitrateEnable_Type()
)
autoBitrateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBitrateEnable.setStatus("current")
_AutoBitrateAddition_Type = Integer32
_AutoBitrateAddition_Object = MibTableColumn
autoBitrateAddition = _AutoBitrateAddition_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 10),
    _AutoBitrateAddition_Type()
)
autoBitrateAddition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBitrateAddition.setStatus("current")
_AutoBitrateMinLevel_Type = Integer32
_AutoBitrateMinLevel_Object = MibTableColumn
autoBitrateMinLevel = _AutoBitrateMinLevel_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 11),
    _AutoBitrateMinLevel_Type()
)
autoBitrateMinLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBitrateMinLevel.setStatus("current")


class _ExtraCost_Type(Integer32):
    """Custom type extraCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtraCost_Type.__name__ = "Integer32"
_ExtraCost_Object = MibTableColumn
extraCost = _ExtraCost_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 12),
    _ExtraCost_Type()
)
extraCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extraCost.setStatus("current")


class _FixedCost_Type(Integer32):
    """Custom type fixedCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FixedCost_Type.__name__ = "Integer32"
_FixedCost_Object = MibTableColumn
fixedCost = _FixedCost_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 13),
    _FixedCost_Type()
)
fixedCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fixedCost.setStatus("current")


class _NodeID_Type(Integer32):
    """Custom type nodeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NodeID_Type.__name__ = "Integer32"
_NodeID_Object = MibTableColumn
nodeID = _NodeID_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 14),
    _NodeID_Type()
)
nodeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeID.setStatus("current")
_AmpLow_Type = Integer32
_AmpLow_Object = MibTableColumn
ampLow = _AmpLow_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 15),
    _AmpLow_Type()
)
ampLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ampLow.setStatus("current")
_AmpHigh_Type = Integer32
_AmpHigh_Object = MibTableColumn
ampHigh = _AmpHigh_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 16),
    _AmpHigh_Type()
)
ampHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ampHigh.setStatus("current")


class _AuthMode_Type(Integer32):
    """Custom type authMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("public", 1),
          ("static", 2),
          ("remote", 3))
    )


_AuthMode_Type.__name__ = "Integer32"
_AuthMode_Object = MibTableColumn
authMode = _AuthMode_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 17),
    _AuthMode_Type()
)
authMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMode.setStatus("current")


class _AuthRelay_Type(Integer32):
    """Custom type authRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_AuthRelay_Type.__name__ = "Integer32"
_AuthRelay_Object = MibTableColumn
authRelay = _AuthRelay_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 18),
    _AuthRelay_Type()
)
authRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authRelay.setStatus("current")


class _Scrambling_Type(Integer32):
    """Custom type scrambling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Scrambling_Type.__name__ = "Integer32"
_Scrambling_Object = MibTableColumn
scrambling = _Scrambling_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 19),
    _Scrambling_Type()
)
scrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrambling.setStatus("current")


class _Compress_Type(Integer32):
    """Custom type compress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Compress_Type.__name__ = "Integer32"
_Compress_Object = MibTableColumn
compress = _Compress_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 20),
    _Compress_Type()
)
compress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    compress.setStatus("current")


class _OverTheAirUpgradeEnable_Type(Integer32):
    """Custom type overTheAirUpgradeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("off", 2),
          ("active", 3))
    )


_OverTheAirUpgradeEnable_Type.__name__ = "Integer32"
_OverTheAirUpgradeEnable_Object = MibTableColumn
overTheAirUpgradeEnable = _OverTheAirUpgradeEnable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 21),
    _OverTheAirUpgradeEnable_Type()
)
overTheAirUpgradeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overTheAirUpgradeEnable.setStatus("current")


class _OverTheAirUpgradeSpeed_Type(Integer32):
    """Custom type overTheAirUpgradeSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("normal", 2),
          ("slow", 3))
    )


_OverTheAirUpgradeSpeed_Type.__name__ = "Integer32"
_OverTheAirUpgradeSpeed_Object = MibTableColumn
overTheAirUpgradeSpeed = _OverTheAirUpgradeSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 22),
    _OverTheAirUpgradeSpeed_Type()
)
overTheAirUpgradeSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overTheAirUpgradeSpeed.setStatus("current")


class _Roaming_Type(Integer32):
    """Custom type roaming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("slave", 1),
          ("off", 2),
          ("leader", 3),
          ("global_leader", 4),
          ("slave_multibs", 5),
          ("slave_global", 6),
          ("slave_multibs_global", 7))
    )


_Roaming_Type.__name__ = "Integer32"
_Roaming_Object = MibTableColumn
roaming = _Roaming_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 23),
    _Roaming_Type()
)
roaming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roaming.setStatus("current")


class _Polling_Type(Integer32):
    """Custom type polling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Polling_Type.__name__ = "Integer32"
_Polling_Object = MibTableColumn
polling = _Polling_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 24),
    _Polling_Type()
)
polling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polling.setStatus("current")
_MintBroadcastRate_Type = Unsigned32
_MintBroadcastRate_Object = MibTableColumn
mintBroadcastRate = _MintBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 25),
    _MintBroadcastRate_Type()
)
mintBroadcastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mintBroadcastRate.setStatus("current")
_NoiseFloor_Type = Integer32
_NoiseFloor_Object = MibTableColumn
noiseFloor = _NoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 26),
    _NoiseFloor_Type()
)
noiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiseFloor.setStatus("current")


class _SecretKey_Type(DisplayString):
    """Custom type secretKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SecretKey_Type.__name__ = "DisplayString"
_SecretKey_Object = MibTableColumn
secretKey = _SecretKey_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 27),
    _SecretKey_Type()
)
secretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secretKey.setStatus("current")
_LinksCountReal_Type = Integer32
_LinksCountReal_Object = MibTableColumn
linksCountReal = _LinksCountReal_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 28),
    _LinksCountReal_Type()
)
linksCountReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linksCountReal.setStatus("current")
_RxCapacity_Type = Integer32
_RxCapacity_Object = MibTableColumn
rxCapacity = _RxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 29),
    _RxCapacity_Type()
)
rxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxCapacity.setStatus("current")
_TxCapacity_Type = Integer32
_TxCapacity_Object = MibTableColumn
txCapacity = _TxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 1, 1, 30),
    _TxCapacity_Type()
)
txCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCapacity.setStatus("current")
_MintLinksTable_Object = MibTable
mintLinksTable = _MintLinksTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mintLinksTable.setStatus("current")
_MintLinksEntry_Object = MibTableRow
mintLinksEntry = _MintLinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1)
)
mintLinksEntry.setIndexNames(
    (0, "AQUAMINT-MIB", "mintInterfaceId"),
    (0, "AQUAMINT-MIB", "neighborAddress"),
)
if mibBuilder.loadTexts:
    mintLinksEntry.setStatus("current")


class _MintInterfaceId_Type(Integer32):
    """Custom type mintInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MintInterfaceId_Type.__name__ = "Integer32"
_MintInterfaceId_Object = MibTableColumn
mintInterfaceId = _MintInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 1),
    _MintInterfaceId_Type()
)
mintInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mintInterfaceId.setStatus("current")
_NeighborAddress_Type = MacAddress
_NeighborAddress_Object = MibTableColumn
neighborAddress = _NeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 2),
    _NeighborAddress_Type()
)
neighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborAddress.setStatus("current")
_LinkName_Type = DisplayString
_LinkName_Object = MibTableColumn
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 3),
    _LinkName_Type()
)
linkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkName.setStatus("current")
_LinkCost_Type = Integer32
_LinkCost_Object = MibTableColumn
linkCost = _LinkCost_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 4),
    _LinkCost_Type()
)
linkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCost.setStatus("current")
_MonitorAmpIn_Type = Integer32
_MonitorAmpIn_Object = MibTableColumn
monitorAmpIn = _MonitorAmpIn_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 5),
    _MonitorAmpIn_Type()
)
monitorAmpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorAmpIn.setStatus("current")
_MonitorAmpOut_Type = Integer32
_MonitorAmpOut_Object = MibTableColumn
monitorAmpOut = _MonitorAmpOut_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 6),
    _MonitorAmpOut_Type()
)
monitorAmpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorAmpOut.setStatus("current")
_WorkingAmpIn_Type = Integer32
_WorkingAmpIn_Object = MibTableColumn
workingAmpIn = _WorkingAmpIn_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 7),
    _WorkingAmpIn_Type()
)
workingAmpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    workingAmpIn.setStatus("current")
_WorkingAmpOut_Type = Integer32
_WorkingAmpOut_Object = MibTableColumn
workingAmpOut = _WorkingAmpOut_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 8),
    _WorkingAmpOut_Type()
)
workingAmpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    workingAmpOut.setStatus("current")
_CurBitrateRX_Type = Integer32
_CurBitrateRX_Object = MibTableColumn
curBitrateRX = _CurBitrateRX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 9),
    _CurBitrateRX_Type()
)
curBitrateRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curBitrateRX.setStatus("current")
_CurBitrateTX_Type = Integer32
_CurBitrateTX_Object = MibTableColumn
curBitrateTX = _CurBitrateTX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 10),
    _CurBitrateTX_Type()
)
curBitrateTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curBitrateTX.setStatus("current")
_CurLoadRX_Type = Integer32
_CurLoadRX_Object = MibTableColumn
curLoadRX = _CurLoadRX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 11),
    _CurLoadRX_Type()
)
curLoadRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curLoadRX.setStatus("current")
_CurLoadPPSRX_Type = Integer32
_CurLoadPPSRX_Object = MibTableColumn
curLoadPPSRX = _CurLoadPPSRX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 12),
    _CurLoadPPSRX_Type()
)
curLoadPPSRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curLoadPPSRX.setStatus("current")
_CurLoadTX_Type = Integer32
_CurLoadTX_Object = MibTableColumn
curLoadTX = _CurLoadTX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 13),
    _CurLoadTX_Type()
)
curLoadTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curLoadTX.setStatus("current")
_CurLoadPPSTX_Type = Integer32
_CurLoadPPSTX_Object = MibTableColumn
curLoadPPSTX = _CurLoadPPSTX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 14),
    _CurLoadPPSTX_Type()
)
curLoadPPSTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curLoadPPSTX.setStatus("current")
_OutputBytes_Type = Counter32
_OutputBytes_Object = MibTableColumn
outputBytes = _OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 15),
    _OutputBytes_Type()
)
outputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputBytes.setStatus("current")
_OutputPackets_Type = Counter32
_OutputPackets_Object = MibTableColumn
outputPackets = _OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 16),
    _OutputPackets_Type()
)
outputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPackets.setStatus("current")
_InputBytes_Type = Counter32
_InputBytes_Object = MibTableColumn
inputBytes = _InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 17),
    _InputBytes_Type()
)
inputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputBytes.setStatus("current")
_InputPackets_Type = Counter32
_InputPackets_Object = MibTableColumn
inputPackets = _InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 18),
    _InputPackets_Type()
)
inputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPackets.setStatus("current")
_RetriesPercentTX_Type = Unsigned32
_RetriesPercentTX_Object = MibTableColumn
retriesPercentTX = _RetriesPercentTX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 19),
    _RetriesPercentTX_Type()
)
retriesPercentTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retriesPercentTX.setStatus("current")
_ErrorsPercentTX_Type = Unsigned32
_ErrorsPercentTX_Object = MibTableColumn
errorsPercentTX = _ErrorsPercentTX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 20),
    _ErrorsPercentTX_Type()
)
errorsPercentTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorsPercentTX.setStatus("current")
_LinkDistance_Type = Integer32
_LinkDistance_Object = MibTableColumn
linkDistance = _LinkDistance_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 21),
    _LinkDistance_Type()
)
linkDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDistance.setStatus("current")
_CurBitrateRXindex_Type = Integer32
_CurBitrateRXindex_Object = MibTableColumn
curBitrateRXindex = _CurBitrateRXindex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 22),
    _CurBitrateRXindex_Type()
)
curBitrateRXindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curBitrateRXindex.setStatus("current")
_CurBitrateTXindex_Type = Integer32
_CurBitrateTXindex_Object = MibTableColumn
curBitrateTXindex = _CurBitrateTXindex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 23),
    _CurBitrateTXindex_Type()
)
curBitrateTXindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curBitrateTXindex.setStatus("current")
_RetriesPercentRX_Type = Unsigned32
_RetriesPercentRX_Object = MibTableColumn
retriesPercentRX = _RetriesPercentRX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 24),
    _RetriesPercentRX_Type()
)
retriesPercentRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retriesPercentRX.setStatus("current")
_ErrorsPercentRX_Type = Unsigned32
_ErrorsPercentRX_Object = MibTableColumn
errorsPercentRX = _ErrorsPercentRX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 25),
    _ErrorsPercentRX_Type()
)
errorsPercentRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorsPercentRX.setStatus("current")
_NeighborIfIndex_Type = Unsigned32
_NeighborIfIndex_Object = MibTableColumn
neighborIfIndex = _NeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 26),
    _NeighborIfIndex_Type()
)
neighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborIfIndex.setStatus("current")
_CurRXpower_Type = Integer32
_CurRXpower_Object = MibTableColumn
curRXpower = _CurRXpower_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 27),
    _CurRXpower_Type()
)
curRXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curRXpower.setStatus("current")
_CurTXpower_Type = Integer32
_CurTXpower_Object = MibTableColumn
curTXpower = _CurTXpower_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 28),
    _CurTXpower_Type()
)
curTXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curTXpower.setStatus("current")
_LinkDistanceMeters_Type = Integer32
_LinkDistanceMeters_Object = MibTableColumn
linkDistanceMeters = _LinkDistanceMeters_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 29),
    _LinkDistanceMeters_Type()
)
linkDistanceMeters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDistanceMeters.setStatus("current")
_RxRSSI_Type = Integer32
_RxRSSI_Object = MibTableColumn
rxRSSI = _RxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 2, 1, 30),
    _RxRSSI_Type()
)
rxRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxRSSI.setStatus("current")
_MintLostNeighbor_ObjectIdentity = ObjectIdentity
mintLostNeighbor = _MintLostNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 3)
)
_LostNeighborIfIndex_Type = Integer32
_LostNeighborIfIndex_Object = MibScalar
lostNeighborIfIndex = _LostNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 3, 1),
    _LostNeighborIfIndex_Type()
)
lostNeighborIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lostNeighborIfIndex.setStatus("current")


class _LostNeighborNetAddress_Type(OctetString):
    """Custom type lostNeighborNetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_LostNeighborNetAddress_Type.__name__ = "OctetString"
_LostNeighborNetAddress_Object = MibScalar
lostNeighborNetAddress = _LostNeighborNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 3, 2),
    _LostNeighborNetAddress_Type()
)
lostNeighborNetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lostNeighborNetAddress.setStatus("current")


class _LostNeighborReason_Type(Integer32):
    """Custom type lostNeighborReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 1),
          ("lost", 2),
          ("other", 3))
    )


_LostNeighborReason_Type.__name__ = "Integer32"
_LostNeighborReason_Object = MibScalar
lostNeighborReason = _LostNeighborReason_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 3, 3),
    _LostNeighborReason_Type()
)
lostNeighborReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lostNeighborReason.setStatus("current")
_LostNeighborName_Type = DisplayString
_LostNeighborName_Object = MibScalar
lostNeighborName = _LostNeighborName_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 3, 4),
    _LostNeighborName_Type()
)
lostNeighborName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lostNeighborName.setStatus("current")
_MintPtpLink_ObjectIdentity = ObjectIdentity
mintPtpLink = _MintPtpLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4)
)


class _PtpInterfaceId_Type(Integer32):
    """Custom type ptpInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PtpInterfaceId_Type.__name__ = "Integer32"
_PtpInterfaceId_Object = MibScalar
ptpInterfaceId = _PtpInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 1),
    _PtpInterfaceId_Type()
)
ptpInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpInterfaceId.setStatus("current")
_PtpNeighborAddress_Type = MacAddress
_PtpNeighborAddress_Object = MibScalar
ptpNeighborAddress = _PtpNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 2),
    _PtpNeighborAddress_Type()
)
ptpNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpNeighborAddress.setStatus("current")
_PtpLinkName_Type = DisplayString
_PtpLinkName_Object = MibScalar
ptpLinkName = _PtpLinkName_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 3),
    _PtpLinkName_Type()
)
ptpLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpLinkName.setStatus("current")
_PtpLinkCost_Type = Integer32
_PtpLinkCost_Object = MibScalar
ptpLinkCost = _PtpLinkCost_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 4),
    _PtpLinkCost_Type()
)
ptpLinkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpLinkCost.setStatus("current")
_PtpMonitorAmpIn_Type = Integer32
_PtpMonitorAmpIn_Object = MibScalar
ptpMonitorAmpIn = _PtpMonitorAmpIn_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 5),
    _PtpMonitorAmpIn_Type()
)
ptpMonitorAmpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpMonitorAmpIn.setStatus("current")
_PtpMonitorAmpOut_Type = Integer32
_PtpMonitorAmpOut_Object = MibScalar
ptpMonitorAmpOut = _PtpMonitorAmpOut_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 6),
    _PtpMonitorAmpOut_Type()
)
ptpMonitorAmpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpMonitorAmpOut.setStatus("current")
_PtpWorkingAmpIn_Type = Integer32
_PtpWorkingAmpIn_Object = MibScalar
ptpWorkingAmpIn = _PtpWorkingAmpIn_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 7),
    _PtpWorkingAmpIn_Type()
)
ptpWorkingAmpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpWorkingAmpIn.setStatus("current")
_PtpWorkingAmpOut_Type = Integer32
_PtpWorkingAmpOut_Object = MibScalar
ptpWorkingAmpOut = _PtpWorkingAmpOut_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 8),
    _PtpWorkingAmpOut_Type()
)
ptpWorkingAmpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpWorkingAmpOut.setStatus("current")
_PtpCurBitrateRX_Type = Integer32
_PtpCurBitrateRX_Object = MibScalar
ptpCurBitrateRX = _PtpCurBitrateRX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 9),
    _PtpCurBitrateRX_Type()
)
ptpCurBitrateRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurBitrateRX.setStatus("current")
_PtpCurBitrateTX_Type = Integer32
_PtpCurBitrateTX_Object = MibScalar
ptpCurBitrateTX = _PtpCurBitrateTX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 10),
    _PtpCurBitrateTX_Type()
)
ptpCurBitrateTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurBitrateTX.setStatus("current")
_PtpCurLoadRX_Type = Integer32
_PtpCurLoadRX_Object = MibScalar
ptpCurLoadRX = _PtpCurLoadRX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 11),
    _PtpCurLoadRX_Type()
)
ptpCurLoadRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurLoadRX.setStatus("current")
_PtpCurLoadPPSRX_Type = Integer32
_PtpCurLoadPPSRX_Object = MibScalar
ptpCurLoadPPSRX = _PtpCurLoadPPSRX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 12),
    _PtpCurLoadPPSRX_Type()
)
ptpCurLoadPPSRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurLoadPPSRX.setStatus("current")
_PtpCurLoadTX_Type = Integer32
_PtpCurLoadTX_Object = MibScalar
ptpCurLoadTX = _PtpCurLoadTX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 13),
    _PtpCurLoadTX_Type()
)
ptpCurLoadTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurLoadTX.setStatus("current")
_PtpCurLoadPPSTX_Type = Integer32
_PtpCurLoadPPSTX_Object = MibScalar
ptpCurLoadPPSTX = _PtpCurLoadPPSTX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 14),
    _PtpCurLoadPPSTX_Type()
)
ptpCurLoadPPSTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurLoadPPSTX.setStatus("current")
_PtpOutputBytes_Type = Counter32
_PtpOutputBytes_Object = MibScalar
ptpOutputBytes = _PtpOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 15),
    _PtpOutputBytes_Type()
)
ptpOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpOutputBytes.setStatus("current")
_PtpOutputPackets_Type = Counter32
_PtpOutputPackets_Object = MibScalar
ptpOutputPackets = _PtpOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 16),
    _PtpOutputPackets_Type()
)
ptpOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpOutputPackets.setStatus("current")
_PtpInputBytes_Type = Counter32
_PtpInputBytes_Object = MibScalar
ptpInputBytes = _PtpInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 17),
    _PtpInputBytes_Type()
)
ptpInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpInputBytes.setStatus("current")
_PtpInputPackets_Type = Counter32
_PtpInputPackets_Object = MibScalar
ptpInputPackets = _PtpInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 18),
    _PtpInputPackets_Type()
)
ptpInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpInputPackets.setStatus("current")
_PtpRetriesPercentTX_Type = Unsigned32
_PtpRetriesPercentTX_Object = MibScalar
ptpRetriesPercentTX = _PtpRetriesPercentTX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 19),
    _PtpRetriesPercentTX_Type()
)
ptpRetriesPercentTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpRetriesPercentTX.setStatus("current")
_PtpErrorsPercentTX_Type = Unsigned32
_PtpErrorsPercentTX_Object = MibScalar
ptpErrorsPercentTX = _PtpErrorsPercentTX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 20),
    _PtpErrorsPercentTX_Type()
)
ptpErrorsPercentTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpErrorsPercentTX.setStatus("current")
_PtpLinkDistance_Type = Integer32
_PtpLinkDistance_Object = MibScalar
ptpLinkDistance = _PtpLinkDistance_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 21),
    _PtpLinkDistance_Type()
)
ptpLinkDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpLinkDistance.setStatus("current")
_PtpCurBitrateRXindex_Type = Integer32
_PtpCurBitrateRXindex_Object = MibScalar
ptpCurBitrateRXindex = _PtpCurBitrateRXindex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 22),
    _PtpCurBitrateRXindex_Type()
)
ptpCurBitrateRXindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurBitrateRXindex.setStatus("current")
_PtpCurBitrateTXindex_Type = Integer32
_PtpCurBitrateTXindex_Object = MibScalar
ptpCurBitrateTXindex = _PtpCurBitrateTXindex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 23),
    _PtpCurBitrateTXindex_Type()
)
ptpCurBitrateTXindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurBitrateTXindex.setStatus("current")
_PtpRetriesPercentRX_Type = Unsigned32
_PtpRetriesPercentRX_Object = MibScalar
ptpRetriesPercentRX = _PtpRetriesPercentRX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 24),
    _PtpRetriesPercentRX_Type()
)
ptpRetriesPercentRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpRetriesPercentRX.setStatus("current")
_PtpErrorsPercentRX_Type = Unsigned32
_PtpErrorsPercentRX_Object = MibScalar
ptpErrorsPercentRX = _PtpErrorsPercentRX_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 25),
    _PtpErrorsPercentRX_Type()
)
ptpErrorsPercentRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpErrorsPercentRX.setStatus("current")
_PtpNeighborIfIndex_Type = Unsigned32
_PtpNeighborIfIndex_Object = MibScalar
ptpNeighborIfIndex = _PtpNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 26),
    _PtpNeighborIfIndex_Type()
)
ptpNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpNeighborIfIndex.setStatus("current")
_PtpCurRXpower_Type = Integer32
_PtpCurRXpower_Object = MibScalar
ptpCurRXpower = _PtpCurRXpower_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 27),
    _PtpCurRXpower_Type()
)
ptpCurRXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurRXpower.setStatus("current")
_PtpCurTXpower_Type = Integer32
_PtpCurTXpower_Object = MibScalar
ptpCurTXpower = _PtpCurTXpower_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 28),
    _PtpCurTXpower_Type()
)
ptpCurTXpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurTXpower.setStatus("current")
_PtpLinkDistanceMeters_Type = Integer32
_PtpLinkDistanceMeters_Object = MibScalar
ptpLinkDistanceMeters = _PtpLinkDistanceMeters_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 29),
    _PtpLinkDistanceMeters_Type()
)
ptpLinkDistanceMeters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpLinkDistanceMeters.setStatus("current")
_PtpLinkRxRSSI_Type = Integer32
_PtpLinkRxRSSI_Object = MibScalar
ptpLinkRxRSSI = _PtpLinkRxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 4, 30),
    _PtpLinkRxRSSI_Type()
)
ptpLinkRxRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpLinkRxRSSI.setStatus("current")


class _MintLinkStatus_Type(Integer32):
    """Custom type mintLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("multipoint", 3))
    )


_MintLinkStatus_Type.__name__ = "Integer32"
_MintLinkStatus_Object = MibScalar
mintLinkStatus = _MintLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 1, 1, 5),
    _MintLinkStatus_Type()
)
mintLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mintLinkStatus.setStatus("current")
_MintMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
mintMIBNotificationsPrefix = _MintMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 2)
)
_MintMIBNotifications_ObjectIdentity = ObjectIdentity
mintMIBNotifications = _MintMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 2, 0)
)
_MintMIBConformance_ObjectIdentity = ObjectIdentity
mintMIBConformance = _MintMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 3)
)

# Managed Objects groups

mintMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 3, 2)
)
mintMIBGroup.setObjects(
      *(("AQUAMINT-MIB", "netAddress"),
        ("AQUAMINT-MIB", "nodeType"),
        ("AQUAMINT-MIB", "nodeMode"),
        ("AQUAMINT-MIB", "linksCount"),
        ("AQUAMINT-MIB", "nodesCount"),
        ("AQUAMINT-MIB", "nodeInterfaceId"),
        ("AQUAMINT-MIB", "protocolEnabled"),
        ("AQUAMINT-MIB", "nodeName"),
        ("AQUAMINT-MIB", "autoBitrateEnable"),
        ("AQUAMINT-MIB", "autoBitrateAddition"),
        ("AQUAMINT-MIB", "autoBitrateMinLevel"),
        ("AQUAMINT-MIB", "extraCost"),
        ("AQUAMINT-MIB", "fixedCost"),
        ("AQUAMINT-MIB", "nodeID"),
        ("AQUAMINT-MIB", "ampLow"),
        ("AQUAMINT-MIB", "ampHigh"),
        ("AQUAMINT-MIB", "authMode"),
        ("AQUAMINT-MIB", "authRelay"),
        ("AQUAMINT-MIB", "scrambling"),
        ("AQUAMINT-MIB", "compress"),
        ("AQUAMINT-MIB", "overTheAirUpgradeEnable"),
        ("AQUAMINT-MIB", "overTheAirUpgradeSpeed"),
        ("AQUAMINT-MIB", "roaming"),
        ("AQUAMINT-MIB", "polling"),
        ("AQUAMINT-MIB", "mintInterfaceId"),
        ("AQUAMINT-MIB", "neighborAddress"),
        ("AQUAMINT-MIB", "linkName"),
        ("AQUAMINT-MIB", "linkCost"),
        ("AQUAMINT-MIB", "monitorAmpIn"),
        ("AQUAMINT-MIB", "monitorAmpOut"),
        ("AQUAMINT-MIB", "workingAmpIn"),
        ("AQUAMINT-MIB", "workingAmpOut"),
        ("AQUAMINT-MIB", "curBitrateRX"),
        ("AQUAMINT-MIB", "curBitrateTX"),
        ("AQUAMINT-MIB", "curLoadRX"),
        ("AQUAMINT-MIB", "curLoadPPSRX"),
        ("AQUAMINT-MIB", "curLoadTX"),
        ("AQUAMINT-MIB", "curLoadPPSTX"),
        ("AQUAMINT-MIB", "outputBytes"),
        ("AQUAMINT-MIB", "outputPackets"),
        ("AQUAMINT-MIB", "inputBytes"),
        ("AQUAMINT-MIB", "inputPackets"),
        ("AQUAMINT-MIB", "retriesPercentTX"),
        ("AQUAMINT-MIB", "errorsPercentTX"),
        ("AQUAMINT-MIB", "linkDistance"),
        ("AQUAMINT-MIB", "curBitrateRXindex"),
        ("AQUAMINT-MIB", "curBitrateTXindex"),
        ("AQUAMINT-MIB", "lostNeighborIfIndex"),
        ("AQUAMINT-MIB", "lostNeighborNetAddress"),
        ("AQUAMINT-MIB", "lostNeighborReason"),
        ("AQUAMINT-MIB", "lostNeighborName"),
        ("AQUAMINT-MIB", "mintBroadcastRate"),
        ("AQUAMINT-MIB", "noiseFloor"),
        ("AQUAMINT-MIB", "retriesPercentRX"),
        ("AQUAMINT-MIB", "errorsPercentRX"),
        ("AQUAMINT-MIB", "neighborIfIndex"),
        ("AQUAMINT-MIB", "curRXpower"),
        ("AQUAMINT-MIB", "curTXpower"),
        ("AQUAMINT-MIB", "secretKey"),
        ("AQUAMINT-MIB", "linksCountReal"),
        ("AQUAMINT-MIB", "linkDistanceMeters"),
        ("AQUAMINT-MIB", "ptpInterfaceId"),
        ("AQUAMINT-MIB", "ptpNeighborAddress"),
        ("AQUAMINT-MIB", "ptpLinkName"),
        ("AQUAMINT-MIB", "ptpLinkCost"),
        ("AQUAMINT-MIB", "ptpMonitorAmpIn"),
        ("AQUAMINT-MIB", "ptpMonitorAmpOut"),
        ("AQUAMINT-MIB", "ptpWorkingAmpIn"),
        ("AQUAMINT-MIB", "ptpWorkingAmpOut"),
        ("AQUAMINT-MIB", "ptpCurBitrateRX"),
        ("AQUAMINT-MIB", "ptpCurBitrateTX"),
        ("AQUAMINT-MIB", "ptpCurLoadRX"),
        ("AQUAMINT-MIB", "ptpCurLoadPPSRX"),
        ("AQUAMINT-MIB", "ptpCurLoadTX"),
        ("AQUAMINT-MIB", "ptpCurLoadPPSTX"),
        ("AQUAMINT-MIB", "ptpOutputBytes"),
        ("AQUAMINT-MIB", "ptpOutputPackets"),
        ("AQUAMINT-MIB", "ptpInputBytes"),
        ("AQUAMINT-MIB", "ptpInputPackets"),
        ("AQUAMINT-MIB", "ptpRetriesPercentTX"),
        ("AQUAMINT-MIB", "ptpErrorsPercentTX"),
        ("AQUAMINT-MIB", "ptpLinkDistance"),
        ("AQUAMINT-MIB", "ptpCurBitrateRXindex"),
        ("AQUAMINT-MIB", "ptpCurBitrateTXindex"),
        ("AQUAMINT-MIB", "ptpRetriesPercentRX"),
        ("AQUAMINT-MIB", "ptpErrorsPercentRX"),
        ("AQUAMINT-MIB", "ptpNeighborIfIndex"),
        ("AQUAMINT-MIB", "ptpCurRXpower"),
        ("AQUAMINT-MIB", "ptpCurTXpower"),
        ("AQUAMINT-MIB", "ptpLinkDistanceMeters"),
        ("AQUAMINT-MIB", "ptpLinkRxRSSI"),
        ("AQUAMINT-MIB", "mintLinkStatus"))
)
if mibBuilder.loadTexts:
    mintMIBGroup.setStatus("current")


# Notification objects

mintTopologyNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 2, 0, 1)
)
mintTopologyNotification.setObjects(
      *(("AQUASYSTEM-MIB", "sysSerialNumber"),
        ("AQUASYSTEM-MIB", "sysTrapSequence"),
        ("AQUAMINT-MIB", "nodeInterfaceId"),
        ("AQUAMINT-MIB", "netAddress"),
        ("AQUAMINT-MIB", "neighborAddress"),
        ("AQUAMINT-MIB", "linkCost"),
        ("AQUAMINT-MIB", "neighborIfIndex"))
)
if mibBuilder.loadTexts:
    mintTopologyNotification.setStatus(
        "current"
    )

mintNewNeighborNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 2, 0, 2)
)
mintNewNeighborNotification.setObjects(
      *(("AQUASYSTEM-MIB", "sysSerialNumber"),
        ("AQUASYSTEM-MIB", "sysTrapSequence"),
        ("AQUAMINT-MIB", "mintInterfaceId"),
        ("AQUAMINT-MIB", "neighborAddress"),
        ("AQUAMINT-MIB", "linkName"))
)
if mibBuilder.loadTexts:
    mintNewNeighborNotification.setStatus(
        "current"
    )

mintNeighborLostNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 2, 0, 3)
)
mintNeighborLostNotification.setObjects(
      *(("AQUASYSTEM-MIB", "sysSerialNumber"),
        ("AQUASYSTEM-MIB", "sysTrapSequence"),
        ("AQUAMINT-MIB", "lostNeighborIfIndex"),
        ("AQUAMINT-MIB", "lostNeighborNetAddress"),
        ("AQUAMINT-MIB", "lostNeighborReason"),
        ("AQUAMINT-MIB", "lostNeighborName"))
)
if mibBuilder.loadTexts:
    mintNeighborLostNotification.setStatus(
        "current"
    )

mintLinkRetriesChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 2, 0, 4)
)
mintLinkRetriesChanged.setObjects(
      *(("AQUASYSTEM-MIB", "sysSerialNumber"),
        ("AQUASYSTEM-MIB", "sysTrapSequence"),
        ("AQUAMINT-MIB", "retriesPercentTX"),
        ("AQUAMINT-MIB", "mintInterfaceId"),
        ("AQUAMINT-MIB", "neighborAddress"))
)
if mibBuilder.loadTexts:
    mintLinkRetriesChanged.setStatus(
        "current"
    )

mintLinkBitrateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 2, 0, 5)
)
mintLinkBitrateChanged.setObjects(
      *(("AQUASYSTEM-MIB", "sysSerialNumber"),
        ("AQUASYSTEM-MIB", "sysTrapSequence"),
        ("AQUAMINT-MIB", "curBitrateTX"),
        ("AQUAMINT-MIB", "nodeInterfaceId"),
        ("AQUAMINT-MIB", "neighborAddress"))
)
if mibBuilder.loadTexts:
    mintLinkBitrateChanged.setStatus(
        "current"
    )

minLinkSignalLevelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 2, 0, 6)
)
minLinkSignalLevelChanged.setObjects(
      *(("AQUASYSTEM-MIB", "sysSerialNumber"),
        ("AQUASYSTEM-MIB", "sysTrapSequence"),
        ("AQUAMINT-MIB", "monitorAmpOut"),
        ("AQUAMINT-MIB", "mintInterfaceId"),
        ("AQUAMINT-MIB", "neighborAddress"))
)
if mibBuilder.loadTexts:
    minLinkSignalLevelChanged.setStatus(
        "current"
    )


# Notifications groups

mintNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 5, 3, 1)
)
mintNotifications.setObjects(
      *(("AQUAMINT-MIB", "mintTopologyNotification"),
        ("AQUAMINT-MIB", "mintNewNeighborNotification"),
        ("AQUAMINT-MIB", "mintNeighborLostNotification"),
        ("AQUAMINT-MIB", "mintLinkRetriesChanged"),
        ("AQUAMINT-MIB", "mintLinkBitrateChanged"),
        ("AQUAMINT-MIB", "minLinkSignalLevelChanged"))
)
if mibBuilder.loadTexts:
    mintNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AQUAMINT-MIB",
    **{"aquamintMIB": aquamintMIB,
       "mintMIBObjects": mintMIBObjects,
       "mint": mint,
       "mintNodesTable": mintNodesTable,
       "mintNodesEntry": mintNodesEntry,
       "netAddress": netAddress,
       "nodeType": nodeType,
       "nodeMode": nodeMode,
       "linksCount": linksCount,
       "nodesCount": nodesCount,
       "nodeInterfaceId": nodeInterfaceId,
       "protocolEnabled": protocolEnabled,
       "nodeName": nodeName,
       "autoBitrateEnable": autoBitrateEnable,
       "autoBitrateAddition": autoBitrateAddition,
       "autoBitrateMinLevel": autoBitrateMinLevel,
       "extraCost": extraCost,
       "fixedCost": fixedCost,
       "nodeID": nodeID,
       "ampLow": ampLow,
       "ampHigh": ampHigh,
       "authMode": authMode,
       "authRelay": authRelay,
       "scrambling": scrambling,
       "compress": compress,
       "overTheAirUpgradeEnable": overTheAirUpgradeEnable,
       "overTheAirUpgradeSpeed": overTheAirUpgradeSpeed,
       "roaming": roaming,
       "polling": polling,
       "mintBroadcastRate": mintBroadcastRate,
       "noiseFloor": noiseFloor,
       "secretKey": secretKey,
       "linksCountReal": linksCountReal,
       "rxCapacity": rxCapacity,
       "txCapacity": txCapacity,
       "mintLinksTable": mintLinksTable,
       "mintLinksEntry": mintLinksEntry,
       "mintInterfaceId": mintInterfaceId,
       "neighborAddress": neighborAddress,
       "linkName": linkName,
       "linkCost": linkCost,
       "monitorAmpIn": monitorAmpIn,
       "monitorAmpOut": monitorAmpOut,
       "workingAmpIn": workingAmpIn,
       "workingAmpOut": workingAmpOut,
       "curBitrateRX": curBitrateRX,
       "curBitrateTX": curBitrateTX,
       "curLoadRX": curLoadRX,
       "curLoadPPSRX": curLoadPPSRX,
       "curLoadTX": curLoadTX,
       "curLoadPPSTX": curLoadPPSTX,
       "outputBytes": outputBytes,
       "outputPackets": outputPackets,
       "inputBytes": inputBytes,
       "inputPackets": inputPackets,
       "retriesPercentTX": retriesPercentTX,
       "errorsPercentTX": errorsPercentTX,
       "linkDistance": linkDistance,
       "curBitrateRXindex": curBitrateRXindex,
       "curBitrateTXindex": curBitrateTXindex,
       "retriesPercentRX": retriesPercentRX,
       "errorsPercentRX": errorsPercentRX,
       "neighborIfIndex": neighborIfIndex,
       "curRXpower": curRXpower,
       "curTXpower": curTXpower,
       "linkDistanceMeters": linkDistanceMeters,
       "rxRSSI": rxRSSI,
       "mintLostNeighbor": mintLostNeighbor,
       "lostNeighborIfIndex": lostNeighborIfIndex,
       "lostNeighborNetAddress": lostNeighborNetAddress,
       "lostNeighborReason": lostNeighborReason,
       "lostNeighborName": lostNeighborName,
       "mintPtpLink": mintPtpLink,
       "ptpInterfaceId": ptpInterfaceId,
       "ptpNeighborAddress": ptpNeighborAddress,
       "ptpLinkName": ptpLinkName,
       "ptpLinkCost": ptpLinkCost,
       "ptpMonitorAmpIn": ptpMonitorAmpIn,
       "ptpMonitorAmpOut": ptpMonitorAmpOut,
       "ptpWorkingAmpIn": ptpWorkingAmpIn,
       "ptpWorkingAmpOut": ptpWorkingAmpOut,
       "ptpCurBitrateRX": ptpCurBitrateRX,
       "ptpCurBitrateTX": ptpCurBitrateTX,
       "ptpCurLoadRX": ptpCurLoadRX,
       "ptpCurLoadPPSRX": ptpCurLoadPPSRX,
       "ptpCurLoadTX": ptpCurLoadTX,
       "ptpCurLoadPPSTX": ptpCurLoadPPSTX,
       "ptpOutputBytes": ptpOutputBytes,
       "ptpOutputPackets": ptpOutputPackets,
       "ptpInputBytes": ptpInputBytes,
       "ptpInputPackets": ptpInputPackets,
       "ptpRetriesPercentTX": ptpRetriesPercentTX,
       "ptpErrorsPercentTX": ptpErrorsPercentTX,
       "ptpLinkDistance": ptpLinkDistance,
       "ptpCurBitrateRXindex": ptpCurBitrateRXindex,
       "ptpCurBitrateTXindex": ptpCurBitrateTXindex,
       "ptpRetriesPercentRX": ptpRetriesPercentRX,
       "ptpErrorsPercentRX": ptpErrorsPercentRX,
       "ptpNeighborIfIndex": ptpNeighborIfIndex,
       "ptpCurRXpower": ptpCurRXpower,
       "ptpCurTXpower": ptpCurTXpower,
       "ptpLinkDistanceMeters": ptpLinkDistanceMeters,
       "ptpLinkRxRSSI": ptpLinkRxRSSI,
       "mintLinkStatus": mintLinkStatus,
       "mintMIBNotificationsPrefix": mintMIBNotificationsPrefix,
       "mintMIBNotifications": mintMIBNotifications,
       "mintTopologyNotification": mintTopologyNotification,
       "mintNewNeighborNotification": mintNewNeighborNotification,
       "mintNeighborLostNotification": mintNeighborLostNotification,
       "mintLinkRetriesChanged": mintLinkRetriesChanged,
       "mintLinkBitrateChanged": mintLinkBitrateChanged,
       "minLinkSignalLevelChanged": minLinkSignalLevelChanged,
       "mintMIBConformance": mintMIBConformance,
       "mintNotifications": mintNotifications,
       "mintMIBGroup": mintMIBGroup}
)
