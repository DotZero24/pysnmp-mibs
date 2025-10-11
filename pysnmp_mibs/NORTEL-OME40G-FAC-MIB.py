# SNMP MIB module (NORTEL-OME40G-FAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NORTEL-OME40G-FAC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:17:16 2025
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

(nnOme40G,) = mibBuilder.importSymbols(
    "NORTEL-OME40G-MIB",
    "nnOme40G")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

nnOme40GFacilities = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1)
)
if mibBuilder.loadTexts:
    nnOme40GFacilities.setRevisions(
        ("2007-08-10 00:00",
         "2009-05-20 00:00",
         "2014-08-18 00:00")
    )


# Types definitions



class GccValues(Integer32):
    """Custom type GccValues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("none", 1),
          ("gcc0", 2),
          ("gcc1", 3),
          ("gcc2", 4))
    )





class AdminState(Integer32):
    """Custom type AdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("is", 1),
          ("oos", 2))
    )





class PrimaryState(Integer32):
    """Custom type PrimaryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("is", 1),
          ("is-anr", 2),
          ("oos-au", 3),
          ("oos-ma", 4),
          ("oos-auma", 5),
          ("oos-maanr", 6))
    )





class LoopbackType(Integer32):
    """Custom type LoopbackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("none", 1),
          ("facility", 2),
          ("terminal", 3),
          ("efmremote", 4))
    )





class Status(Integer32):
    """Custom type Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("enabled", 1),
          ("disabled", 2))
    )





class FecFormat(Integer32):
    """Custom type FecFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("rs8", 2),
          ("scfec", 3),
          ("bch20", 4),
          ("pfec", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnOCn_ObjectIdentity = ObjectIdentity
nnOCn = _NnOCn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1)
)
_NnOCnTable_Object = MibTable
nnOCnTable = _NnOCnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nnOCnTable.setStatus("current")
_NnOCnEntry_Object = MibTableRow
nnOCnEntry = _NnOCnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1)
)
nnOCnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nnOCnEntry.setStatus("current")
_OcnRowStatus_Type = RowStatus
_OcnRowStatus_Object = MibTableColumn
ocnRowStatus = _OcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 1),
    _OcnRowStatus_Type()
)
ocnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocnRowStatus.setStatus("current")


class _StFormat_Type(Integer32):
    """Custom type stFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("num", 1),
          ("string", 2))
    )


_StFormat_Type.__name__ = "Integer32"
_StFormat_Object = MibTableColumn
stFormat = _StFormat_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 2),
    _StFormat_Type()
)
stFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stFormat.setStatus("current")
_ExpSTrc_Type = DisplayString
_ExpSTrc_Object = MibTableColumn
expSTrc = _ExpSTrc_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 3),
    _ExpSTrc_Type()
)
expSTrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expSTrc.setStatus("current")


class _StfMode_Type(Integer32):
    """Custom type stfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("almonly", 2))
    )


_StfMode_Type.__name__ = "Integer32"
_StfMode_Object = MibTableColumn
stfMode = _StfMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 4),
    _StfMode_Type()
)
stfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stfMode.setStatus("current")
_EBerTh_Type = Integer32
_EBerTh_Object = MibTableColumn
eBerTh = _EBerTh_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 5),
    _EBerTh_Type()
)
eBerTh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBerTh.setStatus("current")


