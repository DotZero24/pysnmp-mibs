# SNMP MIB module (CTRON-ISDN-CONFIGURATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cabletron/CTRON-ISDN-CONFIGURATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:54:46 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4)
)
_Ctron_ObjectIdentity = ObjectIdentity
ctron = _Ctron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1)
)
_CtDataLink_ObjectIdentity = ObjectIdentity
ctDataLink = _CtDataLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2)
)
_CtronWan_ObjectIdentity = ObjectIdentity
ctronWan = _CtronWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7)
)
_CtISDNconfigMib_ObjectIdentity = ObjectIdentity
ctISDNconfigMib = _CtISDNconfigMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4)
)
_CtISDNcontrol_ObjectIdentity = ObjectIdentity
ctISDNcontrol = _CtISDNcontrol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1)
)
_IsdnDchTable_Object = MibTable
isdnDchTable = _IsdnDchTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1)
)
if mibBuilder.loadTexts:
    isdnDchTable.setStatus("mandatory")
_IsdnDchEntry_Object = MibTableRow
isdnDchEntry = _IsdnDchEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1)
)
isdnDchEntry.setIndexNames(
    (0, "CTRON-ISDN-CONFIGURATION-MIB", "isdnDchIndex"),
)
if mibBuilder.loadTexts:
    isdnDchEntry.setStatus("mandatory")
_IsdnDchIndex_Type = Integer32
_IsdnDchIndex_Object = MibTableColumn
isdnDchIndex = _IsdnDchIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 1),
    _IsdnDchIndex_Type()
)
isdnDchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchIndex.setStatus("mandatory")


class _IsdnDchRateAccess_Type(Integer32):
    """Custom type isdnDchRateAccess based on Integer32"""
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
        *(("other", 1),
          ("bri1", 2),
          ("pri1", 3),
          ("pri2", 4))
    )


_IsdnDchRateAccess_Type.__name__ = "Integer32"
_IsdnDchRateAccess_Object = MibTableColumn
isdnDchRateAccess = _IsdnDchRateAccess_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 2),
    _IsdnDchRateAccess_Type()
)
isdnDchRateAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchRateAccess.setStatus("mandatory")
_IsdnDchAllowedCh_Type = Integer32
_IsdnDchAllowedCh_Object = MibTableColumn
isdnDchAllowedCh = _IsdnDchAllowedCh_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 3),
    _IsdnDchAllowedCh_Type()
)
isdnDchAllowedCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchAllowedCh.setStatus("mandatory")
_IsdnDchChInUse_Type = Integer32
_IsdnDchChInUse_Object = MibTableColumn
isdnDchChInUse = _IsdnDchChInUse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 4),
    _IsdnDchChInUse_Type()
)
isdnDchChInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchChInUse.setStatus("mandatory")


class _IsdnDchSupportedSwitches_Type(Integer32):
    """Custom type isdnDchSupportedSwitches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              10,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("bri5ESS", 2),
          ("bridms100", 5),
          ("brini1", 10),
          ("pri4ESS", 16),
          ("pri5ESS", 17))
    )


_IsdnDchSupportedSwitches_Type.__name__ = "Integer32"
_IsdnDchSupportedSwitches_Object = MibTableColumn
isdnDchSupportedSwitches = _IsdnDchSupportedSwitches_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 5),
    _IsdnDchSupportedSwitches_Type()
)
isdnDchSupportedSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchSupportedSwitches.setStatus("mandatory")


class _IsdnDchSwitchType_Type(Integer32):
    """Custom type isdnDchSwitchType based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              10,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("bri5ESS", 2),
          ("bridms100", 5),
          ("brini1", 10),
          ("pri4ESS", 16),
          ("pri5ESS", 17))
    )


_IsdnDchSwitchType_Type.__name__ = "Integer32"
_IsdnDchSwitchType_Object = MibTableColumn
isdnDchSwitchType = _IsdnDchSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 6),
    _IsdnDchSwitchType_Type()
)
isdnDchSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDchSwitchType.setStatus("mandatory")


class _IsdnDchSPID1_Type(OctetString):
    """Custom type isdnDchSPID1 based on OctetString"""
    defaultValue = OctetString("")


