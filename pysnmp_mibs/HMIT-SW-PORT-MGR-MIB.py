# SNMP MIB module (HMIT-SW-PORT-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HMIT-SW-PORT-MGR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:10 2025
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

(hmITSwitchTech,) = mibBuilder.importSymbols(
    "HMIT-SMI",
    "hmITSwitchTech")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hmITSwPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    hmITSwPortMIB.setRevisions(
        ("2010-01-08 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmITSwPortmgrMIB_ObjectIdentity = ObjectIdentity
hmITSwPortmgrMIB = _HmITSwPortmgrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13)
)
_HmITPortmgrTable_Object = MibTable
hmITPortmgrTable = _HmITPortmgrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2)
)
if mibBuilder.loadTexts:
    hmITPortmgrTable.setStatus("current")
_HmITPortmgrEntry_Object = MibTableRow
hmITPortmgrEntry = _HmITPortmgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1)
)
hmITPortmgrEntry.setIndexNames(
    (0, "HMIT-SW-PORT-MGR-MIB", "hmITPortId"),
)
if mibBuilder.loadTexts:
    hmITPortmgrEntry.setStatus("current")


class _HmITPortId_Type(Integer32):
    """Custom type hmITPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HmITPortId_Type.__name__ = "Integer32"
_HmITPortId_Object = MibTableColumn
hmITPortId = _HmITPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 1),
    _HmITPortId_Type()
)
hmITPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmITPortId.setStatus("current")


class _HmITMgrLinkStatus_Type(Integer32):
    """Custom type hmITMgrLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noshutdown", 1),
          ("shutdown", 2))
    )


_HmITMgrLinkStatus_Type.__name__ = "Integer32"
_HmITMgrLinkStatus_Object = MibTableColumn
hmITMgrLinkStatus = _HmITMgrLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 2),
    _HmITMgrLinkStatus_Type()
)
hmITMgrLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITMgrLinkStatus.setStatus("current")


class _HmITDescription_Type(DisplayString):
    """Custom type hmITDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_HmITDescription_Type.__name__ = "DisplayString"
_HmITDescription_Object = MibTableColumn
hmITDescription = _HmITDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 3),
    _HmITDescription_Type()
)
hmITDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITDescription.setStatus("current")


class _HmITMgrDuplex_Type(Integer32):
    """Custom type hmITMgrDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duplexauto", 1),
          ("duplexhalf", 2),
          ("duplexfull", 3))
    )


_HmITMgrDuplex_Type.__name__ = "Integer32"
_HmITMgrDuplex_Object = MibTableColumn
hmITMgrDuplex = _HmITMgrDuplex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 4),
    _HmITMgrDuplex_Type()
)
hmITMgrDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITMgrDuplex.setStatus("current")


class _HmITMgrSpeed_Type(Integer32):
    """Custom type hmITMgrSpeed based on Integer32"""
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
              8,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("speedauto", 1),
          ("speed10M", 2),
          ("speed100M", 3),
          ("speed1000M", 4),
          ("speed10000M", 5),
          ("speed40000M", 6),
          ("speed100G", 7),
          ("speed25000M", 8),
          ("speed2500M", 11),
          ("speed13000M", 12))
    )


_HmITMgrSpeed_Type.__name__ = "Integer32"
_HmITMgrSpeed_Object = MibTableColumn
hmITMgrSpeed = _HmITMgrSpeed_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 5),
    _HmITMgrSpeed_Type()
)
hmITMgrSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITMgrSpeed.setStatus("current")


class _HmITFlowControl_Type(Integer32):
    """Custom type hmITFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmITFlowControl_Type.__name__ = "Integer32"
_HmITFlowControl_Object = MibTableColumn
hmITFlowControl = _HmITFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 6),
    _HmITFlowControl_Type()
)
hmITFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITFlowControl.setStatus("current")


class _HmITMdix_Type(Integer32):
    """Custom type hmITMdix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("normal", 2),
          ("cross", 3))
    )