class _OcnPortMode_Type(Integer32):
    """Custom type ocnPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("sonet", 1),
          ("sdh", 2))
    )


_OcnPortMode_Type.__name__ = "Integer32"
_OcnPortMode_Object = MibTableColumn
ocnPortMode = _OcnPortMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 6),
    _OcnPortMode_Type()
)
ocnPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocnPortMode.setStatus("current")
_OcnLaserOffFarEndFail_Type = Status
_OcnLaserOffFarEndFail_Object = MibTableColumn
ocnLaserOffFarEndFail = _OcnLaserOffFarEndFail_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 7),
    _OcnLaserOffFarEndFail_Type()
)
ocnLaserOffFarEndFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocnLaserOffFarEndFail.setStatus("current")
_OChTxActOcnPwr_Type = DisplayString
_OChTxActOcnPwr_Object = MibTableColumn
oChTxActOcnPwr = _OChTxActOcnPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 8),
    _OChTxActOcnPwr_Type()
)
oChTxActOcnPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxActOcnPwr.setStatus("current")
_OChTxMinOcnPwr_Type = DisplayString
_OChTxMinOcnPwr_Object = MibTableColumn
oChTxMinOcnPwr = _OChTxMinOcnPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 9),
    _OChTxMinOcnPwr_Type()
)
oChTxMinOcnPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxMinOcnPwr.setStatus("current")
_OChTxMaxOcnPwr_Type = DisplayString
_OChTxMaxOcnPwr_Object = MibTableColumn
oChTxMaxOcnPwr = _OChTxMaxOcnPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 10),
    _OChTxMaxOcnPwr_Type()
)
oChTxMaxOcnPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxMaxOcnPwr.setStatus("current")
_OChRxActOcnPwr_Type = DisplayString
_OChRxActOcnPwr_Object = MibTableColumn
oChRxActOcnPwr = _OChRxActOcnPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 11),
    _OChRxActOcnPwr_Type()
)
oChRxActOcnPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxActOcnPwr.setStatus("current")
_OChRxMinOcnPwr_Type = DisplayString
_OChRxMinOcnPwr_Object = MibTableColumn
oChRxMinOcnPwr = _OChRxMinOcnPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 12),
    _OChRxMinOcnPwr_Type()
)
oChRxMinOcnPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxMinOcnPwr.setStatus("current")
_OChRxMaxOcnPwr_Type = DisplayString
_OChRxMaxOcnPwr_Object = MibTableColumn
oChRxMaxOcnPwr = _OChRxMaxOcnPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 13),
    _OChRxMaxOcnPwr_Type()
)
oChRxMaxOcnPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxMaxOcnPwr.setStatus("current")
_ExpSectionTraceMsg_Type = DisplayString
_ExpSectionTraceMsg_Object = MibTableColumn
expSectionTraceMsg = _ExpSectionTraceMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 14),
    _ExpSectionTraceMsg_Type()
)
expSectionTraceMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expSectionTraceMsg.setStatus("current")
_IncSectionTraceMsg_Type = DisplayString
_IncSectionTraceMsg_Object = MibTableColumn
incSectionTraceMsg = _IncSectionTraceMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 15),
    _IncSectionTraceMsg_Type()
)
incSectionTraceMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incSectionTraceMsg.setStatus("current")
_OcnLoopbackType_Type = LoopbackType
_OcnLoopbackType_Object = MibTableColumn
ocnLoopbackType = _OcnLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 16),
    _OcnLoopbackType_Type()
)
ocnLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocnLoopbackType.setStatus("current")
_OcnPrimaryState_Type = PrimaryState
_OcnPrimaryState_Object = MibTableColumn
ocnPrimaryState = _OcnPrimaryState_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 17),
    _OcnPrimaryState_Type()
)
ocnPrimaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnPrimaryState.setStatus("current")
_OcnSecondaryState_Type = DisplayString
_OcnSecondaryState_Object = MibTableColumn
ocnSecondaryState = _OcnSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 18),
    _OcnSecondaryState_Type()
)
ocnSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnSecondaryState.setStatus("current")
_OcnAdminState_Type = AdminState
_OcnAdminState_Object = MibTableColumn
ocnAdminState = _OcnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 19),
    _OcnAdminState_Type()
)
ocnAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocnAdminState.setStatus("current")
_OcnAID_Type = DisplayString
_OcnAID_Object = MibTableColumn
ocnAID = _OcnAID_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 1, 1, 1, 20),
    _OcnAID_Type()
)
ocnAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnAID.setStatus("current")
_NnOTMn_ObjectIdentity = ObjectIdentity
nnOTMn = _NnOTMn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2)
)
_NnOTMnTable_Object = MibTable
nnOTMnTable = _NnOTMnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nnOTMnTable.setStatus("current")
_NnOTMnEntry_Object = MibTableRow
nnOTMnEntry = _NnOTMnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1)
)
nnOTMnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nnOTMnEntry.setStatus("current")
_OtmRowStatus_Type = RowStatus
_OtmRowStatus_Object = MibTableColumn
otmRowStatus = _OtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 1),
    _OtmRowStatus_Type()
)
otmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otmRowStatus.setStatus("current")
_Osid_Type = DisplayString
_Osid_Object = MibTableColumn
osid = _Osid_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 2),
    _Osid_Type()
)
osid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osid.setStatus("current")
_OtuTxFecFmt_Type = FecFormat
_OtuTxFecFmt_Object = MibTableColumn
otuTxFecFmt = _OtuTxFecFmt_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 3),
    _OtuTxFecFmt_Type()
)
otuTxFecFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuTxFecFmt.setStatus("current")
_OtuRxFecFmt_Type = FecFormat
_OtuRxFecFmt_Object = MibTableColumn
otuRxFecFmt = _OtuRxFecFmt_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 4),
    _OtuRxFecFmt_Type()
)
otuRxFecFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuRxFecFmt.setStatus("current")


class _OduTerm_Type(Integer32):
    """Custom type oduTerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("yes", 1),
          ("no", 2))
    )


_OduTerm_Type.__name__ = "Integer32"
_OduTerm_Object = MibTableColumn
oduTerm = _OduTerm_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 5),
    _OduTerm_Type()
)
oduTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTerm.setStatus("current")


class _OtuTxTTI_Type(DisplayString):
    """Custom type otuTxTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OtuTxTTI_Type.__name__ = "DisplayString"
_OtuTxTTI_Object = MibTableColumn
otuTxTTI = _OtuTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 6),
    _OtuTxTTI_Type()
)
otuTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuTxTTI.setStatus("current")


class _OduTxTTI_Type(DisplayString):
    """Custom type oduTxTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OduTxTTI_Type.__name__ = "DisplayString"
_OduTxTTI_Object = MibTableColumn
oduTxTTI = _OduTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 7),
    _OduTxTTI_Type()
)
oduTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTxTTI.setStatus("current")


