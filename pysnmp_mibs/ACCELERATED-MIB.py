# SNMP MIB module (ACCELERATED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/digi/ACCELERATED-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:16:41 2025
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

acceleratedMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40083, 11000)
)
if mibBuilder.loadTexts:
    acceleratedMIB.setRevisions(
        ("2021-11-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Accelerated_ObjectIdentity = ObjectIdentity
accelerated = _Accelerated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40083)
)
_ModemHardwareTable_Object = MibTable
modemHardwareTable = _ModemHardwareTable_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1)
)
if mibBuilder.loadTexts:
    modemHardwareTable.setStatus("current")
_ModemHardwareEntry_Object = MibTableRow
modemHardwareEntry = _ModemHardwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1)
)
modemHardwareEntry.setIndexNames(
    (0, "ACCELERATED-MIB", "mHardwareIndex"),
)
if mibBuilder.loadTexts:
    modemHardwareEntry.setStatus("current")


class _MHardwareIndex_Type(Integer32):
    """Custom type mHardwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MHardwareIndex_Type.__name__ = "Integer32"
_MHardwareIndex_Object = MibTableColumn
mHardwareIndex = _MHardwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 1),
    _MHardwareIndex_Type()
)
mHardwareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mHardwareIndex.setStatus("current")


class _MCarrier_Type(OctetString):
    """Custom type mCarrier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MCarrier_Type.__name__ = "OctetString"
_MCarrier_Object = MibTableColumn
mCarrier = _MCarrier_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 2),
    _MCarrier_Type()
)
mCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCarrier.setStatus("current")


class _MCarrierPLMN_Type(OctetString):
    """Custom type mCarrierPLMN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MCarrierPLMN_Type.__name__ = "OctetString"
_MCarrierPLMN_Object = MibTableColumn
mCarrierPLMN = _MCarrierPLMN_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 3),
    _MCarrierPLMN_Type()
)
mCarrierPLMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCarrierPLMN.setStatus("current")


class _MPhone_Type(OctetString):
    """Custom type mPhone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MPhone_Type.__name__ = "OctetString"
_MPhone_Object = MibTableColumn
mPhone = _MPhone_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 4),
    _MPhone_Type()
)
mPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mPhone.setStatus("current")


class _MAPN_Type(OctetString):
    """Custom type mAPN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MAPN_Type.__name__ = "OctetString"
_MAPN_Object = MibTableColumn
mAPN = _MAPN_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 5),
    _MAPN_Type()
)
mAPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mAPN.setStatus("current")


class _MProvider_Type(OctetString):
    """Custom type mProvider based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MProvider_Type.__name__ = "OctetString"
_MProvider_Object = MibTableColumn
mProvider = _MProvider_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 6),
    _MProvider_Type()
)
mProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mProvider.setStatus("current")


class _MProviderPLMN_Type(OctetString):
    """Custom type mProviderPLMN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MProviderPLMN_Type.__name__ = "OctetString"
_MProviderPLMN_Object = MibTableColumn
mProviderPLMN = _MProviderPLMN_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 7),
    _MProviderPLMN_Type()
)
mProviderPLMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mProviderPLMN.setStatus("current")


class _MIMEI_Type(OctetString):
    """Custom type mIMEI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MIMEI_Type.__name__ = "OctetString"
_MIMEI_Object = MibTableColumn
mIMEI = _MIMEI_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 8),
    _MIMEI_Type()
)
mIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIMEI.setStatus("current")


class _MIMSI_Type(OctetString):
    """Custom type mIMSI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MIMSI_Type.__name__ = "OctetString"
_MIMSI_Object = MibTableColumn
mIMSI = _MIMSI_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 9),
    _MIMSI_Type()
)
mIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIMSI.setStatus("current")


class _MICCID_Type(OctetString):
    """Custom type mICCID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MICCID_Type.__name__ = "OctetString"
_MICCID_Object = MibTableColumn
mICCID = _MICCID_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 10),
    _MICCID_Type()
)
mICCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICCID.setStatus("current")


class _MSID_Type(OctetString):
    """Custom type mSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MSID_Type.__name__ = "OctetString"
_MSID_Object = MibTableColumn
mSID = _MSID_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 11),
    _MSID_Type()
)
mSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSID.setStatus("current")


class _MNID_Type(OctetString):
    """Custom type mNID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MNID_Type.__name__ = "OctetString"
_MNID_Object = MibTableColumn
mNID = _MNID_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 12),
    _MNID_Type()
)
mNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mNID.setStatus("current")


