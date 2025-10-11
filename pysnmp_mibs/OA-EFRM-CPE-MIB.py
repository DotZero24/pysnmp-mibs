# SNMP MIB module (OA-EFRM-CPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-EFRM-CPE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:49 2025
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

oaEfrmCpe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16)
)
if mibBuilder.loadTexts:
    oaEfrmCpe.setRevisions(
        ("2006-06-07 00:00",
         "2006-05-16 00:00",
         "2006-05-10 00:00",
         "2006-04-11 00:00",
         "2003-05-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaManagement_ObjectIdentity = ObjectIdentity
oaManagement = _OaManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1)
)
_OaEfrmCpeNotifications_ObjectIdentity = ObjectIdentity
oaEfrmCpeNotifications = _OaEfrmCpeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 0)
)
_OaEfrmCpeGenGrp_ObjectIdentity = ObjectIdentity
oaEfrmCpeGenGrp = _OaEfrmCpeGenGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 2)
)


class _OaEfrmCpeGenSupport_Type(Integer32):
    """Custom type oaEfrmCpeGenSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OaEfrmCpeGenSupport_Type.__name__ = "Integer32"
_OaEfrmCpeGenSupport_Object = MibScalar
oaEfrmCpeGenSupport = _OaEfrmCpeGenSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 2, 1),
    _OaEfrmCpeGenSupport_Type()
)
oaEfrmCpeGenSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeGenSupport.setStatus("current")


class _OaEfrmCoOam_Type(Integer32):
    """Custom type oaEfrmCoOam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("disable", 2),
          ("enable", 3))
    )


_OaEfrmCoOam_Type.__name__ = "Integer32"
_OaEfrmCoOam_Object = MibScalar
oaEfrmCoOam = _OaEfrmCoOam_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 2, 2),
    _OaEfrmCoOam_Type()
)
oaEfrmCoOam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCoOam.setStatus("current")


class _OaEfrmCoNoDiscardLpbkdPkts_Type(Integer32):
    """Custom type oaEfrmCoNoDiscardLpbkdPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("disable", 2),
          ("enable", 3))
    )


_OaEfrmCoNoDiscardLpbkdPkts_Type.__name__ = "Integer32"
_OaEfrmCoNoDiscardLpbkdPkts_Object = MibScalar
oaEfrmCoNoDiscardLpbkdPkts = _OaEfrmCoNoDiscardLpbkdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 2, 3),
    _OaEfrmCoNoDiscardLpbkdPkts_Type()
)
oaEfrmCoNoDiscardLpbkdPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCoNoDiscardLpbkdPkts.setStatus("current")


class _OaEfrmCoSlowProtoPktsLoopback_Type(Integer32):
    """Custom type oaEfrmCoSlowProtoPktsLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("disable", 2),
          ("enable", 3))
    )


_OaEfrmCoSlowProtoPktsLoopback_Type.__name__ = "Integer32"
_OaEfrmCoSlowProtoPktsLoopback_Object = MibScalar
oaEfrmCoSlowProtoPktsLoopback = _OaEfrmCoSlowProtoPktsLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 2, 4),
    _OaEfrmCoSlowProtoPktsLoopback_Type()
)
oaEfrmCoSlowProtoPktsLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCoSlowProtoPktsLoopback.setStatus("current")


class _OaEfrmCpeSlowProtoPktsLoopback_Type(Integer32):
    """Custom type oaEfrmCpeSlowProtoPktsLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("disable", 2),
          ("enable", 3))
    )


_OaEfrmCpeSlowProtoPktsLoopback_Type.__name__ = "Integer32"
_OaEfrmCpeSlowProtoPktsLoopback_Object = MibScalar
oaEfrmCpeSlowProtoPktsLoopback = _OaEfrmCpeSlowProtoPktsLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 2, 5),
    _OaEfrmCpeSlowProtoPktsLoopback_Type()
)
oaEfrmCpeSlowProtoPktsLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCpeSlowProtoPktsLoopback.setStatus("current")
_OaEfrmCpeModuletGrp_ObjectIdentity = ObjectIdentity
oaEfrmCpeModuletGrp = _OaEfrmCpeModuletGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3)
)
_OaEfrmCpeModuleTable_Object = MibTable
oaEfrmCpeModuleTable = _OaEfrmCpeModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    oaEfrmCpeModuleTable.setStatus("current")
_OaEfrmCpeModuleEntry_Object = MibTableRow
oaEfrmCpeModuleEntry = _OaEfrmCpeModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1)
)
oaEfrmCpeModuleEntry.setIndexNames(
    (0, "OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
)
if mibBuilder.loadTexts:
    oaEfrmCpeModuleEntry.setStatus("current")


class _OaEfrmCpeLocalPortIndex_Type(Integer32):
    """Custom type oaEfrmCpeLocalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_OaEfrmCpeLocalPortIndex_Type.__name__ = "Integer32"
_OaEfrmCpeLocalPortIndex_Object = MibTableColumn
oaEfrmCpeLocalPortIndex = _OaEfrmCpeLocalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1, 1),
    _OaEfrmCpeLocalPortIndex_Type()
)
oaEfrmCpeLocalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeLocalPortIndex.setStatus("current")


class _OaEfrmCpeModuleType_Type(Integer32):
    """Custom type oaEfrmCpeModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              19,
              21)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("unknownCardType", 2),
          ("em316efrmosCard", 3),
          ("em316grmahshCard", 19),
          ("em316efrmahshCard", 21))
    )


_OaEfrmCpeModuleType_Type.__name__ = "Integer32"
_OaEfrmCpeModuleType_Object = MibTableColumn
oaEfrmCpeModuleType = _OaEfrmCpeModuleType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1, 2),
    _OaEfrmCpeModuleType_Type()
)
oaEfrmCpeModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleType.setStatus("current")


class _OaEfrmCpeModuleRemoteLoopback_Type(Integer32):
    """Custom type oaEfrmCpeModuleRemoteLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("disable", 2),
          ("enable", 3))
    )


_OaEfrmCpeModuleRemoteLoopback_Type.__name__ = "Integer32"
_OaEfrmCpeModuleRemoteLoopback_Object = MibTableColumn
oaEfrmCpeModuleRemoteLoopback = _OaEfrmCpeModuleRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1, 4),
    _OaEfrmCpeModuleRemoteLoopback_Type()
)
oaEfrmCpeModuleRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleRemoteLoopback.setStatus("current")


class _OaEfrmCpeModuleEnable_Type(Integer32):
    """Custom type oaEfrmCpeModuleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("disable", 2),
          ("enable", 3))
    )


_OaEfrmCpeModuleEnable_Type.__name__ = "Integer32"
_OaEfrmCpeModuleEnable_Object = MibTableColumn
oaEfrmCpeModuleEnable = _OaEfrmCpeModuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1, 5),
    _OaEfrmCpeModuleEnable_Type()
)
oaEfrmCpeModuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleEnable.setStatus("current")


class _OaEfrmCpeModuleIPLessEnable_Type(Integer32):
    """Custom type oaEfrmCpeModuleIPLessEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("disable", 2),
          ("enable", 3))
    )


_OaEfrmCpeModuleIPLessEnable_Type.__name__ = "Integer32"
_OaEfrmCpeModuleIPLessEnable_Object = MibTableColumn
oaEfrmCpeModuleIPLessEnable = _OaEfrmCpeModuleIPLessEnable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1, 6),
    _OaEfrmCpeModuleIPLessEnable_Type()
)
oaEfrmCpeModuleIPLessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleIPLessEnable.setStatus("current")


class _OaEfrmCpeModuleIPLessLink_Type(Integer32):
    """Custom type oaEfrmCpeModuleIPLessLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_OaEfrmCpeModuleIPLessLink_Type.__name__ = "Integer32"
_OaEfrmCpeModuleIPLessLink_Object = MibTableColumn
oaEfrmCpeModuleIPLessLink = _OaEfrmCpeModuleIPLessLink_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1, 7),
    _OaEfrmCpeModuleIPLessLink_Type()
)
oaEfrmCpeModuleIPLessLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleIPLessLink.setStatus("current")


class _OaEfrmCpeCpeCoSW_Type(Integer32):
    """Custom type oaEfrmCpeCpeCoSW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("co", 2),
          ("cpe", 3))
    )


_OaEfrmCpeCpeCoSW_Type.__name__ = "Integer32"
_OaEfrmCpeCpeCoSW_Object = MibTableColumn
oaEfrmCpeCpeCoSW = _OaEfrmCpeCpeCoSW_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1, 11),
    _OaEfrmCpeCpeCoSW_Type()
)
oaEfrmCpeCpeCoSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeCpeCoSW.setStatus("current")


class _OaEfrmCpeCpeManagementSW_Type(Integer32):
    """Custom type oaEfrmCpeCpeManagementSW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("disable", 2),
          ("enable", 3))
    )


_OaEfrmCpeCpeManagementSW_Type.__name__ = "Integer32"
_OaEfrmCpeCpeManagementSW_Object = MibTableColumn
oaEfrmCpeCpeManagementSW = _OaEfrmCpeCpeManagementSW_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1, 12),
    _OaEfrmCpeCpeManagementSW_Type()
)
oaEfrmCpeCpeManagementSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeCpeManagementSW.setStatus("current")


class _OaEfrmCpeCpeLINSW_Type(Integer32):
    """Custom type oaEfrmCpeCpeLINSW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("disable", 2),
          ("enable", 3))
    )


_OaEfrmCpeCpeLINSW_Type.__name__ = "Integer32"
_OaEfrmCpeCpeLINSW_Object = MibTableColumn
oaEfrmCpeCpeLINSW = _OaEfrmCpeCpeLINSW_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1, 13),
    _OaEfrmCpeCpeLINSW_Type()
)
oaEfrmCpeCpeLINSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeCpeLINSW.setStatus("current")


class _OaEfrmCpeModuleMdiSW_Type(Integer32):
    """Custom type oaEfrmCpeModuleMdiSW based on Integer32"""
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
        *(("notSupported", 1),
          ("mdi", 2),
          ("mdix", 3),
          ("auto", 4))
    )


_OaEfrmCpeModuleMdiSW_Type.__name__ = "Integer32"
_OaEfrmCpeModuleMdiSW_Object = MibTableColumn
oaEfrmCpeModuleMdiSW = _OaEfrmCpeModuleMdiSW_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1, 14),
    _OaEfrmCpeModuleMdiSW_Type()
)
oaEfrmCpeModuleMdiSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleMdiSW.setStatus("current")


class _OaEfrmCpePowerFail_Type(Integer32):
    """Custom type oaEfrmCpePowerFail based on Integer32"""
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
        *(("notSupported", 1),
          ("fail", 2),
          ("good", 3),
          ("unknown", 4))
    )