_HmITMdix_Type.__name__ = "Integer32"
_HmITMdix_Object = MibTableColumn
hmITMdix = _HmITMdix_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 7),
    _HmITMdix_Type()
)
hmITMdix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITMdix.setStatus("current")


class _HmITMtu_Type(Integer32):
    """Custom type hmITMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 12288),
    )


_HmITMtu_Type.__name__ = "Integer32"
_HmITMtu_Object = MibTableColumn
hmITMtu = _HmITMtu_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 8),
    _HmITMtu_Type()
)
hmITMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITMtu.setStatus("current")


class _HmITLinkDelay_Type(Integer32):
    """Custom type hmITLinkDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HmITLinkDelay_Type.__name__ = "Integer32"
_HmITLinkDelay_Object = MibTableColumn
hmITLinkDelay = _HmITLinkDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 9),
    _HmITLinkDelay_Type()
)
hmITLinkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITLinkDelay.setStatus("current")


class _HmITLoopBack_Type(Integer32):
    """Custom type hmITLoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("internal", 2),
          ("external", 3))
    )


_HmITLoopBack_Type.__name__ = "Integer32"
_HmITLoopBack_Object = MibTableColumn
hmITLoopBack = _HmITLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 10),
    _HmITLoopBack_Type()
)
hmITLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITLoopBack.setStatus("current")


class _HmITActualLinkStatus_Type(Integer32):
    """Custom type hmITActualLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_HmITActualLinkStatus_Type.__name__ = "Integer32"
_HmITActualLinkStatus_Object = MibTableColumn
hmITActualLinkStatus = _HmITActualLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 11),
    _HmITActualLinkStatus_Type()
)
hmITActualLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITActualLinkStatus.setStatus("current")


class _HmITActualDuplex_Type(Integer32):
    """Custom type hmITActualDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duplexunknown", 1),
          ("duplexhalf", 2),
          ("duplexfull", 3))
    )


_HmITActualDuplex_Type.__name__ = "Integer32"
_HmITActualDuplex_Object = MibTableColumn
hmITActualDuplex = _HmITActualDuplex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 12),
    _HmITActualDuplex_Type()
)
hmITActualDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITActualDuplex.setStatus("current")


class _HmITActualSpeed_Type(Integer32):
    """Custom type hmITActualSpeed based on Integer32"""
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
              8,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("speedauto", 1),
          ("speed10M", 2),
          ("speed100M", 3),
          ("speed1000M", 4),
          ("speed10000M", 5),
          ("speed40000M", 6),
          ("speed100G", 7),
          ("speed25000M", 8),
          ("speed2500M", 11),
          ("speed13000M", 12))
    )


_HmITActualSpeed_Type.__name__ = "Integer32"
_HmITActualSpeed_Object = MibTableColumn
hmITActualSpeed = _HmITActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 13),
    _HmITActualSpeed_Type()
)
hmITActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITActualSpeed.setStatus("current")


class _HmITPhyType_Type(Integer32):
    """Custom type hmITPhyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_HmITPhyType_Type.__name__ = "Integer32"
_HmITPhyType_Object = MibTableColumn
hmITPhyType = _HmITPhyType_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 14),
    _HmITPhyType_Type()
)
hmITPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITPhyType.setStatus("current")
_HmITPhyMacAddress_Type = MacAddress
_HmITPhyMacAddress_Object = MibTableColumn
hmITPhyMacAddress = _HmITPhyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 15),
    _HmITPhyMacAddress_Type()
)
hmITPhyMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITPhyMacAddress.setStatus("current")
_HmITPortMgrPortAbility_Type = Counter64
_HmITPortMgrPortAbility_Object = MibTableColumn
hmITPortMgrPortAbility = _HmITPortMgrPortAbility_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 16),
    _HmITPortMgrPortAbility_Type()
)
hmITPortMgrPortAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITPortMgrPortAbility.setStatus("current")