_IsdnDchSPID1_Type.__name__ = "OctetString"
_IsdnDchSPID1_Object = MibTableColumn
isdnDchSPID1 = _IsdnDchSPID1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 7),
    _IsdnDchSPID1_Type()
)
isdnDchSPID1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDchSPID1.setStatus("mandatory")


class _IsdnDchSPID2_Type(OctetString):
    """Custom type isdnDchSPID2 based on OctetString"""
    defaultValue = OctetString("")


_IsdnDchSPID2_Type.__name__ = "OctetString"
_IsdnDchSPID2_Object = MibTableColumn
isdnDchSPID2 = _IsdnDchSPID2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 8),
    _IsdnDchSPID2_Type()
)
isdnDchSPID2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDchSPID2.setStatus("mandatory")


class _IsdnDchDirNum1_Type(OctetString):
    """Custom type isdnDchDirNum1 based on OctetString"""
    defaultValue = OctetString("")


_IsdnDchDirNum1_Type.__name__ = "OctetString"
_IsdnDchDirNum1_Object = MibTableColumn
isdnDchDirNum1 = _IsdnDchDirNum1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 9),
    _IsdnDchDirNum1_Type()
)
isdnDchDirNum1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDchDirNum1.setStatus("mandatory")


class _IsdnDchDirNum2_Type(OctetString):
    """Custom type isdnDchDirNum2 based on OctetString"""
    defaultValue = OctetString("")


_IsdnDchDirNum2_Type.__name__ = "OctetString"
_IsdnDchDirNum2_Object = MibTableColumn
isdnDchDirNum2 = _IsdnDchDirNum2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 10),
    _IsdnDchDirNum2_Type()
)
isdnDchDirNum2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDchDirNum2.setStatus("mandatory")


class _IsdnDchOperStatus_Type(Integer32):
    """Custom type isdnDchOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_IsdnDchOperStatus_Type.__name__ = "Integer32"
_IsdnDchOperStatus_Object = MibTableColumn
isdnDchOperStatus = _IsdnDchOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 11),
    _IsdnDchOperStatus_Type()
)
isdnDchOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchOperStatus.setStatus("mandatory")
_DialCtlNbrCfgTable_Object = MibTable
dialCtlNbrCfgTable = _DialCtlNbrCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2)
)
if mibBuilder.loadTexts:
    dialCtlNbrCfgTable.setStatus("mandatory")
_DialCtlNbrCfgEntry_Object = MibTableRow
dialCtlNbrCfgEntry = _DialCtlNbrCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2, 1)
)
dialCtlNbrCfgEntry.setIndexNames(
    (0, "CTRON-ISDN-CONFIGURATION-MIB", "dialCtlNbrCfgId"),
    (0, "CTRON-ISDN-CONFIGURATION-MIB", "dialCtlNbrCfgIndex"),
)
if mibBuilder.loadTexts:
    dialCtlNbrCfgEntry.setStatus("mandatory")


class _DialCtlNbrCfgId_Type(Integer32):
    """Custom type dialCtlNbrCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DialCtlNbrCfgId_Type.__name__ = "Integer32"
_DialCtlNbrCfgId_Object = MibTableColumn
dialCtlNbrCfgId = _DialCtlNbrCfgId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2, 1, 1),
    _DialCtlNbrCfgId_Type()
)
dialCtlNbrCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialCtlNbrCfgId.setStatus("mandatory")


class _DialCtlNbrCfgIndex_Type(Integer32):
    """Custom type dialCtlNbrCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DialCtlNbrCfgIndex_Type.__name__ = "Integer32"
_DialCtlNbrCfgIndex_Object = MibTableColumn
dialCtlNbrCfgIndex = _DialCtlNbrCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2, 1, 2),
    _DialCtlNbrCfgIndex_Type()
)
dialCtlNbrCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialCtlNbrCfgIndex.setStatus("mandatory")


class _DialCtlNbrCfgIfIndex_Type(Integer32):
    """Custom type dialCtlNbrCfgIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DialCtlNbrCfgIfIndex_Type.__name__ = "Integer32"
_DialCtlNbrCfgIfIndex_Object = MibTableColumn
dialCtlNbrCfgIfIndex = _DialCtlNbrCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2, 1, 3),
    _DialCtlNbrCfgIfIndex_Type()
)
dialCtlNbrCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialCtlNbrCfgIfIndex.setStatus("mandatory")