class _OtuRxExpTTI_Type(DisplayString):
    """Custom type otuRxExpTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OtuRxExpTTI_Type.__name__ = "DisplayString"
_OtuRxExpTTI_Object = MibTableColumn
otuRxExpTTI = _OtuRxExpTTI_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 8),
    _OtuRxExpTTI_Type()
)
otuRxExpTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuRxExpTTI.setStatus("current")


class _OduRxExpTTI_Type(DisplayString):
    """Custom type oduRxExpTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OduRxExpTTI_Type.__name__ = "DisplayString"
_OduRxExpTTI_Object = MibTableColumn
oduRxExpTTI = _OduRxExpTTI_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 9),
    _OduRxExpTTI_Type()
)
oduRxExpTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduRxExpTTI.setStatus("current")


class _TxPathId_Type(Integer32):
    """Custom type txPathId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TxPathId_Type.__name__ = "Integer32"
_TxPathId_Object = MibTableColumn
txPathId = _TxPathId_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 10),
    _TxPathId_Type()
)
txPathId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txPathId.setStatus("current")
_OChTxPwr_Type = DisplayString
_OChTxPwr_Object = MibTableColumn
oChTxPwr = _OChTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 11),
    _OChTxPwr_Type()
)
oChTxPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oChTxPwr.setStatus("current")
_OChTxActOtmPwr_Type = DisplayString
_OChTxActOtmPwr_Object = MibTableColumn
oChTxActOtmPwr = _OChTxActOtmPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 12),
    _OChTxActOtmPwr_Type()
)
oChTxActOtmPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxActOtmPwr.setStatus("current")
_OChTxMinOtmPwr_Type = DisplayString
_OChTxMinOtmPwr_Object = MibTableColumn
oChTxMinOtmPwr = _OChTxMinOtmPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 13),
    _OChTxMinOtmPwr_Type()
)
oChTxMinOtmPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxMinOtmPwr.setStatus("current")
_OChTxMaxOtmPwr_Type = DisplayString
_OChTxMaxOtmPwr_Object = MibTableColumn
oChTxMaxOtmPwr = _OChTxMaxOtmPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 14),
    _OChTxMaxOtmPwr_Type()
)
oChTxMaxOtmPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxMaxOtmPwr.setStatus("current")
_OChRxActOtmPwr_Type = DisplayString
_OChRxActOtmPwr_Object = MibTableColumn
oChRxActOtmPwr = _OChRxActOtmPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 15),
    _OChRxActOtmPwr_Type()
)
oChRxActOtmPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxActOtmPwr.setStatus("current")
_OChRxMinOtmPwr_Type = DisplayString
_OChRxMinOtmPwr_Object = MibTableColumn
oChRxMinOtmPwr = _OChRxMinOtmPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 16),
    _OChRxMinOtmPwr_Type()
)
oChRxMinOtmPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxMinOtmPwr.setStatus("current")
_OChRxMaxOtmPwr_Type = DisplayString
_OChRxMaxOtmPwr_Object = MibTableColumn
oChRxMaxOtmPwr = _OChRxMaxOtmPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 17),
    _OChRxMaxOtmPwr_Type()
)
oChRxMaxOtmPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxMaxOtmPwr.setStatus("current")
_OChTxWvlngthProv_Type = DisplayString
_OChTxWvlngthProv_Object = MibTableColumn
oChTxWvlngthProv = _OChTxWvlngthProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 18),
    _OChTxWvlngthProv_Type()
)
oChTxWvlngthProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oChTxWvlngthProv.setStatus("current")
_OChTxWvlngthMin_Type = DisplayString
_OChTxWvlngthMin_Object = MibTableColumn
oChTxWvlngthMin = _OChTxWvlngthMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 19),
    _OChTxWvlngthMin_Type()
)
oChTxWvlngthMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxWvlngthMin.setStatus("current")
_OChTxWvlngthMax_Type = DisplayString
_OChTxWvlngthMax_Object = MibTableColumn
oChTxWvlngthMax = _OChTxWvlngthMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 20),
    _OChTxWvlngthMax_Type()
)
oChTxWvlngthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxWvlngthMax.setStatus("current")
_OChTxWvlngthSpacing_Type = DisplayString
_OChTxWvlngthSpacing_Object = MibTableColumn
oChTxWvlngthSpacing = _OChTxWvlngthSpacing_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 21),
    _OChTxWvlngthSpacing_Type()
)
oChTxWvlngthSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxWvlngthSpacing.setStatus("current")
_OChRxActDisp_Type = DisplayString
_OChRxActDisp_Object = MibTableColumn
oChRxActDisp = _OChRxActDisp_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 22),
    _OChRxActDisp_Type()
)
oChRxActDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxActDisp.setStatus("current")
_OChRxActPmd_Type = DisplayString
_OChRxActPmd_Object = MibTableColumn
oChRxActPmd = _OChRxActPmd_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 23),
    _OChRxActPmd_Type()
)
oChRxActPmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxActPmd.setStatus("current")
_OChRxPmdMax_Type = DisplayString
_OChRxPmdMax_Object = MibTableColumn
oChRxPmdMax = _OChRxPmdMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 24),
    _OChRxPmdMax_Type()
)
oChRxPmdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxPmdMax.setStatus("current")
_OChRxEchoTrace_Type = DisplayString
_OChRxEchoTrace_Object = MibTableColumn
oChRxEchoTrace = _OChRxEchoTrace_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 25),
    _OChRxEchoTrace_Type()
)
oChRxEchoTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxEchoTrace.setStatus("current")
_OChTxTrace_Type = DisplayString
_OChTxTrace_Object = MibTableColumn
oChTxTrace = _OChTxTrace_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 26),
    _OChTxTrace_Type()
)
oChTxTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxTrace.setStatus("current")
_OChTxAssocFarEndRx_Type = DisplayString
_OChTxAssocFarEndRx_Object = MibTableColumn
oChTxAssocFarEndRx = _OChTxAssocFarEndRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 27),
    _OChTxAssocFarEndRx_Type()
)
oChTxAssocFarEndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxAssocFarEndRx.setStatus("current")


class _OtmPortMode_Type(Integer32):
    """Custom type otmPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("sonet", 1),
          ("sdh", 2))
    )


