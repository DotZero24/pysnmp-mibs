# SNMP MIB module (NEWTEC-TSDECAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-TSDECAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:05 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcEnable,) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcEnable")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ntcTsDecaps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900)
)
if mibBuilder.loadTexts:
    ntcTsDecaps.setRevisions(
        ("2019-05-14 06:00",
         "2015-09-25 11:00",
         "2015-04-13 07:00",
         "2015-01-30 08:00",
         "2014-07-15 08:00",
         "2014-02-03 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcTsDecObjects_ObjectIdentity = ObjectIdentity
ntcTsDecObjects = _NtcTsDecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1)
)
if mibBuilder.loadTexts:
    ntcTsDecObjects.setStatus("current")
_NtcTsDecIsisTable_Object = MibTable
ntcTsDecIsisTable = _NtcTsDecIsisTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 1)
)
if mibBuilder.loadTexts:
    ntcTsDecIsisTable.setStatus("current")
_NtcTsDecIsisEntry_Object = MibTableRow
ntcTsDecIsisEntry = _NtcTsDecIsisEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 1, 1)
)
ntcTsDecIsisEntry.setIndexNames(
    (0, "NEWTEC-TSDECAPS-MIB", "ntcTsDecIsisName"),
)
if mibBuilder.loadTexts:
    ntcTsDecIsisEntry.setStatus("current")


class _NtcTsDecIsisName_Type(DisplayString):
    """Custom type ntcTsDecIsisName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_NtcTsDecIsisName_Type.__name__ = "DisplayString"
_NtcTsDecIsisName_Object = MibTableColumn
ntcTsDecIsisName = _NtcTsDecIsisName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 1, 1, 1),
    _NtcTsDecIsisName_Type()
)
ntcTsDecIsisName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcTsDecIsisName.setStatus("current")
_NtcTsDecIsisRowStatus_Type = RowStatus
_NtcTsDecIsisRowStatus_Object = MibTableColumn
ntcTsDecIsisRowStatus = _NtcTsDecIsisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 1, 1, 2),
    _NtcTsDecIsisRowStatus_Type()
)
ntcTsDecIsisRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecIsisRowStatus.setStatus("current")
_NtcTsDecIsisEnable_Type = NtcEnable
_NtcTsDecIsisEnable_Object = MibTableColumn
ntcTsDecIsisEnable = _NtcTsDecIsisEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 1, 1, 3),
    _NtcTsDecIsisEnable_Type()
)
ntcTsDecIsisEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecIsisEnable.setStatus("current")
_NtcTsDecIsisIsi_Type = Unsigned32
_NtcTsDecIsisIsi_Object = MibTableColumn
ntcTsDecIsisIsi = _NtcTsDecIsisIsi_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 1, 1, 4),
    _NtcTsDecIsisIsi_Type()
)
ntcTsDecIsisIsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecIsisIsi.setStatus("current")


class _NtcTsDecIsisInTypeName_Type(OctetString):
    """Custom type ntcTsDecIsisInTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcTsDecIsisInTypeName_Type.__name__ = "OctetString"
_NtcTsDecIsisInTypeName_Object = MibTableColumn
ntcTsDecIsisInTypeName = _NtcTsDecIsisInTypeName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 1, 1, 5),
    _NtcTsDecIsisInTypeName_Type()
)
ntcTsDecIsisInTypeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecIsisInTypeName.setStatus("current")


class _NtcTsDecIsisInInstanceName_Type(OctetString):
    """Custom type ntcTsDecIsisInInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcTsDecIsisInInstanceName_Type.__name__ = "OctetString"
_NtcTsDecIsisInInstanceName_Object = MibTableColumn
ntcTsDecIsisInInstanceName = _NtcTsDecIsisInInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 1, 1, 6),
    _NtcTsDecIsisInInstanceName_Type()
)
ntcTsDecIsisInInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecIsisInInstanceName.setStatus("current")
_NtcTsDecPidsTable_Object = MibTable
ntcTsDecPidsTable = _NtcTsDecPidsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 2)
)
if mibBuilder.loadTexts:
    ntcTsDecPidsTable.setStatus("current")
_NtcTsDecPidsEntry_Object = MibTableRow
ntcTsDecPidsEntry = _NtcTsDecPidsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 2, 1)
)
ntcTsDecPidsEntry.setIndexNames(
    (0, "NEWTEC-TSDECAPS-MIB", "ntcTsDecPidsName"),
)
if mibBuilder.loadTexts:
    ntcTsDecPidsEntry.setStatus("current")


class _NtcTsDecPidsName_Type(DisplayString):
    """Custom type ntcTsDecPidsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_NtcTsDecPidsName_Type.__name__ = "DisplayString"