class _MManufacturer_Type(OctetString):
    """Custom type mManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MManufacturer_Type.__name__ = "OctetString"
_MManufacturer_Object = MibTableColumn
mManufacturer = _MManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 13),
    _MManufacturer_Type()
)
mManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mManufacturer.setStatus("current")


class _MModel_Type(OctetString):
    """Custom type mModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MModel_Type.__name__ = "OctetString"
_MModel_Object = MibTableColumn
mModel = _MModel_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 14),
    _MModel_Type()
)
mModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mModel.setStatus("current")


class _MSKU_Type(OctetString):
    """Custom type mSKU based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MSKU_Type.__name__ = "OctetString"
_MSKU_Object = MibTableColumn
mSKU = _MSKU_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 15),
    _MSKU_Type()
)
mSKU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSKU.setStatus("current")


class _MRevision_Type(OctetString):
    """Custom type mRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MRevision_Type.__name__ = "OctetString"
_MRevision_Object = MibTableColumn
mRevision = _MRevision_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 16),
    _MRevision_Type()
)
mRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mRevision.setStatus("current")
_MUSBspeed_Type = Integer32
_MUSBspeed_Object = MibTableColumn
mUSBspeed = _MUSBspeed_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 17),
    _MUSBspeed_Type()
)
mUSBspeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mUSBspeed.setStatus("current")


class _MPort_Type(OctetString):
    """Custom type mPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MPort_Type.__name__ = "OctetString"
_MPort_Object = MibTableColumn
mPort = _MPort_Object(
    (1, 3, 6, 1, 4, 1, 40083, 1, 1, 18),
    _MPort_Type()
)
mPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mPort.setStatus("current")
_ModemStatusTable_Object = MibTable
modemStatusTable = _ModemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2)
)
if mibBuilder.loadTexts:
    modemStatusTable.setStatus("current")
_ModemStatusEntry_Object = MibTableRow
modemStatusEntry = _ModemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1)
)
modemStatusEntry.setIndexNames(
    (0, "ACCELERATED-MIB", "mStatusIndex"),
)
if mibBuilder.loadTexts:
    modemStatusEntry.setStatus("current")


class _MStatusIndex_Type(Integer32):
    """Custom type mStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MStatusIndex_Type.__name__ = "Integer32"
_MStatusIndex_Object = MibTableColumn
mStatusIndex = _MStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 1),
    _MStatusIndex_Type()
)
mStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mStatusIndex.setStatus("current")


class _MSim_Type(OctetString):
    """Custom type mSim based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MSim_Type.__name__ = "OctetString"
_MSim_Object = MibTableColumn
mSim = _MSim_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 2),
    _MSim_Type()
)
mSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSim.setStatus("current")


class _MState_Type(OctetString):
    """Custom type mState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MState_Type.__name__ = "OctetString"
_MState_Object = MibTableColumn
mState = _MState_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 3),
    _MState_Type()
)
mState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mState.setStatus("current")
_MSignal_Type = Integer32
_MSignal_Object = MibTableColumn
mSignal = _MSignal_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 4),
    _MSignal_Type()
)
mSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSignal.setStatus("current")


class _MMode_Type(OctetString):
    """Custom type mMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MMode_Type.__name__ = "OctetString"
_MMode_Object = MibTableColumn
mMode = _MMode_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 5),
    _MMode_Type()
)
mMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mMode.setStatus("current")


class _MCNTI_Type(OctetString):
    """Custom type mCNTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MCNTI_Type.__name__ = "OctetString"
_MCNTI_Object = MibTableColumn
mCNTI = _MCNTI_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 6),
    _MCNTI_Type()
)
mCNTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCNTI.setStatus("current")


class _MBand_Type(OctetString):
    """Custom type mBand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MBand_Type.__name__ = "OctetString"
_MBand_Object = MibTableColumn
mBand = _MBand_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 7),
    _MBand_Type()
)
mBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBand.setStatus("current")


class _MIf_Type(OctetString):
    """Custom type mIf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MIf_Type.__name__ = "OctetString"
_MIf_Object = MibTableColumn
mIf = _MIf_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 8),
    _MIf_Type()
)
mIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIf.setStatus("current")


class _MRx_Type(OctetString):
    """Custom type mRx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MRx_Type.__name__ = "OctetString"
_MRx_Object = MibTableColumn
mRx = _MRx_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 9),
    _MRx_Type()
)
mRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mRx.setStatus("current")


class _MTx_Type(OctetString):
    """Custom type mTx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MTx_Type.__name__ = "OctetString"