_OtmPortMode_Type.__name__ = "Integer32"
_OtmPortMode_Object = MibTableColumn
otmPortMode = _OtmPortMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 28),
    _OtmPortMode_Type()
)
otmPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otmPortMode.setStatus("current")


class _TfMode_Type(Integer32):
    """Custom type tfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("almonly", 2),
          ("linefail", 3))
    )


_TfMode_Type.__name__ = "Integer32"
_TfMode_Object = MibTableColumn
tfMode = _TfMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 29),
    _TfMode_Type()
)
tfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tfMode.setStatus("current")


class _OduTfMode_Type(Integer32):
    """Custom type oduTfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("almonly", 2))
    )


_OduTfMode_Type.__name__ = "Integer32"
_OduTfMode_Object = MibTableColumn
oduTfMode = _OduTfMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 30),
    _OduTfMode_Type()
)
oduTfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTfMode.setStatus("current")
_OtmLaserOffFarEndFail_Type = Status
_OtmLaserOffFarEndFail_Object = MibTableColumn
otmLaserOffFarEndFail = _OtmLaserOffFarEndFail_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 31),
    _OtmLaserOffFarEndFail_Type()
)
otmLaserOffFarEndFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otmLaserOffFarEndFail.setStatus("current")
_PreFecSigFailThreshLevel_Type = DisplayString
_PreFecSigFailThreshLevel_Object = MibTableColumn
preFecSigFailThreshLevel = _PreFecSigFailThreshLevel_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 32),
    _PreFecSigFailThreshLevel_Type()
)
preFecSigFailThreshLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preFecSigFailThreshLevel.setStatus("current")
_OtuSignalDegradeThreshLevel_Type = Integer32
_OtuSignalDegradeThreshLevel_Object = MibTableColumn
otuSignalDegradeThreshLevel = _OtuSignalDegradeThreshLevel_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 33),
    _OtuSignalDegradeThreshLevel_Type()
)
otuSignalDegradeThreshLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuSignalDegradeThreshLevel.setStatus("current")


class _OduMonitorEnabled_Type(Integer32):
    """Custom type oduMonitorEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("yes", 1),
          ("no", 2))
    )


_OduMonitorEnabled_Type.__name__ = "Integer32"
_OduMonitorEnabled_Object = MibTableColumn
oduMonitorEnabled = _OduMonitorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 34),
    _OduMonitorEnabled_Type()
)
oduMonitorEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduMonitorEnabled.setStatus("current")


class _LineRate_Type(Integer32):
    """Custom type lineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rate-uknown", 0),
          ("rate-44G5", 1),
          ("rate-9G95", 2),
          ("rate-10G709", 3),
          ("rate-11G05", 4),
          ("rate-11G09", 5))
    )


_LineRate_Type.__name__ = "Integer32"
_LineRate_Object = MibTableColumn
lineRate = _LineRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 35),
    _LineRate_Type()
)
lineRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lineRate.setStatus("current")
_OtuExpTTI_Type = DisplayString
_OtuExpTTI_Object = MibTableColumn
otuExpTTI = _OtuExpTTI_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 36),
    _OtuExpTTI_Type()
)
otuExpTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuExpTTI.setStatus("current")
_OtuRxIncTTI_Type = DisplayString
_OtuRxIncTTI_Object = MibTableColumn
otuRxIncTTI = _OtuRxIncTTI_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 37),
    _OtuRxIncTTI_Type()
)
otuRxIncTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuRxIncTTI.setStatus("current")
_OduRxIncTTI_Type = DisplayString
_OduRxIncTTI_Object = MibTableColumn
oduRxIncTTI = _OduRxIncTTI_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 38),
    _OduRxIncTTI_Type()
)
oduRxIncTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduRxIncTTI.setStatus("current")
_OduMonitorMsg_Type = DisplayString
_OduMonitorMsg_Object = MibTableColumn
oduMonitorMsg = _OduMonitorMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 39),
    _OduMonitorMsg_Type()
)
oduMonitorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduMonitorMsg.setStatus("current")
_OtmLoopbackType_Type = LoopbackType
_OtmLoopbackType_Object = MibTableColumn
otmLoopbackType = _OtmLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 40),
    _OtmLoopbackType_Type()
)
otmLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otmLoopbackType.setStatus("current")