_NtcTsDecPidsName_Object = MibTableColumn
ntcTsDecPidsName = _NtcTsDecPidsName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 2, 1, 1),
    _NtcTsDecPidsName_Type()
)
ntcTsDecPidsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcTsDecPidsName.setStatus("current")
_NtcTsDecPidsRowStatus_Type = RowStatus
_NtcTsDecPidsRowStatus_Object = MibTableColumn
ntcTsDecPidsRowStatus = _NtcTsDecPidsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 2, 1, 2),
    _NtcTsDecPidsRowStatus_Type()
)
ntcTsDecPidsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecPidsRowStatus.setStatus("current")
_NtcTsDecPidsEnable_Type = NtcEnable
_NtcTsDecPidsEnable_Object = MibTableColumn
ntcTsDecPidsEnable = _NtcTsDecPidsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 2, 1, 3),
    _NtcTsDecPidsEnable_Type()
)
ntcTsDecPidsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecPidsEnable.setStatus("current")


class _NtcTsDecPidsPid_Type(Unsigned32):
    """Custom type ntcTsDecPidsPid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8190),
    )


_NtcTsDecPidsPid_Type.__name__ = "Unsigned32"
_NtcTsDecPidsPid_Object = MibTableColumn
ntcTsDecPidsPid = _NtcTsDecPidsPid_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 2, 1, 4),
    _NtcTsDecPidsPid_Type()
)
ntcTsDecPidsPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecPidsPid.setStatus("current")


class _NtcTsDecPidsInTypeName_Type(OctetString):
    """Custom type ntcTsDecPidsInTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcTsDecPidsInTypeName_Type.__name__ = "OctetString"
_NtcTsDecPidsInTypeName_Object = MibTableColumn
ntcTsDecPidsInTypeName = _NtcTsDecPidsInTypeName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 2, 1, 5),
    _NtcTsDecPidsInTypeName_Type()
)
ntcTsDecPidsInTypeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecPidsInTypeName.setStatus("current")


class _NtcTsDecPidsInInstanceName_Type(OctetString):
    """Custom type ntcTsDecPidsInInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcTsDecPidsInInstanceName_Type.__name__ = "OctetString"
_NtcTsDecPidsInInstanceName_Object = MibTableColumn
ntcTsDecPidsInInstanceName = _NtcTsDecPidsInInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 2, 1, 6),
    _NtcTsDecPidsInInstanceName_Type()
)
ntcTsDecPidsInInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecPidsInInstanceName.setStatus("current")


class _NtcTsDecPidsProtocol_Type(Integer32):
    """Custom type ntcTsDecPidsProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("mpe", 1),
          ("ule", 2))
    )


_NtcTsDecPidsProtocol_Type.__name__ = "Integer32"
_NtcTsDecPidsProtocol_Object = MibTableColumn
ntcTsDecPidsProtocol = _NtcTsDecPidsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 2, 1, 7),
    _NtcTsDecPidsProtocol_Type()
)
ntcTsDecPidsProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecPidsProtocol.setStatus("current")
_NtcTsDecChannelsTable_Object = MibTable
ntcTsDecChannelsTable = _NtcTsDecChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 3)
)
if mibBuilder.loadTexts:
    ntcTsDecChannelsTable.setStatus("current")
_NtcTsDecChannelsEntry_Object = MibTableRow
ntcTsDecChannelsEntry = _NtcTsDecChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 3, 1)
)
ntcTsDecChannelsEntry.setIndexNames(
    (0, "NEWTEC-TSDECAPS-MIB", "ntcTsDecChannelsName"),
)
if mibBuilder.loadTexts:
    ntcTsDecChannelsEntry.setStatus("current")


class _NtcTsDecChannelsName_Type(DisplayString):
    """Custom type ntcTsDecChannelsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_NtcTsDecChannelsName_Type.__name__ = "DisplayString"
_NtcTsDecChannelsName_Object = MibTableColumn
ntcTsDecChannelsName = _NtcTsDecChannelsName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 3, 1, 1),
    _NtcTsDecChannelsName_Type()
)
ntcTsDecChannelsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcTsDecChannelsName.setStatus("current")
_NtcTsDecChannelsRowStatus_Type = RowStatus
_NtcTsDecChannelsRowStatus_Object = MibTableColumn
ntcTsDecChannelsRowStatus = _NtcTsDecChannelsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 3, 1, 2),
    _NtcTsDecChannelsRowStatus_Type()
)
ntcTsDecChannelsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecChannelsRowStatus.setStatus("current")
_NtcTsDecChannelsEnable_Type = NtcEnable
_NtcTsDecChannelsEnable_Object = MibTableColumn
ntcTsDecChannelsEnable = _NtcTsDecChannelsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 3, 1, 3),
    _NtcTsDecChannelsEnable_Type()
)
ntcTsDecChannelsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecChannelsEnable.setStatus("current")


class _NtcTsDecChannelsInTypeName_Type(OctetString):
    """Custom type ntcTsDecChannelsInTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcTsDecChannelsInTypeName_Type.__name__ = "OctetString"