class _DialCtlNbrCfgOriginateAddress_Type(DisplayString):
    """Custom type dialCtlNbrCfgOriginateAddress based on DisplayString"""
    defaultValue = OctetString("")


_DialCtlNbrCfgOriginateAddress_Type.__name__ = "DisplayString"
_DialCtlNbrCfgOriginateAddress_Object = MibTableColumn
dialCtlNbrCfgOriginateAddress = _DialCtlNbrCfgOriginateAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2, 1, 4),
    _DialCtlNbrCfgOriginateAddress_Type()
)
dialCtlNbrCfgOriginateAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialCtlNbrCfgOriginateAddress.setStatus("mandatory")


class _DialCtlNbrCfgAnswerAddress_Type(DisplayString):
    """Custom type dialCtlNbrCfgAnswerAddress based on DisplayString"""
    defaultValue = OctetString("")


_DialCtlNbrCfgAnswerAddress_Type.__name__ = "DisplayString"
_DialCtlNbrCfgAnswerAddress_Object = MibTableColumn
dialCtlNbrCfgAnswerAddress = _DialCtlNbrCfgAnswerAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2, 1, 5),
    _DialCtlNbrCfgAnswerAddress_Type()
)
dialCtlNbrCfgAnswerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialCtlNbrCfgAnswerAddress.setStatus("mandatory")
_RmtProfileTable_Object = MibTable
rmtProfileTable = _RmtProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3)
)
if mibBuilder.loadTexts:
    rmtProfileTable.setStatus("mandatory")
_RmtProfileEntry_Object = MibTableRow
rmtProfileEntry = _RmtProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1)
)
rmtProfileEntry.setIndexNames(
    (0, "CTRON-ISDN-CONFIGURATION-MIB", "rmtProfileEntryIndex"),
)
if mibBuilder.loadTexts:
    rmtProfileEntry.setStatus("mandatory")


class _RmtProfileEntryIndex_Type(Integer32):
    """Custom type rmtProfileEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RmtProfileEntryIndex_Type.__name__ = "Integer32"
_RmtProfileEntryIndex_Object = MibTableColumn
rmtProfileEntryIndex = _RmtProfileEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 1),
    _RmtProfileEntryIndex_Type()
)
rmtProfileEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtProfileEntryIndex.setStatus("mandatory")


class _RmtProfileEntryName_Type(OctetString):
    """Custom type rmtProfileEntryName based on OctetString"""
    defaultValue = OctetString("")


_RmtProfileEntryName_Type.__name__ = "OctetString"
_RmtProfileEntryName_Object = MibTableColumn
rmtProfileEntryName = _RmtProfileEntryName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 2),
    _RmtProfileEntryName_Type()
)
rmtProfileEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryName.setStatus("mandatory")


class _RmtProfileEntryMakerName_Type(OctetString):
    """Custom type rmtProfileEntryMakerName based on OctetString"""
    defaultValue = OctetString("")


_RmtProfileEntryMakerName_Type.__name__ = "OctetString"
_RmtProfileEntryMakerName_Object = MibTableColumn
rmtProfileEntryMakerName = _RmtProfileEntryMakerName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 3),
    _RmtProfileEntryMakerName_Type()
)
rmtProfileEntryMakerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryMakerName.setStatus("mandatory")


class _RmtProfileEntryAction_Type(Integer32):
    """Custom type rmtProfileEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("connect", 2),
          ("hangup", 3))
    )


_RmtProfileEntryAction_Type.__name__ = "Integer32"
_RmtProfileEntryAction_Object = MibTableColumn
rmtProfileEntryAction = _RmtProfileEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 4),
    _RmtProfileEntryAction_Type()
)
rmtProfileEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryAction.setStatus("mandatory")