_MTx_Object = MibTableColumn
mTx = _MTx_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 10),
    _MTx_Type()
)
mTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTx.setStatus("current")


class _MRsrp_Type(OctetString):
    """Custom type mRsrp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MRsrp_Type.__name__ = "OctetString"
_MRsrp_Object = MibTableColumn
mRsrp = _MRsrp_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 11),
    _MRsrp_Type()
)
mRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mRsrp.setStatus("current")


class _MRsrq_Type(OctetString):
    """Custom type mRsrq based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MRsrq_Type.__name__ = "OctetString"
_MRsrq_Object = MibTableColumn
mRsrq = _MRsrq_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 12),
    _MRsrq_Type()
)
mRsrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mRsrq.setStatus("current")


class _MSnr_Type(OctetString):
    """Custom type mSnr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MSnr_Type.__name__ = "OctetString"
_MSnr_Object = MibTableColumn
mSnr = _MSnr_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 13),
    _MSnr_Type()
)
mSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSnr.setStatus("current")


class _MSinr_Type(OctetString):
    """Custom type mSinr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MSinr_Type.__name__ = "OctetString"
_MSinr_Object = MibTableColumn
mSinr = _MSinr_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 14),
    _MSinr_Type()
)
mSinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSinr.setStatus("current")


class _MEcio_Type(OctetString):
    """Custom type mEcio based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MEcio_Type.__name__ = "OctetString"
_MEcio_Object = MibTableColumn
mEcio = _MEcio_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 15),
    _MEcio_Type()
)
mEcio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mEcio.setStatus("current")


class _MRssi_Type(OctetString):
    """Custom type mRssi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MRssi_Type.__name__ = "OctetString"
_MRssi_Object = MibTableColumn
mRssi = _MRssi_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 16),
    _MRssi_Type()
)
mRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mRssi.setStatus("current")


class _MBars_Type(OctetString):
    """Custom type mBars based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MBars_Type.__name__ = "OctetString"
_MBars_Object = MibTableColumn
mBars = _MBars_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 17),
    _MBars_Type()
)
mBars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBars.setStatus("current")


class _MTemp_Type(OctetString):
    """Custom type mTemp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MTemp_Type.__name__ = "OctetString"
_MTemp_Object = MibTableColumn
mTemp = _MTemp_Object(
    (1, 3, 6, 1, 4, 1, 40083, 2, 1, 18),
    _MTemp_Type()
)
mTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTemp.setStatus("current")
_ModemLocationTable_Object = MibTable
modemLocationTable = _ModemLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 40083, 3)
)
if mibBuilder.loadTexts:
    modemLocationTable.setStatus("current")
_ModemLocationEntry_Object = MibTableRow
modemLocationEntry = _ModemLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 40083, 3, 1)
)
modemLocationEntry.setIndexNames(
    (0, "ACCELERATED-MIB", "mLocationIndex"),
)
if mibBuilder.loadTexts:
    modemLocationEntry.setStatus("current")


class _MLocationIndex_Type(Integer32):
    """Custom type mLocationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MLocationIndex_Type.__name__ = "Integer32"
_MLocationIndex_Object = MibTableColumn
mLocationIndex = _MLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 40083, 3, 1, 1),
    _MLocationIndex_Type()
)
mLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mLocationIndex.setStatus("current")


class _MCid_Type(OctetString):
    """Custom type mCid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MCid_Type.__name__ = "OctetString"
_MCid_Object = MibTableColumn
mCid = _MCid_Object(
    (1, 3, 6, 1, 4, 1, 40083, 3, 1, 2),
    _MCid_Type()
)
mCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCid.setStatus("current")


class _MLac_Type(OctetString):
    """Custom type mLac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MLac_Type.__name__ = "OctetString"
_MLac_Object = MibTableColumn
mLac = _MLac_Object(
    (1, 3, 6, 1, 4, 1, 40083, 3, 1, 3),
    _MLac_Type()
)
mLac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLac.setStatus("current")


class _MMcc_Type(OctetString):
    """Custom type mMcc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MMcc_Type.__name__ = "OctetString"
_MMcc_Object = MibTableColumn
mMcc = _MMcc_Object(
    (1, 3, 6, 1, 4, 1, 40083, 3, 1, 4),
    _MMcc_Type()
)
mMcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mMcc.setStatus("current")


