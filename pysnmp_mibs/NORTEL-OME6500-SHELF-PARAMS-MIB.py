# SNMP MIB module (NORTEL-OME6500-SHELF-PARAMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NORTEL-OME6500-SHELF-PARAMS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:19:00 2025
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

(ome6500,) = mibBuilder.importSymbols(
    "NORTEL-OPTICAL-OME6500-MIB",
    "ome6500")

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


# MODULE-IDENTITY

nnOme6500ShelfParams = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1)
)
if mibBuilder.loadTexts:
    nnOme6500ShelfParams.setRevisions(
        ("2007-02-02 00:00",
         "2008-05-01 00:00")
    )


# Types definitions



class ErrorCodes(Integer32):
    """Custom type ErrorCodes based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65)
        )
    )
    namedValues = NamedValues(
        *(("eNil", 0),
          ("eMSG-SENT", 1),
          ("ePRTL", 2),
          ("eCOMPLD", 3),
          ("eDENY", 4),
          ("eENEQ", 5),
          ("eENEX", 6),
          ("eENPS", 7),
          ("eIBEX", 8),
          ("eIBMS", 9),
          ("eICNV", 10),
          ("eIDNV", 11),
          ("eIDRG", 12),
          ("eIEAE", 13),
          ("eIENE", 14),
          ("eIIAC", 15),
          ("eIICT", 16),
          ("eIIPG", 17),
          ("eIITA", 18),
          ("eINUP", 19),
          ("eIPEX", 20),
          ("eIPMS", 21),
          ("eIPNV", 22),
          ("ePICC", 23),
          ("ePIUC", 24),
          ("ePIUI", 25),
          ("ePLNA", 26),
          ("eSAAL", 27),
          ("eSAAS", 28),
          ("eSABT", 29),
          ("eSAIN", 30),
          ("eSAIS", 31),
          ("eSAMS", 32),
          ("eSANP", 33),
          ("eSAOP", 34),
          ("eSAPR", 35),
          ("eSARB", 36),
          ("eSARL", 37),
          ("eSDNC", 38),
          ("eSDNR", 39),
          ("eSLEM", 40),
          ("eSNSR", 41),
          ("eSNVS", 42),
          ("eSPFA", 43),
          ("eSPLD", 44),
          ("eSPUA", 45),
          ("eSRCI", 46),
          ("eSROF", 47),
          ("eSSRD", 48),
          ("eSSRE", 49),
          ("eSSTP", 50),
          ("eSWFA", 51),
          ("eSWLD", 52),
          ("eSRPR", 53),
          ("eEQWT", 54),
          ("eICNS", 55),
          ("eODNV", 56),
          ("eIATA", 57),
          ("eICNI", 58),
          ("eTL1SNA", 59),
          ("eMERR", 60),
          ("eSFTPC-OK", 61),
          ("eSFTPC-ERR", 62),
          ("eLOST", 63),
          ("eCANC", 64),
          ("eMAX", 65))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnOme6500ShelfParamsProv_ObjectIdentity = ObjectIdentity
nnOme6500ShelfParamsProv = _NnOme6500ShelfParamsProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1)
)


class _ShelfId_Type(Integer32):
    """Custom type shelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ShelfId_Type.__name__ = "Integer32"
_ShelfId_Object = MibScalar
shelfId = _ShelfId_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 1),
    _ShelfId_Type()
)
shelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfId.setStatus("current")