class _Opu2reserved_Type(Integer32):
    """Custom type opu2reserved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("yes", 1),
          ("no", 2))
    )


_Opu2reserved_Type.__name__ = "Integer32"
_Opu2reserved_Object = MibTableColumn
opu2reserved = _Opu2reserved_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 41),
    _Opu2reserved_Type()
)
opu2reserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opu2reserved.setStatus("current")


class _ExpectedPayloadType_Type(DisplayString):
    """Custom type expectedPayloadType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_ExpectedPayloadType_Type.__name__ = "DisplayString"
_ExpectedPayloadType_Object = MibTableColumn
expectedPayloadType = _ExpectedPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 42),
    _ExpectedPayloadType_Type()
)
expectedPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expectedPayloadType.setStatus("current")


class _TransmittedPayloadType_Type(DisplayString):
    """Custom type transmittedPayloadType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_TransmittedPayloadType_Type.__name__ = "DisplayString"
_TransmittedPayloadType_Object = MibTableColumn
transmittedPayloadType = _TransmittedPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 43),
    _TransmittedPayloadType_Type()
)
transmittedPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmittedPayloadType.setStatus("current")


class _ReceivedPayloadType_Type(DisplayString):
    """Custom type receivedPayloadType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_ReceivedPayloadType_Type.__name__ = "DisplayString"
_ReceivedPayloadType_Object = MibTableColumn
receivedPayloadType = _ReceivedPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 44),
    _ReceivedPayloadType_Type()
)
receivedPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedPayloadType.setStatus("current")
_OtmPrimaryState_Type = PrimaryState
_OtmPrimaryState_Object = MibTableColumn
otmPrimaryState = _OtmPrimaryState_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 45),
    _OtmPrimaryState_Type()
)
otmPrimaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otmPrimaryState.setStatus("current")
_OtmSecondaryState_Type = DisplayString
_OtmSecondaryState_Object = MibTableColumn
otmSecondaryState = _OtmSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 46),
    _OtmSecondaryState_Type()
)
otmSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otmSecondaryState.setStatus("current")
_OtmAdminState_Type = AdminState
_OtmAdminState_Object = MibTableColumn
otmAdminState = _OtmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 47),
    _OtmAdminState_Type()
)
otmAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otmAdminState.setStatus("current")
_OtmAID_Type = DisplayString
_OtmAID_Object = MibTableColumn
otmAID = _OtmAID_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 48),
    _OtmAID_Type()
)
otmAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otmAID.setStatus("current")
_OtmGCC_Type = GccValues
_OtmGCC_Object = MibTableColumn
otmGCC = _OtmGCC_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 49),
    _OtmGCC_Type()
)
otmGCC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otmGCC.setStatus("current")


class _OspfCircuit_Type(DisplayString):
    """Custom type ospfCircuit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OspfCircuit_Type.__name__ = "DisplayString"
_OspfCircuit_Object = MibTableColumn
ospfCircuit = _OspfCircuit_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 50),
    _OspfCircuit_Type()
)
ospfCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCircuit.setStatus("current")


class _OChDifferentialEncoding_Type(Integer32):
    """Custom type oChDifferentialEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("none", 1),
          ("hard", 2),
          ("soft", 3))
    )