class _HmITPortMgrPortType_Type(Integer32):
    """Custom type hmITPortMgrPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("wan", 2))
    )


_HmITPortMgrPortType_Type.__name__ = "Integer32"
_HmITPortMgrPortType_Object = MibTableColumn
hmITPortMgrPortType = _HmITPortMgrPortType_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 17),
    _HmITPortMgrPortType_Type()
)
hmITPortMgrPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITPortMgrPortType.setStatus("current")


class _HmITPortMgrJumbo_Type(Integer32):
    """Custom type hmITPortMgrJumbo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HmITPortMgrJumbo_Type.__name__ = "Integer32"
_HmITPortMgrJumbo_Object = MibTableColumn
hmITPortMgrJumbo = _HmITPortMgrJumbo_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 18),
    _HmITPortMgrJumbo_Type()
)
hmITPortMgrJumbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITPortMgrJumbo.setStatus("current")


class _HmITPortMgrMediumType_Type(Integer32):
    """Custom type hmITPortMgrMediumType based on Integer32"""
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
        *(("auto", 1),
          ("copper", 2),
          ("fiber", 3),
          ("fiber2copper", 4))
    )


_HmITPortMgrMediumType_Type.__name__ = "Integer32"
_HmITPortMgrMediumType_Object = MibTableColumn
hmITPortMgrMediumType = _HmITPortMgrMediumType_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 19),
    _HmITPortMgrMediumType_Type()
)
hmITPortMgrMediumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITPortMgrMediumType.setStatus("current")


class _HmITPeerDescription_Type(DisplayString):
    """Custom type hmITPeerDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_HmITPeerDescription_Type.__name__ = "DisplayString"
_HmITPeerDescription_Object = MibTableColumn
hmITPeerDescription = _HmITPeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 20),
    _HmITPeerDescription_Type()
)
hmITPeerDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITPeerDescription.setStatus("current")
_HmITPortMgrRowStatus_Type = RowStatus
_HmITPortMgrRowStatus_Object = MibTableColumn
hmITPortMgrRowStatus = _HmITPortMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 2, 1, 21),
    _HmITPortMgrRowStatus_Type()
)
hmITPortMgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmITPortMgrRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMIT-SW-PORT-MGR-MIB",
    **{"hmITSwPortMIB": hmITSwPortMIB,
       "hmITSwPortmgrMIB": hmITSwPortmgrMIB,
       "hmITPortmgrTable": hmITPortmgrTable,
       "hmITPortmgrEntry": hmITPortmgrEntry,
       "hmITPortId": hmITPortId,
       "hmITMgrLinkStatus": hmITMgrLinkStatus,
       "hmITDescription": hmITDescription,
       "hmITMgrDuplex": hmITMgrDuplex,
       "hmITMgrSpeed": hmITMgrSpeed,
       "hmITFlowControl": hmITFlowControl,
       "hmITMdix": hmITMdix,
       "hmITMtu": hmITMtu,
       "hmITLinkDelay": hmITLinkDelay,
       "hmITLoopBack": hmITLoopBack,
       "hmITActualLinkStatus": hmITActualLinkStatus,
       "hmITActualDuplex": hmITActualDuplex,
       "hmITActualSpeed": hmITActualSpeed,
       "hmITPhyType": hmITPhyType,
       "hmITPhyMacAddress": hmITPhyMacAddress,
       "hmITPortMgrPortAbility": hmITPortMgrPortAbility,
       "hmITPortMgrPortType": hmITPortMgrPortType,
       "hmITPortMgrJumbo": hmITPortMgrJumbo,
       "hmITPortMgrMediumType": hmITPortMgrMediumType,
       "hmITPeerDescription": hmITPeerDescription,
       "hmITPortMgrRowStatus": hmITPortMgrRowStatus}
)