class _MMnc_Type(OctetString):
    """Custom type mMnc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MMnc_Type.__name__ = "OctetString"
_MMnc_Object = MibTableColumn
mMnc = _MMnc_Object(
    (1, 3, 6, 1, 4, 1, 40083, 3, 1, 5),
    _MMnc_Type()
)
mMnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mMnc.setStatus("current")
_ModemNetworkTable_Object = MibTable
modemNetworkTable = _ModemNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 40083, 4)
)
if mibBuilder.loadTexts:
    modemNetworkTable.setStatus("current")
_ModemNetworkEntry_Object = MibTableRow
modemNetworkEntry = _ModemNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 40083, 4, 1)
)
modemNetworkEntry.setIndexNames(
    (0, "ACCELERATED-MIB", "mNetworkIndex"),
)
if mibBuilder.loadTexts:
    modemNetworkEntry.setStatus("current")


class _MNetworkIndex_Type(Integer32):
    """Custom type mNetworkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MNetworkIndex_Type.__name__ = "Integer32"
_MNetworkIndex_Object = MibTableColumn
mNetworkIndex = _MNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 40083, 4, 1, 1),
    _MNetworkIndex_Type()
)
mNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mNetworkIndex.setStatus("current")


class _MIPV4Pending_Type(OctetString):
    """Custom type mIPV4Pending based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MIPV4Pending_Type.__name__ = "OctetString"
_MIPV4Pending_Object = MibTableColumn
mIPV4Pending = _MIPV4Pending_Object(
    (1, 3, 6, 1, 4, 1, 40083, 4, 1, 2),
    _MIPV4Pending_Type()
)
mIPV4Pending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIPV4Pending.setStatus("current")


class _MIPV4_Type(OctetString):
    """Custom type mIPV4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MIPV4_Type.__name__ = "OctetString"
_MIPV4_Object = MibTableColumn
mIPV4 = _MIPV4_Object(
    (1, 3, 6, 1, 4, 1, 40083, 4, 1, 3),
    _MIPV4_Type()
)
mIPV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIPV4.setStatus("current")


class _MGatewayV4_Type(OctetString):
    """Custom type mGatewayV4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MGatewayV4_Type.__name__ = "OctetString"
_MGatewayV4_Object = MibTableColumn
mGatewayV4 = _MGatewayV4_Object(
    (1, 3, 6, 1, 4, 1, 40083, 4, 1, 4),
    _MGatewayV4_Type()
)
mGatewayV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGatewayV4.setStatus("current")


class _MNetmaskV4_Type(OctetString):
    """Custom type mNetmaskV4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MNetmaskV4_Type.__name__ = "OctetString"
_MNetmaskV4_Object = MibTableColumn
mNetmaskV4 = _MNetmaskV4_Object(
    (1, 3, 6, 1, 4, 1, 40083, 4, 1, 5),
    _MNetmaskV4_Type()
)
mNetmaskV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mNetmaskV4.setStatus("current")


class _MIPV6_Type(OctetString):
    """Custom type mIPV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MIPV6_Type.__name__ = "OctetString"
_MIPV6_Object = MibTableColumn
mIPV6 = _MIPV6_Object(
    (1, 3, 6, 1, 4, 1, 40083, 4, 1, 6),
    _MIPV6_Type()
)
mIPV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIPV6.setStatus("current")


class _MGatewayV6_Type(OctetString):
    """Custom type mGatewayV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MGatewayV6_Type.__name__ = "OctetString"
_MGatewayV6_Object = MibTableColumn
mGatewayV6 = _MGatewayV6_Object(
    (1, 3, 6, 1, 4, 1, 40083, 4, 1, 7),
    _MGatewayV6_Type()
)
mGatewayV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGatewayV6.setStatus("current")


class _MNetmaskV6_Type(OctetString):
    """Custom type mNetmaskV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MNetmaskV6_Type.__name__ = "OctetString"
_MNetmaskV6_Object = MibTableColumn
mNetmaskV6 = _MNetmaskV6_Object(
    (1, 3, 6, 1, 4, 1, 40083, 4, 1, 8),
    _MNetmaskV6_Type()
)
mNetmaskV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mNetmaskV6.setStatus("current")


class _MPassthroughV4_Type(OctetString):
    """Custom type mPassthroughV4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MPassthroughV4_Type.__name__ = "OctetString"