class _RmtProfileEntryState_Type(Integer32):
    """Custom type rmtProfileEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("calling", 2),
          ("ringing", 3),
          ("connected", 4),
          ("answering", 5),
          ("answered", 6))
    )


_RmtProfileEntryState_Type.__name__ = "Integer32"
_RmtProfileEntryState_Object = MibTableColumn
rmtProfileEntryState = _RmtProfileEntryState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 5),
    _RmtProfileEntryState_Type()
)
rmtProfileEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtProfileEntryState.setStatus("mandatory")


class _RmtProfileEntryMaxNeighbor_Type(Integer32):
    """Custom type rmtProfileEntryMaxNeighbor based on Integer32"""
    defaultValue = 1


_RmtProfileEntryMaxNeighbor_Type.__name__ = "Integer32"
_RmtProfileEntryMaxNeighbor_Object = MibTableColumn
rmtProfileEntryMaxNeighbor = _RmtProfileEntryMaxNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 6),
    _RmtProfileEntryMaxNeighbor_Type()
)
rmtProfileEntryMaxNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtProfileEntryMaxNeighbor.setStatus("mandatory")
_RmtProfileEntryBchInUse_Type = Integer32
_RmtProfileEntryBchInUse_Object = MibTableColumn
rmtProfileEntryBchInUse = _RmtProfileEntryBchInUse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 7),
    _RmtProfileEntryBchInUse_Type()
)
rmtProfileEntryBchInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtProfileEntryBchInUse.setStatus("mandatory")


class _RmtProfileEntryLinkHead_Type(Integer32):
    """Custom type rmtProfileEntryLinkHead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_RmtProfileEntryLinkHead_Type.__name__ = "Integer32"
_RmtProfileEntryLinkHead_Object = MibTableColumn
rmtProfileEntryLinkHead = _RmtProfileEntryLinkHead_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 8),
    _RmtProfileEntryLinkHead_Type()
)
rmtProfileEntryLinkHead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtProfileEntryLinkHead.setStatus("mandatory")


class _RmtProfileEntryNextLink_Type(Integer32):
    """Custom type rmtProfileEntryNextLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_RmtProfileEntryNextLink_Type.__name__ = "Integer32"
_RmtProfileEntryNextLink_Object = MibTableColumn
rmtProfileEntryNextLink = _RmtProfileEntryNextLink_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 9),
    _RmtProfileEntryNextLink_Type()
)
rmtProfileEntryNextLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtProfileEntryNextLink.setStatus("mandatory")


class _RmtProfileEntryMpCapable_Type(Integer32):
    """Custom type rmtProfileEntryMpCapable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RmtProfileEntryMpCapable_Type.__name__ = "Integer32"
_RmtProfileEntryMpCapable_Object = MibTableColumn
rmtProfileEntryMpCapable = _RmtProfileEntryMpCapable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 10),
    _RmtProfileEntryMpCapable_Type()
)
rmtProfileEntryMpCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryMpCapable.setStatus("mandatory")


class _RmtProfileEntryMpLineUtilization_Type(Integer32):
    """Custom type rmtProfileEntryMpLineUtilization based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RmtProfileEntryMpLineUtilization_Type.__name__ = "Integer32"
_RmtProfileEntryMpLineUtilization_Object = MibTableColumn
rmtProfileEntryMpLineUtilization = _RmtProfileEntryMpLineUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 11),
    _RmtProfileEntryMpLineUtilization_Type()
)
rmtProfileEntryMpLineUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryMpLineUtilization.setStatus("mandatory")


class _RmtProfileEntryMpHistoryTime_Type(Integer32):
    """Custom type rmtProfileEntryMpHistoryTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmtProfileEntryMpHistoryTime_Type.__name__ = "Integer32"
_RmtProfileEntryMpHistoryTime_Object = MibTableColumn
rmtProfileEntryMpHistoryTime = _RmtProfileEntryMpHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 12),
    _RmtProfileEntryMpHistoryTime_Type()
)
rmtProfileEntryMpHistoryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryMpHistoryTime.setStatus("mandatory")


class _RmtProfileEntryMpMoreBWSamples_Type(Integer32):
    """Custom type rmtProfileEntryMpMoreBWSamples based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmtProfileEntryMpMoreBWSamples_Type.__name__ = "Integer32"
_RmtProfileEntryMpMoreBWSamples_Object = MibTableColumn
rmtProfileEntryMpMoreBWSamples = _RmtProfileEntryMpMoreBWSamples_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 13),
    _RmtProfileEntryMpMoreBWSamples_Type()
)
rmtProfileEntryMpMoreBWSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryMpMoreBWSamples.setStatus("mandatory")


class _RmtProfileEntryMpLessBWSamples_Type(Integer32):
    """Custom type rmtProfileEntryMpLessBWSamples based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmtProfileEntryMpLessBWSamples_Type.__name__ = "Integer32"