_OaEfrmCpePowerFail_Type.__name__ = "Integer32"
_OaEfrmCpePowerFail_Object = MibTableColumn
oaEfrmCpePowerFail = _OaEfrmCpePowerFail_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1, 15),
    _OaEfrmCpePowerFail_Type()
)
oaEfrmCpePowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpePowerFail.setStatus("current")


class _OaEfrmCpeModuleName_Type(DisplayString):
    """Custom type oaEfrmCpeModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OaEfrmCpeModuleName_Type.__name__ = "DisplayString"
_OaEfrmCpeModuleName_Object = MibTableColumn
oaEfrmCpeModuleName = _OaEfrmCpeModuleName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 1, 1, 16),
    _OaEfrmCpeModuleName_Type()
)
oaEfrmCpeModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleName.setStatus("current")
_OaEfrmCpeModuleExtTable_Object = MibTable
oaEfrmCpeModuleExtTable = _OaEfrmCpeModuleExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2)
)
if mibBuilder.loadTexts:
    oaEfrmCpeModuleExtTable.setStatus("current")
_OaEfrmCpeModuleExtEntry_Object = MibTableRow
oaEfrmCpeModuleExtEntry = _OaEfrmCpeModuleExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1)
)
oaEfrmCpeModuleExtEntry.setIndexNames(
    (0, "OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
)
if mibBuilder.loadTexts:
    oaEfrmCpeModuleExtEntry.setStatus("current")


class _OaEfrmCpeModuleMacAddress_Type(OctetString):
    """Custom type oaEfrmCpeModuleMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_OaEfrmCpeModuleMacAddress_Type.__name__ = "OctetString"
_OaEfrmCpeModuleMacAddress_Object = MibTableColumn
oaEfrmCpeModuleMacAddress = _OaEfrmCpeModuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1, 2),
    _OaEfrmCpeModuleMacAddress_Type()
)
oaEfrmCpeModuleMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleMacAddress.setStatus("current")


class _OaEfrmCpeModuleAppRev_Type(DisplayString):
    """Custom type oaEfrmCpeModuleAppRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OaEfrmCpeModuleAppRev_Type.__name__ = "DisplayString"
_OaEfrmCpeModuleAppRev_Object = MibTableColumn
oaEfrmCpeModuleAppRev = _OaEfrmCpeModuleAppRev_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1, 3),
    _OaEfrmCpeModuleAppRev_Type()
)
oaEfrmCpeModuleAppRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleAppRev.setStatus("current")


class _OaEfrmCpeModuleFpgaRev_Type(DisplayString):
    """Custom type oaEfrmCpeModuleFpgaRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OaEfrmCpeModuleFpgaRev_Type.__name__ = "DisplayString"
_OaEfrmCpeModuleFpgaRev_Object = MibTableColumn
oaEfrmCpeModuleFpgaRev = _OaEfrmCpeModuleFpgaRev_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1, 4),
    _OaEfrmCpeModuleFpgaRev_Type()
)
oaEfrmCpeModuleFpgaRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleFpgaRev.setStatus("current")


class _OaEfrmCpeModuleVendorOUI_Type(OctetString):
    """Custom type oaEfrmCpeModuleVendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_OaEfrmCpeModuleVendorOUI_Type.__name__ = "OctetString"
_OaEfrmCpeModuleVendorOUI_Object = MibTableColumn
oaEfrmCpeModuleVendorOUI = _OaEfrmCpeModuleVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1, 5),
    _OaEfrmCpeModuleVendorOUI_Type()
)
oaEfrmCpeModuleVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleVendorOUI.setStatus("current")


class _OaEfrmCpeModuleVendorInfo_Type(OctetString):
    """Custom type oaEfrmCpeModuleVendorInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OaEfrmCpeModuleVendorInfo_Type.__name__ = "OctetString"
_OaEfrmCpeModuleVendorInfo_Object = MibTableColumn
oaEfrmCpeModuleVendorInfo = _OaEfrmCpeModuleVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1, 6),
    _OaEfrmCpeModuleVendorInfo_Type()
)
oaEfrmCpeModuleVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleVendorInfo.setStatus("current")


class _OaEfrmCpeModuleMaxPduSize_Type(Integer32):
    """Custom type oaEfrmCpeModuleMaxPduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaEfrmCpeModuleMaxPduSize_Type.__name__ = "Integer32"
_OaEfrmCpeModuleMaxPduSize_Object = MibTableColumn
oaEfrmCpeModuleMaxPduSize = _OaEfrmCpeModuleMaxPduSize_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1, 7),
    _OaEfrmCpeModuleMaxPduSize_Type()
)
oaEfrmCpeModuleMaxPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleMaxPduSize.setStatus("current")


class _OaEfrmCpeModuleDiscoveryState_Type(Integer32):
    """Custom type oaEfrmCpeModuleDiscoveryState based on Integer32"""
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
        *(("notSupported", 1),
          ("fault", 2),
          ("activeSendLocal", 3),
          ("passiveWait", 4),
          ("sendLocalRemote", 5),
          ("sendLocalRemoteOk", 6),
          ("sendAny", 7))
    )


_OaEfrmCpeModuleDiscoveryState_Type.__name__ = "Integer32"
_OaEfrmCpeModuleDiscoveryState_Object = MibTableColumn
oaEfrmCpeModuleDiscoveryState = _OaEfrmCpeModuleDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1, 8),
    _OaEfrmCpeModuleDiscoveryState_Type()
)
oaEfrmCpeModuleDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeModuleDiscoveryState.setStatus("current")


class _OaEfrmCpeModulePduState_Type(Integer32):
    """Custom type oaEfrmCpeModulePduState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("lfInfo", 2),
          ("rfInfo", 3),
          ("info", 4),
          ("any", 5))
    )


_OaEfrmCpeModulePduState_Type.__name__ = "Integer32"
_OaEfrmCpeModulePduState_Object = MibTableColumn
oaEfrmCpeModulePduState = _OaEfrmCpeModulePduState_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1, 9),
    _OaEfrmCpeModulePduState_Type()
)
oaEfrmCpeModulePduState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeModulePduState.setStatus("current")


class _OaEfrmCoModuleDiscoveryState_Type(Integer32):
    """Custom type oaEfrmCoModuleDiscoveryState based on Integer32"""
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
        *(("notSupported", 1),
          ("fault", 2),
          ("activeSendLocal", 3),
          ("passiveWait", 4),
          ("sendLocalRemote", 5),
          ("sendLocalRemoteOk", 6),
          ("sendAny", 7))
    )


_OaEfrmCoModuleDiscoveryState_Type.__name__ = "Integer32"
_OaEfrmCoModuleDiscoveryState_Object = MibTableColumn
oaEfrmCoModuleDiscoveryState = _OaEfrmCoModuleDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1, 10),
    _OaEfrmCoModuleDiscoveryState_Type()
)
oaEfrmCoModuleDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoModuleDiscoveryState.setStatus("current")


class _OaEfrmCoModulePduState_Type(Integer32):
    """Custom type oaEfrmCoModulePduState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("lfInfo", 2),
          ("rfInfo", 3),
          ("info", 4),
          ("any", 5))
    )


_OaEfrmCoModulePduState_Type.__name__ = "Integer32"
_OaEfrmCoModulePduState_Object = MibTableColumn
oaEfrmCoModulePduState = _OaEfrmCoModulePduState_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1, 11),
    _OaEfrmCoModulePduState_Type()
)
oaEfrmCoModulePduState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoModulePduState.setStatus("current")


class _OaEfrmCoRedundantMode_Type(Integer32):
    """Custom type oaEfrmCoRedundantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("normal", 2),
          ("dualHome", 3))
    )


_OaEfrmCoRedundantMode_Type.__name__ = "Integer32"
_OaEfrmCoRedundantMode_Object = MibTableColumn
oaEfrmCoRedundantMode = _OaEfrmCoRedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1, 13),
    _OaEfrmCoRedundantMode_Type()
)
oaEfrmCoRedundantMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCoRedundantMode.setStatus("current")


class _OaEfrmCoRedundantActState_Type(Integer32):
    """Custom type oaEfrmCoRedundantActState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("inactive", 2),
          ("active", 3))
    )


_OaEfrmCoRedundantActState_Type.__name__ = "Integer32"
_OaEfrmCoRedundantActState_Object = MibTableColumn
oaEfrmCoRedundantActState = _OaEfrmCoRedundantActState_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 2, 1, 15),
    _OaEfrmCoRedundantActState_Type()
)
oaEfrmCoRedundantActState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoRedundantActState.setStatus("current")
_OaEfrmCoModuleTable_Object = MibTable
oaEfrmCoModuleTable = _OaEfrmCoModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 3)
)
if mibBuilder.loadTexts:
    oaEfrmCoModuleTable.setStatus("current")
_OaEfrmCoModuleEntry_Object = MibTableRow
oaEfrmCoModuleEntry = _OaEfrmCoModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 3, 1)
)
oaEfrmCoModuleEntry.setIndexNames(
    (0, "OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
)
if mibBuilder.loadTexts:
    oaEfrmCoModuleEntry.setStatus("current")


class _OaEfrmCoPortEnable_Type(Integer32):
    """Custom type oaEfrmCoPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("disable", 2),
          ("enable", 3))
    )


_OaEfrmCoPortEnable_Type.__name__ = "Integer32"
_OaEfrmCoPortEnable_Object = MibTableColumn
oaEfrmCoPortEnable = _OaEfrmCoPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 3, 1, 6),
    _OaEfrmCoPortEnable_Type()
)
oaEfrmCoPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCoPortEnable.setStatus("current")
_OaEfrmCoOamPduStatisticsTable_Object = MibTable
oaEfrmCoOamPduStatisticsTable = _OaEfrmCoOamPduStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4)
)
if mibBuilder.loadTexts:
    oaEfrmCoOamPduStatisticsTable.setStatus("current")