_MPassthroughV4_Object = MibTableColumn
mPassthroughV4 = _MPassthroughV4_Object(
    (1, 3, 6, 1, 4, 1, 40083, 4, 1, 9),
    _MPassthroughV4_Type()
)
mPassthroughV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mPassthroughV4.setStatus("current")


class _MPassthroughV6_Type(OctetString):
    """Custom type mPassthroughV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MPassthroughV6_Type.__name__ = "OctetString"
_MPassthroughV6_Object = MibTableColumn
mPassthroughV6 = _MPassthroughV6_Object(
    (1, 3, 6, 1, 4, 1, 40083, 4, 1, 10),
    _MPassthroughV6_Type()
)
mPassthroughV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mPassthroughV6.setStatus("current")


class _EventMessage_Type(OctetString):
    """Custom type eventMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_EventMessage_Type.__name__ = "OctetString"
_EventMessage_Object = MibScalar
eventMessage = _EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 40083, 5, 1),
    _EventMessage_Type()
)
eventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventMessage.setStatus("current")
_AcceleratedConformance_ObjectIdentity = ObjectIdentity
acceleratedConformance = _AcceleratedConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40083, 100)
)
_AcceleratedConformanceGroups_ObjectIdentity = ObjectIdentity
acceleratedConformanceGroups = _AcceleratedConformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40083, 100, 1)
)
_AcceleratedConformanceCompliances_ObjectIdentity = ObjectIdentity
acceleratedConformanceCompliances = _AcceleratedConformanceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40083, 100, 2)
)

# Managed Objects groups

acceleratedHardwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 40083, 100, 1, 1)
)
acceleratedHardwareGroup.setObjects(
      *(("ACCELERATED-MIB", "mCarrier"),
        ("ACCELERATED-MIB", "mCarrierPLMN"),
        ("ACCELERATED-MIB", "mPhone"),
        ("ACCELERATED-MIB", "mAPN"),
        ("ACCELERATED-MIB", "mProvider"),
        ("ACCELERATED-MIB", "mProviderPLMN"),
        ("ACCELERATED-MIB", "mIMEI"),
        ("ACCELERATED-MIB", "mIMSI"),
        ("ACCELERATED-MIB", "mICCID"),
        ("ACCELERATED-MIB", "mSID"),
        ("ACCELERATED-MIB", "mNID"),
        ("ACCELERATED-MIB", "mManufacturer"),
        ("ACCELERATED-MIB", "mModel"),
        ("ACCELERATED-MIB", "mSKU"),
        ("ACCELERATED-MIB", "mRevision"),
        ("ACCELERATED-MIB", "mUSBspeed"),
        ("ACCELERATED-MIB", "mPort"))
)
if mibBuilder.loadTexts:
    acceleratedHardwareGroup.setStatus("current")

acceleratedStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 40083, 100, 1, 2)
)
acceleratedStatusGroup.setObjects(
      *(("ACCELERATED-MIB", "mSim"),
        ("ACCELERATED-MIB", "mState"),
        ("ACCELERATED-MIB", "mSignal"),
        ("ACCELERATED-MIB", "mMode"),
        ("ACCELERATED-MIB", "mCNTI"),
        ("ACCELERATED-MIB", "mBand"),
        ("ACCELERATED-MIB", "mIf"),
        ("ACCELERATED-MIB", "mRx"),
        ("ACCELERATED-MIB", "mTx"),
        ("ACCELERATED-MIB", "mRsrp"),
        ("ACCELERATED-MIB", "mRsrq"),
        ("ACCELERATED-MIB", "mSnr"),
        ("ACCELERATED-MIB", "mSinr"),
        ("ACCELERATED-MIB", "mEcio"),
        ("ACCELERATED-MIB", "mRssi"),
        ("ACCELERATED-MIB", "mBars"),
        ("ACCELERATED-MIB", "mTemp"))
)
if mibBuilder.loadTexts:
    acceleratedStatusGroup.setStatus("current")

acceleratedLocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 40083, 100, 1, 3)
)
acceleratedLocationGroup.setObjects(
      *(("ACCELERATED-MIB", "mCid"),
        ("ACCELERATED-MIB", "mLac"),
        ("ACCELERATED-MIB", "mMcc"),
        ("ACCELERATED-MIB", "mMnc"))
)
if mibBuilder.loadTexts:
    acceleratedLocationGroup.setStatus("current")

acceleratedNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 40083, 100, 1, 4)
)
acceleratedNetworkGroup.setObjects(
      *(("ACCELERATED-MIB", "mIPV4Pending"),
        ("ACCELERATED-MIB", "mIPV4"),
        ("ACCELERATED-MIB", "mGatewayV4"),
        ("ACCELERATED-MIB", "mNetmaskV4"),
        ("ACCELERATED-MIB", "mIPV6"),
        ("ACCELERATED-MIB", "mGatewayV6"),
        ("ACCELERATED-MIB", "mNetmaskV6"),
        ("ACCELERATED-MIB", "mPassthroughV4"),
        ("ACCELERATED-MIB", "mPassthroughV6"))
)
if mibBuilder.loadTexts:
    acceleratedNetworkGroup.setStatus("current")


# Notification objects

event = NotificationType(
    (1, 3, 6, 1, 4, 1, 40083, 5)
)
event.setObjects(
    ("ACCELERATED-MIB", "eventMessage")
)
if mibBuilder.loadTexts:
    event.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

acceleratedConformanceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 40083, 100, 2, 1)
)
acceleratedConformanceCompliance.setObjects(
      *(("ACCELERATED-MIB", "acceleratedHardwareGroup"),
        ("ACCELERATED-MIB", "acceleratedStatusGroup"),
        ("ACCELERATED-MIB", "acceleratedLocationGroup"),
        ("ACCELERATED-MIB", "acceleratedNetworkGroup"))
)
if mibBuilder.loadTexts:
    acceleratedConformanceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACCELERATED-MIB",
    **{"accelerated": accelerated,
       "modemHardwareTable": modemHardwareTable,
       "modemHardwareEntry": modemHardwareEntry,
       "mHardwareIndex": mHardwareIndex,
       "mCarrier": mCarrier,
       "mCarrierPLMN": mCarrierPLMN,
       "mPhone": mPhone,
       "mAPN": mAPN,
       "mProvider": mProvider,
       "mProviderPLMN": mProviderPLMN,
       "mIMEI": mIMEI,
       "mIMSI": mIMSI,
       "mICCID": mICCID,
       "mSID": mSID,
       "mNID": mNID,
       "mManufacturer": mManufacturer,
       "mModel": mModel,
       "mSKU": mSKU,
       "mRevision": mRevision,
       "mUSBspeed": mUSBspeed,
       "mPort": mPort,
       "modemStatusTable": modemStatusTable,
       "modemStatusEntry": modemStatusEntry,
       "mStatusIndex": mStatusIndex,
       "mSim": mSim,
       "mState": mState,
       "mSignal": mSignal,
       "mMode": mMode,
       "mCNTI": mCNTI,
       "mBand": mBand,
       "mIf": mIf,
       "mRx": mRx,
       "mTx": mTx,
       "mRsrp": mRsrp,
       "mRsrq": mRsrq,
       "mSnr": mSnr,
       "mSinr": mSinr,
       "mEcio": mEcio,
       "mRssi": mRssi,
       "mBars": mBars,
       "mTemp": mTemp,
       "modemLocationTable": modemLocationTable,
       "modemLocationEntry": modemLocationEntry,
       "mLocationIndex": mLocationIndex,
       "mCid": mCid,
       "mLac": mLac,
       "mMcc": mMcc,
       "mMnc": mMnc,
       "modemNetworkTable": modemNetworkTable,
       "modemNetworkEntry": modemNetworkEntry,
       "mNetworkIndex": mNetworkIndex,
       "mIPV4Pending": mIPV4Pending,
       "mIPV4": mIPV4,
       "mGatewayV4": mGatewayV4,
       "mNetmaskV4": mNetmaskV4,
       "mIPV6": mIPV6,
       "mGatewayV6": mGatewayV6,
       "mNetmaskV6": mNetmaskV6,
       "mPassthroughV4": mPassthroughV4,
       "mPassthroughV6": mPassthroughV6,
       "event": event,
       "eventMessage": eventMessage,
       "acceleratedConformance": acceleratedConformance,
       "acceleratedConformanceGroups": acceleratedConformanceGroups,
       "acceleratedHardwareGroup": acceleratedHardwareGroup,
       "acceleratedStatusGroup": acceleratedStatusGroup,
       "acceleratedLocationGroup": acceleratedLocationGroup,
       "acceleratedNetworkGroup": acceleratedNetworkGroup,
       "acceleratedConformanceCompliances": acceleratedConformanceCompliances,
       "acceleratedConformanceCompliance": acceleratedConformanceCompliance,
       "acceleratedMIB": acceleratedMIB}
)