_RmtProfileEntryMpLessBWSamples_Object = MibTableColumn
rmtProfileEntryMpLessBWSamples = _RmtProfileEntryMpLessBWSamples_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 14),
    _RmtProfileEntryMpLessBWSamples_Type()
)
rmtProfileEntryMpLessBWSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryMpLessBWSamples.setStatus("mandatory")


class _RmtProfileEntryMpMaxCallsAllowed_Type(Integer32):
    """Custom type rmtProfileEntryMpMaxCallsAllowed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmtProfileEntryMpMaxCallsAllowed_Type.__name__ = "Integer32"
_RmtProfileEntryMpMaxCallsAllowed_Object = MibTableColumn
rmtProfileEntryMpMaxCallsAllowed = _RmtProfileEntryMpMaxCallsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 15),
    _RmtProfileEntryMpMaxCallsAllowed_Type()
)
rmtProfileEntryMpMaxCallsAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryMpMaxCallsAllowed.setStatus("mandatory")


class _RmtProfileEntryMpCallsToAdd_Type(Integer32):
    """Custom type rmtProfileEntryMpCallsToAdd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmtProfileEntryMpCallsToAdd_Type.__name__ = "Integer32"
_RmtProfileEntryMpCallsToAdd_Object = MibTableColumn
rmtProfileEntryMpCallsToAdd = _RmtProfileEntryMpCallsToAdd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 16),
    _RmtProfileEntryMpCallsToAdd_Type()
)
rmtProfileEntryMpCallsToAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryMpCallsToAdd.setStatus("mandatory")


class _RmtProfileEntryMpCallsToRemove_Type(Integer32):
    """Custom type rmtProfileEntryMpCallsToRemove based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmtProfileEntryMpCallsToRemove_Type.__name__ = "Integer32"
_RmtProfileEntryMpCallsToRemove_Object = MibTableColumn
rmtProfileEntryMpCallsToRemove = _RmtProfileEntryMpCallsToRemove_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 17),
    _RmtProfileEntryMpCallsToRemove_Type()
)
rmtProfileEntryMpCallsToRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryMpCallsToRemove.setStatus("mandatory")


class _RmtProfileEntryMpAvgPktSize_Type(Integer32):
    """Custom type rmtProfileEntryMpAvgPktSize based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_RmtProfileEntryMpAvgPktSize_Type.__name__ = "Integer32"
_RmtProfileEntryMpAvgPktSize_Object = MibTableColumn
rmtProfileEntryMpAvgPktSize = _RmtProfileEntryMpAvgPktSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 18),
    _RmtProfileEntryMpAvgPktSize_Type()
)
rmtProfileEntryMpAvgPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryMpAvgPktSize.setStatus("mandatory")


class _RmtProfileEntryMpRmtBwCtrl_Type(Integer32):
    """Custom type rmtProfileEntryMpRmtBwCtrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RmtProfileEntryMpRmtBwCtrl_Type.__name__ = "Integer32"
_RmtProfileEntryMpRmtBwCtrl_Object = MibTableColumn
rmtProfileEntryMpRmtBwCtrl = _RmtProfileEntryMpRmtBwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 19),
    _RmtProfileEntryMpRmtBwCtrl_Type()
)
rmtProfileEntryMpRmtBwCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtProfileEntryMpRmtBwCtrl.setStatus("mandatory")
_CallHistory_ObjectIdentity = ObjectIdentity
callHistory = _CallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2)
)


class _CallHistoryTableMaxLength_Type(Integer32):
    """Custom type callHistoryTableMaxLength based on Integer32"""
    defaultValue = 50


_CallHistoryTableMaxLength_Type.__name__ = "Integer32"
_CallHistoryTableMaxLength_Object = MibScalar
callHistoryTableMaxLength = _CallHistoryTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 1),
    _CallHistoryTableMaxLength_Type()
)
callHistoryTableMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryTableMaxLength.setStatus("mandatory")
_CallHistoryTable_Object = MibTable
callHistoryTable = _CallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2)
)
if mibBuilder.loadTexts:
    callHistoryTable.setStatus("mandatory")
_CallHistoryEntry_Object = MibTableRow
callHistoryEntry = _CallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1)
)
callHistoryEntry.setIndexNames(
    (0, "CTRON-ISDN-CONFIGURATION-MIB", "callHistoryIndex"),
)
if mibBuilder.loadTexts:
    callHistoryEntry.setStatus("mandatory")
_CallHistorySetupTime_Type = Integer32
_CallHistorySetupTime_Object = MibTableColumn
callHistorySetupTime = _CallHistorySetupTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 1),
    _CallHistorySetupTime_Type()
)
callHistorySetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistorySetupTime.setStatus("mandatory")


class _CallHistoryIndex_Type(Integer32):
    """Custom type callHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CallHistoryIndex_Type.__name__ = "Integer32"