_OChDifferentialEncoding_Type.__name__ = "Integer32"
_OChDifferentialEncoding_Object = MibTableColumn
oChDifferentialEncoding = _OChDifferentialEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 2, 1, 1, 51),
    _OChDifferentialEncoding_Type()
)
oChDifferentialEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oChDifferentialEncoding.setStatus("current")
_NnEth_ObjectIdentity = ObjectIdentity
nnEth = _NnEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3)
)
_NnEthTable_Object = MibTable
nnEthTable = _NnEthTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nnEthTable.setStatus("current")
_NnEthEntry_Object = MibTableRow
nnEthEntry = _NnEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1)
)
nnEthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nnEthEntry.setStatus("current")
_EthRowStatus_Type = RowStatus
_EthRowStatus_Object = MibTableColumn
ethRowStatus = _EthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 1),
    _EthRowStatus_Type()
)
ethRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethRowStatus.setStatus("current")
_EthLaserOffFarEndFail_Type = Status
_EthLaserOffFarEndFail_Object = MibTableColumn
ethLaserOffFarEndFail = _EthLaserOffFarEndFail_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 2),
    _EthLaserOffFarEndFail_Type()
)
ethLaserOffFarEndFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethLaserOffFarEndFail.setStatus("current")
_OChTxActEthPwr_Type = DisplayString
_OChTxActEthPwr_Object = MibTableColumn
oChTxActEthPwr = _OChTxActEthPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 3),
    _OChTxActEthPwr_Type()
)
oChTxActEthPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxActEthPwr.setStatus("current")
_OChTxMinEthPwr_Type = DisplayString
_OChTxMinEthPwr_Object = MibTableColumn
oChTxMinEthPwr = _OChTxMinEthPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 4),
    _OChTxMinEthPwr_Type()
)
oChTxMinEthPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxMinEthPwr.setStatus("current")
_OChTxMaxEthPwr_Type = DisplayString
_OChTxMaxEthPwr_Object = MibTableColumn
oChTxMaxEthPwr = _OChTxMaxEthPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 5),
    _OChTxMaxEthPwr_Type()
)
oChTxMaxEthPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChTxMaxEthPwr.setStatus("current")
_OChRxActEthPwr_Type = DisplayString
_OChRxActEthPwr_Object = MibTableColumn
oChRxActEthPwr = _OChRxActEthPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 6),
    _OChRxActEthPwr_Type()
)
oChRxActEthPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxActEthPwr.setStatus("current")
_OChRxMinEthPwr_Type = DisplayString
_OChRxMinEthPwr_Object = MibTableColumn
oChRxMinEthPwr = _OChRxMinEthPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 7),
    _OChRxMinEthPwr_Type()
)
oChRxMinEthPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxMinEthPwr.setStatus("current")
_OChRxMaxEthPwr_Type = DisplayString
_OChRxMaxEthPwr_Object = MibTableColumn
oChRxMaxEthPwr = _OChRxMaxEthPwr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 8),
    _OChRxMaxEthPwr_Type()
)
oChRxMaxEthPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oChRxMaxEthPwr.setStatus("current")


class _MaxTransUnit_Type(Integer32):
    """Custom type maxTransUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mtu-unknown", 0),
          ("mtu-1600", 1),
          ("mtu-9600", 2))
    )


_MaxTransUnit_Type.__name__ = "Integer32"
_MaxTransUnit_Object = MibTableColumn
maxTransUnit = _MaxTransUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 9),
    _MaxTransUnit_Type()
)
maxTransUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxTransUnit.setStatus("current")


class _FlowControl_Type(Integer32):
    """Custom type flowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("none", 1),
          ("asymmetric", 2),
          ("symmetric", 3),
          ("preeemptive", 4))
    )


_FlowControl_Type.__name__ = "Integer32"
_FlowControl_Object = MibTableColumn
flowControl = _FlowControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 10),
    _FlowControl_Type()
)
flowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowControl.setStatus("current")


class _Equipment_Type(Integer32):
    """Custom type equipment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("xge-unknown", 0),
          ("xge-lan", 1),
          ("xge-wan", 2))
    )


_Equipment_Type.__name__ = "Integer32"
_Equipment_Object = MibTableColumn
equipment = _Equipment_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 11),
    _Equipment_Type()
)
equipment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipment.setStatus("current")


class _EthMapping_Type(Integer32):
    """Custom type ethMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("prop237", 1),
          ("prop238", 2),
          ("gfp-mactr", 3),
          ("gfp-std", 4),
          ("gfp-mactr192", 5),
          ("gfp-std192", 6),
          ("gfp-mactr64", 7),
          ("gfp-std64", 8),
          ("gfp-macostr", 9),
          ("gfp-macostr192", 10),
          ("gfp-macostr64", 11),
          ("ull", 12))
    )


_EthMapping_Type.__name__ = "Integer32"
_EthMapping_Object = MibTableColumn
ethMapping = _EthMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 12),
    _EthMapping_Type()
)
ethMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethMapping.setStatus("current")
_EthLoopbackType_Type = LoopbackType
_EthLoopbackType_Object = MibTableColumn
ethLoopbackType = _EthLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 13),
    _EthLoopbackType_Type()
)
ethLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethLoopbackType.setStatus("current")
_EthPrimaryState_Type = PrimaryState
_EthPrimaryState_Object = MibTableColumn
ethPrimaryState = _EthPrimaryState_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 14),
    _EthPrimaryState_Type()
)
ethPrimaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPrimaryState.setStatus("current")
_EthSecondaryState_Type = DisplayString
_EthSecondaryState_Object = MibTableColumn
ethSecondaryState = _EthSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 15),
    _EthSecondaryState_Type()
)
ethSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethSecondaryState.setStatus("current")
_EthAdminState_Type = AdminState
_EthAdminState_Object = MibTableColumn
ethAdminState = _EthAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 16),
    _EthAdminState_Type()
)
ethAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethAdminState.setStatus("current")
_EthAID_Type = DisplayString
_EthAID_Object = MibTableColumn
ethAID = _EthAID_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 3, 1, 1, 17),
    _EthAID_Type()
)
ethAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethAID.setStatus("current")
_NnWAN_ObjectIdentity = ObjectIdentity
nnWAN = _NnWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4)
)
_NnWanTable_Object = MibTable
nnWanTable = _NnWanTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    nnWanTable.setStatus("current")
_NnWanEntry_Object = MibTableRow
nnWanEntry = _NnWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1)
)
nnWanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nnWanEntry.setStatus("current")