_OaEfrmCoOamPduStatisticsEntry_Object = MibTableRow
oaEfrmCoOamPduStatisticsEntry = _OaEfrmCoOamPduStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1)
)
oaEfrmCoOamPduStatisticsEntry.setIndexNames(
    (0, "OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
)
if mibBuilder.loadTexts:
    oaEfrmCoOamPduStatisticsEntry.setStatus("current")
_OaEfrmCoInfoTxOamPduStats_Type = Counter32
_OaEfrmCoInfoTxOamPduStats_Object = MibTableColumn
oaEfrmCoInfoTxOamPduStats = _OaEfrmCoInfoTxOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 1),
    _OaEfrmCoInfoTxOamPduStats_Type()
)
oaEfrmCoInfoTxOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoInfoTxOamPduStats.setStatus("current")
_OaEfrmCoInfoRxOamPduStats_Type = Counter32
_OaEfrmCoInfoRxOamPduStats_Object = MibTableColumn
oaEfrmCoInfoRxOamPduStats = _OaEfrmCoInfoRxOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 2),
    _OaEfrmCoInfoRxOamPduStats_Type()
)
oaEfrmCoInfoRxOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoInfoRxOamPduStats.setStatus("current")
_OaEfrmCoEventTxUniqOamPduStats_Type = Counter32
_OaEfrmCoEventTxUniqOamPduStats_Object = MibTableColumn
oaEfrmCoEventTxUniqOamPduStats = _OaEfrmCoEventTxUniqOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 3),
    _OaEfrmCoEventTxUniqOamPduStats_Type()
)
oaEfrmCoEventTxUniqOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoEventTxUniqOamPduStats.setStatus("current")
_OaEfrmCoEventRxUniqOamPduStats_Type = Counter32
_OaEfrmCoEventRxUniqOamPduStats_Object = MibTableColumn
oaEfrmCoEventRxUniqOamPduStats = _OaEfrmCoEventRxUniqOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 4),
    _OaEfrmCoEventRxUniqOamPduStats_Type()
)
oaEfrmCoEventRxUniqOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoEventRxUniqOamPduStats.setStatus("current")
_OaEfrmCoEventTxDuplOamPduStats_Type = Counter32
_OaEfrmCoEventTxDuplOamPduStats_Object = MibTableColumn
oaEfrmCoEventTxDuplOamPduStats = _OaEfrmCoEventTxDuplOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 5),
    _OaEfrmCoEventTxDuplOamPduStats_Type()
)
oaEfrmCoEventTxDuplOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoEventTxDuplOamPduStats.setStatus("current")
_OaEfrmCoEventRxDuplOamPduStats_Type = Counter32
_OaEfrmCoEventRxDuplOamPduStats_Object = MibTableColumn
oaEfrmCoEventRxDuplOamPduStats = _OaEfrmCoEventRxDuplOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 6),
    _OaEfrmCoEventRxDuplOamPduStats_Type()
)
oaEfrmCoEventRxDuplOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoEventRxDuplOamPduStats.setStatus("current")
_OaEfrmCoLpbkTxOamPduStats_Type = Counter32
_OaEfrmCoLpbkTxOamPduStats_Object = MibTableColumn
oaEfrmCoLpbkTxOamPduStats = _OaEfrmCoLpbkTxOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 7),
    _OaEfrmCoLpbkTxOamPduStats_Type()
)
oaEfrmCoLpbkTxOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoLpbkTxOamPduStats.setStatus("current")
_OaEfrmCoLpbkRxOamPduStats_Type = Counter32
_OaEfrmCoLpbkRxOamPduStats_Object = MibTableColumn
oaEfrmCoLpbkRxOamPduStats = _OaEfrmCoLpbkRxOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 8),
    _OaEfrmCoLpbkRxOamPduStats_Type()
)
oaEfrmCoLpbkRxOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoLpbkRxOamPduStats.setStatus("current")
_OaEfrmCoVarReqTxOamPduStats_Type = Counter32
_OaEfrmCoVarReqTxOamPduStats_Object = MibTableColumn
oaEfrmCoVarReqTxOamPduStats = _OaEfrmCoVarReqTxOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 9),
    _OaEfrmCoVarReqTxOamPduStats_Type()
)
oaEfrmCoVarReqTxOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoVarReqTxOamPduStats.setStatus("current")
_OaEfrmCoVarReqRxOamPduStats_Type = Counter32
_OaEfrmCoVarReqRxOamPduStats_Object = MibTableColumn
oaEfrmCoVarReqRxOamPduStats = _OaEfrmCoVarReqRxOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 10),
    _OaEfrmCoVarReqRxOamPduStats_Type()
)
oaEfrmCoVarReqRxOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoVarReqRxOamPduStats.setStatus("current")
_OaEfrmCoVarRepTxOamPduStats_Type = Counter32
_OaEfrmCoVarRepTxOamPduStats_Object = MibTableColumn
oaEfrmCoVarRepTxOamPduStats = _OaEfrmCoVarRepTxOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 11),
    _OaEfrmCoVarRepTxOamPduStats_Type()
)
oaEfrmCoVarRepTxOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoVarRepTxOamPduStats.setStatus("current")
_OaEfrmCoVarRepRxOamPduStats_Type = Counter32
_OaEfrmCoVarRepRxOamPduStats_Object = MibTableColumn
oaEfrmCoVarRepRxOamPduStats = _OaEfrmCoVarRepRxOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 12),
    _OaEfrmCoVarRepRxOamPduStats_Type()
)
oaEfrmCoVarRepRxOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoVarRepRxOamPduStats.setStatus("current")
_OaEfrmCoOrgSpecTxOamPduStats_Type = Counter32
_OaEfrmCoOrgSpecTxOamPduStats_Object = MibTableColumn
oaEfrmCoOrgSpecTxOamPduStats = _OaEfrmCoOrgSpecTxOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 13),
    _OaEfrmCoOrgSpecTxOamPduStats_Type()
)
oaEfrmCoOrgSpecTxOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoOrgSpecTxOamPduStats.setStatus("current")
_OaEfrmCoOrgSpecRxOamPduStats_Type = Counter32
_OaEfrmCoOrgSpecRxOamPduStats_Object = MibTableColumn
oaEfrmCoOrgSpecRxOamPduStats = _OaEfrmCoOrgSpecRxOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 14),
    _OaEfrmCoOrgSpecRxOamPduStats_Type()
)
oaEfrmCoOrgSpecRxOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoOrgSpecRxOamPduStats.setStatus("current")
_OaEfrmCoOrgTotalTxOamPduStats_Type = Counter32
_OaEfrmCoOrgTotalTxOamPduStats_Object = MibTableColumn
oaEfrmCoOrgTotalTxOamPduStats = _OaEfrmCoOrgTotalTxOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 15),
    _OaEfrmCoOrgTotalTxOamPduStats_Type()
)
oaEfrmCoOrgTotalTxOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoOrgTotalTxOamPduStats.setStatus("current")
_OaEfrmCoOrgTotalRxOamPduStats_Type = Counter32
_OaEfrmCoOrgTotalRxOamPduStats_Object = MibTableColumn
oaEfrmCoOrgTotalRxOamPduStats = _OaEfrmCoOrgTotalRxOamPduStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 4, 1, 16),
    _OaEfrmCoOrgTotalRxOamPduStats_Type()
)
oaEfrmCoOrgTotalRxOamPduStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCoOrgTotalRxOamPduStats.setStatus("current")
_OaEfrmCpePhyStatisticsTable_Object = MibTable
oaEfrmCpePhyStatisticsTable = _OaEfrmCpePhyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5)
)
if mibBuilder.loadTexts:
    oaEfrmCpePhyStatisticsTable.setStatus("current")