_CallHistoryIndex_Object = MibTableColumn
callHistoryIndex = _CallHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 2),
    _CallHistoryIndex_Type()
)
callHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryIndex.setStatus("mandatory")
_CallHistoryPeerAddress_Type = DisplayString
_CallHistoryPeerAddress_Object = MibTableColumn
callHistoryPeerAddress = _CallHistoryPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 3),
    _CallHistoryPeerAddress_Type()
)
callHistoryPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryPeerAddress.setStatus("mandatory")


class _CallHistoryNeighborId_Type(Integer32):
    """Custom type callHistoryNeighborId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CallHistoryNeighborId_Type.__name__ = "Integer32"
_CallHistoryNeighborId_Object = MibTableColumn
callHistoryNeighborId = _CallHistoryNeighborId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 4),
    _CallHistoryNeighborId_Type()
)
callHistoryNeighborId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryNeighborId.setStatus("mandatory")


class _CallHistoryLogicalIfIndex_Type(Integer32):
    """Custom type callHistoryLogicalIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CallHistoryLogicalIfIndex_Type.__name__ = "Integer32"
_CallHistoryLogicalIfIndex_Object = MibTableColumn
callHistoryLogicalIfIndex = _CallHistoryLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 5),
    _CallHistoryLogicalIfIndex_Type()
)
callHistoryLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryLogicalIfIndex.setStatus("mandatory")


class _CallHistoryDisconnectCause_Type(Integer32):
    """Custom type callHistoryDisconnectCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              16,
              17,
              18,
              21,
              22,
              28,
              31,
              34,
              38,
              41,
              42,
              43,
              44,
              52,
              54,
              58,
              63,
              65,
              66,
              70,
              79,
              81,
              82,
              85,
              88,
              90,
              91,
              95,
              96,
              97,
              98,
              99,
              100,
              111,
              133,
              134,
              135,
              136,
              138)
        )
    )
    namedValues = NamedValues(
        *(("unassignedNumber", 1),
          ("noRouteToDestination", 2),
          ("channelUnacceptable", 6),
          ("normalCallClearing", 16),
          ("userBusy", 17),
          ("noUserResponding", 18),
          ("callRejected", 21),
          ("numberChangedAddress", 22),
          ("invalidNumberFormat", 28),
          ("normalUnspecified", 31),
          ("noChannelAvailable", 34),
          ("networkOutOfOrder", 38),
          ("temporaryFailure", 41),
          ("switchingEquipmentCongestion", 42),
          ("userInfoDiscarded", 43),
          ("requestedChannelNotAvailable", 44),
          ("outgoingCallsBarred", 52),
          ("incomingCallsBarred", 54),
          ("bearerCapabilityNotPresentlyAvail", 58),
          ("serviceNotAvailable", 63),
          ("bearerServiceNotImplemented", 65),
          ("channelTypeNotImplemented", 66),
          ("onlyRestrictedChannelAvailable", 70),
          ("serviceOrOptionNotImplemeted", 79),
          ("invalidCallReferenceValue", 81),
          ("identifiedChannelDoesNotExist", 82),
          ("invalidDigitValueForAddress", 85),
          ("incompatibleDestination", 88),
          ("destinationAddressMissing", 90),
          ("transitNetworkDoesNotExist", 91),
          ("invalidMessageSpecified", 95),
          ("mandatoryIEmissing", 96),
          ("messageTypeNonexistentOrNotImplemented", 97),
          ("messageNotCompatibleWithCallState", 98),
          ("iEnotImplemented", 99),
          ("invalidIEcontents", 100),
          ("protocolError", 111),
          ("callAlreadyActive", 133),
          ("lineDisabled", 134),
          ("badParameter", 135),
          ("timeoutOccured", 136),
          ("noCallActive", 138))
    )


_CallHistoryDisconnectCause_Type.__name__ = "Integer32"
_CallHistoryDisconnectCause_Object = MibTableColumn
callHistoryDisconnectCause = _CallHistoryDisconnectCause_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 6),
    _CallHistoryDisconnectCause_Type()
)
callHistoryDisconnectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryDisconnectCause.setStatus("mandatory")
_CallHistoryConnectTime_Type = Integer32
_CallHistoryConnectTime_Object = MibTableColumn
callHistoryConnectTime = _CallHistoryConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 7),
    _CallHistoryConnectTime_Type()
)
callHistoryConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryConnectTime.setStatus("mandatory")
_CallHistoryDisconnectTime_Type = Integer32
_CallHistoryDisconnectTime_Object = MibTableColumn
callHistoryDisconnectTime = _CallHistoryDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 8),
    _CallHistoryDisconnectTime_Type()
)
callHistoryDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryDisconnectTime.setStatus("mandatory")


class _CallHistoryCallOrigin_Type(Integer32):
    """Custom type callHistoryCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("originate", 1),
          ("answer", 2),
          ("callback", 3))
    )