class _FrameChecksum_Type(Integer32):
    """Custom type frameChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
    )


_FrameChecksum_Type.__name__ = "Integer32"
_FrameChecksum_Object = MibTableColumn
frameChecksum = _FrameChecksum_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1, 1),
    _FrameChecksum_Type()
)
frameChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameChecksum.setStatus("current")


class _WanMapping_Type(Integer32):
    """Custom type wanMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("gfp-f", 1),
          ("gfp-t", 2))
    )


_WanMapping_Type.__name__ = "Integer32"
_WanMapping_Object = MibTableColumn
wanMapping = _WanMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1, 2),
    _WanMapping_Type()
)
wanMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanMapping.setStatus("current")


class _GfpRfi_Type(Integer32):
    """Custom type gfpRfi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("enable", 1),
          ("disable", 2))
    )


_GfpRfi_Type.__name__ = "Integer32"
_GfpRfi_Object = MibTableColumn
gfpRfi = _GfpRfi_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1, 3),
    _GfpRfi_Type()
)
gfpRfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpRfi.setStatus("current")


class _GfpRtDelay_Type(Integer32):
    """Custom type gfpRtDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("enable", 1),
          ("disable", 2))
    )


_GfpRtDelay_Type.__name__ = "Integer32"
_GfpRtDelay_Object = MibTableColumn
gfpRtDelay = _GfpRtDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1, 4),
    _GfpRtDelay_Type()
)
gfpRtDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpRtDelay.setStatus("current")


class _CondType_Type(Integer32):
    """Custom type condType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("gfpcmf", 1))
    )


_CondType_Type.__name__ = "Integer32"
_CondType_Object = MibTableColumn
condType = _CondType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1, 5),
    _CondType_Type()
)
condType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    condType.setStatus("current")


class _Preamble_Type(Integer32):
    """Custom type preamble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("keep", 1),
          ("discard", 2))
    )


_Preamble_Type.__name__ = "Integer32"
_Preamble_Object = MibTableColumn
preamble = _Preamble_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1, 6),
    _Preamble_Type()
)
preamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preamble.setStatus("current")


class _FcsErrFrames_Type(Integer32):
    """Custom type fcsErrFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("keep", 1),
          ("discard", 2))
    )


_FcsErrFrames_Type.__name__ = "Integer32"
_FcsErrFrames_Object = MibTableColumn
fcsErrFrames = _FcsErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1, 7),
    _FcsErrFrames_Type()
)
fcsErrFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcsErrFrames.setStatus("current")


class _TransmittedUPI_Type(DisplayString):
    """Custom type transmittedUPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_TransmittedUPI_Type.__name__ = "DisplayString"