class _ShelfSubId_Type(Integer32):
    """Custom type shelfSubId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ShelfSubId_Type.__name__ = "Integer32"
_ShelfSubId_Object = MibScalar
shelfSubId = _ShelfSubId_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 2),
    _ShelfSubId_Type()
)
shelfSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfSubId.setStatus("current")
_ShelfTid_Type = DisplayString
_ShelfTid_Object = MibScalar
shelfTid = _ShelfTid_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 3),
    _ShelfTid_Type()
)
shelfTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfTid.setStatus("current")
_ShelfIpAddress_Type = IpAddress
_ShelfIpAddress_Object = MibScalar
shelfIpAddress = _ShelfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 4),
    _ShelfIpAddress_Type()
)
shelfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfIpAddress.setStatus("current")
_ShelfSoftwareVersion_Type = DisplayString
_ShelfSoftwareVersion_Object = MibScalar
shelfSoftwareVersion = _ShelfSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 5),
    _ShelfSoftwareVersion_Type()
)
shelfSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfSoftwareVersion.setStatus("current")


class _ShelfSiteId_Type(Integer32):
    """Custom type shelfSiteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ShelfSiteId_Type.__name__ = "Integer32"
_ShelfSiteId_Object = MibScalar
shelfSiteId = _ShelfSiteId_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 6),
    _ShelfSiteId_Type()
)
shelfSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfSiteId.setStatus("current")
_ShelfSiteName_Type = DisplayString
_ShelfSiteName_Object = MibScalar
shelfSiteName = _ShelfSiteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 7),
    _ShelfSiteName_Type()
)
shelfSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfSiteName.setStatus("current")


class _ShelfSnmpVersion_Type(Integer32):
    """Custom type shelfSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1v2c", 1),
          ("v1v2cv3", 2),
          ("v3", 3))
    )


_ShelfSnmpVersion_Type.__name__ = "Integer32"
_ShelfSnmpVersion_Object = MibScalar
shelfSnmpVersion = _ShelfSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 8),
    _ShelfSnmpVersion_Type()
)
shelfSnmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfSnmpVersion.setStatus("current")


class _ShelfMode_Type(Integer32):
    """Custom type shelfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sonet", 1),
          ("sdh", 2),
          ("jsdh", 3))
    )


_ShelfMode_Type.__name__ = "Integer32"
_ShelfMode_Object = MibScalar
shelfMode = _ShelfMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 9),
    _ShelfMode_Type()
)
shelfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfMode.setStatus("current")


class _ShelfIsGne_Type(Integer32):
    """Custom type shelfIsGne based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ShelfIsGne_Type.__name__ = "Integer32"
_ShelfIsGne_Object = MibScalar
shelfIsGne = _ShelfIsGne_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 10),
    _ShelfIsGne_Type()
)
shelfIsGne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfIsGne.setStatus("current")
_ShelfGneIpAddress_Type = IpAddress
_ShelfGneIpAddress_Object = MibScalar
shelfGneIpAddress = _ShelfGneIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 11),
    _ShelfGneIpAddress_Type()
)
shelfGneIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfGneIpAddress.setStatus("current")
_LastErrorRc_Type = ErrorCodes
_LastErrorRc_Object = MibScalar
lastErrorRc = _LastErrorRc_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 12),
    _LastErrorRc_Type()
)
lastErrorRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastErrorRc.setStatus("current")
_LastErrorDescription_Type = DisplayString
_LastErrorDescription_Object = MibScalar
lastErrorDescription = _LastErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 1, 1, 13),
    _LastErrorDescription_Type()
)
lastErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastErrorDescription.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-OME6500-SHELF-PARAMS-MIB",
    **{"ErrorCodes": ErrorCodes,
       "nnOme6500ShelfParams": nnOme6500ShelfParams,
       "nnOme6500ShelfParamsProv": nnOme6500ShelfParamsProv,
       "shelfId": shelfId,
       "shelfSubId": shelfSubId,
       "shelfTid": shelfTid,
       "shelfIpAddress": shelfIpAddress,
       "shelfSoftwareVersion": shelfSoftwareVersion,
       "shelfSiteId": shelfSiteId,
       "shelfSiteName": shelfSiteName,
       "shelfSnmpVersion": shelfSnmpVersion,
       "shelfMode": shelfMode,
       "shelfIsGne": shelfIsGne,
       "shelfGneIpAddress": shelfGneIpAddress,
       "lastErrorRc": lastErrorRc,
       "lastErrorDescription": lastErrorDescription}
)