_OaEfrmCpePhyStatisticsEntry_Object = MibTableRow
oaEfrmCpePhyStatisticsEntry = _OaEfrmCpePhyStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1)
)
oaEfrmCpePhyStatisticsEntry.setIndexNames(
    (0, "OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
    (0, "OA-EFRM-CPE-MIB", "oaEfrmCpePortLogicalType"),
)
if mibBuilder.loadTexts:
    oaEfrmCpePhyStatisticsEntry.setStatus("current")
_OaEfrmCpeUcastPktsTxPhyStats_Type = Counter32
_OaEfrmCpeUcastPktsTxPhyStats_Object = MibTableColumn
oaEfrmCpeUcastPktsTxPhyStats = _OaEfrmCpeUcastPktsTxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 1),
    _OaEfrmCpeUcastPktsTxPhyStats_Type()
)
oaEfrmCpeUcastPktsTxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeUcastPktsTxPhyStats.setStatus("current")
_OaEfrmCpeUcastPktsRxPhyStats_Type = Counter32
_OaEfrmCpeUcastPktsRxPhyStats_Object = MibTableColumn
oaEfrmCpeUcastPktsRxPhyStats = _OaEfrmCpeUcastPktsRxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 2),
    _OaEfrmCpeUcastPktsRxPhyStats_Type()
)
oaEfrmCpeUcastPktsRxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeUcastPktsRxPhyStats.setStatus("current")
_OaEfrmCpeMcastPktsTxPhyStats_Type = Counter32
_OaEfrmCpeMcastPktsTxPhyStats_Object = MibTableColumn
oaEfrmCpeMcastPktsTxPhyStats = _OaEfrmCpeMcastPktsTxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 3),
    _OaEfrmCpeMcastPktsTxPhyStats_Type()
)
oaEfrmCpeMcastPktsTxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeMcastPktsTxPhyStats.setStatus("current")
_OaEfrmCpeMcastPktsRxPhyStats_Type = Counter32
_OaEfrmCpeMcastPktsRxPhyStats_Object = MibTableColumn
oaEfrmCpeMcastPktsRxPhyStats = _OaEfrmCpeMcastPktsRxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 4),
    _OaEfrmCpeMcastPktsRxPhyStats_Type()
)
oaEfrmCpeMcastPktsRxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeMcastPktsRxPhyStats.setStatus("current")
_OaEfrmCpeBcastPktsTxPhyStats_Type = Counter32
_OaEfrmCpeBcastPktsTxPhyStats_Object = MibTableColumn
oaEfrmCpeBcastPktsTxPhyStats = _OaEfrmCpeBcastPktsTxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 5),
    _OaEfrmCpeBcastPktsTxPhyStats_Type()
)
oaEfrmCpeBcastPktsTxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeBcastPktsTxPhyStats.setStatus("current")
_OaEfrmCpeBcastPktsRxPhyStats_Type = Counter32
_OaEfrmCpeBcastPktsRxPhyStats_Object = MibTableColumn
oaEfrmCpeBcastPktsRxPhyStats = _OaEfrmCpeBcastPktsRxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 6),
    _OaEfrmCpeBcastPktsRxPhyStats_Type()
)
oaEfrmCpeBcastPktsRxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeBcastPktsRxPhyStats.setStatus("current")
_OaEfrmCpeDiscardTxPhyStats_Type = Counter32
_OaEfrmCpeDiscardTxPhyStats_Object = MibTableColumn
oaEfrmCpeDiscardTxPhyStats = _OaEfrmCpeDiscardTxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 7),
    _OaEfrmCpeDiscardTxPhyStats_Type()
)
oaEfrmCpeDiscardTxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeDiscardTxPhyStats.setStatus("current")
_OaEfrmCpeDiscardRxPhyStats_Type = Counter32
_OaEfrmCpeDiscardRxPhyStats_Object = MibTableColumn
oaEfrmCpeDiscardRxPhyStats = _OaEfrmCpeDiscardRxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 8),
    _OaEfrmCpeDiscardRxPhyStats_Type()
)
oaEfrmCpeDiscardRxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeDiscardRxPhyStats.setStatus("current")
_OaEfrmCpeAllignErrRxPhyStats_Type = Counter32
_OaEfrmCpeAllignErrRxPhyStats_Object = MibTableColumn
oaEfrmCpeAllignErrRxPhyStats = _OaEfrmCpeAllignErrRxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 9),
    _OaEfrmCpeAllignErrRxPhyStats_Type()
)
oaEfrmCpeAllignErrRxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeAllignErrRxPhyStats.setStatus("current")
_OaEfrmCpeFCSErrRxPhyStats_Type = Counter32
_OaEfrmCpeFCSErrRxPhyStats_Object = MibTableColumn
oaEfrmCpeFCSErrRxPhyStats = _OaEfrmCpeFCSErrRxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 10),
    _OaEfrmCpeFCSErrRxPhyStats_Type()
)
oaEfrmCpeFCSErrRxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeFCSErrRxPhyStats.setStatus("current")
_OaEfrmCpeUnderSizeErrRxPhyStats_Type = Counter32
_OaEfrmCpeUnderSizeErrRxPhyStats_Object = MibTableColumn
oaEfrmCpeUnderSizeErrRxPhyStats = _OaEfrmCpeUnderSizeErrRxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 11),
    _OaEfrmCpeUnderSizeErrRxPhyStats_Type()
)
oaEfrmCpeUnderSizeErrRxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeUnderSizeErrRxPhyStats.setStatus("current")
_OaEfrmCpeOverSizeErrRxPhyStats_Type = Counter32
_OaEfrmCpeOverSizeErrRxPhyStats_Object = MibTableColumn
oaEfrmCpeOverSizeErrRxPhyStats = _OaEfrmCpeOverSizeErrRxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 12),
    _OaEfrmCpeOverSizeErrRxPhyStats_Type()
)
oaEfrmCpeOverSizeErrRxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeOverSizeErrRxPhyStats.setStatus("current")
_OaEfrmCpeJabbersErrRxPhyStats_Type = Counter32
_OaEfrmCpeJabbersErrRxPhyStats_Object = MibTableColumn
oaEfrmCpeJabbersErrRxPhyStats = _OaEfrmCpeJabbersErrRxPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 13),
    _OaEfrmCpeJabbersErrRxPhyStats_Type()
)
oaEfrmCpeJabbersErrRxPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeJabbersErrRxPhyStats.setStatus("current")
_OaEfrmCpeDeferredsErrPhyStats_Type = Counter32
_OaEfrmCpeDeferredsErrPhyStats_Object = MibTableColumn
oaEfrmCpeDeferredsErrPhyStats = _OaEfrmCpeDeferredsErrPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 14),
    _OaEfrmCpeDeferredsErrPhyStats_Type()
)
oaEfrmCpeDeferredsErrPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeDeferredsErrPhyStats.setStatus("current")
_OaEfrmCpeSingleCollPhyStats_Type = Counter32
_OaEfrmCpeSingleCollPhyStats_Object = MibTableColumn
oaEfrmCpeSingleCollPhyStats = _OaEfrmCpeSingleCollPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 15),
    _OaEfrmCpeSingleCollPhyStats_Type()
)
oaEfrmCpeSingleCollPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeSingleCollPhyStats.setStatus("current")
_OaEfrmCpeMultipleCollPhyStats_Type = Counter32
_OaEfrmCpeMultipleCollPhyStats_Object = MibTableColumn
oaEfrmCpeMultipleCollPhyStats = _OaEfrmCpeMultipleCollPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 16),
    _OaEfrmCpeMultipleCollPhyStats_Type()
)
oaEfrmCpeMultipleCollPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeMultipleCollPhyStats.setStatus("current")
_OaEfrmCpeLateCollPhyStats_Type = Counter32
_OaEfrmCpeLateCollPhyStats_Object = MibTableColumn
oaEfrmCpeLateCollPhyStats = _OaEfrmCpeLateCollPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 17),
    _OaEfrmCpeLateCollPhyStats_Type()
)
oaEfrmCpeLateCollPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeLateCollPhyStats.setStatus("current")
_OaEfrmCpeExcessCollPhyStats_Type = Counter32
_OaEfrmCpeExcessCollPhyStats_Object = MibTableColumn
oaEfrmCpeExcessCollPhyStats = _OaEfrmCpeExcessCollPhyStats_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 3, 5, 1, 18),
    _OaEfrmCpeExcessCollPhyStats_Type()
)
oaEfrmCpeExcessCollPhyStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeExcessCollPhyStats.setStatus("current")
_OaEfrmCpePortGrp_ObjectIdentity = ObjectIdentity
oaEfrmCpePortGrp = _OaEfrmCpePortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4)
)


class _OaEfrmCpeNumberOfPorts_Type(Integer32):
    """Custom type oaEfrmCpeNumberOfPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OaEfrmCpeNumberOfPorts_Type.__name__ = "Integer32"
_OaEfrmCpeNumberOfPorts_Object = MibScalar
oaEfrmCpeNumberOfPorts = _OaEfrmCpeNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 1),
    _OaEfrmCpeNumberOfPorts_Type()
)
oaEfrmCpeNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeNumberOfPorts.setStatus("current")
_OaEfrmCpePortTable_Object = MibTable
oaEfrmCpePortTable = _OaEfrmCpePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5)
)
if mibBuilder.loadTexts:
    oaEfrmCpePortTable.setStatus("current")
_OaEfrmCpePortEntry_Object = MibTableRow
oaEfrmCpePortEntry = _OaEfrmCpePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1)
)
oaEfrmCpePortEntry.setIndexNames(
    (0, "OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
    (0, "OA-EFRM-CPE-MIB", "oaEfrmCpeCPEPortIndex"),
)
if mibBuilder.loadTexts:
    oaEfrmCpePortEntry.setStatus("current")


class _OaEfrmCpeCPEPortIndex_Type(Integer32):
    """Custom type oaEfrmCpeCPEPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OaEfrmCpeCPEPortIndex_Type.__name__ = "Integer32"
_OaEfrmCpeCPEPortIndex_Object = MibTableColumn
oaEfrmCpeCPEPortIndex = _OaEfrmCpeCPEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 2),
    _OaEfrmCpeCPEPortIndex_Type()
)
oaEfrmCpeCPEPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeCPEPortIndex.setStatus("current")


class _OaEfrmCpePortType_Type(Integer32):
    """Custom type oaEfrmCpePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              16,
              17,
              18,
              19,
              20,
              24,
              25,
              26,
              27,
              28,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("rj45Rj45Na", 1),
          ("notInstalled", 2),
          ("unknownType", 3),
          ("mLcMm", 16),
          ("mxLcMmmx", 17),
          ("s1LcSms1", 18),
          ("s2LcSms2", 19),
          ("s3LcSms3", 20),
          ("mDscMm", 24),
          ("mxDscMmmx", 25),
          ("s1DscSms1", 26),
          ("s2DscSms2", 27),
          ("s3DscSms3", 28),
          ("s2ScSms2", 32),
          ("s3ScSms3", 33))
    )


_OaEfrmCpePortType_Type.__name__ = "Integer32"
_OaEfrmCpePortType_Object = MibTableColumn
oaEfrmCpePortType = _OaEfrmCpePortType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 5),
    _OaEfrmCpePortType_Type()
)
oaEfrmCpePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpePortType.setStatus("current")


class _OaEfrmCpePortLink_Type(Integer32):
    """Custom type oaEfrmCpePortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("noLink", 2),
          ("link", 3))
    )


_OaEfrmCpePortLink_Type.__name__ = "Integer32"
_OaEfrmCpePortLink_Object = MibTableColumn
oaEfrmCpePortLink = _OaEfrmCpePortLink_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 6),
    _OaEfrmCpePortLink_Type()
)
oaEfrmCpePortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpePortLink.setStatus("current")


class _OaEfrmCpePortAutoNegotiation_Type(Integer32):
    """Custom type oaEfrmCpePortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_OaEfrmCpePortAutoNegotiation_Type.__name__ = "Integer32"
_OaEfrmCpePortAutoNegotiation_Object = MibTableColumn
oaEfrmCpePortAutoNegotiation = _OaEfrmCpePortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 7),
    _OaEfrmCpePortAutoNegotiation_Type()
)
oaEfrmCpePortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCpePortAutoNegotiation.setStatus("current")


class _OaEfrmCpePortDuplex_Type(Integer32):
    """Custom type oaEfrmCpePortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("half", 2),
          ("full", 3))
    )


_OaEfrmCpePortDuplex_Type.__name__ = "Integer32"
_OaEfrmCpePortDuplex_Object = MibTableColumn
oaEfrmCpePortDuplex = _OaEfrmCpePortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 8),
    _OaEfrmCpePortDuplex_Type()
)
oaEfrmCpePortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCpePortDuplex.setStatus("current")


class _OaEfrmCpePortSpeed_Type(Integer32):
    """Custom type oaEfrmCpePortSpeed based on Integer32"""
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
          ("spd10mbps", 2),
          ("spd100mbps", 3),
          ("spd1000mbps", 4))
    )


_OaEfrmCpePortSpeed_Type.__name__ = "Integer32"
_OaEfrmCpePortSpeed_Object = MibTableColumn
oaEfrmCpePortSpeed = _OaEfrmCpePortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 9),
    _OaEfrmCpePortSpeed_Type()
)
oaEfrmCpePortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCpePortSpeed.setStatus("current")


class _OaEfrmCpePortActivity_Type(Integer32):
    """Custom type oaEfrmCpePortActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_OaEfrmCpePortActivity_Type.__name__ = "Integer32"
_OaEfrmCpePortActivity_Object = MibTableColumn
oaEfrmCpePortActivity = _OaEfrmCpePortActivity_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 10),
    _OaEfrmCpePortActivity_Type()
)
oaEfrmCpePortActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpePortActivity.setStatus("current")


class _OaEfrmCpePortLogicalType_Type(Integer32):
    """Custom type oaEfrmCpePortLogicalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("user", 2),
          ("trunk", 3))
    )


_OaEfrmCpePortLogicalType_Type.__name__ = "Integer32"
_OaEfrmCpePortLogicalType_Object = MibTableColumn
oaEfrmCpePortLogicalType = _OaEfrmCpePortLogicalType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 11),
    _OaEfrmCpePortLogicalType_Type()
)
oaEfrmCpePortLogicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpePortLogicalType.setStatus("current")


class _OaEfrmCpePortConnectorType_Type(Integer32):
    """Custom type oaEfrmCpePortConnectorType based on Integer32"""
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
          ("static", 2),
          ("gbic", 3),
          ("sfp", 4))
    )


_OaEfrmCpePortConnectorType_Type.__name__ = "Integer32"
_OaEfrmCpePortConnectorType_Object = MibTableColumn
oaEfrmCpePortConnectorType = _OaEfrmCpePortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 12),
    _OaEfrmCpePortConnectorType_Type()
)
oaEfrmCpePortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpePortConnectorType.setStatus("current")