_TransmittedUPI_Object = MibTableColumn
transmittedUPI = _TransmittedUPI_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1, 8),
    _TransmittedUPI_Type()
)
transmittedUPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmittedUPI.setStatus("current")
_WanPrimaryState_Type = PrimaryState
_WanPrimaryState_Object = MibTableColumn
wanPrimaryState = _WanPrimaryState_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1, 9),
    _WanPrimaryState_Type()
)
wanPrimaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPrimaryState.setStatus("current")
_WanSecondaryState_Type = DisplayString
_WanSecondaryState_Object = MibTableColumn
wanSecondaryState = _WanSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1, 10),
    _WanSecondaryState_Type()
)
wanSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanSecondaryState.setStatus("current")
_WanAdminState_Type = AdminState
_WanAdminState_Object = MibTableColumn
wanAdminState = _WanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1, 11),
    _WanAdminState_Type()
)
wanAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanAdminState.setStatus("current")
_WanAID_Type = DisplayString
_WanAID_Object = MibTableColumn
wanAID = _WanAID_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 1, 4, 1, 1, 12),
    _WanAID_Type()
)
wanAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-OME40G-FAC-MIB",
    **{"GccValues": GccValues,
       "AdminState": AdminState,
       "PrimaryState": PrimaryState,
       "LoopbackType": LoopbackType,
       "Status": Status,
       "FecFormat": FecFormat,
       "nnOme40GFacilities": nnOme40GFacilities,
       "nnOCn": nnOCn,
       "nnOCnTable": nnOCnTable,
       "nnOCnEntry": nnOCnEntry,
       "ocnRowStatus": ocnRowStatus,
       "stFormat": stFormat,
       "expSTrc": expSTrc,
       "stfMode": stfMode,
       "eBerTh": eBerTh,
       "ocnPortMode": ocnPortMode,
       "ocnLaserOffFarEndFail": ocnLaserOffFarEndFail,
       "oChTxActOcnPwr": oChTxActOcnPwr,
       "oChTxMinOcnPwr": oChTxMinOcnPwr,
       "oChTxMaxOcnPwr": oChTxMaxOcnPwr,
       "oChRxActOcnPwr": oChRxActOcnPwr,
       "oChRxMinOcnPwr": oChRxMinOcnPwr,
       "oChRxMaxOcnPwr": oChRxMaxOcnPwr,
       "expSectionTraceMsg": expSectionTraceMsg,
       "incSectionTraceMsg": incSectionTraceMsg,
       "ocnLoopbackType": ocnLoopbackType,
       "ocnPrimaryState": ocnPrimaryState,
       "ocnSecondaryState": ocnSecondaryState,
       "ocnAdminState": ocnAdminState,
       "ocnAID": ocnAID,
       "nnOTMn": nnOTMn,
       "nnOTMnTable": nnOTMnTable,
       "nnOTMnEntry": nnOTMnEntry,
       "otmRowStatus": otmRowStatus,
       "osid": osid,
       "otuTxFecFmt": otuTxFecFmt,
       "otuRxFecFmt": otuRxFecFmt,
       "oduTerm": oduTerm,
       "otuTxTTI": otuTxTTI,
       "oduTxTTI": oduTxTTI,
       "otuRxExpTTI": otuRxExpTTI,
       "oduRxExpTTI": oduRxExpTTI,
       "txPathId": txPathId,
       "oChTxPwr": oChTxPwr,
       "oChTxActOtmPwr": oChTxActOtmPwr,
       "oChTxMinOtmPwr": oChTxMinOtmPwr,
       "oChTxMaxOtmPwr": oChTxMaxOtmPwr,
       "oChRxActOtmPwr": oChRxActOtmPwr,
       "oChRxMinOtmPwr": oChRxMinOtmPwr,
       "oChRxMaxOtmPwr": oChRxMaxOtmPwr,
       "oChTxWvlngthProv": oChTxWvlngthProv,
       "oChTxWvlngthMin": oChTxWvlngthMin,
       "oChTxWvlngthMax": oChTxWvlngthMax,
       "oChTxWvlngthSpacing": oChTxWvlngthSpacing,
       "oChRxActDisp": oChRxActDisp,
       "oChRxActPmd": oChRxActPmd,
       "oChRxPmdMax": oChRxPmdMax,
       "oChRxEchoTrace": oChRxEchoTrace,
       "oChTxTrace": oChTxTrace,
       "oChTxAssocFarEndRx": oChTxAssocFarEndRx,
       "otmPortMode": otmPortMode,
       "tfMode": tfMode,
       "oduTfMode": oduTfMode,
       "otmLaserOffFarEndFail": otmLaserOffFarEndFail,
       "preFecSigFailThreshLevel": preFecSigFailThreshLevel,
       "otuSignalDegradeThreshLevel": otuSignalDegradeThreshLevel,
       "oduMonitorEnabled": oduMonitorEnabled,
       "lineRate": lineRate,
       "otuExpTTI": otuExpTTI,
       "otuRxIncTTI": otuRxIncTTI,
       "oduRxIncTTI": oduRxIncTTI,
       "oduMonitorMsg": oduMonitorMsg,
       "otmLoopbackType": otmLoopbackType,
       "opu2reserved": opu2reserved,
       "expectedPayloadType": expectedPayloadType,
       "transmittedPayloadType": transmittedPayloadType,
       "receivedPayloadType": receivedPayloadType,
       "otmPrimaryState": otmPrimaryState,
       "otmSecondaryState": otmSecondaryState,
       "otmAdminState": otmAdminState,
       "otmAID": otmAID,
       "otmGCC": otmGCC,
       "ospfCircuit": ospfCircuit,
       "oChDifferentialEncoding": oChDifferentialEncoding,
       "nnEth": nnEth,
       "nnEthTable": nnEthTable,
       "nnEthEntry": nnEthEntry,
       "ethRowStatus": ethRowStatus,
       "ethLaserOffFarEndFail": ethLaserOffFarEndFail,
       "oChTxActEthPwr": oChTxActEthPwr,
       "oChTxMinEthPwr": oChTxMinEthPwr,
       "oChTxMaxEthPwr": oChTxMaxEthPwr,
       "oChRxActEthPwr": oChRxActEthPwr,
       "oChRxMinEthPwr": oChRxMinEthPwr,
       "oChRxMaxEthPwr": oChRxMaxEthPwr,
       "maxTransUnit": maxTransUnit,
       "flowControl": flowControl,
       "equipment": equipment,
       "ethMapping": ethMapping,
       "ethLoopbackType": ethLoopbackType,
       "ethPrimaryState": ethPrimaryState,
       "ethSecondaryState": ethSecondaryState,
       "ethAdminState": ethAdminState,
       "ethAID": ethAID,
       "nnWAN": nnWAN,
       "nnWanTable": nnWanTable,
       "nnWanEntry": nnWanEntry,
       "frameChecksum": frameChecksum,
       "wanMapping": wanMapping,
       "gfpRfi": gfpRfi,
       "gfpRtDelay": gfpRtDelay,
       "condType": condType,
       "preamble": preamble,
       "fcsErrFrames": fcsErrFrames,
       "transmittedUPI": transmittedUPI,
       "wanPrimaryState": wanPrimaryState,
       "wanSecondaryState": wanSecondaryState,
       "wanAdminState": wanAdminState,
       "wanAID": wanAID}
)