_NtcTsDecChannelsInTypeName_Object = MibTableColumn
ntcTsDecChannelsInTypeName = _NtcTsDecChannelsInTypeName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 3, 1, 4),
    _NtcTsDecChannelsInTypeName_Type()
)
ntcTsDecChannelsInTypeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecChannelsInTypeName.setStatus("current")


class _NtcTsDecChannelsInInstanceName_Type(OctetString):
    """Custom type ntcTsDecChannelsInInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcTsDecChannelsInInstanceName_Type.__name__ = "OctetString"
_NtcTsDecChannelsInInstanceName_Object = MibTableColumn
ntcTsDecChannelsInInstanceName = _NtcTsDecChannelsInInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 3, 1, 5),
    _NtcTsDecChannelsInInstanceName_Type()
)
ntcTsDecChannelsInInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecChannelsInInstanceName.setStatus("current")


class _NtcTsDecChannelsLabel_Type(DisplayString):
    """Custom type ntcTsDecChannelsLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcTsDecChannelsLabel_Type.__name__ = "DisplayString"
_NtcTsDecChannelsLabel_Object = MibTableColumn
ntcTsDecChannelsLabel = _NtcTsDecChannelsLabel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 3, 1, 6),
    _NtcTsDecChannelsLabel_Type()
)
ntcTsDecChannelsLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecChannelsLabel.setStatus("current")


class _NtcTsDecChannelsVirualNetwork_Type(OctetString):
    """Custom type ntcTsDecChannelsVirualNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcTsDecChannelsVirualNetwork_Type.__name__ = "OctetString"
_NtcTsDecChannelsVirualNetwork_Object = MibTableColumn
ntcTsDecChannelsVirualNetwork = _NtcTsDecChannelsVirualNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 3, 1, 7),
    _NtcTsDecChannelsVirualNetwork_Type()
)
ntcTsDecChannelsVirualNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecChannelsVirualNetwork.setStatus("current")


class _NtcTsDecChannelsAccessVlan_Type(Unsigned32):
    """Custom type ntcTsDecChannelsAccessVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NtcTsDecChannelsAccessVlan_Type.__name__ = "Unsigned32"
_NtcTsDecChannelsAccessVlan_Object = MibTableColumn
ntcTsDecChannelsAccessVlan = _NtcTsDecChannelsAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 3, 1, 8),
    _NtcTsDecChannelsAccessVlan_Type()
)
ntcTsDecChannelsAccessVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTsDecChannelsAccessVlan.setStatus("current")