_CallHistoryCallOrigin_Type.__name__ = "Integer32"
_CallHistoryCallOrigin_Object = MibTableColumn
callHistoryCallOrigin = _CallHistoryCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 9),
    _CallHistoryCallOrigin_Type()
)
callHistoryCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryCallOrigin.setStatus("mandatory")


class _CallHistoryInfoType_Type(Integer32):
    """Custom type callHistoryInfoType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("speech", 2),
          ("unrestrictedDigital", 3),
          ("unrestrictedDigital56", 4),
          ("restrictedDigital", 5),
          ("audio31", 6),
          ("audio7", 7),
          ("video", 8),
          ("packetSwitched", 9))
    )


_CallHistoryInfoType_Type.__name__ = "Integer32"
_CallHistoryInfoType_Object = MibTableColumn
callHistoryInfoType = _CallHistoryInfoType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 10),
    _CallHistoryInfoType_Type()
)
callHistoryInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryInfoType.setStatus("mandatory")
_CallHistoryTransmitPackets_Type = Counter32
_CallHistoryTransmitPackets_Object = MibTableColumn
callHistoryTransmitPackets = _CallHistoryTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 11),
    _CallHistoryTransmitPackets_Type()
)
callHistoryTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryTransmitPackets.setStatus("mandatory")
_CallHistoryTransmitBytes_Type = Counter32
_CallHistoryTransmitBytes_Object = MibTableColumn
callHistoryTransmitBytes = _CallHistoryTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 12),
    _CallHistoryTransmitBytes_Type()
)
callHistoryTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryTransmitBytes.setStatus("mandatory")
_CallHistoryReceivePackets_Type = Counter32
_CallHistoryReceivePackets_Object = MibTableColumn
callHistoryReceivePackets = _CallHistoryReceivePackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 13),
    _CallHistoryReceivePackets_Type()
)
callHistoryReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryReceivePackets.setStatus("mandatory")
_CallHistoryReceiveBytes_Type = Counter32
_CallHistoryReceiveBytes_Object = MibTableColumn
callHistoryReceiveBytes = _CallHistoryReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 14),
    _CallHistoryReceiveBytes_Type()
)
callHistoryReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryReceiveBytes.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-ISDN-CONFIGURATION-MIB",
    **{"DisplayString": DisplayString,
       "cabletron": cabletron,
       "mibs": mibs,
       "ctron": ctron,
       "ctDataLink": ctDataLink,
       "ctronWan": ctronWan,
       "ctISDNconfigMib": ctISDNconfigMib,
       "ctISDNcontrol": ctISDNcontrol,
       "isdnDchTable": isdnDchTable,
       "isdnDchEntry": isdnDchEntry,
       "isdnDchIndex": isdnDchIndex,
       "isdnDchRateAccess": isdnDchRateAccess,
       "isdnDchAllowedCh": isdnDchAllowedCh,
       "isdnDchChInUse": isdnDchChInUse,
       "isdnDchSupportedSwitches": isdnDchSupportedSwitches,
       "isdnDchSwitchType": isdnDchSwitchType,
       "isdnDchSPID1": isdnDchSPID1,
       "isdnDchSPID2": isdnDchSPID2,
       "isdnDchDirNum1": isdnDchDirNum1,
       "isdnDchDirNum2": isdnDchDirNum2,
       "isdnDchOperStatus": isdnDchOperStatus,
       "dialCtlNbrCfgTable": dialCtlNbrCfgTable,
       "dialCtlNbrCfgEntry": dialCtlNbrCfgEntry,
       "dialCtlNbrCfgId": dialCtlNbrCfgId,
       "dialCtlNbrCfgIndex": dialCtlNbrCfgIndex,
       "dialCtlNbrCfgIfIndex": dialCtlNbrCfgIfIndex,
       "dialCtlNbrCfgOriginateAddress": dialCtlNbrCfgOriginateAddress,
       "dialCtlNbrCfgAnswerAddress": dialCtlNbrCfgAnswerAddress,
       "rmtProfileTable": rmtProfileTable,
       "rmtProfileEntry": rmtProfileEntry,
       "rmtProfileEntryIndex": rmtProfileEntryIndex,
       "rmtProfileEntryName": rmtProfileEntryName,
       "rmtProfileEntryMakerName": rmtProfileEntryMakerName,
       "rmtProfileEntryAction": rmtProfileEntryAction,
       "rmtProfileEntryState": rmtProfileEntryState,
       "rmtProfileEntryMaxNeighbor": rmtProfileEntryMaxNeighbor,
       "rmtProfileEntryBchInUse": rmtProfileEntryBchInUse,
       "rmtProfileEntryLinkHead": rmtProfileEntryLinkHead,
       "rmtProfileEntryNextLink": rmtProfileEntryNextLink,
       "rmtProfileEntryMpCapable": rmtProfileEntryMpCapable,
       "rmtProfileEntryMpLineUtilization": rmtProfileEntryMpLineUtilization,
       "rmtProfileEntryMpHistoryTime": rmtProfileEntryMpHistoryTime,
       "rmtProfileEntryMpMoreBWSamples": rmtProfileEntryMpMoreBWSamples,
       "rmtProfileEntryMpLessBWSamples": rmtProfileEntryMpLessBWSamples,
       "rmtProfileEntryMpMaxCallsAllowed": rmtProfileEntryMpMaxCallsAllowed,
       "rmtProfileEntryMpCallsToAdd": rmtProfileEntryMpCallsToAdd,
       "rmtProfileEntryMpCallsToRemove": rmtProfileEntryMpCallsToRemove,
       "rmtProfileEntryMpAvgPktSize": rmtProfileEntryMpAvgPktSize,
       "rmtProfileEntryMpRmtBwCtrl": rmtProfileEntryMpRmtBwCtrl,
       "callHistory": callHistory,
       "callHistoryTableMaxLength": callHistoryTableMaxLength,
       "callHistoryTable": callHistoryTable,
       "callHistoryEntry": callHistoryEntry,
       "callHistorySetupTime": callHistorySetupTime,
       "callHistoryIndex": callHistoryIndex,
       "callHistoryPeerAddress": callHistoryPeerAddress,
       "callHistoryNeighborId": callHistoryNeighborId,
       "callHistoryLogicalIfIndex": callHistoryLogicalIfIndex,
       "callHistoryDisconnectCause": callHistoryDisconnectCause,
       "callHistoryConnectTime": callHistoryConnectTime,
       "callHistoryDisconnectTime": callHistoryDisconnectTime,
       "callHistoryCallOrigin": callHistoryCallOrigin,
       "callHistoryInfoType": callHistoryInfoType,
       "callHistoryTransmitPackets": callHistoryTransmitPackets,
       "callHistoryTransmitBytes": callHistoryTransmitBytes,
       "callHistoryReceivePackets": callHistoryReceivePackets,
       "callHistoryReceiveBytes": callHistoryReceiveBytes}
)