class _OaEfrmCpePortConnectorSubType_Type(Integer32):
    """Custom type oaEfrmCpePortConnectorSubType based on Integer32"""
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
        *(("other", 1),
          ("rj45", 2),
          ("sc", 3),
          ("lc", 4),
          ("mtrj", 5),
          ("vf", 6))
    )


_OaEfrmCpePortConnectorSubType_Type.__name__ = "Integer32"
_OaEfrmCpePortConnectorSubType_Object = MibTableColumn
oaEfrmCpePortConnectorSubType = _OaEfrmCpePortConnectorSubType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 13),
    _OaEfrmCpePortConnectorSubType_Type()
)
oaEfrmCpePortConnectorSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpePortConnectorSubType.setStatus("current")


class _OaEfrmCpePortSfpPresent_Type(Integer32):
    """Custom type oaEfrmCpePortSfpPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("present", 2),
          ("notPresent", 3))
    )


_OaEfrmCpePortSfpPresent_Type.__name__ = "Integer32"
_OaEfrmCpePortSfpPresent_Object = MibTableColumn
oaEfrmCpePortSfpPresent = _OaEfrmCpePortSfpPresent_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 14),
    _OaEfrmCpePortSfpPresent_Type()
)
oaEfrmCpePortSfpPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpePortSfpPresent.setStatus("current")


class _OaEfrmCpePortAutoNegCaps_Type(Bits):
    """Custom type oaEfrmCpePortAutoNegCaps based on Bits"""
    namedValues = NamedValues(
        *(("cap10half", 0),
          ("cap10full", 1),
          ("cap100half", 2),
          ("cap100full", 3),
          ("cap1000half", 4),
          ("cap1000full", 5))
    )

_OaEfrmCpePortAutoNegCaps_Type.__name__ = "Bits"
_OaEfrmCpePortAutoNegCaps_Object = MibTableColumn
oaEfrmCpePortAutoNegCaps = _OaEfrmCpePortAutoNegCaps_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 15),
    _OaEfrmCpePortAutoNegCaps_Type()
)
oaEfrmCpePortAutoNegCaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCpePortAutoNegCaps.setStatus("current")


class _OaEfrmCpePortMdi_Type(Integer32):
    """Custom type oaEfrmCpePortMdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("mdi", 2),
          ("mdix", 3))
    )


_OaEfrmCpePortMdi_Type.__name__ = "Integer32"
_OaEfrmCpePortMdi_Object = MibTableColumn
oaEfrmCpePortMdi = _OaEfrmCpePortMdi_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 16),
    _OaEfrmCpePortMdi_Type()
)
oaEfrmCpePortMdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCpePortMdi.setStatus("current")


class _OaEfrmCpePortAutoSense_Type(Integer32):
    """Custom type oaEfrmCpePortAutoSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("autoSense", 2),
          ("force", 3))
    )


_OaEfrmCpePortAutoSense_Type.__name__ = "Integer32"
_OaEfrmCpePortAutoSense_Object = MibTableColumn
oaEfrmCpePortAutoSense = _OaEfrmCpePortAutoSense_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 4, 5, 1, 17),
    _OaEfrmCpePortAutoSense_Type()
)
oaEfrmCpePortAutoSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaEfrmCpePortAutoSense.setStatus("current")
_OaEfrmCpeSfp_ObjectIdentity = ObjectIdentity
oaEfrmCpeSfp = _OaEfrmCpeSfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10)
)
_OaEfrmSfpMIBObjects_ObjectIdentity = ObjectIdentity
oaEfrmSfpMIBObjects = _OaEfrmSfpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1)
)
_OaEfrmSfpInfoTable_Object = MibTable
oaEfrmSfpInfoTable = _OaEfrmSfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2)
)
if mibBuilder.loadTexts:
    oaEfrmSfpInfoTable.setStatus("current")
_OaEfrmSfpInfoEntry_Object = MibTableRow
oaEfrmSfpInfoEntry = _OaEfrmSfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1)
)
oaEfrmSfpInfoEntry.setIndexNames(
    (0, "OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
    (0, "OA-EFRM-CPE-MIB", "oaEfrmCpeCPEPortIndex"),
)
if mibBuilder.loadTexts:
    oaEfrmSfpInfoEntry.setStatus("current")


class _OaEfrmSfpInfoIdentifier_Type(Integer32):
    """Custom type oaEfrmSfpInfoIdentifier based on Integer32"""
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("gbic", 3),
          ("fixed", 4),
          ("sfp", 5),
          ("xbi300pin", 6),
          ("xenpak", 7),
          ("xfp", 8),
          ("xff", 9),
          ("xfpE", 10),
          ("xpak", 11),
          ("x2", 12),
          ("dsfp", 13))
    )


_OaEfrmSfpInfoIdentifier_Type.__name__ = "Integer32"
_OaEfrmSfpInfoIdentifier_Object = MibTableColumn
oaEfrmSfpInfoIdentifier = _OaEfrmSfpInfoIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 3),
    _OaEfrmSfpInfoIdentifier_Type()
)
oaEfrmSfpInfoIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoIdentifier.setStatus("current")


class _OaEfrmSfpInfoVendorSpecId_Type(DisplayString):
    """Custom type oaEfrmSfpInfoVendorSpecId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_OaEfrmSfpInfoVendorSpecId_Type.__name__ = "DisplayString"
_OaEfrmSfpInfoVendorSpecId_Object = MibTableColumn
oaEfrmSfpInfoVendorSpecId = _OaEfrmSfpInfoVendorSpecId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 4),
    _OaEfrmSfpInfoVendorSpecId_Type()
)
oaEfrmSfpInfoVendorSpecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoVendorSpecId.setStatus("current")


class _OaEfrmSfpInfoConnector_Type(Integer32):
    """Custom type oaEfrmSfpInfoConnector based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("sc", 3),
          ("fcs1cc", 4),
          ("fcs2cc", 5),
          ("bnctnc", 6),
          ("fcch", 7),
          ("fiberJack", 8),
          ("lc", 9),
          ("mtrj", 10),
          ("mu", 11),
          ("sg", 12),
          ("opticalPigtail", 13),
          ("hssdcii", 34),
          ("copperPigtail", 35))
    )


_OaEfrmSfpInfoConnector_Type.__name__ = "Integer32"
_OaEfrmSfpInfoConnector_Object = MibTableColumn
oaEfrmSfpInfoConnector = _OaEfrmSfpInfoConnector_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 8),
    _OaEfrmSfpInfoConnector_Type()
)
oaEfrmSfpInfoConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoConnector.setStatus("current")


class _OaEfrmSfpInfoVendorSpecConnector_Type(DisplayString):
    """Custom type oaEfrmSfpInfoVendorSpecConnector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_OaEfrmSfpInfoVendorSpecConnector_Type.__name__ = "DisplayString"
_OaEfrmSfpInfoVendorSpecConnector_Object = MibTableColumn
oaEfrmSfpInfoVendorSpecConnector = _OaEfrmSfpInfoVendorSpecConnector_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 9),
    _OaEfrmSfpInfoVendorSpecConnector_Type()
)
oaEfrmSfpInfoVendorSpecConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoVendorSpecConnector.setStatus("current")


class _OaEfrmSfpInfoVendorName_Type(DisplayString):
    """Custom type oaEfrmSfpInfoVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OaEfrmSfpInfoVendorName_Type.__name__ = "DisplayString"
_OaEfrmSfpInfoVendorName_Object = MibTableColumn
oaEfrmSfpInfoVendorName = _OaEfrmSfpInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 24),
    _OaEfrmSfpInfoVendorName_Type()
)
oaEfrmSfpInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoVendorName.setStatus("current")


class _OaEfrmSfpInfoVendorOUI_Type(DisplayString):
    """Custom type oaEfrmSfpInfoVendorOUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_OaEfrmSfpInfoVendorOUI_Type.__name__ = "DisplayString"
_OaEfrmSfpInfoVendorOUI_Object = MibTableColumn
oaEfrmSfpInfoVendorOUI = _OaEfrmSfpInfoVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 25),
    _OaEfrmSfpInfoVendorOUI_Type()
)
oaEfrmSfpInfoVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoVendorOUI.setStatus("current")


class _OaEfrmSfpInfoVendorPN_Type(DisplayString):
    """Custom type oaEfrmSfpInfoVendorPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OaEfrmSfpInfoVendorPN_Type.__name__ = "DisplayString"
_OaEfrmSfpInfoVendorPN_Object = MibTableColumn
oaEfrmSfpInfoVendorPN = _OaEfrmSfpInfoVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 26),
    _OaEfrmSfpInfoVendorPN_Type()
)
oaEfrmSfpInfoVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoVendorPN.setStatus("current")


class _OaEfrmSfpInfoVendorRev_Type(DisplayString):
    """Custom type oaEfrmSfpInfoVendorRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OaEfrmSfpInfoVendorRev_Type.__name__ = "DisplayString"
_OaEfrmSfpInfoVendorRev_Object = MibTableColumn
oaEfrmSfpInfoVendorRev = _OaEfrmSfpInfoVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 27),
    _OaEfrmSfpInfoVendorRev_Type()
)
oaEfrmSfpInfoVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoVendorRev.setStatus("current")
_OaEfrmSfpInfoLaserWavelength_Type = Integer32
_OaEfrmSfpInfoLaserWavelength_Object = MibTableColumn
oaEfrmSfpInfoLaserWavelength = _OaEfrmSfpInfoLaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 28),
    _OaEfrmSfpInfoLaserWavelength_Type()
)
oaEfrmSfpInfoLaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoLaserWavelength.setStatus("current")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoLaserWavelength.setUnits("0.01 Nano Meter(nm)")


class _OaEfrmSfpInfoVendorSN_Type(DisplayString):
    """Custom type oaEfrmSfpInfoVendorSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OaEfrmSfpInfoVendorSN_Type.__name__ = "DisplayString"
_OaEfrmSfpInfoVendorSN_Object = MibTableColumn
oaEfrmSfpInfoVendorSN = _OaEfrmSfpInfoVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 32),
    _OaEfrmSfpInfoVendorSN_Type()
)
oaEfrmSfpInfoVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoVendorSN.setStatus("current")


class _OaEfrmSfpInfoVendorDate_Type(DisplayString):
    """Custom type oaEfrmSfpInfoVendorDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_OaEfrmSfpInfoVendorDate_Type.__name__ = "DisplayString"
_OaEfrmSfpInfoVendorDate_Object = MibTableColumn
oaEfrmSfpInfoVendorDate = _OaEfrmSfpInfoVendorDate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 33),
    _OaEfrmSfpInfoVendorDate_Type()
)
oaEfrmSfpInfoVendorDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoVendorDate.setStatus("current")