class _NtcTsDecDefEncProt_Type(Integer32):
    """Custom type ntcTsDecDefEncProt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mpe", 0),
          ("ule", 1))
    )


_NtcTsDecDefEncProt_Type.__name__ = "Integer32"
_NtcTsDecDefEncProt_Object = MibScalar
ntcTsDecDefEncProt = _NtcTsDecDefEncProt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 4),
    _NtcTsDecDefEncProt_Type()
)
ntcTsDecDefEncProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsDecDefEncProt.setStatus("current")


class _NtcTsDecMpeCrcVal_Type(NtcEnable):
    """Custom type ntcTsDecMpeCrcVal based on NtcEnable"""
    defaultValue = 1


_NtcTsDecMpeCrcVal_Type.__name__ = "NtcEnable"
_NtcTsDecMpeCrcVal_Object = MibScalar
ntcTsDecMpeCrcVal = _NtcTsDecMpeCrcVal_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 1, 5),
    _NtcTsDecMpeCrcVal_Type()
)
ntcTsDecMpeCrcVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsDecMpeCrcVal.setStatus("current")
_NtcTsDecConformance_ObjectIdentity = ObjectIdentity
ntcTsDecConformance = _NtcTsDecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 2)
)
if mibBuilder.loadTexts:
    ntcTsDecConformance.setStatus("current")
_NtcTsDecConfCompliance_ObjectIdentity = ObjectIdentity
ntcTsDecConfCompliance = _NtcTsDecConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 2, 1)
)
if mibBuilder.loadTexts:
    ntcTsDecConfCompliance.setStatus("current")
_NtcTsDecConfGroup_ObjectIdentity = ObjectIdentity
ntcTsDecConfGroup = _NtcTsDecConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 2, 2)
)
if mibBuilder.loadTexts:
    ntcTsDecConfGroup.setStatus("current")

# Managed Objects groups

ntcTsDecConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 2, 2, 1)
)
ntcTsDecConfGrpV1Standard.setObjects(
      *(("NEWTEC-TSDECAPS-MIB", "ntcTsDecIsisRowStatus"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecIsisEnable"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecIsisIsi"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecIsisInTypeName"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecIsisInInstanceName"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecPidsRowStatus"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecPidsEnable"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecPidsPid"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecPidsInTypeName"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecPidsInInstanceName"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecPidsProtocol"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecChannelsRowStatus"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecChannelsEnable"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecChannelsInTypeName"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecChannelsInInstanceName"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecChannelsLabel"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecChannelsVirualNetwork"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecChannelsAccessVlan"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecDefEncProt"),
        ("NEWTEC-TSDECAPS-MIB", "ntcTsDecMpeCrcVal"))
)
if mibBuilder.loadTexts:
    ntcTsDecConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcTsDecConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5900, 2, 1, 1)
)
ntcTsDecConfCompV1Standard.setObjects(
    ("NEWTEC-TSDECAPS-MIB", "ntcTsDecConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcTsDecConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-TSDECAPS-MIB",
    **{"ntcTsDecaps": ntcTsDecaps,
       "ntcTsDecObjects": ntcTsDecObjects,
       "ntcTsDecIsisTable": ntcTsDecIsisTable,
       "ntcTsDecIsisEntry": ntcTsDecIsisEntry,
       "ntcTsDecIsisName": ntcTsDecIsisName,
       "ntcTsDecIsisRowStatus": ntcTsDecIsisRowStatus,
       "ntcTsDecIsisEnable": ntcTsDecIsisEnable,
       "ntcTsDecIsisIsi": ntcTsDecIsisIsi,
       "ntcTsDecIsisInTypeName": ntcTsDecIsisInTypeName,
       "ntcTsDecIsisInInstanceName": ntcTsDecIsisInInstanceName,
       "ntcTsDecPidsTable": ntcTsDecPidsTable,
       "ntcTsDecPidsEntry": ntcTsDecPidsEntry,
       "ntcTsDecPidsName": ntcTsDecPidsName,
       "ntcTsDecPidsRowStatus": ntcTsDecPidsRowStatus,
       "ntcTsDecPidsEnable": ntcTsDecPidsEnable,
       "ntcTsDecPidsPid": ntcTsDecPidsPid,
       "ntcTsDecPidsInTypeName": ntcTsDecPidsInTypeName,
       "ntcTsDecPidsInInstanceName": ntcTsDecPidsInInstanceName,
       "ntcTsDecPidsProtocol": ntcTsDecPidsProtocol,
       "ntcTsDecChannelsTable": ntcTsDecChannelsTable,
       "ntcTsDecChannelsEntry": ntcTsDecChannelsEntry,
       "ntcTsDecChannelsName": ntcTsDecChannelsName,
       "ntcTsDecChannelsRowStatus": ntcTsDecChannelsRowStatus,
       "ntcTsDecChannelsEnable": ntcTsDecChannelsEnable,
       "ntcTsDecChannelsInTypeName": ntcTsDecChannelsInTypeName,
       "ntcTsDecChannelsInInstanceName": ntcTsDecChannelsInInstanceName,
       "ntcTsDecChannelsLabel": ntcTsDecChannelsLabel,
       "ntcTsDecChannelsVirualNetwork": ntcTsDecChannelsVirualNetwork,
       "ntcTsDecChannelsAccessVlan": ntcTsDecChannelsAccessVlan,
       "ntcTsDecDefEncProt": ntcTsDecDefEncProt,
       "ntcTsDecMpeCrcVal": ntcTsDecMpeCrcVal,
       "ntcTsDecConformance": ntcTsDecConformance,
       "ntcTsDecConfCompliance": ntcTsDecConfCompliance,
       "ntcTsDecConfCompV1Standard": ntcTsDecConfCompV1Standard,
       "ntcTsDecConfGroup": ntcTsDecConfGroup,
       "ntcTsDecConfGrpV1Standard": ntcTsDecConfGrpV1Standard}
)