class _OaEfrmSfpInfoVendorSpecLotCode_Type(DisplayString):
    """Custom type oaEfrmSfpInfoVendorSpecLotCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_OaEfrmSfpInfoVendorSpecLotCode_Type.__name__ = "DisplayString"
_OaEfrmSfpInfoVendorSpecLotCode_Object = MibTableColumn
oaEfrmSfpInfoVendorSpecLotCode = _OaEfrmSfpInfoVendorSpecLotCode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 34),
    _OaEfrmSfpInfoVendorSpecLotCode_Type()
)
oaEfrmSfpInfoVendorSpecLotCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoVendorSpecLotCode.setStatus("current")


class _OaEfrmSfpInfoVendorSpecData_Type(OctetString):
    """Custom type oaEfrmSfpInfoVendorSpecData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OaEfrmSfpInfoVendorSpecData_Type.__name__ = "OctetString"
_OaEfrmSfpInfoVendorSpecData_Object = MibTableColumn
oaEfrmSfpInfoVendorSpecData = _OaEfrmSfpInfoVendorSpecData_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 35),
    _OaEfrmSfpInfoVendorSpecData_Type()
)
oaEfrmSfpInfoVendorSpecData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoVendorSpecData.setStatus("current")


class _OaEfrmSfpInfoDiagnosticPowerType_Type(Integer32):
    """Custom type oaEfrmSfpInfoDiagnosticPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_OaEfrmSfpInfoDiagnosticPowerType_Type.__name__ = "Integer32"
_OaEfrmSfpInfoDiagnosticPowerType_Object = MibTableColumn
oaEfrmSfpInfoDiagnosticPowerType = _OaEfrmSfpInfoDiagnosticPowerType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 36),
    _OaEfrmSfpInfoDiagnosticPowerType_Type()
)
oaEfrmSfpInfoDiagnosticPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoDiagnosticPowerType.setStatus("current")


class _OaEfrmSfpInfoDigitalDiagnostic_Type(Integer32):
    """Custom type oaEfrmSfpInfoDigitalDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("digitalDiagnostic", 2),
          ("noDigitalDiagnostic", 3))
    )


_OaEfrmSfpInfoDigitalDiagnostic_Type.__name__ = "Integer32"
_OaEfrmSfpInfoDigitalDiagnostic_Object = MibTableColumn
oaEfrmSfpInfoDigitalDiagnostic = _OaEfrmSfpInfoDigitalDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 37),
    _OaEfrmSfpInfoDigitalDiagnostic_Type()
)
oaEfrmSfpInfoDigitalDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoDigitalDiagnostic.setStatus("current")


class _OaEfrmSfpInfoDiagCalibration_Type(Integer32):
    """Custom type oaEfrmSfpInfoDiagCalibration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("externalCalibration", 2),
          ("internalCalibration", 3))
    )


_OaEfrmSfpInfoDiagCalibration_Type.__name__ = "Integer32"
_OaEfrmSfpInfoDiagCalibration_Object = MibTableColumn
oaEfrmSfpInfoDiagCalibration = _OaEfrmSfpInfoDiagCalibration_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 38),
    _OaEfrmSfpInfoDiagCalibration_Type()
)
oaEfrmSfpInfoDiagCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoDiagCalibration.setStatus("current")


class _OaEfrmSfpInfoInstalledStatus_Type(Integer32):
    """Custom type oaEfrmSfpInfoInstalledStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notInstalled", 2),
          ("installed", 3))
    )


_OaEfrmSfpInfoInstalledStatus_Type.__name__ = "Integer32"
_OaEfrmSfpInfoInstalledStatus_Object = MibTableColumn
oaEfrmSfpInfoInstalledStatus = _OaEfrmSfpInfoInstalledStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 40),
    _OaEfrmSfpInfoInstalledStatus_Type()
)
oaEfrmSfpInfoInstalledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoInstalledStatus.setStatus("current")


class _OaEfrmSfpInfofaultStatus_Type(Integer32):
    """Custom type oaEfrmSfpInfofaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("faulty", 2),
          ("operational", 3))
    )


_OaEfrmSfpInfofaultStatus_Type.__name__ = "Integer32"
_OaEfrmSfpInfofaultStatus_Object = MibTableColumn
oaEfrmSfpInfofaultStatus = _OaEfrmSfpInfofaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 41),
    _OaEfrmSfpInfofaultStatus_Type()
)
oaEfrmSfpInfofaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfofaultStatus.setStatus("current")


class _OaEfrmSfpInfoEnableStatus_Type(Integer32):
    """Custom type oaEfrmSfpInfoEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_OaEfrmSfpInfoEnableStatus_Type.__name__ = "Integer32"
_OaEfrmSfpInfoEnableStatus_Object = MibTableColumn
oaEfrmSfpInfoEnableStatus = _OaEfrmSfpInfoEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 2, 1, 42),
    _OaEfrmSfpInfoEnableStatus_Type()
)
oaEfrmSfpInfoEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpInfoEnableStatus.setStatus("current")
_OaEfrmSfpDiagnosticTable_Object = MibTable
oaEfrmSfpDiagnosticTable = _OaEfrmSfpDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 3)
)
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticTable.setStatus("current")
_OaEfrmSfpDiagnosticEntry_Object = MibTableRow
oaEfrmSfpDiagnosticEntry = _OaEfrmSfpDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 3, 1)
)
oaEfrmSfpDiagnosticEntry.setIndexNames(
    (0, "OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
    (0, "OA-EFRM-CPE-MIB", "oaEfrmCpeCPEPortIndex"),
)
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticEntry.setStatus("current")
_OaEfrmSfpDiagnosticTemperature_Type = Integer32
_OaEfrmSfpDiagnosticTemperature_Object = MibTableColumn
oaEfrmSfpDiagnosticTemperature = _OaEfrmSfpDiagnosticTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 3, 1, 3),
    _OaEfrmSfpDiagnosticTemperature_Type()
)
oaEfrmSfpDiagnosticTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticTemperature.setStatus("current")
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticTemperature.setUnits("1/10 degrees Celsius (C)")
_OaEfrmSfpDiagnosticVcc_Type = Integer32
_OaEfrmSfpDiagnosticVcc_Object = MibTableColumn
oaEfrmSfpDiagnosticVcc = _OaEfrmSfpDiagnosticVcc_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 3, 1, 4),
    _OaEfrmSfpDiagnosticVcc_Type()
)
oaEfrmSfpDiagnosticVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticVcc.setStatus("current")
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticVcc.setUnits("100 micro Volts (V)")
_OaEfrmSfpDiagnosticTxBias_Type = Integer32
_OaEfrmSfpDiagnosticTxBias_Object = MibTableColumn
oaEfrmSfpDiagnosticTxBias = _OaEfrmSfpDiagnosticTxBias_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 3, 1, 5),
    _OaEfrmSfpDiagnosticTxBias_Type()
)
oaEfrmSfpDiagnosticTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticTxBias.setStatus("current")
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticTxBias.setUnits("1 micro Amperes (A)")
_OaEfrmSfpDiagnosticTxPower_Type = Integer32
_OaEfrmSfpDiagnosticTxPower_Object = MibTableColumn
oaEfrmSfpDiagnosticTxPower = _OaEfrmSfpDiagnosticTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 3, 1, 6),
    _OaEfrmSfpDiagnosticTxPower_Type()
)
oaEfrmSfpDiagnosticTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticTxPower.setStatus("current")
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticTxPower.setUnits("0.01 decibel (dBm)")
_OaEfrmSfpDiagnosticRxPower_Type = Integer32
_OaEfrmSfpDiagnosticRxPower_Object = MibTableColumn
oaEfrmSfpDiagnosticRxPower = _OaEfrmSfpDiagnosticRxPower_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 10, 1, 3, 1, 7),
    _OaEfrmSfpDiagnosticRxPower_Type()
)
oaEfrmSfpDiagnosticRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticRxPower.setStatus("current")
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticRxPower.setUnits("0.01 decibel (dBm)")
_OaEfrmCpeTrapVars_ObjectIdentity = ObjectIdentity
oaEfrmCpeTrapVars = _OaEfrmCpeTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 50)
)


class _OaEfrmCpeTrapDescription_Type(DisplayString):
    """Custom type oaEfrmCpeTrapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OaEfrmCpeTrapDescription_Type.__name__ = "DisplayString"
_OaEfrmCpeTrapDescription_Object = MibScalar
oaEfrmCpeTrapDescription = _OaEfrmCpeTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 50, 1),
    _OaEfrmCpeTrapDescription_Type()
)
oaEfrmCpeTrapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEfrmCpeTrapDescription.setStatus("current")
_OaEfrmCpeConformance_ObjectIdentity = ObjectIdentity
oaEfrmCpeConformance = _OaEfrmCpeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 100)
)
_OaEfrmCpeMIBCompliances_ObjectIdentity = ObjectIdentity
oaEfrmCpeMIBCompliances = _OaEfrmCpeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 100, 1)
)
_OaEfrmCpeMIBGroups_ObjectIdentity = ObjectIdentity
oaEfrmCpeMIBGroups = _OaEfrmCpeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 100, 2)
)

# Managed Objects groups

oaEfrmCpeMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 100, 2, 1)
)
oaEfrmCpeMandatoryGroup.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeGenSupport"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoOam"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleType"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleIPLessEnable"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoPortEnable"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleIPLessLink"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeNumberOfPorts"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeTrapDescription"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleMacAddress"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleAppRev"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleVendorOUI"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleVendorInfo"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleMaxPduSize"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoModuleDiscoveryState"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoModulePduState"))
)
if mibBuilder.loadTexts:
    oaEfrmCpeMandatoryGroup.setStatus("current")

oaEfrmCpePortMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 100, 2, 2)
)
oaEfrmCpePortMandatoryGroup.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeCPEPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortLink"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortConnectorType"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortConnectorSubType"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortSfpPresent"))
)
if mibBuilder.loadTexts:
    oaEfrmCpePortMandatoryGroup.setStatus("current")

oaEfrmCpeOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 100, 2, 3)
)
oaEfrmCpeOptionalGroup.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleRemoteLoopback"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleEnable"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeCpeCoSW"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeCpeManagementSW"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeCpeLINSW"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleMdiSW"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePowerFail"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleName"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleFpgaRev"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModuleDiscoveryState"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeModulePduState"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoRedundantMode"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoRedundantActState"))
)
if mibBuilder.loadTexts:
    oaEfrmCpeOptionalGroup.setStatus("current")

oaEfrmCpePortOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 100, 2, 4)
)
oaEfrmCpePortOptionalGroup.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpePortType"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortAutoNegotiation"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortDuplex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortSpeed"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortActivity"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortLogicalType"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortAutoNegCaps"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortMdi"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortAutoSense"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoInfoTxOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoInfoRxOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoEventTxUniqOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoEventRxUniqOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoEventTxDuplOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoEventRxDuplOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoLpbkTxOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoLpbkRxOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoVarReqTxOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoVarReqRxOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoVarRepTxOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoVarRepRxOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoOrgSpecTxOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoOrgSpecRxOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoOrgTotalTxOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCoOrgTotalRxOamPduStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeUcastPktsTxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeUcastPktsRxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeMcastPktsTxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeMcastPktsRxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeBcastPktsTxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeBcastPktsRxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeDiscardTxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeDiscardRxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeAllignErrRxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeFCSErrRxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeUnderSizeErrRxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeOverSizeErrRxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeJabbersErrRxPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeDeferredsErrPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeSingleCollPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeMultipleCollPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeLateCollPhyStats"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeExcessCollPhyStats"))
)
if mibBuilder.loadTexts:
    oaEfrmCpePortOptionalGroup.setStatus("current")

oaEfrmSfpInfoOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 100, 2, 6)
)
oaEfrmSfpInfoOptionalGroup.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoIdentifier"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoVendorSpecId"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoConnector"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoVendorSpecConnector"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoVendorName"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoVendorOUI"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoVendorPN"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoVendorSN"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoVendorRev"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoLaserWavelength"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoVendorDate"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoVendorSpecLotCode"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoVendorSpecData"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoDiagnosticPowerType"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoDigitalDiagnostic"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoDiagCalibration"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoInstalledStatus"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfofaultStatus"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoEnableStatus"))
)
if mibBuilder.loadTexts:
    oaEfrmSfpInfoOptionalGroup.setStatus("current")

oaEfrmSfpDiagnosticOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 100, 2, 7)
)
oaEfrmSfpDiagnosticOptionalGroup.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmSfpDiagnosticTemperature"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpDiagnosticVcc"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpDiagnosticTxBias"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpDiagnosticTxPower"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpDiagnosticRxPower"))
)
if mibBuilder.loadTexts:
    oaEfrmSfpDiagnosticOptionalGroup.setStatus("current")


# Notification objects

oaEfmCpeEventCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 0, 14)
)
oaEfmCpeEventCritical.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeTrapDescription"))
)
if mibBuilder.loadTexts:
    oaEfmCpeEventCritical.setStatus(
        "current"
    )

oaEfmCpeEventGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 0, 15)
)
oaEfmCpeEventGasp.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeTrapDescription"))
)
if mibBuilder.loadTexts:
    oaEfmCpeEventGasp.setStatus(
        "current"
    )

oaEfmCpeEventLinkFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 0, 16)
)
oaEfmCpeEventLinkFault.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeTrapDescription"))
)
if mibBuilder.loadTexts:
    oaEfmCpeEventLinkFault.setStatus(
        "current"
    )

oaEfmCpeEventErrSymbolPeriod = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 0, 17)
)
oaEfmCpeEventErrSymbolPeriod.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeTrapDescription"))
)
if mibBuilder.loadTexts:
    oaEfmCpeEventErrSymbolPeriod.setStatus(
        "current"
    )

oaEfmCpeEventErrFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 0, 18)
)
oaEfmCpeEventErrFrame.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeTrapDescription"))
)
if mibBuilder.loadTexts:
    oaEfmCpeEventErrFrame.setStatus(
        "current"
    )

oaEfmCpeEventErrFramePeriod = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 0, 19)
)
oaEfmCpeEventErrFramePeriod.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeTrapDescription"))
)
if mibBuilder.loadTexts:
    oaEfmCpeEventErrFramePeriod.setStatus(
        "current"
    )

oaEfmCpeEventErrFrameSecSum = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 0, 23)
)
oaEfmCpeEventErrFrameSecSum.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeTrapDescription"))
)
if mibBuilder.loadTexts:
    oaEfmCpeEventErrFrameSecSum.setStatus(
        "current"
    )

oaEfmCpeEventCpeUserPortLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 0, 24)
)
oaEfmCpeEventCpeUserPortLink.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortLink"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeTrapDescription"))
)
if mibBuilder.loadTexts:
    oaEfmCpeEventCpeUserPortLink.setStatus(
        "current"
    )

oaEfmCoPortEventConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 0, 25)
)
oaEfmCoPortEventConnectionUp.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeTrapDescription"))
)
if mibBuilder.loadTexts:
    oaEfmCoPortEventConnectionUp.setStatus(
        "current"
    )

oaEfmCoPortEventRdndHomeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 0, 26)
)
oaEfmCoPortEventRdndHomeChange.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeTrapDescription"))
)
if mibBuilder.loadTexts:
    oaEfmCoPortEventRdndHomeChange.setStatus(
        "current"
    )

oaEfmCpeEventGaspClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 0, 27)
)
oaEfmCpeEventGaspClear.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeLocalPortIndex"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeTrapDescription"))
)
if mibBuilder.loadTexts:
    oaEfmCpeEventGaspClear.setStatus(
        "current"
    )


# Notifications groups

oaEfrmCpeNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 100, 2, 5)
)
oaEfrmCpeNotificationsGroup.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfmCpeEventCritical"),
        ("OA-EFRM-CPE-MIB", "oaEfmCpeEventGasp"),
        ("OA-EFRM-CPE-MIB", "oaEfmCpeEventLinkFault"),
        ("OA-EFRM-CPE-MIB", "oaEfmCpeEventErrSymbolPeriod"),
        ("OA-EFRM-CPE-MIB", "oaEfmCpeEventErrFrame"),
        ("OA-EFRM-CPE-MIB", "oaEfmCpeEventErrFramePeriod"),
        ("OA-EFRM-CPE-MIB", "oaEfmCpeEventErrFrameSecSum"),
        ("OA-EFRM-CPE-MIB", "oaEfmCpeEventCpeUserPortLink"),
        ("OA-EFRM-CPE-MIB", "oaEfmCoPortEventConnectionUp"),
        ("OA-EFRM-CPE-MIB", "oaEfmCoPortEventRdndHomeChange"),
        ("OA-EFRM-CPE-MIB", "oaEfmCpeEventGaspClear"))
)
if mibBuilder.loadTexts:
    oaEfrmCpeNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

oaEfrmCpeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 1, 16, 100, 1, 1)
)
oaEfrmCpeMIBCompliance.setObjects(
      *(("OA-EFRM-CPE-MIB", "oaEfrmCpeMandatoryGroup"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortMandatoryGroup"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeNotificationsGroup"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpeOptionalGroup"),
        ("OA-EFRM-CPE-MIB", "oaEfrmCpePortOptionalGroup"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpInfoOptionalGroup"),
        ("OA-EFRM-CPE-MIB", "oaEfrmSfpDiagnosticOptionalGroup"))
)
if mibBuilder.loadTexts:
    oaEfrmCpeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-EFRM-CPE-MIB",
    **{"oaccess": oaccess,
       "oaManagement": oaManagement,
       "oaEfrmCpe": oaEfrmCpe,
       "oaEfrmCpeNotifications": oaEfrmCpeNotifications,
       "oaEfmCpeEventCritical": oaEfmCpeEventCritical,
       "oaEfmCpeEventGasp": oaEfmCpeEventGasp,
       "oaEfmCpeEventLinkFault": oaEfmCpeEventLinkFault,
       "oaEfmCpeEventErrSymbolPeriod": oaEfmCpeEventErrSymbolPeriod,
       "oaEfmCpeEventErrFrame": oaEfmCpeEventErrFrame,
       "oaEfmCpeEventErrFramePeriod": oaEfmCpeEventErrFramePeriod,
       "oaEfmCpeEventErrFrameSecSum": oaEfmCpeEventErrFrameSecSum,
       "oaEfmCpeEventCpeUserPortLink": oaEfmCpeEventCpeUserPortLink,
       "oaEfmCoPortEventConnectionUp": oaEfmCoPortEventConnectionUp,
       "oaEfmCoPortEventRdndHomeChange": oaEfmCoPortEventRdndHomeChange,
       "oaEfmCpeEventGaspClear": oaEfmCpeEventGaspClear,
       "oaEfrmCpeGenGrp": oaEfrmCpeGenGrp,
       "oaEfrmCpeGenSupport": oaEfrmCpeGenSupport,
       "oaEfrmCoOam": oaEfrmCoOam,
       "oaEfrmCoNoDiscardLpbkdPkts": oaEfrmCoNoDiscardLpbkdPkts,
       "oaEfrmCoSlowProtoPktsLoopback": oaEfrmCoSlowProtoPktsLoopback,
       "oaEfrmCpeSlowProtoPktsLoopback": oaEfrmCpeSlowProtoPktsLoopback,
       "oaEfrmCpeModuletGrp": oaEfrmCpeModuletGrp,
       "oaEfrmCpeModuleTable": oaEfrmCpeModuleTable,
       "oaEfrmCpeModuleEntry": oaEfrmCpeModuleEntry,
       "oaEfrmCpeLocalPortIndex": oaEfrmCpeLocalPortIndex,
       "oaEfrmCpeModuleType": oaEfrmCpeModuleType,
       "oaEfrmCpeModuleRemoteLoopback": oaEfrmCpeModuleRemoteLoopback,
       "oaEfrmCpeModuleEnable": oaEfrmCpeModuleEnable,
       "oaEfrmCpeModuleIPLessEnable": oaEfrmCpeModuleIPLessEnable,
       "oaEfrmCpeModuleIPLessLink": oaEfrmCpeModuleIPLessLink,
       "oaEfrmCpeCpeCoSW": oaEfrmCpeCpeCoSW,
       "oaEfrmCpeCpeManagementSW": oaEfrmCpeCpeManagementSW,
       "oaEfrmCpeCpeLINSW": oaEfrmCpeCpeLINSW,
       "oaEfrmCpeModuleMdiSW": oaEfrmCpeModuleMdiSW,
       "oaEfrmCpePowerFail": oaEfrmCpePowerFail,
       "oaEfrmCpeModuleName": oaEfrmCpeModuleName,
       "oaEfrmCpeModuleExtTable": oaEfrmCpeModuleExtTable,
       "oaEfrmCpeModuleExtEntry": oaEfrmCpeModuleExtEntry,
       "oaEfrmCpeModuleMacAddress": oaEfrmCpeModuleMacAddress,
       "oaEfrmCpeModuleAppRev": oaEfrmCpeModuleAppRev,
       "oaEfrmCpeModuleFpgaRev": oaEfrmCpeModuleFpgaRev,
       "oaEfrmCpeModuleVendorOUI": oaEfrmCpeModuleVendorOUI,
       "oaEfrmCpeModuleVendorInfo": oaEfrmCpeModuleVendorInfo,
       "oaEfrmCpeModuleMaxPduSize": oaEfrmCpeModuleMaxPduSize,
       "oaEfrmCpeModuleDiscoveryState": oaEfrmCpeModuleDiscoveryState,
       "oaEfrmCpeModulePduState": oaEfrmCpeModulePduState,
       "oaEfrmCoModuleDiscoveryState": oaEfrmCoModuleDiscoveryState,
       "oaEfrmCoModulePduState": oaEfrmCoModulePduState,
       "oaEfrmCoRedundantMode": oaEfrmCoRedundantMode,
       "oaEfrmCoRedundantActState": oaEfrmCoRedundantActState,
       "oaEfrmCoModuleTable": oaEfrmCoModuleTable,
       "oaEfrmCoModuleEntry": oaEfrmCoModuleEntry,
       "oaEfrmCoPortEnable": oaEfrmCoPortEnable,
       "oaEfrmCoOamPduStatisticsTable": oaEfrmCoOamPduStatisticsTable,
       "oaEfrmCoOamPduStatisticsEntry": oaEfrmCoOamPduStatisticsEntry,
       "oaEfrmCoInfoTxOamPduStats": oaEfrmCoInfoTxOamPduStats,
       "oaEfrmCoInfoRxOamPduStats": oaEfrmCoInfoRxOamPduStats,
       "oaEfrmCoEventTxUniqOamPduStats": oaEfrmCoEventTxUniqOamPduStats,
       "oaEfrmCoEventRxUniqOamPduStats": oaEfrmCoEventRxUniqOamPduStats,
       "oaEfrmCoEventTxDuplOamPduStats": oaEfrmCoEventTxDuplOamPduStats,
       "oaEfrmCoEventRxDuplOamPduStats": oaEfrmCoEventRxDuplOamPduStats,
       "oaEfrmCoLpbkTxOamPduStats": oaEfrmCoLpbkTxOamPduStats,
       "oaEfrmCoLpbkRxOamPduStats": oaEfrmCoLpbkRxOamPduStats,
       "oaEfrmCoVarReqTxOamPduStats": oaEfrmCoVarReqTxOamPduStats,
       "oaEfrmCoVarReqRxOamPduStats": oaEfrmCoVarReqRxOamPduStats,
       "oaEfrmCoVarRepTxOamPduStats": oaEfrmCoVarRepTxOamPduStats,
       "oaEfrmCoVarRepRxOamPduStats": oaEfrmCoVarRepRxOamPduStats,
       "oaEfrmCoOrgSpecTxOamPduStats": oaEfrmCoOrgSpecTxOamPduStats,
       "oaEfrmCoOrgSpecRxOamPduStats": oaEfrmCoOrgSpecRxOamPduStats,
       "oaEfrmCoOrgTotalTxOamPduStats": oaEfrmCoOrgTotalTxOamPduStats,
       "oaEfrmCoOrgTotalRxOamPduStats": oaEfrmCoOrgTotalRxOamPduStats,
       "oaEfrmCpePhyStatisticsTable": oaEfrmCpePhyStatisticsTable,
       "oaEfrmCpePhyStatisticsEntry": oaEfrmCpePhyStatisticsEntry,
       "oaEfrmCpeUcastPktsTxPhyStats": oaEfrmCpeUcastPktsTxPhyStats,
       "oaEfrmCpeUcastPktsRxPhyStats": oaEfrmCpeUcastPktsRxPhyStats,
       "oaEfrmCpeMcastPktsTxPhyStats": oaEfrmCpeMcastPktsTxPhyStats,
       "oaEfrmCpeMcastPktsRxPhyStats": oaEfrmCpeMcastPktsRxPhyStats,
       "oaEfrmCpeBcastPktsTxPhyStats": oaEfrmCpeBcastPktsTxPhyStats,
       "oaEfrmCpeBcastPktsRxPhyStats": oaEfrmCpeBcastPktsRxPhyStats,
       "oaEfrmCpeDiscardTxPhyStats": oaEfrmCpeDiscardTxPhyStats,
       "oaEfrmCpeDiscardRxPhyStats": oaEfrmCpeDiscardRxPhyStats,
       "oaEfrmCpeAllignErrRxPhyStats": oaEfrmCpeAllignErrRxPhyStats,
       "oaEfrmCpeFCSErrRxPhyStats": oaEfrmCpeFCSErrRxPhyStats,
       "oaEfrmCpeUnderSizeErrRxPhyStats": oaEfrmCpeUnderSizeErrRxPhyStats,
       "oaEfrmCpeOverSizeErrRxPhyStats": oaEfrmCpeOverSizeErrRxPhyStats,
       "oaEfrmCpeJabbersErrRxPhyStats": oaEfrmCpeJabbersErrRxPhyStats,
       "oaEfrmCpeDeferredsErrPhyStats": oaEfrmCpeDeferredsErrPhyStats,
       "oaEfrmCpeSingleCollPhyStats": oaEfrmCpeSingleCollPhyStats,
       "oaEfrmCpeMultipleCollPhyStats": oaEfrmCpeMultipleCollPhyStats,
       "oaEfrmCpeLateCollPhyStats": oaEfrmCpeLateCollPhyStats,
       "oaEfrmCpeExcessCollPhyStats": oaEfrmCpeExcessCollPhyStats,
       "oaEfrmCpePortGrp": oaEfrmCpePortGrp,
       "oaEfrmCpeNumberOfPorts": oaEfrmCpeNumberOfPorts,
       "oaEfrmCpePortTable": oaEfrmCpePortTable,
       "oaEfrmCpePortEntry": oaEfrmCpePortEntry,
       "oaEfrmCpeCPEPortIndex": oaEfrmCpeCPEPortIndex,
       "oaEfrmCpePortType": oaEfrmCpePortType,
       "oaEfrmCpePortLink": oaEfrmCpePortLink,
       "oaEfrmCpePortAutoNegotiation": oaEfrmCpePortAutoNegotiation,
       "oaEfrmCpePortDuplex": oaEfrmCpePortDuplex,
       "oaEfrmCpePortSpeed": oaEfrmCpePortSpeed,
       "oaEfrmCpePortActivity": oaEfrmCpePortActivity,
       "oaEfrmCpePortLogicalType": oaEfrmCpePortLogicalType,
       "oaEfrmCpePortConnectorType": oaEfrmCpePortConnectorType,
       "oaEfrmCpePortConnectorSubType": oaEfrmCpePortConnectorSubType,
       "oaEfrmCpePortSfpPresent": oaEfrmCpePortSfpPresent,
       "oaEfrmCpePortAutoNegCaps": oaEfrmCpePortAutoNegCaps,
       "oaEfrmCpePortMdi": oaEfrmCpePortMdi,
       "oaEfrmCpePortAutoSense": oaEfrmCpePortAutoSense,
       "oaEfrmCpeSfp": oaEfrmCpeSfp,
       "oaEfrmSfpMIBObjects": oaEfrmSfpMIBObjects,
       "oaEfrmSfpInfoTable": oaEfrmSfpInfoTable,
       "oaEfrmSfpInfoEntry": oaEfrmSfpInfoEntry,
       "oaEfrmSfpInfoIdentifier": oaEfrmSfpInfoIdentifier,
       "oaEfrmSfpInfoVendorSpecId": oaEfrmSfpInfoVendorSpecId,
       "oaEfrmSfpInfoConnector": oaEfrmSfpInfoConnector,
       "oaEfrmSfpInfoVendorSpecConnector": oaEfrmSfpInfoVendorSpecConnector,
       "oaEfrmSfpInfoVendorName": oaEfrmSfpInfoVendorName,
       "oaEfrmSfpInfoVendorOUI": oaEfrmSfpInfoVendorOUI,
       "oaEfrmSfpInfoVendorPN": oaEfrmSfpInfoVendorPN,
       "oaEfrmSfpInfoVendorRev": oaEfrmSfpInfoVendorRev,
       "oaEfrmSfpInfoLaserWavelength": oaEfrmSfpInfoLaserWavelength,
       "oaEfrmSfpInfoVendorSN": oaEfrmSfpInfoVendorSN,
       "oaEfrmSfpInfoVendorDate": oaEfrmSfpInfoVendorDate,
       "oaEfrmSfpInfoVendorSpecLotCode": oaEfrmSfpInfoVendorSpecLotCode,
       "oaEfrmSfpInfoVendorSpecData": oaEfrmSfpInfoVendorSpecData,
       "oaEfrmSfpInfoDiagnosticPowerType": oaEfrmSfpInfoDiagnosticPowerType,
       "oaEfrmSfpInfoDigitalDiagnostic": oaEfrmSfpInfoDigitalDiagnostic,
       "oaEfrmSfpInfoDiagCalibration": oaEfrmSfpInfoDiagCalibration,
       "oaEfrmSfpInfoInstalledStatus": oaEfrmSfpInfoInstalledStatus,
       "oaEfrmSfpInfofaultStatus": oaEfrmSfpInfofaultStatus,
       "oaEfrmSfpInfoEnableStatus": oaEfrmSfpInfoEnableStatus,
       "oaEfrmSfpDiagnosticTable": oaEfrmSfpDiagnosticTable,
       "oaEfrmSfpDiagnosticEntry": oaEfrmSfpDiagnosticEntry,
       "oaEfrmSfpDiagnosticTemperature": oaEfrmSfpDiagnosticTemperature,
       "oaEfrmSfpDiagnosticVcc": oaEfrmSfpDiagnosticVcc,
       "oaEfrmSfpDiagnosticTxBias": oaEfrmSfpDiagnosticTxBias,
       "oaEfrmSfpDiagnosticTxPower": oaEfrmSfpDiagnosticTxPower,
       "oaEfrmSfpDiagnosticRxPower": oaEfrmSfpDiagnosticRxPower,
       "oaEfrmCpeTrapVars": oaEfrmCpeTrapVars,
       "oaEfrmCpeTrapDescription": oaEfrmCpeTrapDescription,
       "oaEfrmCpeConformance": oaEfrmCpeConformance,
       "oaEfrmCpeMIBCompliances": oaEfrmCpeMIBCompliances,
       "oaEfrmCpeMIBCompliance": oaEfrmCpeMIBCompliance,
       "oaEfrmCpeMIBGroups": oaEfrmCpeMIBGroups,
       "oaEfrmCpeMandatoryGroup": oaEfrmCpeMandatoryGroup,
       "oaEfrmCpePortMandatoryGroup": oaEfrmCpePortMandatoryGroup,
       "oaEfrmCpeOptionalGroup": oaEfrmCpeOptionalGroup,
       "oaEfrmCpePortOptionalGroup": oaEfrmCpePortOptionalGroup,
       "oaEfrmCpeNotificationsGroup": oaEfrmCpeNotificationsGroup,
       "oaEfrmSfpInfoOptionalGroup": oaEfrmSfpInfoOptionalGroup,
       "oaEfrmSfpDiagnosticOptionalGroup": oaEfrmSfpDiagnosticOptionalGroup}
)
