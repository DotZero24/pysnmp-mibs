# SNMP MIB module (ZTE-AN-VOIP-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-VOIP-BASE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:25 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

zxAnVoipBaseMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class A200ShelfTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dBCONBSTBASE", 1),
          ("dBCONBSTBASE1", 2),
          ("dBCONBSTSLC", 3),
          ("dBCONBSTSLC1", 4),
          ("dBCONBSTMSAGEX", 5),
          ("dBCONBSTMSAGCTL", 6),
          ("dBONU100", 8),
          ("dBOUT50C", 9),
          ("dBOUT50D", 10),
          ("dBMBSLCTL", 11),
          ("dBMBSLEX", 12),
          ("dBTPUEX", 13),
          ("dBPPEX", 14),
          ("dBDOUBLEPPEX", 15))
    )



class A200BoardTypes(TextualConvention, Integer32):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dBCONWBTASCL", 1),
          ("dBCONWBTAMTT", 2),
          ("dBCONWBTMFP", 3),
          ("dBCONWBTAPR", 4),
          ("dBCONWBTAMSNIC", 5),
          ("dBCONWBTASP", 6),
          ("dBCONWBTASPI", 7),
          ("dBCONWBTAPOW", 8),
          ("dBCONWBTAPOWP", 9),
          ("dBCONWBTAFAN", 10))
    )



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Msag_ObjectIdentity = ObjectIdentity
msag = _Msag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015)
)
_MsagmajorVersion_ObjectIdentity = ObjectIdentity
msagmajorVersion = _MsagmajorVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3)
)
_MsagGlobalConfig_ObjectIdentity = ObjectIdentity
msagGlobalConfig = _MsagGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1)
)
_A200MgCfgTable_Object = MibTable
a200MgCfgTable = _A200MgCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1)
)
if mibBuilder.loadTexts:
    a200MgCfgTable.setStatus("current")
_A200MgCfgEntry_Object = MibTableRow
a200MgCfgEntry = _A200MgCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1)
)
a200MgCfgEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200mgid"),
)
if mibBuilder.loadTexts:
    a200MgCfgEntry.setStatus("current")
_A200mgid_Type = Integer32
_A200mgid_Object = MibTableColumn
a200mgid = _A200mgid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 1),
    _A200mgid_Type()
)
a200mgid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200mgid.setStatus("current")
_A200protype_Type = Integer32
_A200protype_Object = MibTableColumn
a200protype = _A200protype_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 2),
    _A200protype_Type()
)
a200protype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200protype.setStatus("current")
_A200version_Type = Integer32
_A200version_Object = MibTableColumn
a200version = _A200version_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 3),
    _A200version_Type()
)
a200version.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200version.setStatus("current")
_A200encodetp_Type = Integer32
_A200encodetp_Object = MibTableColumn
a200encodetp = _A200encodetp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 4),
    _A200encodetp_Type()
)
a200encodetp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200encodetp.setStatus("current")
_A200mgport_Type = Integer32
_A200mgport_Object = MibTableColumn
a200mgport = _A200mgport_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 5),
    _A200mgport_Type()
)
a200mgport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgport.setStatus("current")
_A200translay_Type = Integer32
_A200translay_Object = MibTableColumn
a200translay = _A200translay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 6),
    _A200translay_Type()
)
a200translay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200translay.setStatus("current")
_A200transpro_Type = Integer32
_A200transpro_Object = MibTableColumn
a200transpro = _A200transpro_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 7),
    _A200transpro_Type()
)
a200transpro.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200transpro.setStatus("current")


class _A200mgDomainName_Type(DisplayString):
    """Custom type a200mgDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_A200mgDomainName_Type.__name__ = "DisplayString"
_A200mgDomainName_Object = MibTableColumn
a200mgDomainName = _A200mgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 8),
    _A200mgDomainName_Type()
)
a200mgDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgDomainName.setStatus("current")


class _A200mgInfo_Type(Integer32):
    """Custom type a200mgInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              128)
        )
    )
    namedValues = NamedValues(
        *(("useIp", 0),
          ("useDomain", 1),
          ("ipsIdle", 4),
          ("englishTone", 128))
    )


_A200mgInfo_Type.__name__ = "Integer32"
_A200mgInfo_Object = MibTableColumn
a200mgInfo = _A200mgInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 9),
    _A200mgInfo_Type()
)
a200mgInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgInfo.setStatus("current")


class _A200mgcid1_Type(Integer32):
    """Custom type a200mgcid1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A200mgcid1_Type.__name__ = "Integer32"
_A200mgcid1_Object = MibTableColumn
a200mgcid1 = _A200mgcid1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 10),
    _A200mgcid1_Type()
)
a200mgcid1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgcid1.setStatus("current")


class _A200mgcid2_Type(Integer32):
    """Custom type a200mgcid2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A200mgcid2_Type.__name__ = "Integer32"
_A200mgcid2_Object = MibTableColumn
a200mgcid2 = _A200mgcid2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 11),
    _A200mgcid2_Type()
)
a200mgcid2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgcid2.setStatus("current")


class _A200mgcid3_Type(Integer32):
    """Custom type a200mgcid3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A200mgcid3_Type.__name__ = "Integer32"
_A200mgcid3_Object = MibTableColumn
a200mgcid3 = _A200mgcid3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 12),
    _A200mgcid3_Type()
)
a200mgcid3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgcid3.setStatus("current")


class _A200mgcid4_Type(Integer32):
    """Custom type a200mgcid4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A200mgcid4_Type.__name__ = "Integer32"
_A200mgcid4_Object = MibTableColumn
a200mgcid4 = _A200mgcid4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 13),
    _A200mgcid4_Type()
)
a200mgcid4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgcid4.setStatus("current")


class _A200selfexchange_Type(Integer32):
    """Custom type a200selfexchange based on Integer32"""
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


_A200selfexchange_Type.__name__ = "Integer32"
_A200selfexchange_Object = MibTableColumn
a200selfexchange = _A200selfexchange_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 14),
    _A200selfexchange_Type()
)
a200selfexchange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200selfexchange.setStatus("current")


class _A200protectcall_Type(Integer32):
    """Custom type a200protectcall based on Integer32"""
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


_A200protectcall_Type.__name__ = "Integer32"
_A200protectcall_Object = MibTableColumn
a200protectcall = _A200protectcall_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 15),
    _A200protectcall_Type()
)
a200protectcall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200protectcall.setStatus("current")


class _A200disasterprot_Type(Integer32):
    """Custom type a200disasterprot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disble", 0),
          ("enable", 1))
    )


_A200disasterprot_Type.__name__ = "Integer32"
_A200disasterprot_Object = MibTableColumn
a200disasterprot = _A200disasterprot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 16),
    _A200disasterprot_Type()
)
a200disasterprot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200disasterprot.setStatus("current")
_A200mgRowStatus_Type = RowStatus
_A200mgRowStatus_Object = MibTableColumn
a200mgRowStatus = _A200mgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 17),
    _A200mgRowStatus_Type()
)
a200mgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgRowStatus.setStatus("current")
_A200tractnum_Type = Integer32
_A200tractnum_Object = MibTableColumn
a200tractnum = _A200tractnum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 18),
    _A200tractnum_Type()
)
a200tractnum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200tractnum.setStatus("current")
_A200sdpcho_Type = Integer32
_A200sdpcho_Object = MibTableColumn
a200sdpcho = _A200sdpcho_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 19),
    _A200sdpcho_Type()
)
a200sdpcho.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200sdpcho.setStatus("current")
_A200retrannum_Type = Integer32
_A200retrannum_Object = MibTableColumn
a200retrannum = _A200retrannum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 20),
    _A200retrannum_Type()
)
a200retrannum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200retrannum.setStatus("current")
_A200resdelay_Type = Integer32
_A200resdelay_Object = MibTableColumn
a200resdelay = _A200resdelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 21),
    _A200resdelay_Type()
)
a200resdelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200resdelay.setStatus("current")
_A200retranmin_Type = Integer32
_A200retranmin_Object = MibTableColumn
a200retranmin = _A200retranmin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 22),
    _A200retranmin_Type()
)
a200retranmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200retranmin.setStatus("current")
_A200lkpttime_Type = Integer32
_A200lkpttime_Object = MibTableColumn
a200lkpttime = _A200lkpttime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 23),
    _A200lkpttime_Type()
)
a200lkpttime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200lkpttime.setStatus("current")
_A200pendtime_Type = Integer32
_A200pendtime_Object = MibTableColumn
a200pendtime = _A200pendtime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 24),
    _A200pendtime_Type()
)
a200pendtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200pendtime.setStatus("current")
_A200pendcount_Type = Integer32
_A200pendcount_Object = MibTableColumn
a200pendcount = _A200pendcount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 25),
    _A200pendcount_Type()
)
a200pendcount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200pendcount.setStatus("current")
_A200kprestime_Type = Integer32
_A200kprestime_Object = MibTableColumn
a200kprestime = _A200kprestime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 26),
    _A200kprestime_Type()
)
a200kprestime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200kprestime.setStatus("current")
_A200tranidmax_Type = Unsigned32
_A200tranidmax_Object = MibTableColumn
a200tranidmax = _A200tranidmax_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 27),
    _A200tranidmax_Type()
)
a200tranidmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200tranidmax.setStatus("current")
_A200tranidmin_Type = Unsigned32
_A200tranidmin_Object = MibTableColumn
a200tranidmin = _A200tranidmin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 28),
    _A200tranidmin_Type()
)
a200tranidmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200tranidmin.setStatus("current")


class _A200rtpFaxPri1_Type(Integer32):
    """Custom type a200rtpFaxPri1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faxVBD", 1),
          ("faxT38", 2))
    )


_A200rtpFaxPri1_Type.__name__ = "Integer32"
_A200rtpFaxPri1_Object = MibTableColumn
a200rtpFaxPri1 = _A200rtpFaxPri1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 29),
    _A200rtpFaxPri1_Type()
)
a200rtpFaxPri1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200rtpFaxPri1.setStatus("current")


class _A200rtpFaxPri2_Type(Integer32):
    """Custom type a200rtpFaxPri2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faxVBD", 1),
          ("faxT38", 2))
    )


_A200rtpFaxPri2_Type.__name__ = "Integer32"
_A200rtpFaxPri2_Object = MibTableColumn
a200rtpFaxPri2 = _A200rtpFaxPri2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 30),
    _A200rtpFaxPri2_Type()
)
a200rtpFaxPri2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200rtpFaxPri2.setStatus("current")


class _A200subsuspendrtp_Type(Integer32):
    """Custom type a200subsuspendrtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sub", 1),
          ("notsub", 2))
    )


_A200subsuspendrtp_Type.__name__ = "Integer32"
_A200subsuspendrtp_Object = MibTableColumn
a200subsuspendrtp = _A200subsuspendrtp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 31),
    _A200subsuspendrtp_Type()
)
a200subsuspendrtp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200subsuspendrtp.setStatus("current")


class _A200hotlinewithspace_Type(Integer32):
    """Custom type a200hotlinewithspace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("withoutSpace", 0),
          ("withSpace", 1),
          ("withT", 2))
    )


_A200hotlinewithspace_Type.__name__ = "Integer32"
_A200hotlinewithspace_Object = MibTableColumn
a200hotlinewithspace = _A200hotlinewithspace_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 32),
    _A200hotlinewithspace_Type()
)
a200hotlinewithspace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200hotlinewithspace.setStatus("current")


class _A200rtp2833Type_Type(Integer32):
    """Custom type a200rtp2833Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type2833Redun", 1),
          ("typeRTP", 2),
          ("type2833NoRedun", 3))
    )


_A200rtp2833Type_Type.__name__ = "Integer32"
_A200rtp2833Type_Object = MibTableColumn
a200rtp2833Type = _A200rtp2833Type_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 33),
    _A200rtp2833Type_Type()
)
a200rtp2833Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200rtp2833Type.setStatus("current")


class _A200ipsThreshold_Type(Integer32):
    """Custom type a200ipsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_A200ipsThreshold_Type.__name__ = "Integer32"
_A200ipsThreshold_Object = MibTableColumn
a200ipsThreshold = _A200ipsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 34),
    _A200ipsThreshold_Type()
)
a200ipsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200ipsThreshold.setStatus("current")


class _A200congesttime_Type(Integer32):
    """Custom type a200congesttime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20),
    )


_A200congesttime_Type.__name__ = "Integer32"
_A200congesttime_Object = MibTableColumn
a200congesttime = _A200congesttime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 35),
    _A200congesttime_Type()
)
a200congesttime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200congesttime.setStatus("current")


class _A200congesttone_Type(Integer32):
    """Custom type a200congesttone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("congtone", 0)
    )


_A200congesttone_Type.__name__ = "Integer32"
_A200congesttone_Object = MibTableColumn
a200congesttone = _A200congesttone_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 36),
    _A200congesttone_Type()
)
a200congesttone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200congesttone.setStatus("current")
_A200callmatchtype_Type = Integer32
_A200callmatchtype_Object = MibTableColumn
a200callmatchtype = _A200callmatchtype_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 37),
    _A200callmatchtype_Type()
)
a200callmatchtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200callmatchtype.setStatus("current")
_A200currentmgcid_Type = Integer32
_A200currentmgcid_Object = MibTableColumn
a200currentmgcid = _A200currentmgcid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 38),
    _A200currentmgcid_Type()
)
a200currentmgcid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200currentmgcid.setStatus("current")


class _A200mgSigTos_Type(Integer32):
    """Custom type a200mgSigTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("typeCommon", 0),
          ("typeMinFee", 1),
          ("typeMaxSecurity", 2),
          ("typeMaxThruput", 4),
          ("typeMinDelay", 8))
    )


_A200mgSigTos_Type.__name__ = "Integer32"
_A200mgSigTos_Object = MibTableColumn
a200mgSigTos = _A200mgSigTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 39),
    _A200mgSigTos_Type()
)
a200mgSigTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgSigTos.setStatus("current")


class _A200mgPSTNMediaVoiceTos_Type(Integer32):
    """Custom type a200mgPSTNMediaVoiceTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("typeCommon", 0),
          ("typeMinFee", 1),
          ("typeMaxSecurity", 2),
          ("typeMaxThruput", 4),
          ("typeMinDelay", 8))
    )


_A200mgPSTNMediaVoiceTos_Type.__name__ = "Integer32"
_A200mgPSTNMediaVoiceTos_Object = MibTableColumn
a200mgPSTNMediaVoiceTos = _A200mgPSTNMediaVoiceTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 40),
    _A200mgPSTNMediaVoiceTos_Type()
)
a200mgPSTNMediaVoiceTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgPSTNMediaVoiceTos.setStatus("current")


class _A200mgPSTNMediaFaxTos_Type(Integer32):
    """Custom type a200mgPSTNMediaFaxTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("typeCommon", 0),
          ("typeMinFee", 1),
          ("typeMaxSecurity", 2),
          ("typeMaxThruput", 4),
          ("typeMinDelay", 8))
    )


_A200mgPSTNMediaFaxTos_Type.__name__ = "Integer32"
_A200mgPSTNMediaFaxTos_Object = MibTableColumn
a200mgPSTNMediaFaxTos = _A200mgPSTNMediaFaxTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 41),
    _A200mgPSTNMediaFaxTos_Type()
)
a200mgPSTNMediaFaxTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgPSTNMediaFaxTos.setStatus("current")


class _A200mgPSTNMediaModemTos_Type(Integer32):
    """Custom type a200mgPSTNMediaModemTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("typeCommon", 0),
          ("typeMinFee", 1),
          ("typeMaxSecurity", 2),
          ("typeMaxThruput", 4),
          ("typeMinDelay", 8))
    )


_A200mgPSTNMediaModemTos_Type.__name__ = "Integer32"
_A200mgPSTNMediaModemTos_Object = MibTableColumn
a200mgPSTNMediaModemTos = _A200mgPSTNMediaModemTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 42),
    _A200mgPSTNMediaModemTos_Type()
)
a200mgPSTNMediaModemTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgPSTNMediaModemTos.setStatus("current")


class _A200mgPSTNMediaDataTos_Type(Integer32):
    """Custom type a200mgPSTNMediaDataTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("typeCommon", 0),
          ("typeMinFee", 1),
          ("typeMaxSecurity", 2),
          ("typeMaxThruput", 4),
          ("typeMinDelay", 8))
    )


_A200mgPSTNMediaDataTos_Type.__name__ = "Integer32"
_A200mgPSTNMediaDataTos_Object = MibTableColumn
a200mgPSTNMediaDataTos = _A200mgPSTNMediaDataTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 43),
    _A200mgPSTNMediaDataTos_Type()
)
a200mgPSTNMediaDataTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgPSTNMediaDataTos.setStatus("current")


class _A200mgISDNMediaVoiceTos_Type(Integer32):
    """Custom type a200mgISDNMediaVoiceTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("typeCommon", 0),
          ("typeMinFee", 1),
          ("typeMaxSecurity", 2),
          ("typeMaxThruput", 4),
          ("typeMinDelay", 8))
    )


_A200mgISDNMediaVoiceTos_Type.__name__ = "Integer32"
_A200mgISDNMediaVoiceTos_Object = MibTableColumn
a200mgISDNMediaVoiceTos = _A200mgISDNMediaVoiceTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 44),
    _A200mgISDNMediaVoiceTos_Type()
)
a200mgISDNMediaVoiceTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgISDNMediaVoiceTos.setStatus("current")


class _A200mgISDNMediaFaxTos_Type(Integer32):
    """Custom type a200mgISDNMediaFaxTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("typeCommon", 0),
          ("typeMinFee", 1),
          ("typeMaxSecurity", 2),
          ("typeMaxThruput", 4),
          ("typeMinDelay", 8))
    )


_A200mgISDNMediaFaxTos_Type.__name__ = "Integer32"
_A200mgISDNMediaFaxTos_Object = MibTableColumn
a200mgISDNMediaFaxTos = _A200mgISDNMediaFaxTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 45),
    _A200mgISDNMediaFaxTos_Type()
)
a200mgISDNMediaFaxTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgISDNMediaFaxTos.setStatus("current")


class _A200mgISDNMediaModemTos_Type(Integer32):
    """Custom type a200mgISDNMediaModemTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("typeCommon", 0),
          ("typeMinFee", 1),
          ("typeMaxSecurity", 2),
          ("typeMaxThruput", 4),
          ("typeMinDelay", 8))
    )


_A200mgISDNMediaModemTos_Type.__name__ = "Integer32"
_A200mgISDNMediaModemTos_Object = MibTableColumn
a200mgISDNMediaModemTos = _A200mgISDNMediaModemTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 46),
    _A200mgISDNMediaModemTos_Type()
)
a200mgISDNMediaModemTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgISDNMediaModemTos.setStatus("current")


class _A200mgISDNMediaDataTos_Type(Integer32):
    """Custom type a200mgISDNMediaDataTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("typeCommon", 0),
          ("typeMinFee", 1),
          ("typeMaxSecurity", 2),
          ("typeMaxThruput", 4),
          ("typeMinDelay", 8))
    )


_A200mgISDNMediaDataTos_Type.__name__ = "Integer32"
_A200mgISDNMediaDataTos_Object = MibTableColumn
a200mgISDNMediaDataTos = _A200mgISDNMediaDataTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 47),
    _A200mgISDNMediaDataTos_Type()
)
a200mgISDNMediaDataTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgISDNMediaDataTos.setStatus("current")


class _A200ringprofile_Type(Integer32):
    """Custom type a200ringprofile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A200ringprofile_Type.__name__ = "Integer32"
_A200ringprofile_Object = MibTableColumn
a200ringprofile = _A200ringprofile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 48),
    _A200ringprofile_Type()
)
a200ringprofile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200ringprofile.setStatus("current")


class _A200toneprofile_Type(Integer32):
    """Custom type a200toneprofile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A200toneprofile_Type.__name__ = "Integer32"
_A200toneprofile_Object = MibTableColumn
a200toneprofile = _A200toneprofile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 49),
    _A200toneprofile_Type()
)
a200toneprofile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200toneprofile.setStatus("current")


class _A200flashprofile_Type(Integer32):
    """Custom type a200flashprofile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A200flashprofile_Type.__name__ = "Integer32"
_A200flashprofile_Object = MibTableColumn
a200flashprofile = _A200flashprofile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 50),
    _A200flashprofile_Type()
)
a200flashprofile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200flashprofile.setStatus("current")


class _A200chg16kcwidth_Type(Unsigned32):
    """Custom type a200chg16kcwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_A200chg16kcwidth_Type.__name__ = "Unsigned32"
_A200chg16kcwidth_Object = MibTableColumn
a200chg16kcwidth = _A200chg16kcwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 51),
    _A200chg16kcwidth_Type()
)
a200chg16kcwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200chg16kcwidth.setStatus("current")


class _A200chg16kcinterval_Type(Unsigned32):
    """Custom type a200chg16kcinterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_A200chg16kcinterval_Type.__name__ = "Unsigned32"
_A200chg16kcinterval_Object = MibTableColumn
a200chg16kcinterval = _A200chg16kcinterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 52),
    _A200chg16kcinterval_Type()
)
a200chg16kcinterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200chg16kcinterval.setStatus("current")


class _A200charge16kcvol_Type(Integer32):
    """Custom type a200charge16kcvol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_A200charge16kcvol_Type.__name__ = "Integer32"
_A200charge16kcvol_Object = MibTableColumn
a200charge16kcvol = _A200charge16kcvol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 53),
    _A200charge16kcvol_Type()
)
a200charge16kcvol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200charge16kcvol.setStatus("current")


class _A200kcflag_Type(Integer32):
    """Custom type a200kcflag based on Integer32"""
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
        *(("power16KC", 0),
          ("power12KC", 1),
          ("nopower16KC", 2),
          ("nopower12KC", 3))
    )


_A200kcflag_Type.__name__ = "Integer32"
_A200kcflag_Object = MibTableColumn
a200kcflag = _A200kcflag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 54),
    _A200kcflag_Type()
)
a200kcflag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200kcflag.setStatus("current")


class _A200ExternalSelfswitchEnable_Type(Integer32):
    """Custom type a200ExternalSelfswitchEnable based on Integer32"""
    defaultValue = 2

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


_A200ExternalSelfswitchEnable_Type.__name__ = "Integer32"
_A200ExternalSelfswitchEnable_Object = MibTableColumn
a200ExternalSelfswitchEnable = _A200ExternalSelfswitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 55),
    _A200ExternalSelfswitchEnable_Type()
)
a200ExternalSelfswitchEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200ExternalSelfswitchEnable.setStatus("current")


class _ZxAnIpsUsage_Type(Integer32):
    """Custom type zxAnIpsUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnIpsUsage_Type.__name__ = "Integer32"
_ZxAnIpsUsage_Object = MibTableColumn
zxAnIpsUsage = _ZxAnIpsUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 56),
    _ZxAnIpsUsage_Type()
)
zxAnIpsUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIpsUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIpsUsage.setUnits("percent")


class _A200MgCallEscapeMode_Type(Integer32):
    """Custom type a200MgCallEscapeMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pri", 2),
          ("fxo", 3))
    )


_A200MgCallEscapeMode_Type.__name__ = "Integer32"
_A200MgCallEscapeMode_Object = MibTableColumn
a200MgCallEscapeMode = _A200MgCallEscapeMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1, 1, 57),
    _A200MgCallEscapeMode_Type()
)
a200MgCallEscapeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgCallEscapeMode.setStatus("current")
_A200mgccfgTable_Object = MibTable
a200mgccfgTable = _A200mgccfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 2)
)
if mibBuilder.loadTexts:
    a200mgccfgTable.setStatus("current")
_A200mgccfgEntry_Object = MibTableRow
a200mgccfgEntry = _A200mgccfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 2, 1)
)
a200mgccfgEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200mgcmgcid"),
)
if mibBuilder.loadTexts:
    a200mgccfgEntry.setStatus("current")
_A200mgcmgcid_Type = Integer32
_A200mgcmgcid_Object = MibTableColumn
a200mgcmgcid = _A200mgcmgcid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 2, 1, 1),
    _A200mgcmgcid_Type()
)
a200mgcmgcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200mgcmgcid.setStatus("current")


class _A200mgctypeid_Type(Integer32):
    """Custom type a200mgctypeid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A200mgctypeid_Type.__name__ = "Integer32"
_A200mgctypeid_Object = MibTableColumn
a200mgctypeid = _A200mgctypeid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 2, 1, 2),
    _A200mgctypeid_Type()
)
a200mgctypeid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgctypeid.setStatus("current")
_A200mgcip_Type = IpAddress
_A200mgcip_Object = MibTableColumn
a200mgcip = _A200mgcip_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 2, 1, 3),
    _A200mgcip_Type()
)
a200mgcip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgcip.setStatus("current")
_A200mgcport_Type = Integer32
_A200mgcport_Object = MibTableColumn
a200mgcport = _A200mgcport_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 2, 1, 4),
    _A200mgcport_Type()
)
a200mgcport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgcport.setStatus("current")


class _A200mgcdomain_Type(DisplayString):
    """Custom type a200mgcdomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_A200mgcdomain_Type.__name__ = "DisplayString"
_A200mgcdomain_Object = MibTableColumn
a200mgcdomain = _A200mgcdomain_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 2, 1, 5),
    _A200mgcdomain_Type()
)
a200mgcdomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgcdomain.setStatus("current")


class _A200mgcinfo_Type(Integer32):
    """Custom type a200mgcinfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A200mgcinfo_Type.__name__ = "Integer32"
_A200mgcinfo_Object = MibTableColumn
a200mgcinfo = _A200mgcinfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 2, 1, 6),
    _A200mgcinfo_Type()
)
a200mgcinfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgcinfo.setStatus("current")


class _A200mgcMD5Info_Type(Integer32):
    """Custom type a200mgcMD5Info based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_A200mgcMD5Info_Type.__name__ = "Integer32"
_A200mgcMD5Info_Object = MibTableColumn
a200mgcMD5Info = _A200mgcMD5Info_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 2, 1, 7),
    _A200mgcMD5Info_Type()
)
a200mgcMD5Info.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgcMD5Info.setStatus("current")
_A200mgcRowStatus_Type = RowStatus
_A200mgcRowStatus_Object = MibTableColumn
a200mgcRowStatus = _A200mgcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 2, 1, 8),
    _A200mgcRowStatus_Type()
)
a200mgcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mgcRowStatus.setStatus("current")
_A200MgcTypeTable_Object = MibTable
a200MgcTypeTable = _A200MgcTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3)
)
if mibBuilder.loadTexts:
    a200MgcTypeTable.setStatus("current")
_A200MgcTypeEntry_Object = MibTableRow
a200MgcTypeEntry = _A200MgcTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1)
)
a200MgcTypeEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200MgcTypeId"),
)
if mibBuilder.loadTexts:
    a200MgcTypeEntry.setStatus("current")


class _A200MgcTypeId_Type(Integer32):
    """Custom type a200MgcTypeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A200MgcTypeId_Type.__name__ = "Integer32"
_A200MgcTypeId_Object = MibTableColumn
a200MgcTypeId = _A200MgcTypeId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 1),
    _A200MgcTypeId_Type()
)
a200MgcTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200MgcTypeId.setStatus("current")


class _A200MgcTypeDesc_Type(DisplayString):
    """Custom type a200MgcTypeDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_A200MgcTypeDesc_Type.__name__ = "DisplayString"
_A200MgcTypeDesc_Object = MibTableColumn
a200MgcTypeDesc = _A200MgcTypeDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 2),
    _A200MgcTypeDesc_Type()
)
a200MgcTypeDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeDesc.setStatus("current")


class _A200MgcTypeMaxTransPkg_Type(Integer32):
    """Custom type a200MgcTypeMaxTransPkg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_A200MgcTypeMaxTransPkg_Type.__name__ = "Integer32"
_A200MgcTypeMaxTransPkg_Object = MibTableColumn
a200MgcTypeMaxTransPkg = _A200MgcTypeMaxTransPkg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 3),
    _A200MgcTypeMaxTransPkg_Type()
)
a200MgcTypeMaxTransPkg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeMaxTransPkg.setStatus("current")


class _A200MgcTypeReasonQuote_Type(Integer32):
    """Custom type a200MgcTypeReasonQuote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("typeEnable", 1),
          ("typeDisable", 2))
    )


_A200MgcTypeReasonQuote_Type.__name__ = "Integer32"
_A200MgcTypeReasonQuote_Object = MibTableColumn
a200MgcTypeReasonQuote = _A200MgcTypeReasonQuote_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 4),
    _A200MgcTypeReasonQuote_Type()
)
a200MgcTypeReasonQuote.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeReasonQuote.setStatus("current")


class _A200MgcTypeQueryStatus_Type(Integer32):
    """Custom type a200MgcTypeQueryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("typeDisable", 0),
          ("typeEnable", 1))
    )


_A200MgcTypeQueryStatus_Type.__name__ = "Integer32"
_A200MgcTypeQueryStatus_Object = MibTableColumn
a200MgcTypeQueryStatus = _A200MgcTypeQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 5),
    _A200MgcTypeQueryStatus_Type()
)
a200MgcTypeQueryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeQueryStatus.setStatus("current")


class _A200MgcTypeHeartBeat_Type(Integer32):
    """Custom type a200MgcTypeHeartBeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A200MgcTypeHeartBeat_Type.__name__ = "Integer32"
_A200MgcTypeHeartBeat_Object = MibTableColumn
a200MgcTypeHeartBeat = _A200MgcTypeHeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 6),
    _A200MgcTypeHeartBeat_Type()
)
a200MgcTypeHeartBeat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeHeartBeat.setStatus("current")


class _A200MgcTypeDmLong_Type(Integer32):
    """Custom type a200MgcTypeDmLong based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_A200MgcTypeDmLong_Type.__name__ = "Integer32"
_A200MgcTypeDmLong_Object = MibTableColumn
a200MgcTypeDmLong = _A200MgcTypeDmLong_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 7),
    _A200MgcTypeDmLong_Type()
)
a200MgcTypeDmLong.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeDmLong.setStatus("current")


class _A200MgcTypeDmShort_Type(Integer32):
    """Custom type a200MgcTypeDmShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_A200MgcTypeDmShort_Type.__name__ = "Integer32"
_A200MgcTypeDmShort_Object = MibTableColumn
a200MgcTypeDmShort = _A200MgcTypeDmShort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 8),
    _A200MgcTypeDmShort_Type()
)
a200MgcTypeDmShort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeDmShort.setStatus("current")


class _A200MgcTypeDmStart_Type(Integer32):
    """Custom type a200MgcTypeDmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_A200MgcTypeDmStart_Type.__name__ = "Integer32"
_A200MgcTypeDmStart_Object = MibTableColumn
a200MgcTypeDmStart = _A200MgcTypeDmStart_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 9),
    _A200MgcTypeDmStart_Type()
)
a200MgcTypeDmStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeDmStart.setStatus("current")


class _A200MgcTypeWithTime_Type(Integer32):
    """Custom type a200MgcTypeWithTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("notinclude", 2))
    )


_A200MgcTypeWithTime_Type.__name__ = "Integer32"
_A200MgcTypeWithTime_Object = MibTableColumn
a200MgcTypeWithTime = _A200MgcTypeWithTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 10),
    _A200MgcTypeWithTime_Type()
)
a200MgcTypeWithTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeWithTime.setStatus("current")


class _A200MgcTypeWithDelay_Type(Integer32):
    """Custom type a200MgcTypeWithDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A200MgcTypeWithDelay_Type.__name__ = "Integer32"
_A200MgcTypeWithDelay_Object = MibTableColumn
a200MgcTypeWithDelay = _A200MgcTypeWithDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 11),
    _A200MgcTypeWithDelay_Type()
)
a200MgcTypeWithDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeWithDelay.setStatus("current")


class _A200MgcTypeProfileName_Type(DisplayString):
    """Custom type a200MgcTypeProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_A200MgcTypeProfileName_Type.__name__ = "DisplayString"
_A200MgcTypeProfileName_Object = MibTableColumn
a200MgcTypeProfileName = _A200MgcTypeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 12),
    _A200MgcTypeProfileName_Type()
)
a200MgcTypeProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeProfileName.setStatus("current")


class _A200MgcTypeUserOut_Type(Integer32):
    """Custom type a200MgcTypeUserOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 915),
    )


_A200MgcTypeUserOut_Type.__name__ = "Integer32"
_A200MgcTypeUserOut_Object = MibTableColumn
a200MgcTypeUserOut = _A200MgcTypeUserOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 13),
    _A200MgcTypeUserOut_Type()
)
a200MgcTypeUserOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeUserOut.setStatus("current")


class _A200MgcTypeAgOut_Type(Integer32):
    """Custom type a200MgcTypeAgOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 915),
    )


_A200MgcTypeAgOut_Type.__name__ = "Integer32"
_A200MgcTypeAgOut_Object = MibTableColumn
a200MgcTypeAgOut = _A200MgcTypeAgOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 14),
    _A200MgcTypeAgOut_Type()
)
a200MgcTypeAgOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeAgOut.setStatus("current")
_A200MgcTypeHeartId_Type = Unsigned32
_A200MgcTypeHeartId_Object = MibTableColumn
a200MgcTypeHeartId = _A200MgcTypeHeartId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 15),
    _A200MgcTypeHeartId_Type()
)
a200MgcTypeHeartId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeHeartId.setStatus("current")


class _A200MgcTypeAgRegOldMT_Type(Integer32):
    """Custom type a200MgcTypeAgRegOldMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_A200MgcTypeAgRegOldMT_Type.__name__ = "Integer32"
_A200MgcTypeAgRegOldMT_Object = MibTableColumn
a200MgcTypeAgRegOldMT = _A200MgcTypeAgRegOldMT_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 16),
    _A200MgcTypeAgRegOldMT_Type()
)
a200MgcTypeAgRegOldMT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeAgRegOldMT.setStatus("current")


class _A200MgcTypeCanclerror_Type(Integer32):
    """Custom type a200MgcTypeCanclerror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_A200MgcTypeCanclerror_Type.__name__ = "Integer32"
_A200MgcTypeCanclerror_Object = MibTableColumn
a200MgcTypeCanclerror = _A200MgcTypeCanclerror_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 17),
    _A200MgcTypeCanclerror_Type()
)
a200MgcTypeCanclerror.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeCanclerror.setStatus("current")
_A200MgcTypeRowStatus_Type = RowStatus
_A200MgcTypeRowStatus_Object = MibTableColumn
a200MgcTypeRowStatus = _A200MgcTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 3, 1, 18),
    _A200MgcTypeRowStatus_Type()
)
a200MgcTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200MgcTypeRowStatus.setStatus("current")
_A200MedNatTable_Object = MibTable
a200MedNatTable = _A200MedNatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4)
)
if mibBuilder.loadTexts:
    a200MedNatTable.setStatus("current")
_A200MedNatEntry_Object = MibTableRow
a200MedNatEntry = _A200MedNatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1)
)
a200MedNatEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200mednatIpsRack"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200mednatIpsShelf"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200mednatIpsSlot"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200mednatSubCard"),
)
if mibBuilder.loadTexts:
    a200MedNatEntry.setStatus("current")
_A200mednatIpsRack_Type = Integer32
_A200mednatIpsRack_Object = MibTableColumn
a200mednatIpsRack = _A200mednatIpsRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 1),
    _A200mednatIpsRack_Type()
)
a200mednatIpsRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200mednatIpsRack.setStatus("current")
_A200mednatIpsShelf_Type = Integer32
_A200mednatIpsShelf_Object = MibTableColumn
a200mednatIpsShelf = _A200mednatIpsShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 2),
    _A200mednatIpsShelf_Type()
)
a200mednatIpsShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200mednatIpsShelf.setStatus("current")
_A200mednatIpsSlot_Type = Integer32
_A200mednatIpsSlot_Object = MibTableColumn
a200mednatIpsSlot = _A200mednatIpsSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 3),
    _A200mednatIpsSlot_Type()
)
a200mednatIpsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200mednatIpsSlot.setStatus("current")
_A200mednatSubCard_Type = Integer32
_A200mednatSubCard_Object = MibTableColumn
a200mednatSubCard = _A200mednatSubCard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 4),
    _A200mednatSubCard_Type()
)
a200mednatSubCard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200mednatSubCard.setStatus("current")
_A200mednatNicRack_Type = Integer32
_A200mednatNicRack_Object = MibTableColumn
a200mednatNicRack = _A200mednatNicRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 5),
    _A200mednatNicRack_Type()
)
a200mednatNicRack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mednatNicRack.setStatus("current")
_A200mednatNicShelf_Type = Integer32
_A200mednatNicShelf_Object = MibTableColumn
a200mednatNicShelf = _A200mednatNicShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 6),
    _A200mednatNicShelf_Type()
)
a200mednatNicShelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mednatNicShelf.setStatus("current")
_A200mednatNicSlot_Type = Integer32
_A200mednatNicSlot_Object = MibTableColumn
a200mednatNicSlot = _A200mednatNicSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 7),
    _A200mednatNicSlot_Type()
)
a200mednatNicSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mednatNicSlot.setStatus("current")
_A200mednatInPhyPort_Type = Integer32
_A200mednatInPhyPort_Object = MibTableColumn
a200mednatInPhyPort = _A200mednatInPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 8),
    _A200mednatInPhyPort_Type()
)
a200mednatInPhyPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mednatInPhyPort.setStatus("current")
_A200mednatExPhyPort_Type = Integer32
_A200mednatExPhyPort_Object = MibTableColumn
a200mednatExPhyPort = _A200mednatExPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 9),
    _A200mednatExPhyPort_Type()
)
a200mednatExPhyPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mednatExPhyPort.setStatus("current")
_A200mednatExIp_Type = IpAddress
_A200mednatExIp_Object = MibTableColumn
a200mednatExIp = _A200mednatExIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 10),
    _A200mednatExIp_Type()
)
a200mednatExIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mednatExIp.setStatus("current")
_A200mednatUdpPort_Type = Integer32
_A200mednatUdpPort_Object = MibTableColumn
a200mednatUdpPort = _A200mednatUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 11),
    _A200mednatUdpPort_Type()
)
a200mednatUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mednatUdpPort.setStatus("current")
_A200mednatRowStatus_Type = RowStatus
_A200mednatRowStatus_Object = MibTableColumn
a200mednatRowStatus = _A200mednatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 12),
    _A200mednatRowStatus_Type()
)
a200mednatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200mednatRowStatus.setStatus("current")
_A200natCtrlId_Type = Integer32
_A200natCtrlId_Object = MibTableColumn
a200natCtrlId = _A200natCtrlId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 4, 1, 13),
    _A200natCtrlId_Type()
)
a200natCtrlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a200natCtrlId.setStatus("current")
_A200QovsTable_Object = MibTable
a200QovsTable = _A200QovsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 5)
)
if mibBuilder.loadTexts:
    a200QovsTable.setStatus("current")
_A200QovsEntry_Object = MibTableRow
a200QovsEntry = _A200QovsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 5, 1)
)
a200QovsEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200QovsId"),
)
if mibBuilder.loadTexts:
    a200QovsEntry.setStatus("current")


class _A200QovsId_Type(Integer32):
    """Custom type a200QovsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_A200QovsId_Type.__name__ = "Integer32"
_A200QovsId_Object = MibTableColumn
a200QovsId = _A200QovsId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 5, 1, 1),
    _A200QovsId_Type()
)
a200QovsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200QovsId.setStatus("current")


class _A200QovsLoss_Type(Integer32):
    """Custom type a200QovsLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_A200QovsLoss_Type.__name__ = "Integer32"
_A200QovsLoss_Object = MibTableColumn
a200QovsLoss = _A200QovsLoss_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 5, 1, 2),
    _A200QovsLoss_Type()
)
a200QovsLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200QovsLoss.setStatus("current")


class _A200QovsDelay_Type(Integer32):
    """Custom type a200QovsDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_A200QovsDelay_Type.__name__ = "Integer32"
_A200QovsDelay_Object = MibTableColumn
a200QovsDelay = _A200QovsDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 5, 1, 3),
    _A200QovsDelay_Type()
)
a200QovsDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200QovsDelay.setStatus("current")


class _A200QovsJitter_Type(Integer32):
    """Custom type a200QovsJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_A200QovsJitter_Type.__name__ = "Integer32"
_A200QovsJitter_Object = MibTableColumn
a200QovsJitter = _A200QovsJitter_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 5, 1, 4),
    _A200QovsJitter_Type()
)
a200QovsJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200QovsJitter.setStatus("current")
_A200QovsRowStatus_Type = RowStatus
_A200QovsRowStatus_Object = MibTableColumn
a200QovsRowStatus = _A200QovsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 5, 1, 5),
    _A200QovsRowStatus_Type()
)
a200QovsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200QovsRowStatus.setStatus("current")
_A200MiscTable_Object = MibTable
a200MiscTable = _A200MiscTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7)
)
if mibBuilder.loadTexts:
    a200MiscTable.setStatus("current")
_A200MiscEntry_Object = MibTableRow
a200MiscEntry = _A200MiscEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1)
)
a200MiscEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200MiscIndex"),
)
if mibBuilder.loadTexts:
    a200MiscEntry.setStatus("current")


class _A200MiscIndex_Type(Integer32):
    """Custom type a200MiscIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_A200MiscIndex_Type.__name__ = "Integer32"
_A200MiscIndex_Object = MibTableColumn
a200MiscIndex = _A200MiscIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 1),
    _A200MiscIndex_Type()
)
a200MiscIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200MiscIndex.setStatus("current")


class _A200MiscFlashDelay_Type(Integer32):
    """Custom type a200MiscFlashDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 50),
    )


_A200MiscFlashDelay_Type.__name__ = "Integer32"
_A200MiscFlashDelay_Object = MibTableColumn
a200MiscFlashDelay = _A200MiscFlashDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 2),
    _A200MiscFlashDelay_Type()
)
a200MiscFlashDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscFlashDelay.setStatus("current")


class _A200MiscCalledPartyReanwer_Type(Integer32):
    """Custom type a200MiscCalledPartyReanwer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_A200MiscCalledPartyReanwer_Type.__name__ = "Integer32"
_A200MiscCalledPartyReanwer_Object = MibTableColumn
a200MiscCalledPartyReanwer = _A200MiscCalledPartyReanwer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 3),
    _A200MiscCalledPartyReanwer_Type()
)
a200MiscCalledPartyReanwer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscCalledPartyReanwer.setStatus("current")


class _A200MiscH248BusyStatus_Type(Integer32):
    """Custom type a200MiscH248BusyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_A200MiscH248BusyStatus_Type.__name__ = "Integer32"
_A200MiscH248BusyStatus_Object = MibTableColumn
a200MiscH248BusyStatus = _A200MiscH248BusyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 4),
    _A200MiscH248BusyStatus_Type()
)
a200MiscH248BusyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscH248BusyStatus.setStatus("current")


class _A200MiscHowlTone_Type(Integer32):
    """Custom type a200MiscHowlTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_A200MiscHowlTone_Type.__name__ = "Integer32"
_A200MiscHowlTone_Object = MibTableColumn
a200MiscHowlTone = _A200MiscHowlTone_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 5),
    _A200MiscHowlTone_Type()
)
a200MiscHowlTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscHowlTone.setStatus("current")


class _A200MiscH248Short_Type(Integer32):
    """Custom type a200MiscH248Short based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 50),
    )


_A200MiscH248Short_Type.__name__ = "Integer32"
_A200MiscH248Short_Object = MibTableColumn
a200MiscH248Short = _A200MiscH248Short_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 6),
    _A200MiscH248Short_Type()
)
a200MiscH248Short.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscH248Short.setStatus("current")


class _A200MiscH248Long_Type(Integer32):
    """Custom type a200MiscH248Long based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_A200MiscH248Long_Type.__name__ = "Integer32"
_A200MiscH248Long_Object = MibTableColumn
a200MiscH248Long = _A200MiscH248Long_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 7),
    _A200MiscH248Long_Type()
)
a200MiscH248Long.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscH248Long.setStatus("current")


class _A200MiscRTPtimer_Type(Integer32):
    """Custom type a200MiscRTPtimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 50),
    )


_A200MiscRTPtimer_Type.__name__ = "Integer32"
_A200MiscRTPtimer_Object = MibTableColumn
a200MiscRTPtimer = _A200MiscRTPtimer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 8),
    _A200MiscRTPtimer_Type()
)
a200MiscRTPtimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscRTPtimer.setStatus("current")


class _A200MiscH248RingPattern_Type(Integer32):
    """Custom type a200MiscH248RingPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms", 1),
          ("tenms", 2),
          ("hundredms", 3))
    )


_A200MiscH248RingPattern_Type.__name__ = "Integer32"
_A200MiscH248RingPattern_Object = MibTableColumn
a200MiscH248RingPattern = _A200MiscH248RingPattern_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 9),
    _A200MiscH248RingPattern_Type()
)
a200MiscH248RingPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscH248RingPattern.setStatus("current")


class _A200MiscCallAlarm_Type(Integer32):
    """Custom type a200MiscCallAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_A200MiscCallAlarm_Type.__name__ = "Integer32"
_A200MiscCallAlarm_Object = MibTableColumn
a200MiscCallAlarm = _A200MiscCallAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 10),
    _A200MiscCallAlarm_Type()
)
a200MiscCallAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscCallAlarm.setStatus("current")


class _A200MiscInterCallAlarm_Type(Integer32):
    """Custom type a200MiscInterCallAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_A200MiscInterCallAlarm_Type.__name__ = "Integer32"
_A200MiscInterCallAlarm_Object = MibTableColumn
a200MiscInterCallAlarm = _A200MiscInterCallAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 11),
    _A200MiscInterCallAlarm_Type()
)
a200MiscInterCallAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscInterCallAlarm.setStatus("current")


class _A200MiscFreshTnet_Type(Integer32):
    """Custom type a200MiscFreshTnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_A200MiscFreshTnet_Type.__name__ = "Integer32"
_A200MiscFreshTnet_Object = MibTableColumn
a200MiscFreshTnet = _A200MiscFreshTnet_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 12),
    _A200MiscFreshTnet_Type()
)
a200MiscFreshTnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscFreshTnet.setStatus("current")


class _A200MiscCheckContext_Type(Integer32):
    """Custom type a200MiscCheckContext based on Integer32"""
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


_A200MiscCheckContext_Type.__name__ = "Integer32"
_A200MiscCheckContext_Object = MibTableColumn
a200MiscCheckContext = _A200MiscCheckContext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 13),
    _A200MiscCheckContext_Type()
)
a200MiscCheckContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscCheckContext.setStatus("current")


class _A200MiscUpPort_Type(Integer32):
    """Custom type a200MiscUpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("withTimeStamp", 0),
          ("noTimeStamp", 1))
    )


_A200MiscUpPort_Type.__name__ = "Integer32"
_A200MiscUpPort_Object = MibTableColumn
a200MiscUpPort = _A200MiscUpPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 14),
    _A200MiscUpPort_Type()
)
a200MiscUpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscUpPort.setStatus("current")


class _A200MiscResReportPeriod_Type(Integer32):
    """Custom type a200MiscResReportPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A200MiscResReportPeriod_Type.__name__ = "Integer32"
_A200MiscResReportPeriod_Object = MibTableColumn
a200MiscResReportPeriod = _A200MiscResReportPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 15),
    _A200MiscResReportPeriod_Type()
)
a200MiscResReportPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscResReportPeriod.setStatus("current")


class _A200MiscAgMustDetOvrLd_Type(Integer32):
    """Custom type a200MiscAgMustDetOvrLd based on Integer32"""
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


_A200MiscAgMustDetOvrLd_Type.__name__ = "Integer32"
_A200MiscAgMustDetOvrLd_Object = MibTableColumn
a200MiscAgMustDetOvrLd = _A200MiscAgMustDetOvrLd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 16),
    _A200MiscAgMustDetOvrLd_Type()
)
a200MiscAgMustDetOvrLd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscAgMustDetOvrLd.setStatus("current")


class _A200MiscErrReplyInformSSEn_Type(Integer32):
    """Custom type a200MiscErrReplyInformSSEn based on Integer32"""
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


_A200MiscErrReplyInformSSEn_Type.__name__ = "Integer32"
_A200MiscErrReplyInformSSEn_Object = MibTableColumn
a200MiscErrReplyInformSSEn = _A200MiscErrReplyInformSSEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 17),
    _A200MiscErrReplyInformSSEn_Type()
)
a200MiscErrReplyInformSSEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscErrReplyInformSSEn.setStatus("current")


class _A200MiscCookieEchoFormat_Type(Integer32):
    """Custom type a200MiscCookieEchoFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("formZTE", 0),
          ("formStandard", 1))
    )


_A200MiscCookieEchoFormat_Type.__name__ = "Integer32"
_A200MiscCookieEchoFormat_Object = MibTableColumn
a200MiscCookieEchoFormat = _A200MiscCookieEchoFormat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 18),
    _A200MiscCookieEchoFormat_Type()
)
a200MiscCookieEchoFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscCookieEchoFormat.setStatus("current")


class _A200MiscCheckSumFormat_Type(Integer32):
    """Custom type a200MiscCheckSumFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("formADLER32", 0),
          ("formCRC32", 1))
    )


_A200MiscCheckSumFormat_Type.__name__ = "Integer32"
_A200MiscCheckSumFormat_Object = MibTableColumn
a200MiscCheckSumFormat = _A200MiscCheckSumFormat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 19),
    _A200MiscCheckSumFormat_Type()
)
a200MiscCheckSumFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscCheckSumFormat.setStatus("current")


class _A200MiscIuaIsdnHwFormat_Type(Integer32):
    """Custom type a200MiscIuaIsdnHwFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("formDisable", 0),
          ("formEnable", 1))
    )


_A200MiscIuaIsdnHwFormat_Type.__name__ = "Integer32"
_A200MiscIuaIsdnHwFormat_Object = MibTableColumn
a200MiscIuaIsdnHwFormat = _A200MiscIuaIsdnHwFormat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 7, 1, 20),
    _A200MiscIuaIsdnHwFormat_Type()
)
a200MiscIuaIsdnHwFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200MiscIuaIsdnHwFormat.setStatus("current")
_A200DigitMapTable_Object = MibTable
a200DigitMapTable = _A200DigitMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 8)
)
if mibBuilder.loadTexts:
    a200DigitMapTable.setStatus("current")
_A200DigitMapEntry_Object = MibTableRow
a200DigitMapEntry = _A200DigitMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 8, 1)
)
a200DigitMapEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200DigitMapDas"),
)
if mibBuilder.loadTexts:
    a200DigitMapEntry.setStatus("current")


class _A200DigitMapDas_Type(Integer32):
    """Custom type a200DigitMapDas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A200DigitMapDas_Type.__name__ = "Integer32"
_A200DigitMapDas_Object = MibTableColumn
a200DigitMapDas = _A200DigitMapDas_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 8, 1, 1),
    _A200DigitMapDas_Type()
)
a200DigitMapDas.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200DigitMapDas.setStatus("current")


class _A200DigitMapMgid_Type(Integer32):
    """Custom type a200DigitMapMgid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_A200DigitMapMgid_Type.__name__ = "Integer32"
_A200DigitMapMgid_Object = MibTableColumn
a200DigitMapMgid = _A200DigitMapMgid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 8, 1, 2),
    _A200DigitMapMgid_Type()
)
a200DigitMapMgid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200DigitMapMgid.setStatus("current")


class _A200DigitMapSrvType_Type(Integer32):
    """Custom type a200DigitMapSrvType based on Integer32"""
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
        *(("h248", 0),
          ("selfchange", 1),
          ("sip", 2),
          ("urgencymap", 3),
          ("callEscape", 4))
    )


_A200DigitMapSrvType_Type.__name__ = "Integer32"
_A200DigitMapSrvType_Object = MibTableColumn
a200DigitMapSrvType = _A200DigitMapSrvType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 8, 1, 3),
    _A200DigitMapSrvType_Type()
)
a200DigitMapSrvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200DigitMapSrvType.setStatus("current")


class _A200DigitMapDgtName_Type(DisplayString):
    """Custom type a200DigitMapDgtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_A200DigitMapDgtName_Type.__name__ = "DisplayString"
_A200DigitMapDgtName_Object = MibTableColumn
a200DigitMapDgtName = _A200DigitMapDgtName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 8, 1, 4),
    _A200DigitMapDgtName_Type()
)
a200DigitMapDgtName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200DigitMapDgtName.setStatus("current")


class _A200DigitMapDgtMap_Type(DisplayString):
    """Custom type a200DigitMapDgtMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 250),
    )


_A200DigitMapDgtMap_Type.__name__ = "DisplayString"
_A200DigitMapDgtMap_Object = MibTableColumn
a200DigitMapDgtMap = _A200DigitMapDgtMap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 8, 1, 5),
    _A200DigitMapDgtMap_Type()
)
a200DigitMapDgtMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200DigitMapDgtMap.setStatus("current")
_A200DigitMapRowStatus_Type = RowStatus
_A200DigitMapRowStatus_Object = MibTableColumn
a200DigitMapRowStatus = _A200DigitMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 8, 1, 6),
    _A200DigitMapRowStatus_Type()
)
a200DigitMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200DigitMapRowStatus.setStatus("current")
_A200VoipRouteTable_Object = MibTable
a200VoipRouteTable = _A200VoipRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 10)
)
if mibBuilder.loadTexts:
    a200VoipRouteTable.setStatus("current")
_A200VoipRouteEntry_Object = MibTableRow
a200VoipRouteEntry = _A200VoipRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 10, 1)
)
a200VoipRouteEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200VoipRouteMgId"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200VoipRouteType"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200VoipRouteDestIp"),
)
if mibBuilder.loadTexts:
    a200VoipRouteEntry.setStatus("current")


class _A200VoipRouteMgId_Type(Integer32):
    """Custom type a200VoipRouteMgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_A200VoipRouteMgId_Type.__name__ = "Integer32"
_A200VoipRouteMgId_Object = MibTableColumn
a200VoipRouteMgId = _A200VoipRouteMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 10, 1, 1),
    _A200VoipRouteMgId_Type()
)
a200VoipRouteMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200VoipRouteMgId.setStatus("current")


class _A200VoipRouteType_Type(Integer32):
    """Custom type a200VoipRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("media", 1),
          ("ctrl", 2))
    )


_A200VoipRouteType_Type.__name__ = "Integer32"
_A200VoipRouteType_Object = MibTableColumn
a200VoipRouteType = _A200VoipRouteType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 10, 1, 2),
    _A200VoipRouteType_Type()
)
a200VoipRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200VoipRouteType.setStatus("current")
_A200VoipRouteDestIp_Type = IpAddress
_A200VoipRouteDestIp_Object = MibTableColumn
a200VoipRouteDestIp = _A200VoipRouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 10, 1, 3),
    _A200VoipRouteDestIp_Type()
)
a200VoipRouteDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200VoipRouteDestIp.setStatus("current")
_A200VoipRouteDestMask_Type = IpAddress
_A200VoipRouteDestMask_Object = MibTableColumn
a200VoipRouteDestMask = _A200VoipRouteDestMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 10, 1, 4),
    _A200VoipRouteDestMask_Type()
)
a200VoipRouteDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200VoipRouteDestMask.setStatus("current")
_A200VoipRouteNexthop_Type = IpAddress
_A200VoipRouteNexthop_Object = MibTableColumn
a200VoipRouteNexthop = _A200VoipRouteNexthop_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 10, 1, 5),
    _A200VoipRouteNexthop_Type()
)
a200VoipRouteNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200VoipRouteNexthop.setStatus("current")
_A200VoipRouteNexthopMac_Type = MacAddress
_A200VoipRouteNexthopMac_Object = MibTableColumn
a200VoipRouteNexthopMac = _A200VoipRouteNexthopMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 10, 1, 6),
    _A200VoipRouteNexthopMac_Type()
)
a200VoipRouteNexthopMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200VoipRouteNexthopMac.setStatus("current")


class _A200VoipRouteArpTime_Type(Integer32):
    """Custom type a200VoipRouteArpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 720),
    )


_A200VoipRouteArpTime_Type.__name__ = "Integer32"
_A200VoipRouteArpTime_Object = MibTableColumn
a200VoipRouteArpTime = _A200VoipRouteArpTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 10, 1, 7),
    _A200VoipRouteArpTime_Type()
)
a200VoipRouteArpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200VoipRouteArpTime.setStatus("current")
_A200VoipRouteRowStatus_Type = RowStatus
_A200VoipRouteRowStatus_Object = MibTableColumn
a200VoipRouteRowStatus = _A200VoipRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 10, 1, 20),
    _A200VoipRouteRowStatus_Type()
)
a200VoipRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200VoipRouteRowStatus.setStatus("current")
_A200CtlPortTable_Object = MibTable
a200CtlPortTable = _A200CtlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 11)
)
if mibBuilder.loadTexts:
    a200CtlPortTable.setStatus("current")
_A200CtlPortEntry_Object = MibTableRow
a200CtlPortEntry = _A200CtlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 11, 1)
)
a200CtlPortEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200CtlPortCtlId"),
)
if mibBuilder.loadTexts:
    a200CtlPortEntry.setStatus("current")


class _A200CtlPortCtlId_Type(Integer32):
    """Custom type a200CtlPortCtlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_A200CtlPortCtlId_Type.__name__ = "Integer32"
_A200CtlPortCtlId_Object = MibTableColumn
a200CtlPortCtlId = _A200CtlPortCtlId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 11, 1, 1),
    _A200CtlPortCtlId_Type()
)
a200CtlPortCtlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200CtlPortCtlId.setStatus("current")


class _A200CtlPortInfo_Type(Integer32):
    """Custom type a200CtlPortInfo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("tcp", 1))
    )


_A200CtlPortInfo_Type.__name__ = "Integer32"
_A200CtlPortInfo_Object = MibTableColumn
a200CtlPortInfo = _A200CtlPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 11, 1, 2),
    _A200CtlPortInfo_Type()
)
a200CtlPortInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200CtlPortInfo.setStatus("current")


class _A200CtlPortUdpPort_Type(Integer32):
    """Custom type a200CtlPortUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A200CtlPortUdpPort_Type.__name__ = "Integer32"
_A200CtlPortUdpPort_Object = MibTableColumn
a200CtlPortUdpPort = _A200CtlPortUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 11, 1, 3),
    _A200CtlPortUdpPort_Type()
)
a200CtlPortUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200CtlPortUdpPort.setStatus("current")
_A200CtlPortRowStatus_Type = RowStatus
_A200CtlPortRowStatus_Object = MibTableColumn
a200CtlPortRowStatus = _A200CtlPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 11, 1, 4),
    _A200CtlPortRowStatus_Type()
)
a200CtlPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200CtlPortRowStatus.setStatus("current")
_CallOptimizeTable_Object = MibTable
callOptimizeTable = _CallOptimizeTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13)
)
if mibBuilder.loadTexts:
    callOptimizeTable.setStatus("current")
_CallOptimizeEntry_Object = MibTableRow
callOptimizeEntry = _CallOptimizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1)
)
callOptimizeEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "calloptIndex"),
)
if mibBuilder.loadTexts:
    callOptimizeEntry.setStatus("current")


class _CalloptIndex_Type(Integer32):
    """Custom type calloptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CalloptIndex_Type.__name__ = "Integer32"
_CalloptIndex_Object = MibTableColumn
calloptIndex = _CalloptIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 1),
    _CalloptIndex_Type()
)
calloptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calloptIndex.setStatus("current")


class _CalloptOpenMsgAck_Type(Integer32):
    """Custom type calloptOpenMsgAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("notsend", 2))
    )


_CalloptOpenMsgAck_Type.__name__ = "Integer32"
_CalloptOpenMsgAck_Object = MibTableColumn
calloptOpenMsgAck = _CalloptOpenMsgAck_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 2),
    _CalloptOpenMsgAck_Type()
)
calloptOpenMsgAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptOpenMsgAck.setStatus("current")


class _CalloptPlayToneAck_Type(Integer32):
    """Custom type calloptPlayToneAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("notsend", 2))
    )


_CalloptPlayToneAck_Type.__name__ = "Integer32"
_CalloptPlayToneAck_Object = MibTableColumn
calloptPlayToneAck = _CalloptPlayToneAck_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 3),
    _CalloptPlayToneAck_Type()
)
calloptPlayToneAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptPlayToneAck.setStatus("current")


class _CalloptSubPriority_Type(Integer32):
    """Custom type calloptSubPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("higher", 1),
          ("nothigher", 2))
    )


_CalloptSubPriority_Type.__name__ = "Integer32"
_CalloptSubPriority_Object = MibTableColumn
calloptSubPriority = _CalloptSubPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 4),
    _CalloptSubPriority_Type()
)
calloptSubPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptSubPriority.setStatus("current")


class _CalloptNumMax_Type(Integer32):
    """Custom type calloptNumMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CalloptNumMax_Type.__name__ = "Integer32"
_CalloptNumMax_Object = MibTableColumn
calloptNumMax = _CalloptNumMax_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 5),
    _CalloptNumMax_Type()
)
calloptNumMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptNumMax.setStatus("current")


class _CalloptH248MsgAck_Type(Integer32):
    """Custom type calloptH248MsgAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("notsend", 2))
    )


_CalloptH248MsgAck_Type.__name__ = "Integer32"
_CalloptH248MsgAck_Object = MibTableColumn
calloptH248MsgAck = _CalloptH248MsgAck_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 6),
    _CalloptH248MsgAck_Type()
)
calloptH248MsgAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptH248MsgAck.setStatus("current")


class _CalloptH248MsgPn_Type(Integer32):
    """Custom type calloptH248MsgPn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("notsend", 2))
    )


_CalloptH248MsgPn_Type.__name__ = "Integer32"
_CalloptH248MsgPn_Object = MibTableColumn
calloptH248MsgPn = _CalloptH248MsgPn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 7),
    _CalloptH248MsgPn_Type()
)
calloptH248MsgPn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptH248MsgPn.setStatus("current")


class _CalloptH248Statistic_Type(Integer32):
    """Custom type calloptH248Statistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("notsend", 2))
    )


_CalloptH248Statistic_Type.__name__ = "Integer32"
_CalloptH248Statistic_Object = MibTableColumn
calloptH248Statistic = _CalloptH248Statistic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 8),
    _CalloptH248Statistic_Type()
)
calloptH248Statistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptH248Statistic.setStatus("current")


class _CalloptH248HookOffEvent_Type(Integer32):
    """Custom type calloptH248HookOffEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwayssend", 1),
          ("notalways", 2))
    )


_CalloptH248HookOffEvent_Type.__name__ = "Integer32"
_CalloptH248HookOffEvent_Object = MibTableColumn
calloptH248HookOffEvent = _CalloptH248HookOffEvent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 9),
    _CalloptH248HookOffEvent_Type()
)
calloptH248HookOffEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptH248HookOffEvent.setStatus("current")


class _CalloptH248HookOnEvent_Type(Integer32):
    """Custom type calloptH248HookOnEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwayssend", 1),
          ("notalways", 2))
    )


_CalloptH248HookOnEvent_Type.__name__ = "Integer32"
_CalloptH248HookOnEvent_Object = MibTableColumn
calloptH248HookOnEvent = _CalloptH248HookOnEvent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 10),
    _CalloptH248HookOnEvent_Type()
)
calloptH248HookOnEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptH248HookOnEvent.setStatus("current")


class _CalloptServiceAbnormal_Type(Integer32):
    """Custom type calloptServiceAbnormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwayssend", 1),
          ("notalways", 2))
    )


_CalloptServiceAbnormal_Type.__name__ = "Integer32"
_CalloptServiceAbnormal_Object = MibTableColumn
calloptServiceAbnormal = _CalloptServiceAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 11),
    _CalloptServiceAbnormal_Type()
)
calloptServiceAbnormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptServiceAbnormal.setStatus("current")


class _CalloptMgProtocolErr_Type(Integer32):
    """Custom type calloptMgProtocolErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwayssend", 1),
          ("notalways", 2))
    )


_CalloptMgProtocolErr_Type.__name__ = "Integer32"
_CalloptMgProtocolErr_Object = MibTableColumn
calloptMgProtocolErr = _CalloptMgProtocolErr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 12),
    _CalloptMgProtocolErr_Type()
)
calloptMgProtocolErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptMgProtocolErr.setStatus("current")


class _CalloptMgcProtocolErr_Type(Integer32):
    """Custom type calloptMgcProtocolErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwayssend", 1),
          ("notalways", 2))
    )


_CalloptMgcProtocolErr_Type.__name__ = "Integer32"
_CalloptMgcProtocolErr_Object = MibTableColumn
calloptMgcProtocolErr = _CalloptMgcProtocolErr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 13),
    _CalloptMgcProtocolErr_Type()
)
calloptMgcProtocolErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptMgcProtocolErr.setStatus("current")


class _CalloptMgInsideErr_Type(Integer32):
    """Custom type calloptMgInsideErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwayssend", 1),
          ("notalways", 2))
    )


_CalloptMgInsideErr_Type.__name__ = "Integer32"
_CalloptMgInsideErr_Object = MibTableColumn
calloptMgInsideErr = _CalloptMgInsideErr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 14),
    _CalloptMgInsideErr_Type()
)
calloptMgInsideErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptMgInsideErr.setStatus("current")


class _CalloptHookOffLimiteCycle_Type(Integer32):
    """Custom type calloptHookOffLimiteCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_CalloptHookOffLimiteCycle_Type.__name__ = "Integer32"
_CalloptHookOffLimiteCycle_Object = MibTableColumn
calloptHookOffLimiteCycle = _CalloptHookOffLimiteCycle_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 15),
    _CalloptHookOffLimiteCycle_Type()
)
calloptHookOffLimiteCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptHookOffLimiteCycle.setStatus("current")


class _CalloptHookOffLimiteBlock_Type(Integer32):
    """Custom type calloptHookOffLimiteBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_CalloptHookOffLimiteBlock_Type.__name__ = "Integer32"
_CalloptHookOffLimiteBlock_Object = MibTableColumn
calloptHookOffLimiteBlock = _CalloptHookOffLimiteBlock_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 16),
    _CalloptHookOffLimiteBlock_Type()
)
calloptHookOffLimiteBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptHookOffLimiteBlock.setStatus("current")


class _CalloptHookOffLimiteUnblock_Type(Integer32):
    """Custom type calloptHookOffLimiteUnblock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 600),
    )


_CalloptHookOffLimiteUnblock_Type.__name__ = "Integer32"
_CalloptHookOffLimiteUnblock_Object = MibTableColumn
calloptHookOffLimiteUnblock = _CalloptHookOffLimiteUnblock_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 17),
    _CalloptHookOffLimiteUnblock_Type()
)
calloptHookOffLimiteUnblock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptHookOffLimiteUnblock.setStatus("current")


class _CalloptMgcCallWaitTone_Type(Integer32):
    """Custom type calloptMgcCallWaitTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("breakdown", 1),
          ("notbreakdown", 2))
    )


_CalloptMgcCallWaitTone_Type.__name__ = "Integer32"
_CalloptMgcCallWaitTone_Object = MibTableColumn
calloptMgcCallWaitTone = _CalloptMgcCallWaitTone_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 18),
    _CalloptMgcCallWaitTone_Type()
)
calloptMgcCallWaitTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptMgcCallWaitTone.setStatus("current")


class _CalloptToneArea_Type(Integer32):
    """Custom type calloptToneArea based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("mainland", 1),
          ("hongkong", 2),
          ("singapore", 3),
          ("russia", 4),
          ("chile", 5),
          ("dominican", 6),
          ("argentina", 7),
          ("croatia", 8),
          ("turkey", 9),
          ("singapore2", 10),
          ("malaysia", 11),
          ("belgium", 12),
          ("india", 13),
          ("taiwan", 14),
          ("srilanka", 15),
          ("austria", 16),
          ("greece", 17),
          ("nepal", 18),
          ("colombia", 19),
          ("peru", 20),
          ("morocco", 21),
          ("hungary", 22))
    )


_CalloptToneArea_Type.__name__ = "Integer32"
_CalloptToneArea_Object = MibTableColumn
calloptToneArea = _CalloptToneArea_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 19),
    _CalloptToneArea_Type()
)
calloptToneArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptToneArea.setStatus("current")


class _CalloptH248LinkBreakTone_Type(Integer32):
    """Custom type calloptH248LinkBreakTone based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busyTone", 1),
          ("informationTone", 2))
    )


_CalloptH248LinkBreakTone_Type.__name__ = "Integer32"
_CalloptH248LinkBreakTone_Object = MibTableColumn
calloptH248LinkBreakTone = _CalloptH248LinkBreakTone_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 13, 1, 20),
    _CalloptH248LinkBreakTone_Type()
)
calloptH248LinkBreakTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calloptH248LinkBreakTone.setStatus("current")


class _MsagLoadDefaultRingProfile_Type(Integer32):
    """Custom type msagLoadDefaultRingProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MsagLoadDefaultRingProfile_Type.__name__ = "Integer32"
_MsagLoadDefaultRingProfile_Object = MibScalar
msagLoadDefaultRingProfile = _MsagLoadDefaultRingProfile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 14),
    _MsagLoadDefaultRingProfile_Type()
)
msagLoadDefaultRingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msagLoadDefaultRingProfile.setStatus("current")
_ZxAnVoipInterfaceTable_Object = MibTable
zxAnVoipInterfaceTable = _ZxAnVoipInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 15)
)
if mibBuilder.loadTexts:
    zxAnVoipInterfaceTable.setStatus("current")
_ZxAnVoipInterfaceEntry_Object = MibTableRow
zxAnVoipInterfaceEntry = _ZxAnVoipInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 15, 1)
)
zxAnVoipInterfaceEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnMgId"),
)
if mibBuilder.loadTexts:
    zxAnVoipInterfaceEntry.setStatus("current")


class _ZxAnMgId_Type(Integer32):
    """Custom type zxAnMgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxAnMgId_Type.__name__ = "Integer32"
_ZxAnMgId_Object = MibTableColumn
zxAnMgId = _ZxAnMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 15, 1, 1),
    _ZxAnMgId_Type()
)
zxAnMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMgId.setStatus("current")
_ZxAnVoipCtrlIpAddr_Type = IpAddress
_ZxAnVoipCtrlIpAddr_Object = MibTableColumn
zxAnVoipCtrlIpAddr = _ZxAnVoipCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 15, 1, 2),
    _ZxAnVoipCtrlIpAddr_Type()
)
zxAnVoipCtrlIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipCtrlIpAddr.setStatus("current")
_ZxAnVoipCtrlIpMask_Type = IpAddress
_ZxAnVoipCtrlIpMask_Object = MibTableColumn
zxAnVoipCtrlIpMask = _ZxAnVoipCtrlIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 15, 1, 3),
    _ZxAnVoipCtrlIpMask_Type()
)
zxAnVoipCtrlIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipCtrlIpMask.setStatus("current")
_ZxAnVoipMediaIpaddr_Type = IpAddress
_ZxAnVoipMediaIpaddr_Object = MibTableColumn
zxAnVoipMediaIpaddr = _ZxAnVoipMediaIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 15, 1, 4),
    _ZxAnVoipMediaIpaddr_Type()
)
zxAnVoipMediaIpaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipMediaIpaddr.setStatus("current")
_ZxAnVoipMediaIpMask_Type = IpAddress
_ZxAnVoipMediaIpMask_Object = MibTableColumn
zxAnVoipMediaIpMask = _ZxAnVoipMediaIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 15, 1, 5),
    _ZxAnVoipMediaIpMask_Type()
)
zxAnVoipMediaIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipMediaIpMask.setStatus("current")
_ZxAnVoipInterfaceRowStatus_Type = RowStatus
_ZxAnVoipInterfaceRowStatus_Object = MibTableColumn
zxAnVoipInterfaceRowStatus = _ZxAnVoipInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 15, 1, 20),
    _ZxAnVoipInterfaceRowStatus_Type()
)
zxAnVoipInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipInterfaceRowStatus.setStatus("current")
_ZxAnVoipBaseGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnVoipBaseGlobalObjects = _ZxAnVoipBaseGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 17)
)


class _ZxAnVoipBaseCapabilities_Type(Bits):
    """Custom type zxAnVoipBaseCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("externalSelfswitch", 0),
          ("slcFeedCurrent", 1),
          ("slcHighImpedance", 2),
          ("callerTestMode", 3),
          ("callEscapeMode", 4))
    )

_ZxAnVoipBaseCapabilities_Type.__name__ = "Bits"
_ZxAnVoipBaseCapabilities_Object = MibScalar
zxAnVoipBaseCapabilities = _ZxAnVoipBaseCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 17, 1),
    _ZxAnVoipBaseCapabilities_Type()
)
zxAnVoipBaseCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipBaseCapabilities.setStatus("current")
_ZxAnSelfswitchTktObjects_ObjectIdentity = ObjectIdentity
zxAnSelfswitchTktObjects = _ZxAnSelfswitchTktObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 17, 2)
)


class _ZxAnSelfswitchTktEnable_Type(Integer32):
    """Custom type zxAnSelfswitchTktEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnSelfswitchTktEnable_Type.__name__ = "Integer32"
_ZxAnSelfswitchTktEnable_Object = MibScalar
zxAnSelfswitchTktEnable = _ZxAnSelfswitchTktEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 17, 2, 1),
    _ZxAnSelfswitchTktEnable_Type()
)
zxAnSelfswitchTktEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSelfswitchTktEnable.setStatus("current")


class _ZxAnSelfswitchTktUploadInterval_Type(Integer32):
    """Custom type zxAnSelfswitchTktUploadInterval based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44640),
    )


_ZxAnSelfswitchTktUploadInterval_Type.__name__ = "Integer32"
_ZxAnSelfswitchTktUploadInterval_Object = MibScalar
zxAnSelfswitchTktUploadInterval = _ZxAnSelfswitchTktUploadInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 17, 2, 2),
    _ZxAnSelfswitchTktUploadInterval_Type()
)
zxAnSelfswitchTktUploadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSelfswitchTktUploadInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSelfswitchTktUploadInterval.setUnits("minute")


class _ZxAnSelfswitchTktSizeThreshold_Type(Integer32):
    """Custom type zxAnSelfswitchTktSizeThreshold based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ZxAnSelfswitchTktSizeThreshold_Type.__name__ = "Integer32"
_ZxAnSelfswitchTktSizeThreshold_Object = MibScalar
zxAnSelfswitchTktSizeThreshold = _ZxAnSelfswitchTktSizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 17, 2, 3),
    _ZxAnSelfswitchTktSizeThreshold_Type()
)
zxAnSelfswitchTktSizeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSelfswitchTktSizeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSelfswitchTktSizeThreshold.setUnits("percent")
_ZxAnSelfswitchTelLoadObjects_ObjectIdentity = ObjectIdentity
zxAnSelfswitchTelLoadObjects = _ZxAnSelfswitchTelLoadObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 17, 3)
)


class _ZxAnSelfswitchTelLoadFileName_Type(DisplayString):
    """Custom type zxAnSelfswitchTelLoadFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnSelfswitchTelLoadFileName_Type.__name__ = "DisplayString"
_ZxAnSelfswitchTelLoadFileName_Object = MibScalar
zxAnSelfswitchTelLoadFileName = _ZxAnSelfswitchTelLoadFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 17, 3, 1),
    _ZxAnSelfswitchTelLoadFileName_Type()
)
zxAnSelfswitchTelLoadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSelfswitchTelLoadFileName.setStatus("current")


class _ZxAnSelfswitchTelLoadStatus_Type(Integer32):
    """Custom type zxAnSelfswitchTelLoadStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnSelfswitchTelLoadStatus_Type.__name__ = "Integer32"
_ZxAnSelfswitchTelLoadStatus_Object = MibScalar
zxAnSelfswitchTelLoadStatus = _ZxAnSelfswitchTelLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 17, 3, 2),
    _ZxAnSelfswitchTelLoadStatus_Type()
)
zxAnSelfswitchTelLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSelfswitchTelLoadStatus.setStatus("current")


class _ZxAnSelfswitchTelLoadFailReason_Type(Integer32):
    """Custom type zxAnSelfswitchTelLoadFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("badFile", 2),
          ("noTelOfSelfNe", 3),
          ("otherErrors", 255))
    )


_ZxAnSelfswitchTelLoadFailReason_Type.__name__ = "Integer32"
_ZxAnSelfswitchTelLoadFailReason_Object = MibScalar
zxAnSelfswitchTelLoadFailReason = _ZxAnSelfswitchTelLoadFailReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 17, 3, 3),
    _ZxAnSelfswitchTelLoadFailReason_Type()
)
zxAnSelfswitchTelLoadFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSelfswitchTelLoadFailReason.setStatus("current")


class _ZxAnVoicePortLockoutTrapEnable_Type(Integer32):
    """Custom type zxAnVoicePortLockoutTrapEnable based on Integer32"""
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


_ZxAnVoicePortLockoutTrapEnable_Type.__name__ = "Integer32"
_ZxAnVoicePortLockoutTrapEnable_Object = MibScalar
zxAnVoicePortLockoutTrapEnable = _ZxAnVoicePortLockoutTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 17, 4),
    _ZxAnVoicePortLockoutTrapEnable_Type()
)
zxAnVoicePortLockoutTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoicePortLockoutTrapEnable.setStatus("current")
_ZxAnSelfswitchTktFtpTable_Object = MibTable
zxAnSelfswitchTktFtpTable = _ZxAnSelfswitchTktFtpTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 18)
)
if mibBuilder.loadTexts:
    zxAnSelfswitchTktFtpTable.setStatus("current")
_ZxAnSelfswitchTktFtpEntry_Object = MibTableRow
zxAnSelfswitchTktFtpEntry = _ZxAnSelfswitchTktFtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 18, 1)
)
zxAnSelfswitchTktFtpEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnSelfswitchTktFtpServerId"),
)
if mibBuilder.loadTexts:
    zxAnSelfswitchTktFtpEntry.setStatus("current")


class _ZxAnSelfswitchTktFtpServerId_Type(Integer32):
    """Custom type zxAnSelfswitchTktFtpServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxAnSelfswitchTktFtpServerId_Type.__name__ = "Integer32"
_ZxAnSelfswitchTktFtpServerId_Object = MibTableColumn
zxAnSelfswitchTktFtpServerId = _ZxAnSelfswitchTktFtpServerId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 18, 1, 1),
    _ZxAnSelfswitchTktFtpServerId_Type()
)
zxAnSelfswitchTktFtpServerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSelfswitchTktFtpServerId.setStatus("current")
_ZxAnSelfswitchTktFtpServerIpType_Type = InetAddressType
_ZxAnSelfswitchTktFtpServerIpType_Object = MibTableColumn
zxAnSelfswitchTktFtpServerIpType = _ZxAnSelfswitchTktFtpServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 18, 1, 2),
    _ZxAnSelfswitchTktFtpServerIpType_Type()
)
zxAnSelfswitchTktFtpServerIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSelfswitchTktFtpServerIpType.setStatus("current")
_ZxAnSelfswitchTktFtpServerIp_Type = InetAddress
_ZxAnSelfswitchTktFtpServerIp_Object = MibTableColumn
zxAnSelfswitchTktFtpServerIp = _ZxAnSelfswitchTktFtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 18, 1, 3),
    _ZxAnSelfswitchTktFtpServerIp_Type()
)
zxAnSelfswitchTktFtpServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSelfswitchTktFtpServerIp.setStatus("current")


class _ZxAnSelfswitchTktFtpUserName_Type(DisplayString):
    """Custom type zxAnSelfswitchTktFtpUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnSelfswitchTktFtpUserName_Type.__name__ = "DisplayString"
_ZxAnSelfswitchTktFtpUserName_Object = MibTableColumn
zxAnSelfswitchTktFtpUserName = _ZxAnSelfswitchTktFtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 18, 1, 4),
    _ZxAnSelfswitchTktFtpUserName_Type()
)
zxAnSelfswitchTktFtpUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSelfswitchTktFtpUserName.setStatus("current")


class _ZxAnSelfswitchTktFtpUserPwd_Type(DisplayString):
    """Custom type zxAnSelfswitchTktFtpUserPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnSelfswitchTktFtpUserPwd_Type.__name__ = "DisplayString"
_ZxAnSelfswitchTktFtpUserPwd_Object = MibTableColumn
zxAnSelfswitchTktFtpUserPwd = _ZxAnSelfswitchTktFtpUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 18, 1, 5),
    _ZxAnSelfswitchTktFtpUserPwd_Type()
)
zxAnSelfswitchTktFtpUserPwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSelfswitchTktFtpUserPwd.setStatus("current")


class _ZxAnSelfswitchTktFtpServerPath_Type(DisplayString):
    """Custom type zxAnSelfswitchTktFtpServerPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSelfswitchTktFtpServerPath_Type.__name__ = "DisplayString"
_ZxAnSelfswitchTktFtpServerPath_Object = MibTableColumn
zxAnSelfswitchTktFtpServerPath = _ZxAnSelfswitchTktFtpServerPath_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 18, 1, 6),
    _ZxAnSelfswitchTktFtpServerPath_Type()
)
zxAnSelfswitchTktFtpServerPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSelfswitchTktFtpServerPath.setStatus("current")
_ZxAnSelfswitchTktFtpRowStatus_Type = RowStatus
_ZxAnSelfswitchTktFtpRowStatus_Object = MibTableColumn
zxAnSelfswitchTktFtpRowStatus = _ZxAnSelfswitchTktFtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 18, 1, 20),
    _ZxAnSelfswitchTktFtpRowStatus_Type()
)
zxAnSelfswitchTktFtpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSelfswitchTktFtpRowStatus.setStatus("current")
_ZxAnDsx1ProtectionGroupTable_Object = MibTable
zxAnDsx1ProtectionGroupTable = _ZxAnDsx1ProtectionGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19)
)
if mibBuilder.loadTexts:
    zxAnDsx1ProtectionGroupTable.setStatus("current")
_ZxAnDsx1ProtectionGroupEntry_Object = MibTableRow
zxAnDsx1ProtectionGroupEntry = _ZxAnDsx1ProtectionGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1)
)
zxAnDsx1ProtectionGroupEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnDsx1ProtectionGroupId"),
)
if mibBuilder.loadTexts:
    zxAnDsx1ProtectionGroupEntry.setStatus("current")


class _ZxAnDsx1ProtectionGroupId_Type(Integer32):
    """Custom type zxAnDsx1ProtectionGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ZxAnDsx1ProtectionGroupId_Type.__name__ = "Integer32"
_ZxAnDsx1ProtectionGroupId_Object = MibTableColumn
zxAnDsx1ProtectionGroupId = _ZxAnDsx1ProtectionGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1, 1),
    _ZxAnDsx1ProtectionGroupId_Type()
)
zxAnDsx1ProtectionGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsx1ProtectionGroupId.setStatus("current")


class _ZxAnDsx1ProtectionGroupName_Type(DisplayString):
    """Custom type zxAnDsx1ProtectionGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnDsx1ProtectionGroupName_Type.__name__ = "DisplayString"
_ZxAnDsx1ProtectionGroupName_Object = MibTableColumn
zxAnDsx1ProtectionGroupName = _ZxAnDsx1ProtectionGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1, 2),
    _ZxAnDsx1ProtectionGroupName_Type()
)
zxAnDsx1ProtectionGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsx1ProtectionGroupName.setStatus("current")
_ZxAnDsx1MasterDsx1Rack_Type = Integer32
_ZxAnDsx1MasterDsx1Rack_Object = MibTableColumn
zxAnDsx1MasterDsx1Rack = _ZxAnDsx1MasterDsx1Rack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1, 3),
    _ZxAnDsx1MasterDsx1Rack_Type()
)
zxAnDsx1MasterDsx1Rack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsx1MasterDsx1Rack.setStatus("current")
_ZxAnDsx1MasterDsx1Shelf_Type = Integer32
_ZxAnDsx1MasterDsx1Shelf_Object = MibTableColumn
zxAnDsx1MasterDsx1Shelf = _ZxAnDsx1MasterDsx1Shelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1, 4),
    _ZxAnDsx1MasterDsx1Shelf_Type()
)
zxAnDsx1MasterDsx1Shelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsx1MasterDsx1Shelf.setStatus("current")
_ZxAnDsx1MasterDsx1Slot_Type = Integer32
_ZxAnDsx1MasterDsx1Slot_Object = MibTableColumn
zxAnDsx1MasterDsx1Slot = _ZxAnDsx1MasterDsx1Slot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1, 5),
    _ZxAnDsx1MasterDsx1Slot_Type()
)
zxAnDsx1MasterDsx1Slot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsx1MasterDsx1Slot.setStatus("current")
_ZxAnDsx1MasterDsx1LinkNo_Type = Integer32
_ZxAnDsx1MasterDsx1LinkNo_Object = MibTableColumn
zxAnDsx1MasterDsx1LinkNo = _ZxAnDsx1MasterDsx1LinkNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1, 6),
    _ZxAnDsx1MasterDsx1LinkNo_Type()
)
zxAnDsx1MasterDsx1LinkNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsx1MasterDsx1LinkNo.setStatus("current")
_ZxAnDsx1StandbyDsx1Rack_Type = Integer32
_ZxAnDsx1StandbyDsx1Rack_Object = MibTableColumn
zxAnDsx1StandbyDsx1Rack = _ZxAnDsx1StandbyDsx1Rack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1, 7),
    _ZxAnDsx1StandbyDsx1Rack_Type()
)
zxAnDsx1StandbyDsx1Rack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsx1StandbyDsx1Rack.setStatus("current")
_ZxAnDsx1StandbyDsx1Shelf_Type = Integer32
_ZxAnDsx1StandbyDsx1Shelf_Object = MibTableColumn
zxAnDsx1StandbyDsx1Shelf = _ZxAnDsx1StandbyDsx1Shelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1, 8),
    _ZxAnDsx1StandbyDsx1Shelf_Type()
)
zxAnDsx1StandbyDsx1Shelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsx1StandbyDsx1Shelf.setStatus("current")
_ZxAnDsx1StandbyDsx1Slot_Type = Integer32
_ZxAnDsx1StandbyDsx1Slot_Object = MibTableColumn
zxAnDsx1StandbyDsx1Slot = _ZxAnDsx1StandbyDsx1Slot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1, 9),
    _ZxAnDsx1StandbyDsx1Slot_Type()
)
zxAnDsx1StandbyDsx1Slot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsx1StandbyDsx1Slot.setStatus("current")
_ZxAnDsx1StandbyDsx1LinkNo_Type = Integer32
_ZxAnDsx1StandbyDsx1LinkNo_Object = MibTableColumn
zxAnDsx1StandbyDsx1LinkNo = _ZxAnDsx1StandbyDsx1LinkNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1, 10),
    _ZxAnDsx1StandbyDsx1LinkNo_Type()
)
zxAnDsx1StandbyDsx1LinkNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsx1StandbyDsx1LinkNo.setStatus("current")


class _ZxAnDsx1CurrWorkingDsx1_Type(Integer32):
    """Custom type zxAnDsx1CurrWorkingDsx1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("master", 2),
          ("standby", 3))
    )


_ZxAnDsx1CurrWorkingDsx1_Type.__name__ = "Integer32"
_ZxAnDsx1CurrWorkingDsx1_Object = MibTableColumn
zxAnDsx1CurrWorkingDsx1 = _ZxAnDsx1CurrWorkingDsx1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1, 11),
    _ZxAnDsx1CurrWorkingDsx1_Type()
)
zxAnDsx1CurrWorkingDsx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDsx1CurrWorkingDsx1.setStatus("current")
_ZxAnDsx1ProtectionGroupRowStatus_Type = RowStatus
_ZxAnDsx1ProtectionGroupRowStatus_Object = MibTableColumn
zxAnDsx1ProtectionGroupRowStatus = _ZxAnDsx1ProtectionGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 19, 1, 20),
    _ZxAnDsx1ProtectionGroupRowStatus_Type()
)
zxAnDsx1ProtectionGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDsx1ProtectionGroupRowStatus.setStatus("current")
_ZxAnHwTimeSlotUsageObjects_ObjectIdentity = ObjectIdentity
zxAnHwTimeSlotUsageObjects = _ZxAnHwTimeSlotUsageObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 20)
)
_ZxAnHwTimeSlotUsageGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnHwTimeSlotUsageGlobalObjects = _ZxAnHwTimeSlotUsageGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 20, 1)
)


class _ZxAnHwTimeSlotUsageThreshold_Type(Integer32):
    """Custom type zxAnHwTimeSlotUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnHwTimeSlotUsageThreshold_Type.__name__ = "Integer32"
_ZxAnHwTimeSlotUsageThreshold_Object = MibScalar
zxAnHwTimeSlotUsageThreshold = _ZxAnHwTimeSlotUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 20, 1, 1),
    _ZxAnHwTimeSlotUsageThreshold_Type()
)
zxAnHwTimeSlotUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnHwTimeSlotUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnHwTimeSlotUsageThreshold.setUnits("percent")
_ZxAnHwTimeSlotUsageTable_Object = MibTable
zxAnHwTimeSlotUsageTable = _ZxAnHwTimeSlotUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 20, 2)
)
if mibBuilder.loadTexts:
    zxAnHwTimeSlotUsageTable.setStatus("current")
_ZxAnHwTimeSlotUsageEntry_Object = MibTableRow
zxAnHwTimeSlotUsageEntry = _ZxAnHwTimeSlotUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 20, 2, 1)
)
zxAnHwTimeSlotUsageEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnHwTimeSlotUsageRack"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnHwTimeSlotUsageShelf"),
)
if mibBuilder.loadTexts:
    zxAnHwTimeSlotUsageEntry.setStatus("current")
_ZxAnHwTimeSlotUsageRack_Type = Integer32
_ZxAnHwTimeSlotUsageRack_Object = MibTableColumn
zxAnHwTimeSlotUsageRack = _ZxAnHwTimeSlotUsageRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 20, 2, 1, 1),
    _ZxAnHwTimeSlotUsageRack_Type()
)
zxAnHwTimeSlotUsageRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnHwTimeSlotUsageRack.setStatus("current")
_ZxAnHwTimeSlotUsageShelf_Type = Integer32
_ZxAnHwTimeSlotUsageShelf_Object = MibTableColumn
zxAnHwTimeSlotUsageShelf = _ZxAnHwTimeSlotUsageShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 20, 2, 1, 2),
    _ZxAnHwTimeSlotUsageShelf_Type()
)
zxAnHwTimeSlotUsageShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnHwTimeSlotUsageShelf.setStatus("current")


class _ZxAnHwTimeSlotUsage_Type(Integer32):
    """Custom type zxAnHwTimeSlotUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnHwTimeSlotUsage_Type.__name__ = "Integer32"
_ZxAnHwTimeSlotUsage_Object = MibTableColumn
zxAnHwTimeSlotUsage = _ZxAnHwTimeSlotUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 20, 2, 1, 3),
    _ZxAnHwTimeSlotUsage_Type()
)
zxAnHwTimeSlotUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnHwTimeSlotUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnHwTimeSlotUsage.setUnits("percent")
_MsagResource_ObjectIdentity = ObjectIdentity
msagResource = _MsagResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3)
)
_A200SlcTermIDTable_Object = MibTable
a200SlcTermIDTable = _A200SlcTermIDTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6)
)
if mibBuilder.loadTexts:
    a200SlcTermIDTable.setStatus("current")
_A200SlcTermIDEntry_Object = MibTableRow
a200SlcTermIDEntry = _A200SlcTermIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1)
)
a200SlcTermIDEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200slcTermIDrackno"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200slcTermIDshelfno"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200slcTermIDslotno"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200slcTermIDBeginIndex"),
)
if mibBuilder.loadTexts:
    a200SlcTermIDEntry.setStatus("current")
_A200slcTermIDrackno_Type = Integer32
_A200slcTermIDrackno_Object = MibTableColumn
a200slcTermIDrackno = _A200slcTermIDrackno_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1, 1),
    _A200slcTermIDrackno_Type()
)
a200slcTermIDrackno.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200slcTermIDrackno.setStatus("current")
_A200slcTermIDshelfno_Type = Integer32
_A200slcTermIDshelfno_Object = MibTableColumn
a200slcTermIDshelfno = _A200slcTermIDshelfno_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1, 2),
    _A200slcTermIDshelfno_Type()
)
a200slcTermIDshelfno.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200slcTermIDshelfno.setStatus("current")
_A200slcTermIDslotno_Type = Integer32
_A200slcTermIDslotno_Object = MibTableColumn
a200slcTermIDslotno = _A200slcTermIDslotno_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1, 3),
    _A200slcTermIDslotno_Type()
)
a200slcTermIDslotno.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200slcTermIDslotno.setStatus("current")


class _A200slcTermIDBeginIndex_Type(Integer32):
    """Custom type a200slcTermIDBeginIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_A200slcTermIDBeginIndex_Type.__name__ = "Integer32"
_A200slcTermIDBeginIndex_Object = MibTableColumn
a200slcTermIDBeginIndex = _A200slcTermIDBeginIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1, 4),
    _A200slcTermIDBeginIndex_Type()
)
a200slcTermIDBeginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200slcTermIDBeginIndex.setStatus("current")


class _A200slcTermIDOperSum_Type(Integer32):
    """Custom type a200slcTermIDOperSum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_A200slcTermIDOperSum_Type.__name__ = "Integer32"
_A200slcTermIDOperSum_Object = MibTableColumn
a200slcTermIDOperSum = _A200slcTermIDOperSum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1, 5),
    _A200slcTermIDOperSum_Type()
)
a200slcTermIDOperSum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200slcTermIDOperSum.setStatus("current")


class _A200slcTermIDTMID_Type(OctetString):
    """Custom type a200slcTermIDTMID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_A200slcTermIDTMID_Type.__name__ = "OctetString"
_A200slcTermIDTMID_Object = MibTableColumn
a200slcTermIDTMID = _A200slcTermIDTMID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1, 6),
    _A200slcTermIDTMID_Type()
)
a200slcTermIDTMID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200slcTermIDTMID.setStatus("current")


class _A200slcTermIDType_Type(Integer32):
    """Custom type a200slcTermIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2),
          ("type3", 3))
    )


_A200slcTermIDType_Type.__name__ = "Integer32"
_A200slcTermIDType_Object = MibTableColumn
a200slcTermIDType = _A200slcTermIDType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1, 7),
    _A200slcTermIDType_Type()
)
a200slcTermIDType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200slcTermIDType.setStatus("current")
_A200slcTermIDBeginNo_Type = Integer32
_A200slcTermIDBeginNo_Object = MibTableColumn
a200slcTermIDBeginNo = _A200slcTermIDBeginNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1, 8),
    _A200slcTermIDBeginNo_Type()
)
a200slcTermIDBeginNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200slcTermIDBeginNo.setStatus("current")


class _A200slcTermIDDigitLen_Type(Integer32):
    """Custom type a200slcTermIDDigitLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 64),
    )


_A200slcTermIDDigitLen_Type.__name__ = "Integer32"
_A200slcTermIDDigitLen_Object = MibTableColumn
a200slcTermIDDigitLen = _A200slcTermIDDigitLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1, 9),
    _A200slcTermIDDigitLen_Type()
)
a200slcTermIDDigitLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200slcTermIDDigitLen.setStatus("current")


class _A200slcTermIDMgId_Type(Integer32):
    """Custom type a200slcTermIDMgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A200slcTermIDMgId_Type.__name__ = "Integer32"
_A200slcTermIDMgId_Object = MibTableColumn
a200slcTermIDMgId = _A200slcTermIDMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1, 11),
    _A200slcTermIDMgId_Type()
)
a200slcTermIDMgId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200slcTermIDMgId.setStatus("current")


class _A200slcTerminationID_Type(Integer32):
    """Custom type a200slcTerminationID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 64),
    )


_A200slcTerminationID_Type.__name__ = "Integer32"
_A200slcTerminationID_Object = MibTableColumn
a200slcTerminationID = _A200slcTerminationID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1, 12),
    _A200slcTerminationID_Type()
)
a200slcTerminationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a200slcTerminationID.setStatus("current")
_A200slcTermIDRowStatus_Type = RowStatus
_A200slcTermIDRowStatus_Object = MibTableColumn
a200slcTermIDRowStatus = _A200slcTermIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 6, 1, 13),
    _A200slcTermIDRowStatus_Type()
)
a200slcTermIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200slcTermIDRowStatus.setStatus("current")
_A200IpsTermIDTable_Object = MibTable
a200IpsTermIDTable = _A200IpsTermIDTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7)
)
if mibBuilder.loadTexts:
    a200IpsTermIDTable.setStatus("current")
_A200IpsTermIDEntry_Object = MibTableRow
a200IpsTermIDEntry = _A200IpsTermIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7, 1)
)
a200IpsTermIDEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200IpsTermIDSeqNo"),
)
if mibBuilder.loadTexts:
    a200IpsTermIDEntry.setStatus("current")
_A200IpsTermIDSeqNo_Type = Integer32
_A200IpsTermIDSeqNo_Object = MibTableColumn
a200IpsTermIDSeqNo = _A200IpsTermIDSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7, 1, 1),
    _A200IpsTermIDSeqNo_Type()
)
a200IpsTermIDSeqNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200IpsTermIDSeqNo.setStatus("current")


class _A200IpsTermIDDeltag_Type(Integer32):
    """Custom type a200IpsTermIDDeltag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_A200IpsTermIDDeltag_Type.__name__ = "Integer32"
_A200IpsTermIDDeltag_Object = MibTableColumn
a200IpsTermIDDeltag = _A200IpsTermIDDeltag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7, 1, 2),
    _A200IpsTermIDDeltag_Type()
)
a200IpsTermIDDeltag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200IpsTermIDDeltag.setStatus("current")


class _A200IpsTermIDBeginSeqNo_Type(Integer32):
    """Custom type a200IpsTermIDBeginSeqNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_A200IpsTermIDBeginSeqNo_Type.__name__ = "Integer32"
_A200IpsTermIDBeginSeqNo_Object = MibTableColumn
a200IpsTermIDBeginSeqNo = _A200IpsTermIDBeginSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7, 1, 3),
    _A200IpsTermIDBeginSeqNo_Type()
)
a200IpsTermIDBeginSeqNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200IpsTermIDBeginSeqNo.setStatus("current")


class _A200IpsTermIDOperNum_Type(Integer32):
    """Custom type a200IpsTermIDOperNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_A200IpsTermIDOperNum_Type.__name__ = "Integer32"
_A200IpsTermIDOperNum_Object = MibTableColumn
a200IpsTermIDOperNum = _A200IpsTermIDOperNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7, 1, 4),
    _A200IpsTermIDOperNum_Type()
)
a200IpsTermIDOperNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200IpsTermIDOperNum.setStatus("current")


class _A200IpsTermIDTMIDFix_Type(DisplayString):
    """Custom type a200IpsTermIDTMIDFix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_A200IpsTermIDTMIDFix_Type.__name__ = "DisplayString"
_A200IpsTermIDTMIDFix_Object = MibTableColumn
a200IpsTermIDTMIDFix = _A200IpsTermIDTMIDFix_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7, 1, 5),
    _A200IpsTermIDTMIDFix_Type()
)
a200IpsTermIDTMIDFix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200IpsTermIDTMIDFix.setStatus("current")


class _A200IpsTermIDType_Type(Integer32):
    """Custom type a200IpsTermIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type2", 2),
          ("type3", 3))
    )


_A200IpsTermIDType_Type.__name__ = "Integer32"
_A200IpsTermIDType_Object = MibTableColumn
a200IpsTermIDType = _A200IpsTermIDType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7, 1, 6),
    _A200IpsTermIDType_Type()
)
a200IpsTermIDType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200IpsTermIDType.setStatus("current")


class _A200IpsTermIDDigitLen_Type(Integer32):
    """Custom type a200IpsTermIDDigitLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 64),
    )


_A200IpsTermIDDigitLen_Type.__name__ = "Integer32"
_A200IpsTermIDDigitLen_Object = MibTableColumn
a200IpsTermIDDigitLen = _A200IpsTermIDDigitLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7, 1, 7),
    _A200IpsTermIDDigitLen_Type()
)
a200IpsTermIDDigitLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200IpsTermIDDigitLen.setStatus("current")
_A200IpsTermIDBeginNo_Type = Integer32
_A200IpsTermIDBeginNo_Object = MibTableColumn
a200IpsTermIDBeginNo = _A200IpsTermIDBeginNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7, 1, 8),
    _A200IpsTermIDBeginNo_Type()
)
a200IpsTermIDBeginNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200IpsTermIDBeginNo.setStatus("current")


class _A200IpsTermIDMgId_Type(Integer32):
    """Custom type a200IpsTermIDMgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A200IpsTermIDMgId_Type.__name__ = "Integer32"
_A200IpsTermIDMgId_Object = MibTableColumn
a200IpsTermIDMgId = _A200IpsTermIDMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7, 1, 9),
    _A200IpsTermIDMgId_Type()
)
a200IpsTermIDMgId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200IpsTermIDMgId.setStatus("current")


class _A200IpsTerminationID_Type(DisplayString):
    """Custom type a200IpsTerminationID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_A200IpsTerminationID_Type.__name__ = "DisplayString"
_A200IpsTerminationID_Object = MibTableColumn
a200IpsTerminationID = _A200IpsTerminationID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7, 1, 10),
    _A200IpsTerminationID_Type()
)
a200IpsTerminationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a200IpsTerminationID.setStatus("current")
_A200IpsTermIDRowStatus_Type = RowStatus
_A200IpsTermIDRowStatus_Object = MibTableColumn
a200IpsTermIDRowStatus = _A200IpsTermIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 7, 1, 11),
    _A200IpsTermIDRowStatus_Type()
)
a200IpsTermIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    a200IpsTermIDRowStatus.setStatus("current")
_A200RtpParTable_Object = MibTable
a200RtpParTable = _A200RtpParTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8)
)
if mibBuilder.loadTexts:
    a200RtpParTable.setStatus("current")
_A200RtpParEntry_Object = MibTableRow
a200RtpParEntry = _A200RtpParEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1)
)
a200RtpParEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "a200rtpparparid"),
)
if mibBuilder.loadTexts:
    a200RtpParEntry.setStatus("current")


class _A200rtpparparid_Type(Integer32):
    """Custom type a200rtpparparid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_A200rtpparparid_Type.__name__ = "Integer32"
_A200rtpparparid_Object = MibTableColumn
a200rtpparparid = _A200rtpparparid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 1),
    _A200rtpparparid_Type()
)
a200rtpparparid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a200rtpparparid.setStatus("current")


class _A200rtpparvadval_Type(Integer32):
    """Custom type a200rtpparvadval based on Integer32"""
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
        *(("disable", 0),
          ("defaultscheme", 1),
          ("pt13scheme", 2),
          ("nosilence", 3))
    )


_A200rtpparvadval_Type.__name__ = "Integer32"
_A200rtpparvadval_Object = MibTableColumn
a200rtpparvadval = _A200rtpparvadval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 2),
    _A200rtpparvadval_Type()
)
a200rtpparvadval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparvadval.setStatus("current")


class _A200rtppardtmfrlmod_Type(Integer32):
    """Custom type a200rtppardtmfrlmod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notRelay", 0),
          ("voiceCoding", 1),
          ("redRfc2833", 2),
          ("aal2Ietf", 4),
          ("nredRfc2833", 6))
    )


_A200rtppardtmfrlmod_Type.__name__ = "Integer32"
_A200rtppardtmfrlmod_Object = MibTableColumn
a200rtppardtmfrlmod = _A200rtppardtmfrlmod_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 3),
    _A200rtppardtmfrlmod_Type()
)
a200rtppardtmfrlmod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtppardtmfrlmod.setStatus("current")


class _A200rtpparpcmlaw_Type(Integer32):
    """Custom type a200rtpparpcmlaw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 0),
          ("uLaw", 1))
    )


_A200rtpparpcmlaw_Type.__name__ = "Integer32"
_A200rtpparpcmlaw_Object = MibTableColumn
a200rtpparpcmlaw = _A200rtpparpcmlaw_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 4),
    _A200rtpparpcmlaw_Type()
)
a200rtpparpcmlaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparpcmlaw.setStatus("current")


class _A200rtpparsiltopcm_Type(Integer32):
    """Custom type a200rtpparsiltopcm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("comfortNoise", 0),
          ("silence", 1))
    )


_A200rtpparsiltopcm_Type.__name__ = "Integer32"
_A200rtpparsiltopcm_Object = MibTableColumn
a200rtpparsiltopcm = _A200rtpparsiltopcm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 5),
    _A200rtpparsiltopcm_Type()
)
a200rtpparsiltopcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparsiltopcm.setStatus("current")


class _A200rtppardcfilter_Type(Integer32):
    """Custom type a200rtppardcfilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_A200rtppardcfilter_Type.__name__ = "Integer32"
_A200rtppardcfilter_Object = MibTableColumn
a200rtppardcfilter = _A200rtppardcfilter_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 6),
    _A200rtppardcfilter_Type()
)
a200rtppardcfilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtppardcfilter.setStatus("current")


class _A200rtpparpcmtopkggain_Type(Integer32):
    """Custom type a200rtpparpcmtopkggain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_A200rtpparpcmtopkggain_Type.__name__ = "Integer32"
_A200rtpparpcmtopkggain_Object = MibTableColumn
a200rtpparpcmtopkggain = _A200rtpparpcmtopkggain_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 7),
    _A200rtpparpcmtopkggain_Type()
)
a200rtpparpcmtopkggain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparpcmtopkggain.setStatus("current")


class _A200rtpparpkgtopcmgain_Type(Integer32):
    """Custom type a200rtpparpkgtopcmgain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_A200rtpparpkgtopcmgain_Type.__name__ = "Integer32"
_A200rtpparpkgtopcmgain_Object = MibTableColumn
a200rtpparpkgtopcmgain = _A200rtpparpkgtopcmgain_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 8),
    _A200rtpparpkgtopcmgain_Type()
)
a200rtpparpkgtopcmgain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparpkgtopcmgain.setStatus("current")


class _A200rtpparconceal_Type(Integer32):
    """Custom type a200rtpparconceal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notReplace", 0),
          ("whiteLine", 1),
          ("lastLine", 2))
    )


_A200rtpparconceal_Type.__name__ = "Integer32"
_A200rtpparconceal_Object = MibTableColumn
a200rtpparconceal = _A200rtpparconceal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 9),
    _A200rtpparconceal_Type()
)
a200rtpparconceal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparconceal.setStatus("current")


class _A200rtpparecmdisabl_Type(Integer32):
    """Custom type a200rtpparecmdisabl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_A200rtpparecmdisabl_Type.__name__ = "Integer32"
_A200rtpparecmdisabl_Object = MibTableColumn
a200rtpparecmdisabl = _A200rtpparecmdisabl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 10),
    _A200rtpparecmdisabl_Type()
)
a200rtpparecmdisabl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparecmdisabl.setStatus("current")


class _A200rtpparspeedlim_Type(Integer32):
    """Custom type a200rtpparspeedlim based on Integer32"""
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
        *(("noLimit", 0),
          ("is2400bps", 1),
          ("is4800bps", 2),
          ("is7200bps", 3),
          ("is9600bps", 4),
          ("is12000bps", 5),
          ("is14400bps", 6))
    )


_A200rtpparspeedlim_Type.__name__ = "Integer32"
_A200rtpparspeedlim_Object = MibTableColumn
a200rtpparspeedlim = _A200rtpparspeedlim_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 11),
    _A200rtpparspeedlim_Type()
)
a200rtpparspeedlim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparspeedlim.setStatus("current")


class _A200rtpparerrrecov_Type(Integer32):
    """Custom type a200rtpparerrrecov based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("redundancy", 0),
          ("fec", 1))
    )


_A200rtpparerrrecov_Type.__name__ = "Integer32"
_A200rtpparerrrecov_Object = MibTableColumn
a200rtpparerrrecov = _A200rtpparerrrecov_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 12),
    _A200rtpparerrrecov_Type()
)
a200rtpparerrrecov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparerrrecov.setStatus("current")


class _A200rtppartcfproc_Type(Integer32):
    """Custom type a200rtppartcfproc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("procedure2", 0),
          ("procedure1", 1))
    )


_A200rtppartcfproc_Type.__name__ = "Integer32"
_A200rtppartcfproc_Object = MibTableColumn
a200rtppartcfproc = _A200rtppartcfproc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 13),
    _A200rtppartcfproc_Type()
)
a200rtppartcfproc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtppartcfproc.setStatus("current")


class _A200rtppart38enable_Type(Integer32):
    """Custom type a200rtppart38enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("t30", 0),
          ("t38", 1),
          ("rtp", 2),
          ("halfControl", 10),
          ("fullControl", 11))
    )


_A200rtppart38enable_Type.__name__ = "Integer32"
_A200rtppart38enable_Object = MibTableColumn
a200rtppart38enable = _A200rtppart38enable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 14),
    _A200rtppart38enable_Type()
)
a200rtppart38enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtppart38enable.setStatus("current")


class _A200rtppardtmfduplex_Type(Integer32):
    """Custom type a200rtppardtmfduplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A200rtppardtmfduplex_Type.__name__ = "Integer32"
_A200rtppardtmfduplex_Object = MibTableColumn
a200rtppardtmfduplex = _A200rtppardtmfduplex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 15),
    _A200rtppardtmfduplex_Type()
)
a200rtppardtmfduplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtppardtmfduplex.setStatus("current")


class _A200rtpparNumBeforeOff_Type(Integer32):
    """Custom type a200rtpparNumBeforeOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_A200rtpparNumBeforeOff_Type.__name__ = "Integer32"
_A200rtpparNumBeforeOff_Object = MibTableColumn
a200rtpparNumBeforeOff = _A200rtpparNumBeforeOff_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 16),
    _A200rtpparNumBeforeOff_Type()
)
a200rtpparNumBeforeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparNumBeforeOff.setStatus("current")


class _A200rtpparIgnoreA_Type(Integer32):
    """Custom type a200rtpparIgnoreA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A200rtpparIgnoreA_Type.__name__ = "Integer32"
_A200rtpparIgnoreA_Object = MibTableColumn
a200rtpparIgnoreA = _A200rtpparIgnoreA_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 17),
    _A200rtpparIgnoreA_Type()
)
a200rtpparIgnoreA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparIgnoreA.setStatus("current")


class _A200rtpparToneDuplex_Type(Integer32):
    """Custom type a200rtpparToneDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A200rtpparToneDuplex_Type.__name__ = "Integer32"
_A200rtpparToneDuplex_Object = MibTableColumn
a200rtpparToneDuplex = _A200rtpparToneDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 18),
    _A200rtpparToneDuplex_Type()
)
a200rtpparToneDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparToneDuplex.setStatus("current")


class _A200rtppardecodadapt_Type(Integer32):
    """Custom type a200rtppardecodadapt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A200rtppardecodadapt_Type.__name__ = "Integer32"
_A200rtppardecodadapt_Object = MibTableColumn
a200rtppardecodadapt = _A200rtppardecodadapt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 19),
    _A200rtppardecodadapt_Type()
)
a200rtppardecodadapt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtppardecodadapt.setStatus("current")


class _A200rtpparg723rate_Type(Integer32):
    """Custom type a200rtpparg723rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lowRate", 0),
          ("highRate", 1))
    )


_A200rtpparg723rate_Type.__name__ = "Integer32"
_A200rtpparg723rate_Object = MibTableColumn
a200rtpparg723rate = _A200rtpparg723rate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 20),
    _A200rtpparg723rate_Type()
)
a200rtpparg723rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparg723rate.setStatus("current")


class _A200rtpparpckgendis_Type(Integer32):
    """Custom type a200rtpparpckgendis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_A200rtpparpckgendis_Type.__name__ = "Integer32"
_A200rtpparpckgendis_Object = MibTableColumn
a200rtpparpckgendis = _A200rtpparpckgendis_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 21),
    _A200rtpparpckgendis_Type()
)
a200rtpparpckgendis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparpckgendis.setStatus("current")


class _A200rtppardtmfpyld_Type(Integer32):
    """Custom type a200rtppardtmfpyld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A200rtppardtmfpyld_Type.__name__ = "Integer32"
_A200rtppardtmfpyld_Object = MibTableColumn
a200rtppardtmfpyld = _A200rtppardtmfpyld_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 22),
    _A200rtppardtmfpyld_Type()
)
a200rtppardtmfpyld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtppardtmfpyld.setStatus("current")


class _A200rtppardtmfredpyld_Type(Integer32):
    """Custom type a200rtppardtmfredpyld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A200rtppardtmfredpyld_Type.__name__ = "Integer32"
_A200rtppardtmfredpyld_Object = MibTableColumn
a200rtppardtmfredpyld = _A200rtppardtmfredpyld_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 23),
    _A200rtppardtmfredpyld_Type()
)
a200rtppardtmfredpyld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtppardtmfredpyld.setStatus("current")


class _A200rtpparfaxdatared_Type(Integer32):
    """Custom type a200rtpparfaxdatared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_A200rtpparfaxdatared_Type.__name__ = "Integer32"
_A200rtpparfaxdatared_Object = MibTableColumn
a200rtpparfaxdatared = _A200rtpparfaxdatared_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 24),
    _A200rtpparfaxdatared_Type()
)
a200rtpparfaxdatared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparfaxdatared.setStatus("current")


class _A200rtppart30msgred_Type(Integer32):
    """Custom type a200rtppart30msgred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_A200rtppart30msgred_Type.__name__ = "Integer32"
_A200rtppart30msgred_Object = MibTableColumn
a200rtppart30msgred = _A200rtppart30msgred_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 25),
    _A200rtppart30msgred_Type()
)
a200rtppart30msgred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtppart30msgred.setStatus("current")


class _A200rtpparmasecenal_Type(Integer32):
    """Custom type a200rtpparmasecenal based on Integer32"""
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


_A200rtpparmasecenal_Type.__name__ = "Integer32"
_A200rtpparmasecenal_Object = MibTableColumn
a200rtpparmasecenal = _A200rtpparmasecenal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 26),
    _A200rtpparmasecenal_Type()
)
a200rtpparmasecenal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparmasecenal.setStatus("current")


class _A200rtpparhdwecdis_Type(Integer32):
    """Custom type a200rtpparhdwecdis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_A200rtpparhdwecdis_Type.__name__ = "Integer32"
_A200rtpparhdwecdis_Object = MibTableColumn
a200rtpparhdwecdis = _A200rtpparhdwecdis_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 27),
    _A200rtpparhdwecdis_Type()
)
a200rtpparhdwecdis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparhdwecdis.setStatus("current")


class _A200rtpparhecfrz_Type(Integer32):
    """Custom type a200rtpparhecfrz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowUpdate", 0),
          ("disableUpdate", 1))
    )


_A200rtpparhecfrz_Type.__name__ = "Integer32"
_A200rtpparhecfrz_Object = MibTableColumn
a200rtpparhecfrz = _A200rtpparhecfrz_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 28),
    _A200rtpparhecfrz_Type()
)
a200rtpparhecfrz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparhecfrz.setStatus("current")


class _A200rtpparectxf_Type(Integer32):
    """Custom type a200rtpparectxf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonLinear", 0),
          ("fixedGain", 1))
    )


_A200rtpparectxf_Type.__name__ = "Integer32"
_A200rtpparectxf_Object = MibTableColumn
a200rtpparectxf = _A200rtpparectxf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 29),
    _A200rtpparectxf_Type()
)
a200rtpparectxf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparectxf.setStatus("current")


class _A200rtpparectxm_Type(Integer32):
    """Custom type a200rtpparectxm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("mute", 1))
    )


_A200rtpparectxm_Type.__name__ = "Integer32"
_A200rtpparectxm_Object = MibTableColumn
a200rtpparectxm = _A200rtpparectxm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 30),
    _A200rtpparectxm_Type()
)
a200rtpparectxm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparectxm.setStatus("current")


class _A200rtpparecrxm_Type(Integer32):
    """Custom type a200rtpparecrxm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("mute", 1))
    )


_A200rtpparecrxm_Type.__name__ = "Integer32"
_A200rtpparecrxm_Object = MibTableColumn
a200rtpparecrxm = _A200rtpparecrxm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 31),
    _A200rtpparecrxm_Type()
)
a200rtpparecrxm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparecrxm.setStatus("current")


class _A200rtpparheclen_Type(Integer32):
    """Custom type a200rtpparheclen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A200rtpparheclen_Type.__name__ = "Integer32"
_A200rtpparheclen_Object = MibTableColumn
a200rtpparheclen = _A200rtpparheclen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 32),
    _A200rtpparheclen_Type()
)
a200rtpparheclen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparheclen.setStatus("current")


class _A200rtpparlpwmin_Type(Integer32):
    """Custom type a200rtpparlpwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A200rtpparlpwmin_Type.__name__ = "Integer32"
_A200rtpparlpwmin_Object = MibTableColumn
a200rtpparlpwmin = _A200rtpparlpwmin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 33),
    _A200rtpparlpwmin_Type()
)
a200rtpparlpwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparlpwmin.setStatus("current")


class _A200rtpparlpwmax_Type(Integer32):
    """Custom type a200rtpparlpwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A200rtpparlpwmax_Type.__name__ = "Integer32"
_A200rtpparlpwmax_Object = MibTableColumn
a200rtpparlpwmax = _A200rtpparlpwmax_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 34),
    _A200rtpparlpwmax_Type()
)
a200rtpparlpwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparlpwmax.setStatus("current")


class _A200rtpparlpwinit_Type(Integer32):
    """Custom type a200rtpparlpwinit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A200rtpparlpwinit_Type.__name__ = "Integer32"
_A200rtpparlpwinit_Object = MibTableColumn
a200rtpparlpwinit = _A200rtpparlpwinit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 35),
    _A200rtpparlpwinit_Type()
)
a200rtpparlpwinit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparlpwinit.setStatus("current")


class _A200rtpparlpr_Type(Integer32):
    """Custom type a200rtpparlpr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_A200rtpparlpr_Type.__name__ = "Integer32"
_A200rtpparlpr_Object = MibTableColumn
a200rtpparlpr = _A200rtpparlpr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 36),
    _A200rtpparlpr_Type()
)
a200rtpparlpr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparlpr.setStatus("current")


class _A200rtpparfsklevel_Type(Integer32):
    """Custom type a200rtpparfsklevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(62, 382),
    )


_A200rtpparfsklevel_Type.__name__ = "Integer32"
_A200rtpparfsklevel_Object = MibTableColumn
a200rtpparfsklevel = _A200rtpparfsklevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 37),
    _A200rtpparfsklevel_Type()
)
a200rtpparfsklevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparfsklevel.setStatus("current")


class _A200rtpparg711redund_Type(Integer32):
    """Custom type a200rtpparg711redund based on Integer32"""
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
        *(("noRedundancy", 0),
          ("is1Package", 1),
          ("is2Package", 2),
          ("is3Package", 3))
    )


_A200rtpparg711redund_Type.__name__ = "Integer32"
_A200rtpparg711redund_Object = MibTableColumn
a200rtpparg711redund = _A200rtpparg711redund_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 38),
    _A200rtpparg711redund_Type()
)
a200rtpparg711redund.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparg711redund.setStatus("current")


class _A200rtpparmodemmode_Type(Integer32):
    """Custom type a200rtpparmodemmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              11)
        )
    )
    namedValues = NamedValues(
        *(("modemDelay5s", 0),
          ("transparent", 2),
          ("modemImmediate", 3),
          ("faxImmediate", 4),
          ("cidImmediate", 5),
          ("ipModem", 6),
          ("fullCtrl", 11))
    )


_A200rtpparmodemmode_Type.__name__ = "Integer32"
_A200rtpparmodemmode_Object = MibTableColumn
a200rtpparmodemmode = _A200rtpparmodemmode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 39),
    _A200rtpparmodemmode_Type()
)
a200rtpparmodemmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparmodemmode.setStatus("current")


class _A200rtpparap_Type(Integer32):
    """Custom type a200rtpparap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A200rtpparap_Type.__name__ = "Integer32"
_A200rtpparap_Object = MibTableColumn
a200rtpparap = _A200rtpparap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 40),
    _A200rtpparap_Type()
)
a200rtpparap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparap.setStatus("current")


class _A200rtppardeletmode_Type(Integer32):
    """Custom type a200rtppardeletmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A200rtppardeletmode_Type.__name__ = "Integer32"
_A200rtppardeletmode_Object = MibTableColumn
a200rtppardeletmode = _A200rtppardeletmode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 41),
    _A200rtppardeletmode_Type()
)
a200rtppardeletmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtppardeletmode.setStatus("current")


class _A200rtpparnortptime_Type(Integer32):
    """Custom type a200rtpparnortptime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A200rtpparnortptime_Type.__name__ = "Integer32"
_A200rtpparnortptime_Object = MibTableColumn
a200rtpparnortptime = _A200rtpparnortptime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 42),
    _A200rtpparnortptime_Type()
)
a200rtpparnortptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparnortptime.setStatus("current")


class _A200rtpparfaxswtime_Type(Integer32):
    """Custom type a200rtpparfaxswtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A200rtpparfaxswtime_Type.__name__ = "Integer32"
_A200rtpparfaxswtime_Object = MibTableColumn
a200rtpparfaxswtime = _A200rtpparfaxswtime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 43),
    _A200rtpparfaxswtime_Type()
)
a200rtpparfaxswtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtpparfaxswtime.setStatus("current")


class _A200rtppardtmfcidelec_Type(Integer32):
    """Custom type a200rtppardtmfcidelec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 630),
    )


_A200rtppardtmfcidelec_Type.__name__ = "Integer32"
_A200rtppardtmfcidelec_Object = MibTableColumn
a200rtppardtmfcidelec = _A200rtppardtmfcidelec_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 3, 8, 1, 44),
    _A200rtppardtmfcidelec_Type()
)
a200rtppardtmfcidelec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a200rtppardtmfcidelec.setStatus("current")
_MsagCallCtrl_ObjectIdentity = ObjectIdentity
msagCallCtrl = _MsagCallCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6)
)
_UpPortTable_Object = MibTable
upPortTable = _UpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1)
)
if mibBuilder.loadTexts:
    upPortTable.setStatus("current")
_UpPortEntry_Object = MibTableRow
upPortEntry = _UpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1, 1)
)
upPortEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "upportid"),
)
if mibBuilder.loadTexts:
    upPortEntry.setStatus("current")


class _Upportid_Type(Integer32):
    """Custom type upportid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Upportid_Type.__name__ = "Integer32"
_Upportid_Object = MibTableColumn
upportid = _Upportid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1, 1, 1),
    _Upportid_Type()
)
upportid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upportid.setStatus("current")


class _Upportrack_Type(Integer32):
    """Custom type upportrack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Upportrack_Type.__name__ = "Integer32"
_Upportrack_Object = MibTableColumn
upportrack = _Upportrack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1, 1, 2),
    _Upportrack_Type()
)
upportrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upportrack.setStatus("current")


class _Upportshelf_Type(Integer32):
    """Custom type upportshelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Upportshelf_Type.__name__ = "Integer32"
_Upportshelf_Object = MibTableColumn
upportshelf = _Upportshelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1, 1, 3),
    _Upportshelf_Type()
)
upportshelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upportshelf.setStatus("current")


class _Upportslot_Type(Integer32):
    """Custom type upportslot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_Upportslot_Type.__name__ = "Integer32"
_Upportslot_Object = MibTableColumn
upportslot = _Upportslot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1, 1, 29),
    _Upportslot_Type()
)
upportslot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upportslot.setStatus("current")


class _Upportport_Type(Integer32):
    """Custom type upportport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Upportport_Type.__name__ = "Integer32"
_Upportport_Object = MibTableColumn
upportport = _Upportport_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1, 1, 31),
    _Upportport_Type()
)
upportport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upportport.setStatus("current")


class _Upportsendrateth_Type(Unsigned32):
    """Custom type upportsendrateth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 104857600),
    )


_Upportsendrateth_Type.__name__ = "Unsigned32"
_Upportsendrateth_Object = MibTableColumn
upportsendrateth = _Upportsendrateth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1, 1, 33),
    _Upportsendrateth_Type()
)
upportsendrateth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upportsendrateth.setStatus("current")


class _Upportreceiverateth_Type(Unsigned32):
    """Custom type upportreceiverateth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 104857600),
    )


_Upportreceiverateth_Type.__name__ = "Unsigned32"
_Upportreceiverateth_Object = MibTableColumn
upportreceiverateth = _Upportreceiverateth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1, 1, 35),
    _Upportreceiverateth_Type()
)
upportreceiverateth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upportreceiverateth.setStatus("current")
_UpportRowStatus_Type = RowStatus
_UpportRowStatus_Object = MibTableColumn
upportRowStatus = _UpportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1, 1, 37),
    _UpportRowStatus_Type()
)
upportRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upportRowStatus.setStatus("current")
_ToneTable_Object = MibTable
toneTable = _ToneTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 2)
)
if mibBuilder.loadTexts:
    toneTable.setStatus("current")
_ToneEntry_Object = MibTableRow
toneEntry = _ToneEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 2, 1)
)
toneEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "tonemgid"),
)
if mibBuilder.loadTexts:
    toneEntry.setStatus("current")


class _Tonemgid_Type(Integer32):
    """Custom type tonemgid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Tonemgid_Type.__name__ = "Integer32"
_Tonemgid_Object = MibTableColumn
tonemgid = _Tonemgid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 2, 1, 1),
    _Tonemgid_Type()
)
tonemgid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tonemgid.setStatus("current")


class _Tonefaxcngtone_Type(Integer32):
    """Custom type tonefaxcngtone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notReport", 0),
          ("report", 1))
    )


_Tonefaxcngtone_Type.__name__ = "Integer32"
_Tonefaxcngtone_Object = MibTableColumn
tonefaxcngtone = _Tonefaxcngtone_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 2, 1, 2),
    _Tonefaxcngtone_Type()
)
tonefaxcngtone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonefaxcngtone.setStatus("current")


class _Tonev21flagstone_Type(Integer32):
    """Custom type tonev21flagstone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notReport", 0),
          ("report", 1))
    )


_Tonev21flagstone_Type.__name__ = "Integer32"
_Tonev21flagstone_Object = MibTableColumn
tonev21flagstone = _Tonev21flagstone_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 2, 1, 3),
    _Tonev21flagstone_Type()
)
tonev21flagstone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonev21flagstone.setStatus("current")


class _Tonet38faxend_Type(Integer32):
    """Custom type tonet38faxend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notReport", 0),
          ("report", 1))
    )


_Tonet38faxend_Type.__name__ = "Integer32"
_Tonet38faxend_Object = MibTableColumn
tonet38faxend = _Tonet38faxend_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 2, 1, 4),
    _Tonet38faxend_Type()
)
tonet38faxend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonet38faxend.setStatus("current")


class _Toneansamwitone_Type(Integer32):
    """Custom type toneansamwitone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notReport", 0),
          ("report", 1))
    )


_Toneansamwitone_Type.__name__ = "Integer32"
_Toneansamwitone_Object = MibTableColumn
toneansamwitone = _Toneansamwitone_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 2, 1, 5),
    _Toneansamwitone_Type()
)
toneansamwitone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    toneansamwitone.setStatus("current")


class _Toneansamwotone_Type(Integer32):
    """Custom type toneansamwotone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notReport", 0),
          ("report", 1))
    )


_Toneansamwotone_Type.__name__ = "Integer32"
_Toneansamwotone_Object = MibTableColumn
toneansamwotone = _Toneansamwotone_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 2, 1, 6),
    _Toneansamwotone_Type()
)
toneansamwotone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    toneansamwotone.setStatus("current")


class _Toneanswitone_Type(Integer32):
    """Custom type toneanswitone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notReport", 0),
          ("report", 1))
    )


_Toneanswitone_Type.__name__ = "Integer32"
_Toneanswitone_Object = MibTableColumn
toneanswitone = _Toneanswitone_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 2, 1, 7),
    _Toneanswitone_Type()
)
toneanswitone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    toneanswitone.setStatus("current")


class _Toneanswotone_Type(Integer32):
    """Custom type toneanswotone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notReport", 0),
          ("report", 1))
    )


_Toneanswotone_Type.__name__ = "Integer32"
_Toneanswotone_Object = MibTableColumn
toneanswotone = _Toneanswotone_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 2, 1, 8),
    _Toneanswotone_Type()
)
toneanswotone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    toneanswotone.setStatus("current")


class _Tonefixtonechip_Type(Integer32):
    """Custom type tonefixtonechip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsp", 1),
          ("ips", 2))
    )


_Tonefixtonechip_Type.__name__ = "Integer32"
_Tonefixtonechip_Object = MibScalar
tonefixtonechip = _Tonefixtonechip_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 3),
    _Tonefixtonechip_Type()
)
tonefixtonechip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonefixtonechip.setStatus("current")
_MsagH248Perform_ObjectIdentity = ObjectIdentity
msagH248Perform = _MsagH248Perform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 6)
)
_MsagH248PSRecMsg_Type = Integer32
_MsagH248PSRecMsg_Object = MibScalar
msagH248PSRecMsg = _MsagH248PSRecMsg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 6, 1),
    _MsagH248PSRecMsg_Type()
)
msagH248PSRecMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagH248PSRecMsg.setStatus("current")
_MsagH248PSSendMsg_Type = Integer32
_MsagH248PSSendMsg_Object = MibScalar
msagH248PSSendMsg = _MsagH248PSSendMsg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 6, 2),
    _MsagH248PSSendMsg_Type()
)
msagH248PSSendMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagH248PSSendMsg.setStatus("current")
_MsagH248PSRecMsgByte_Type = Integer32
_MsagH248PSRecMsgByte_Object = MibScalar
msagH248PSRecMsgByte = _MsagH248PSRecMsgByte_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 6, 3),
    _MsagH248PSRecMsgByte_Type()
)
msagH248PSRecMsgByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagH248PSRecMsgByte.setStatus("current")
_MsagH248PSSendMsgByte_Type = Integer32
_MsagH248PSSendMsgByte_Object = MibScalar
msagH248PSSendMsgByte = _MsagH248PSSendMsgByte_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 6, 4),
    _MsagH248PSSendMsgByte_Type()
)
msagH248PSSendMsgByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagH248PSSendMsgByte.setStatus("current")
_MsagH248PSProtocolError_Type = Integer32
_MsagH248PSProtocolError_Object = MibScalar
msagH248PSProtocolError = _MsagH248PSProtocolError_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 6, 5),
    _MsagH248PSProtocolError_Type()
)
msagH248PSProtocolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagH248PSProtocolError.setStatus("current")
_MsagH248PSTimerOut_Type = Integer32
_MsagH248PSTimerOut_Object = MibScalar
msagH248PSTimerOut = _MsagH248PSTimerOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 6, 6),
    _MsagH248PSTimerOut_Type()
)
msagH248PSTimerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagH248PSTimerOut.setStatus("current")
_MsagH248PSDisconnect_Type = Integer32
_MsagH248PSDisconnect_Object = MibScalar
msagH248PSDisconnect = _MsagH248PSDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 6, 7),
    _MsagH248PSDisconnect_Type()
)
msagH248PSDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagH248PSDisconnect.setStatus("current")
_MsagH248PSMGCChange_Type = Integer32
_MsagH248PSMGCChange_Object = MibScalar
msagH248PSMGCChange = _MsagH248PSMGCChange_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 6, 8),
    _MsagH248PSMGCChange_Type()
)
msagH248PSMGCChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagH248PSMGCChange.setStatus("current")
_MsagH248PSTransmitError_Type = Integer32
_MsagH248PSTransmitError_Object = MibScalar
msagH248PSTransmitError = _MsagH248PSTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 6, 9),
    _MsagH248PSTransmitError_Type()
)
msagH248PSTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagH248PSTransmitError.setStatus("current")


class _Calllimitipsthruput_Type(Unsigned32):
    """Custom type calllimitipsthruput based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Calllimitipsthruput_Type.__name__ = "Unsigned32"
_Calllimitipsthruput_Object = MibScalar
calllimitipsthruput = _Calllimitipsthruput_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 19),
    _Calllimitipsthruput_Type()
)
calllimitipsthruput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calllimitipsthruput.setStatus("current")


class _Calllimitnicthruput_Type(Unsigned32):
    """Custom type calllimitnicthruput based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Calllimitnicthruput_Type.__name__ = "Unsigned32"
_Calllimitnicthruput_Object = MibScalar
calllimitnicthruput = _Calllimitnicthruput_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 20),
    _Calllimitnicthruput_Type()
)
calllimitnicthruput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calllimitnicthruput.setStatus("current")


class _Calllimitcalllimit_Type(Integer32):
    """Custom type calllimitcalllimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("limitByMg", 1),
          ("limitByMgc", 2),
          ("notLimit", 3))
    )


_Calllimitcalllimit_Type.__name__ = "Integer32"
_Calllimitcalllimit_Object = MibScalar
calllimitcalllimit = _Calllimitcalllimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 21),
    _Calllimitcalllimit_Type()
)
calllimitcalllimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calllimitcalllimit.setStatus("current")


class _Calllimitcpubusylimit_Type(Integer32):
    """Custom type calllimitcpubusylimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allwaysLimit", 1),
          ("notLimit", 2))
    )


_Calllimitcpubusylimit_Type.__name__ = "Integer32"
_Calllimitcpubusylimit_Object = MibScalar
calllimitcpubusylimit = _Calllimitcpubusylimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 22),
    _Calllimitcpubusylimit_Type()
)
calllimitcpubusylimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calllimitcpubusylimit.setStatus("current")


class _Calllimitupportlimit_Type(Integer32):
    """Custom type calllimitupportlimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allwaysLimit", 1),
          ("notLimit", 2))
    )


_Calllimitupportlimit_Type.__name__ = "Integer32"
_Calllimitupportlimit_Object = MibScalar
calllimitupportlimit = _Calllimitupportlimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 23),
    _Calllimitupportlimit_Type()
)
calllimitupportlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calllimitupportlimit.setStatus("current")


class _Calllimitipslimit_Type(Integer32):
    """Custom type calllimitipslimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allwaysLimit", 1),
          ("notLimit", 2))
    )


_Calllimitipslimit_Type.__name__ = "Integer32"
_Calllimitipslimit_Object = MibScalar
calllimitipslimit = _Calllimitipslimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 24),
    _Calllimitipslimit_Type()
)
calllimitipslimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calllimitipslimit.setStatus("current")


class _Calllimitniclimit_Type(Integer32):
    """Custom type calllimitniclimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allwaysLimit", 1),
          ("notLimit", 2))
    )


_Calllimitniclimit_Type.__name__ = "Integer32"
_Calllimitniclimit_Object = MibScalar
calllimitniclimit = _Calllimitniclimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 25),
    _Calllimitniclimit_Type()
)
calllimitniclimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calllimitniclimit.setStatus("current")
_MsagTrap_ObjectIdentity = ObjectIdentity
msagTrap = _MsagTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10)
)
_MsagTrapId_ObjectIdentity = ObjectIdentity
msagTrapId = _MsagTrapId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1)
)
_MsagTrapObjectMib_ObjectIdentity = ObjectIdentity
msagTrapObjectMib = _MsagTrapObjectMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2)
)


class _ZxAnNarrowbandResCfgType_Type(Integer32):
    """Custom type zxAnNarrowbandResCfgType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("tone", 2),
          ("ipsMprb", 3),
          ("conference", 4),
          ("ipsSixty", 5),
          ("msdti", 6),
          ("odtT1", 7),
          ("notSourceType", 8))
    )


_ZxAnNarrowbandResCfgType_Type.__name__ = "Integer32"
_ZxAnNarrowbandResCfgType_Object = MibScalar
zxAnNarrowbandResCfgType = _ZxAnNarrowbandResCfgType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 1),
    _ZxAnNarrowbandResCfgType_Type()
)
zxAnNarrowbandResCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnNarrowbandResCfgType.setStatus("current")


class _ZxAnNarrowbandResActType_Type(DisplayString):
    """Custom type zxAnNarrowbandResActType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnNarrowbandResActType_Type.__name__ = "DisplayString"
_ZxAnNarrowbandResActType_Object = MibScalar
zxAnNarrowbandResActType = _ZxAnNarrowbandResActType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 2),
    _ZxAnNarrowbandResActType_Type()
)
zxAnNarrowbandResActType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnNarrowbandResActType.setStatus("current")
_ZxAnIpsResourceAlarmReason_Type = Integer32
_ZxAnIpsResourceAlarmReason_Object = MibScalar
zxAnIpsResourceAlarmReason = _ZxAnIpsResourceAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 3),
    _ZxAnIpsResourceAlarmReason_Type()
)
zxAnIpsResourceAlarmReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIpsResourceAlarmReason.setStatus("current")
_ZxAnTrapRack_Type = Integer32
_ZxAnTrapRack_Object = MibScalar
zxAnTrapRack = _ZxAnTrapRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 4),
    _ZxAnTrapRack_Type()
)
zxAnTrapRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnTrapRack.setStatus("current")
_ZxAnTrapShelf_Type = Integer32
_ZxAnTrapShelf_Object = MibScalar
zxAnTrapShelf = _ZxAnTrapShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 5),
    _ZxAnTrapShelf_Type()
)
zxAnTrapShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnTrapShelf.setStatus("current")
_ZxAnTrapSlot_Type = Integer32
_ZxAnTrapSlot_Object = MibScalar
zxAnTrapSlot = _ZxAnTrapSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 6),
    _ZxAnTrapSlot_Type()
)
zxAnTrapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnTrapSlot.setStatus("current")
_ZxAnTrapUnit_Type = Integer32
_ZxAnTrapUnit_Object = MibScalar
zxAnTrapUnit = _ZxAnTrapUnit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 7),
    _ZxAnTrapUnit_Type()
)
zxAnTrapUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnTrapUnit.setStatus("current")
_ZxAnTrapSunit_Type = Integer32
_ZxAnTrapSunit_Object = MibScalar
zxAnTrapSunit = _ZxAnTrapSunit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 8),
    _ZxAnTrapSunit_Type()
)
zxAnTrapSunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnTrapSunit.setStatus("current")
_ZxAnTrapPort_Type = Integer32
_ZxAnTrapPort_Object = MibScalar
zxAnTrapPort = _ZxAnTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 9),
    _ZxAnTrapPort_Type()
)
zxAnTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnTrapPort.setStatus("current")
_MsagTrapReason_Type = Integer32
_MsagTrapReason_Object = MibScalar
msagTrapReason = _MsagTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 10),
    _MsagTrapReason_Type()
)
msagTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapReason.setStatus("current")
_MsagTrapLinkState_Type = Integer32
_MsagTrapLinkState_Object = MibScalar
msagTrapLinkState = _MsagTrapLinkState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 11),
    _MsagTrapLinkState_Type()
)
msagTrapLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapLinkState.setStatus("current")
_MsagTrapMgcNo_Type = Integer32
_MsagTrapMgcNo_Object = MibScalar
msagTrapMgcNo = _MsagTrapMgcNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 12),
    _MsagTrapMgcNo_Type()
)
msagTrapMgcNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapMgcNo.setStatus("current")
_MsagTrapSLN_Type = Integer32
_MsagTrapSLN_Object = MibScalar
msagTrapSLN = _MsagTrapSLN_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 13),
    _MsagTrapSLN_Type()
)
msagTrapSLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapSLN.setStatus("current")
_MsagTrapFlag_Type = Integer32
_MsagTrapFlag_Object = MibScalar
msagTrapFlag = _MsagTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 14),
    _MsagTrapFlag_Type()
)
msagTrapFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapFlag.setStatus("current")
_MsagTrapErrcode_Type = Integer32
_MsagTrapErrcode_Object = MibScalar
msagTrapErrcode = _MsagTrapErrcode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 15),
    _MsagTrapErrcode_Type()
)
msagTrapErrcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapErrcode.setStatus("current")
_MsagTrapIpAddress_Type = Integer32
_MsagTrapIpAddress_Object = MibScalar
msagTrapIpAddress = _MsagTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 16),
    _MsagTrapIpAddress_Type()
)
msagTrapIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapIpAddress.setStatus("current")
_MsagTrapBETime_Type = Integer32
_MsagTrapBETime_Object = MibScalar
msagTrapBETime = _MsagTrapBETime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 17),
    _MsagTrapBETime_Type()
)
msagTrapBETime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapBETime.setStatus("current")


class _ZxAnTrapInfoType_Type(Integer32):
    """Custom type zxAnTrapInfoType based on Integer32"""
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
        *(("ei2", 1),
          ("ei3", 2),
          ("lsl", 3),
          ("rsy", 4),
          ("fj", 5))
    )


_ZxAnTrapInfoType_Type.__name__ = "Integer32"
_ZxAnTrapInfoType_Object = MibScalar
zxAnTrapInfoType = _ZxAnTrapInfoType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 18),
    _ZxAnTrapInfoType_Type()
)
zxAnTrapInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnTrapInfoType.setStatus("current")
_MsagTrapUnitNo_Type = Integer32
_MsagTrapUnitNo_Object = MibScalar
msagTrapUnitNo = _MsagTrapUnitNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 19),
    _MsagTrapUnitNo_Type()
)
msagTrapUnitNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapUnitNo.setStatus("current")
_MsagTrapPcmNo_Type = Integer32
_MsagTrapPcmNo_Object = MibScalar
msagTrapPcmNo = _MsagTrapPcmNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 20),
    _MsagTrapPcmNo_Type()
)
msagTrapPcmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapPcmNo.setStatus("current")
_MsagTrapReasionValue_Type = Integer32
_MsagTrapReasionValue_Object = MibScalar
msagTrapReasionValue = _MsagTrapReasionValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 21),
    _MsagTrapReasionValue_Type()
)
msagTrapReasionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapReasionValue.setStatus("current")
_MsagTrapRack_Type = Integer32
_MsagTrapRack_Object = MibScalar
msagTrapRack = _MsagTrapRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 22),
    _MsagTrapRack_Type()
)
msagTrapRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapRack.setStatus("current")
_MsagTrapShelf_Type = Integer32
_MsagTrapShelf_Object = MibScalar
msagTrapShelf = _MsagTrapShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 23),
    _MsagTrapShelf_Type()
)
msagTrapShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapShelf.setStatus("current")
_MsagTrapSlot_Type = Integer32
_MsagTrapSlot_Object = MibScalar
msagTrapSlot = _MsagTrapSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 24),
    _MsagTrapSlot_Type()
)
msagTrapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapSlot.setStatus("current")
_MsagTrapV5InterId_Type = Integer32
_MsagTrapV5InterId_Object = MibScalar
msagTrapV5InterId = _MsagTrapV5InterId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 25),
    _MsagTrapV5InterId_Type()
)
msagTrapV5InterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapV5InterId.setStatus("current")
_MsagTrapDLProType_Type = Integer32
_MsagTrapDLProType_Object = MibScalar
msagTrapDLProType = _MsagTrapDLProType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 26),
    _MsagTrapDLProType_Type()
)
msagTrapDLProType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapDLProType.setStatus("current")
_MsagTrapCurEvent_Type = Integer32
_MsagTrapCurEvent_Object = MibScalar
msagTrapCurEvent = _MsagTrapCurEvent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 27),
    _MsagTrapCurEvent_Type()
)
msagTrapCurEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapCurEvent.setStatus("current")
_MsagTrapCurState_Type = Integer32
_MsagTrapCurState_Object = MibScalar
msagTrapCurState = _MsagTrapCurState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 28),
    _MsagTrapCurState_Type()
)
msagTrapCurState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapCurState.setStatus("current")
_MsagTrapParaLinkId_Type = Integer32
_MsagTrapParaLinkId_Object = MibScalar
msagTrapParaLinkId = _MsagTrapParaLinkId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 29),
    _MsagTrapParaLinkId_Type()
)
msagTrapParaLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapParaLinkId.setStatus("current")
_MsagQosAlarmType_Type = Integer32
_MsagQosAlarmType_Object = MibScalar
msagQosAlarmType = _MsagQosAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 30),
    _MsagQosAlarmType_Type()
)
msagQosAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagQosAlarmType.setStatus("current")
_MsagQosAlarmDetail_Type = Integer32
_MsagQosAlarmDetail_Object = MibScalar
msagQosAlarmDetail = _MsagQosAlarmDetail_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 31),
    _MsagQosAlarmDetail_Type()
)
msagQosAlarmDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagQosAlarmDetail.setStatus("current")
_MsagTrapPort_Type = Integer32
_MsagTrapPort_Object = MibScalar
msagTrapPort = _MsagTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 2, 32),
    _MsagTrapPort_Type()
)
msagTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagTrapPort.setStatus("current")
_ZxAnVoipCallTest_ObjectIdentity = ObjectIdentity
zxAnVoipCallTest = _ZxAnVoipCallTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12)
)
_ZxAnVoipCalleeTestTable_Object = MibTable
zxAnVoipCalleeTestTable = _ZxAnVoipCalleeTestTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1)
)
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestTable.setStatus("current")
_ZxAnVoipCalleeTestEntry_Object = MibTableRow
zxAnVoipCalleeTestEntry = _ZxAnVoipCalleeTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1)
)
zxAnVoipCalleeTestEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCalleeTestRack"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCalleeTestShelf"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCalleeTestSlot"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCalleeTestPort"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCalleeTestOnu"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCalleeTestCircuitType"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCalleeTestLogicalId"),
)
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestEntry.setStatus("current")
_ZxAnVoipCalleeTestRack_Type = Integer32
_ZxAnVoipCalleeTestRack_Object = MibTableColumn
zxAnVoipCalleeTestRack = _ZxAnVoipCalleeTestRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 1),
    _ZxAnVoipCalleeTestRack_Type()
)
zxAnVoipCalleeTestRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestRack.setStatus("current")
_ZxAnVoipCalleeTestShelf_Type = Integer32
_ZxAnVoipCalleeTestShelf_Object = MibTableColumn
zxAnVoipCalleeTestShelf = _ZxAnVoipCalleeTestShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 2),
    _ZxAnVoipCalleeTestShelf_Type()
)
zxAnVoipCalleeTestShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestShelf.setStatus("current")
_ZxAnVoipCalleeTestSlot_Type = Integer32
_ZxAnVoipCalleeTestSlot_Object = MibTableColumn
zxAnVoipCalleeTestSlot = _ZxAnVoipCalleeTestSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 3),
    _ZxAnVoipCalleeTestSlot_Type()
)
zxAnVoipCalleeTestSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestSlot.setStatus("current")
_ZxAnVoipCalleeTestPort_Type = Integer32
_ZxAnVoipCalleeTestPort_Object = MibTableColumn
zxAnVoipCalleeTestPort = _ZxAnVoipCalleeTestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 4),
    _ZxAnVoipCalleeTestPort_Type()
)
zxAnVoipCalleeTestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestPort.setStatus("current")
_ZxAnVoipCalleeTestOnu_Type = Integer32
_ZxAnVoipCalleeTestOnu_Object = MibTableColumn
zxAnVoipCalleeTestOnu = _ZxAnVoipCalleeTestOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 5),
    _ZxAnVoipCalleeTestOnu_Type()
)
zxAnVoipCalleeTestOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestOnu.setStatus("current")


class _ZxAnVoipCalleeTestCircuitType_Type(Integer32):
    """Custom type zxAnVoipCalleeTestCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              11)
        )
    )
    namedValues = NamedValues(
        *(("physicalPort", 1),
          ("bridgePort", 2),
          ("onu", 3),
          ("gemportOrLlid", 4),
          ("onuUni", 5),
          ("servicePort", 11))
    )


_ZxAnVoipCalleeTestCircuitType_Type.__name__ = "Integer32"
_ZxAnVoipCalleeTestCircuitType_Object = MibTableColumn
zxAnVoipCalleeTestCircuitType = _ZxAnVoipCalleeTestCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 6),
    _ZxAnVoipCalleeTestCircuitType_Type()
)
zxAnVoipCalleeTestCircuitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestCircuitType.setStatus("current")
_ZxAnVoipCalleeTestLogicalId_Type = ObjectIdentifier
_ZxAnVoipCalleeTestLogicalId_Object = MibTableColumn
zxAnVoipCalleeTestLogicalId = _ZxAnVoipCalleeTestLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 7),
    _ZxAnVoipCalleeTestLogicalId_Type()
)
zxAnVoipCalleeTestLogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestLogicalId.setStatus("current")


class _ZxAnVoipCalleeTestAction_Type(Integer32):
    """Custom type zxAnVoipCalleeTestAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_ZxAnVoipCalleeTestAction_Type.__name__ = "Integer32"
_ZxAnVoipCalleeTestAction_Object = MibTableColumn
zxAnVoipCalleeTestAction = _ZxAnVoipCalleeTestAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 8),
    _ZxAnVoipCalleeTestAction_Type()
)
zxAnVoipCalleeTestAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestAction.setStatus("current")


class _ZxAnVoipCalleeTestTimeout_Type(Integer32):
    """Custom type zxAnVoipCalleeTestTimeout based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_ZxAnVoipCalleeTestTimeout_Type.__name__ = "Integer32"
_ZxAnVoipCalleeTestTimeout_Object = MibTableColumn
zxAnVoipCalleeTestTimeout = _ZxAnVoipCalleeTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 9),
    _ZxAnVoipCalleeTestTimeout_Type()
)
zxAnVoipCalleeTestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestTimeout.setUnits("seconds")


class _ZxAnVoipCalleeTestStatus_Type(Integer32):
    """Custom type zxAnVoipCalleeTestStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnVoipCalleeTestStatus_Type.__name__ = "Integer32"
_ZxAnVoipCalleeTestStatus_Object = MibTableColumn
zxAnVoipCalleeTestStatus = _ZxAnVoipCalleeTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 10),
    _ZxAnVoipCalleeTestStatus_Type()
)
zxAnVoipCalleeTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestStatus.setStatus("current")


class _ZxAnVoipCalleeTestPortStatus_Type(Integer32):
    """Custom type zxAnVoipCalleeTestPortStatus based on Integer32"""
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
        *(("idle", 1),
          ("ringing", 2),
          ("offHook", 3),
          ("connected", 4),
          ("busyTone", 5),
          ("onHook", 6),
          ("testEnd", 7))
    )


_ZxAnVoipCalleeTestPortStatus_Type.__name__ = "Integer32"
_ZxAnVoipCalleeTestPortStatus_Object = MibTableColumn
zxAnVoipCalleeTestPortStatus = _ZxAnVoipCalleeTestPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 11),
    _ZxAnVoipCalleeTestPortStatus_Type()
)
zxAnVoipCalleeTestPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestPortStatus.setStatus("current")


class _ZxAnVoipCalleeTestFailReason_Type(Integer32):
    """Custom type zxAnVoipCalleeTestFailReason based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("noRing", 2),
          ("noUpstreamVoice", 3),
          ("noDownstreamVoice", 4),
          ("noBidirectionVoice", 5),
          ("ringReleasedEarly", 6),
          ("noDigit", 7),
          ("wrongDigit", 8))
    )


_ZxAnVoipCalleeTestFailReason_Type.__name__ = "Integer32"
_ZxAnVoipCalleeTestFailReason_Object = MibTableColumn
zxAnVoipCalleeTestFailReason = _ZxAnVoipCalleeTestFailReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 12),
    _ZxAnVoipCalleeTestFailReason_Type()
)
zxAnVoipCalleeTestFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestFailReason.setStatus("current")


class _ZxAnVoipCalleeTestFailDetail_Type(DisplayString):
    """Custom type zxAnVoipCalleeTestFailDetail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnVoipCalleeTestFailDetail_Type.__name__ = "DisplayString"
_ZxAnVoipCalleeTestFailDetail_Object = MibTableColumn
zxAnVoipCalleeTestFailDetail = _ZxAnVoipCalleeTestFailDetail_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 13),
    _ZxAnVoipCalleeTestFailDetail_Type()
)
zxAnVoipCalleeTestFailDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestFailDetail.setStatus("current")
_ZxAnVoipCalleeTestRowStatus_Type = RowStatus
_ZxAnVoipCalleeTestRowStatus_Object = MibTableColumn
zxAnVoipCalleeTestRowStatus = _ZxAnVoipCalleeTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 1, 1, 50),
    _ZxAnVoipCalleeTestRowStatus_Type()
)
zxAnVoipCalleeTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipCalleeTestRowStatus.setStatus("current")
_ZxAnVoipCallerTestTable_Object = MibTable
zxAnVoipCallerTestTable = _ZxAnVoipCallerTestTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2)
)
if mibBuilder.loadTexts:
    zxAnVoipCallerTestTable.setStatus("current")
_ZxAnVoipCallerTestEntry_Object = MibTableRow
zxAnVoipCallerTestEntry = _ZxAnVoipCallerTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1)
)
zxAnVoipCallerTestEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCallerTestRack"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCallerTestShelf"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCallerTestSlot"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCallerTestPort"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCallerTestOnu"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCallerTestCircuitType"),
    (0, "ZTE-AN-VOIP-BASE-MIB", "zxAnVoipCallerTestLogicalId"),
)
if mibBuilder.loadTexts:
    zxAnVoipCallerTestEntry.setStatus("current")
_ZxAnVoipCallerTestRack_Type = Integer32
_ZxAnVoipCallerTestRack_Object = MibTableColumn
zxAnVoipCallerTestRack = _ZxAnVoipCallerTestRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 1),
    _ZxAnVoipCallerTestRack_Type()
)
zxAnVoipCallerTestRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestRack.setStatus("current")
_ZxAnVoipCallerTestShelf_Type = Integer32
_ZxAnVoipCallerTestShelf_Object = MibTableColumn
zxAnVoipCallerTestShelf = _ZxAnVoipCallerTestShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 2),
    _ZxAnVoipCallerTestShelf_Type()
)
zxAnVoipCallerTestShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestShelf.setStatus("current")
_ZxAnVoipCallerTestSlot_Type = Integer32
_ZxAnVoipCallerTestSlot_Object = MibTableColumn
zxAnVoipCallerTestSlot = _ZxAnVoipCallerTestSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 3),
    _ZxAnVoipCallerTestSlot_Type()
)
zxAnVoipCallerTestSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestSlot.setStatus("current")
_ZxAnVoipCallerTestPort_Type = Integer32
_ZxAnVoipCallerTestPort_Object = MibTableColumn
zxAnVoipCallerTestPort = _ZxAnVoipCallerTestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 4),
    _ZxAnVoipCallerTestPort_Type()
)
zxAnVoipCallerTestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestPort.setStatus("current")
_ZxAnVoipCallerTestOnu_Type = Integer32
_ZxAnVoipCallerTestOnu_Object = MibTableColumn
zxAnVoipCallerTestOnu = _ZxAnVoipCallerTestOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 5),
    _ZxAnVoipCallerTestOnu_Type()
)
zxAnVoipCallerTestOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestOnu.setStatus("current")


class _ZxAnVoipCallerTestCircuitType_Type(Integer32):
    """Custom type zxAnVoipCallerTestCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              11)
        )
    )
    namedValues = NamedValues(
        *(("physicalPort", 1),
          ("bridgePort", 2),
          ("onu", 3),
          ("gemportOrLlid", 4),
          ("onuUni", 5),
          ("servicePort", 11))
    )


_ZxAnVoipCallerTestCircuitType_Type.__name__ = "Integer32"
_ZxAnVoipCallerTestCircuitType_Object = MibTableColumn
zxAnVoipCallerTestCircuitType = _ZxAnVoipCallerTestCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 6),
    _ZxAnVoipCallerTestCircuitType_Type()
)
zxAnVoipCallerTestCircuitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestCircuitType.setStatus("current")
_ZxAnVoipCallerTestLogicalId_Type = ObjectIdentifier
_ZxAnVoipCallerTestLogicalId_Object = MibTableColumn
zxAnVoipCallerTestLogicalId = _ZxAnVoipCallerTestLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 7),
    _ZxAnVoipCallerTestLogicalId_Type()
)
zxAnVoipCallerTestLogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestLogicalId.setStatus("current")


class _ZxAnVoipCallerTestAction_Type(Integer32):
    """Custom type zxAnVoipCallerTestAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_ZxAnVoipCallerTestAction_Type.__name__ = "Integer32"
_ZxAnVoipCallerTestAction_Object = MibTableColumn
zxAnVoipCallerTestAction = _ZxAnVoipCallerTestAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 8),
    _ZxAnVoipCallerTestAction_Type()
)
zxAnVoipCallerTestAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestAction.setStatus("current")


class _ZxAnVoipCallerTestTimeout_Type(Integer32):
    """Custom type zxAnVoipCallerTestTimeout based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_ZxAnVoipCallerTestTimeout_Type.__name__ = "Integer32"
_ZxAnVoipCallerTestTimeout_Object = MibTableColumn
zxAnVoipCallerTestTimeout = _ZxAnVoipCallerTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 9),
    _ZxAnVoipCallerTestTimeout_Type()
)
zxAnVoipCallerTestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestTimeout.setUnits("seconds")


class _ZxAnVoipCallerTestDialedNumber_Type(DisplayString):
    """Custom type zxAnVoipCallerTestDialedNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ZxAnVoipCallerTestDialedNumber_Type.__name__ = "DisplayString"
_ZxAnVoipCallerTestDialedNumber_Object = MibTableColumn
zxAnVoipCallerTestDialedNumber = _ZxAnVoipCallerTestDialedNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 10),
    _ZxAnVoipCallerTestDialedNumber_Type()
)
zxAnVoipCallerTestDialedNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestDialedNumber.setStatus("current")


class _ZxAnVoipCallerTestStatus_Type(Integer32):
    """Custom type zxAnVoipCallerTestStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4),
          ("notForced", 5))
    )


_ZxAnVoipCallerTestStatus_Type.__name__ = "Integer32"
_ZxAnVoipCallerTestStatus_Object = MibTableColumn
zxAnVoipCallerTestStatus = _ZxAnVoipCallerTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 11),
    _ZxAnVoipCallerTestStatus_Type()
)
zxAnVoipCallerTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestStatus.setStatus("current")


class _ZxAnVoipCallerTestPortStatus_Type(Integer32):
    """Custom type zxAnVoipCallerTestPortStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("offHook", 2),
          ("dialTone", 3),
          ("receiveNumber", 4),
          ("receiveEnd", 5),
          ("ringBackTone", 6),
          ("connected", 7),
          ("busyTone", 8),
          ("onHook", 9),
          ("testEnd", 10))
    )


_ZxAnVoipCallerTestPortStatus_Type.__name__ = "Integer32"
_ZxAnVoipCallerTestPortStatus_Object = MibTableColumn
zxAnVoipCallerTestPortStatus = _ZxAnVoipCallerTestPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 12),
    _ZxAnVoipCallerTestPortStatus_Type()
)
zxAnVoipCallerTestPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestPortStatus.setStatus("current")


class _ZxAnVoipCallerTestFailReason_Type(Integer32):
    """Custom type zxAnVoipCallerTestFailReason based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("noDialTone", 2),
          ("noRingBack", 3),
          ("noAnswer", 4),
          ("noUpstreamVoice", 5),
          ("noDownstreamVoice", 6),
          ("noBidirectionVoice", 7),
          ("sipTestFailed", 8),
          ("noDigit", 9),
          ("wrongDigit", 10))
    )


_ZxAnVoipCallerTestFailReason_Type.__name__ = "Integer32"
_ZxAnVoipCallerTestFailReason_Object = MibTableColumn
zxAnVoipCallerTestFailReason = _ZxAnVoipCallerTestFailReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 13),
    _ZxAnVoipCallerTestFailReason_Type()
)
zxAnVoipCallerTestFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestFailReason.setStatus("current")


class _ZxAnVoipCallerTestFailDetail_Type(DisplayString):
    """Custom type zxAnVoipCallerTestFailDetail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnVoipCallerTestFailDetail_Type.__name__ = "DisplayString"
_ZxAnVoipCallerTestFailDetail_Object = MibTableColumn
zxAnVoipCallerTestFailDetail = _ZxAnVoipCallerTestFailDetail_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 14),
    _ZxAnVoipCallerTestFailDetail_Type()
)
zxAnVoipCallerTestFailDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestFailDetail.setStatus("current")


class _ZxAnVoipCallerTestSipFailReason_Type(Integer32):
    """Custom type zxAnVoipCallerTestSipFailReason based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("inviteOkButNoBearerData", 1),
          ("callTimeoutNo200Ok", 2),
          ("noResponseToInvite", 3),
          ("errorCodeAndReasonPhrase", 4),
          ("callCancelledByServer", 5),
          ("callCancelledByOnt", 6),
          ("lineNotConfigured", 7),
          ("lineNotInValidState", 8),
          ("lineNotRegistered", 9),
          ("notchFiltersRequired", 10),
          ("dialToneTestFailure", 11))
    )


_ZxAnVoipCallerTestSipFailReason_Type.__name__ = "Integer32"
_ZxAnVoipCallerTestSipFailReason_Object = MibTableColumn
zxAnVoipCallerTestSipFailReason = _ZxAnVoipCallerTestSipFailReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 15),
    _ZxAnVoipCallerTestSipFailReason_Type()
)
zxAnVoipCallerTestSipFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestSipFailReason.setStatus("current")


class _ZxAnVoipCallerTestSipErrorCode_Type(Integer32):
    """Custom type zxAnVoipCallerTestSipErrorCode based on Integer32"""
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
        *(("unauthorized", 1),
          ("forbidden", 2),
          ("notFound", 3),
          ("proxyAuthenticationRequired", 4),
          ("requestTimeout", 5),
          ("temporarilyUnavailable", 6),
          ("addressIncomplete", 7),
          ("busyHere", 8),
          ("requestTerminated", 9),
          ("notAcceptableHere", 10),
          ("serverInternalError", 11),
          ("serviceUnavailable", 12),
          ("serverTimeout", 13))
    )


_ZxAnVoipCallerTestSipErrorCode_Type.__name__ = "Integer32"
_ZxAnVoipCallerTestSipErrorCode_Object = MibTableColumn
zxAnVoipCallerTestSipErrorCode = _ZxAnVoipCallerTestSipErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 16),
    _ZxAnVoipCallerTestSipErrorCode_Type()
)
zxAnVoipCallerTestSipErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestSipErrorCode.setStatus("current")


class _ZxAnVoipCallerTestSipDelay_Type(Integer32):
    """Custom type zxAnVoipCallerTestSipDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnVoipCallerTestSipDelay_Type.__name__ = "Integer32"
_ZxAnVoipCallerTestSipDelay_Object = MibTableColumn
zxAnVoipCallerTestSipDelay = _ZxAnVoipCallerTestSipDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 17),
    _ZxAnVoipCallerTestSipDelay_Type()
)
zxAnVoipCallerTestSipDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestSipDelay.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestSipDelay.setUnits("0.1second")


class _ZxAnVoipCallerTestMode_Type(Integer32):
    """Custom type zxAnVoipCallerTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interactive", 1),
          ("nonInteractive", 2))
    )


_ZxAnVoipCallerTestMode_Type.__name__ = "Integer32"
_ZxAnVoipCallerTestMode_Object = MibTableColumn
zxAnVoipCallerTestMode = _ZxAnVoipCallerTestMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 18),
    _ZxAnVoipCallerTestMode_Type()
)
zxAnVoipCallerTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestMode.setStatus("current")
_ZxAnVoipCallerTestRowStatus_Type = RowStatus
_ZxAnVoipCallerTestRowStatus_Object = MibTableColumn
zxAnVoipCallerTestRowStatus = _ZxAnVoipCallerTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 12, 2, 1, 50),
    _ZxAnVoipCallerTestRowStatus_Type()
)
zxAnVoipCallerTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipCallerTestRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

zxAnNarrowbandResAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 1)
)
zxAnNarrowbandResAvailable.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnNarrowbandResCfgType"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnNarrowbandResActType"))
)
if mibBuilder.loadTexts:
    zxAnNarrowbandResAvailable.setStatus(
        "current"
    )

zxAnNarrowbandResUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 2)
)
zxAnNarrowbandResUnavailable.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnNarrowbandResCfgType"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnNarrowbandResActType"))
)
if mibBuilder.loadTexts:
    zxAnNarrowbandResUnavailable.setStatus(
        "current"
    )

zxAnIpsResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 3)
)
zxAnIpsResource.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnIpsResourceAlarmReason"),
        ("ZTE-AN-VOIP-BASE-MIB", "a200ipsThreshold"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnIpsUsage"))
)
if mibBuilder.loadTexts:
    zxAnIpsResource.setStatus(
        "current"
    )

zxAnIpsResourceRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 4)
)
zxAnIpsResourceRestore.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnIpsResourceAlarmReason"),
        ("ZTE-AN-VOIP-BASE-MIB", "a200ipsThreshold"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnIpsUsage"))
)
if mibBuilder.loadTexts:
    zxAnIpsResourceRestore.setStatus(
        "current"
    )

zxAnIpsChannelFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 5)
)
zxAnIpsChannelFault.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapUnit"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSunit"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnIpsChannelFault.setStatus(
        "current"
    )

zxAnIpsChannelFaultRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 6)
)
zxAnIpsChannelFaultRestore.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapUnit"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSunit"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnIpsChannelFaultRestore.setStatus(
        "current"
    )

zxMsagH248Link = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 7)
)
zxMsagH248Link.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "msagTrapReason"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapLinkState"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapMgcNo"))
)
if mibBuilder.loadTexts:
    zxMsagH248Link.setStatus(
        "current"
    )

zxMsagH248LinkRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 8)
)
zxMsagH248LinkRestore.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "msagTrapReason"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapLinkState"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapMgcNo"))
)
if mibBuilder.loadTexts:
    zxMsagH248LinkRestore.setStatus(
        "current"
    )

zxMsagH248ErrorCode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 9)
)
zxMsagH248ErrorCode.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "msagTrapErrcode"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxMsagH248ErrorCode.setStatus(
        "current"
    )

zxAnDlccNT1Los = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 10)
)
zxAnDlccNT1Los.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapInfoType"))
)
if mibBuilder.loadTexts:
    zxAnDlccNT1Los.setStatus(
        "current"
    )

zxMsagMgcpLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 11)
)
zxMsagMgcpLink.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "msagTrapReason"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapLinkState"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapMgcNo"))
)
if mibBuilder.loadTexts:
    zxMsagMgcpLink.setStatus(
        "current"
    )

zxMsagMgcpLinkRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 12)
)
zxMsagMgcpLinkRestore.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "msagTrapReason"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapLinkState"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapMgcNo"))
)
if mibBuilder.loadTexts:
    zxMsagMgcpLinkRestore.setStatus(
        "current"
    )

zxMsagMgcpAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 13)
)
zxMsagMgcpAbnormal.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "msagTrapReason"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapLinkState"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapMgcNo"))
)
if mibBuilder.loadTexts:
    zxMsagMgcpAbnormal.setStatus(
        "current"
    )

zxMsagMgcpAbnormalRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 14)
)
zxMsagMgcpAbnormalRestore.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "msagTrapReason"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapLinkState"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapMgcNo"))
)
if mibBuilder.loadTexts:
    zxMsagMgcpAbnormalRestore.setStatus(
        "current"
    )

zxMsagV5Pcm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 15)
)
zxMsagV5Pcm.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "msagTrapUnitNo"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapPcmNo"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapReasionValue"))
)
if mibBuilder.loadTexts:
    zxMsagV5Pcm.setStatus(
        "current"
    )

zxMsagV5PcmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 16)
)
zxMsagV5PcmRestore.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "msagTrapUnitNo"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapPcmNo"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapReasionValue"))
)
if mibBuilder.loadTexts:
    zxMsagV5PcmRestore.setStatus(
        "current"
    )

zxMsagV5Proto = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 17)
)
zxMsagV5Proto.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "msagTrapV5InterId"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapDLProType"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapCurEvent"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapCurState"))
)
if mibBuilder.loadTexts:
    zxMsagV5Proto.setStatus(
        "current"
    )

zxMsagV5ProtoRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 18)
)
zxMsagV5ProtoRestore.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "msagTrapV5InterId"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapDLProType"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapCurEvent"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapCurState"))
)
if mibBuilder.loadTexts:
    zxMsagV5ProtoRestore.setStatus(
        "current"
    )

zxMsagISDNSctpInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 19)
)
zxMsagISDNSctpInform.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "msagTrapReason"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapParaLinkId"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapIpAddress"))
)
if mibBuilder.loadTexts:
    zxMsagISDNSctpInform.setStatus(
        "current"
    )

zxMsagISDNSctpAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 20)
)
zxMsagISDNSctpAlarm.setObjects(
    ("ZTE-AN-VOIP-BASE-MIB", "msagTrapReason")
)
if mibBuilder.loadTexts:
    zxMsagISDNSctpAlarm.setStatus(
        "current"
    )

zxMsagIUAInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 21)
)
zxMsagIUAInform.setObjects(
    ("ZTE-AN-VOIP-BASE-MIB", "msagTrapReason")
)
if mibBuilder.loadTexts:
    zxMsagIUAInform.setStatus(
        "current"
    )

zxMsagIUAAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 22)
)
zxMsagIUAAlarm.setObjects(
    ("ZTE-AN-VOIP-BASE-MIB", "msagTrapReason")
)
if mibBuilder.loadTexts:
    zxMsagIUAAlarm.setStatus(
        "current"
    )

zxMsagIUAAlarmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 23)
)
zxMsagIUAAlarmRestore.setObjects(
    ("ZTE-AN-VOIP-BASE-MIB", "msagTrapReason")
)
if mibBuilder.loadTexts:
    zxMsagIUAAlarmRestore.setStatus(
        "current"
    )

zxMsagCallAllocMemoryErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 24)
)
zxMsagCallAllocMemoryErrorAlarm.setObjects(
    ("ZTE-AN-VOIP-BASE-MIB", "msagTrapReason")
)
if mibBuilder.loadTexts:
    zxMsagCallAllocMemoryErrorAlarm.setStatus(
        "current"
    )

zxMsagQosPoorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 25)
)
zxMsagQosPoorAlarm.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapUnit"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSunit"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapPort"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagQosAlarmType"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagQosAlarmDetail"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxMsagQosPoorAlarm.setStatus(
        "current"
    )

zxMsagQosPoorRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 26)
)
zxMsagQosPoorRestore.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapUnit"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSunit"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagTrapPort"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagQosAlarmType"),
        ("ZTE-AN-VOIP-BASE-MIB", "msagQosAlarmDetail"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxMsagQosPoorRestore.setStatus(
        "current"
    )

zxAnSlcFreqOffOnHookAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 100)
)
zxAnSlcFreqOffOnHookAlarm.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnSlcFreqOffOnHookAlarm.setStatus(
        "current"
    )

zxAnSlcFreqOffOnHookAlarmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 101)
)
zxAnSlcFreqOffOnHookAlarmRestore.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnSlcFreqOffOnHookAlarmRestore.setStatus(
        "current"
    )

zxAnSlcGroundedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 102)
)
zxAnSlcGroundedAlarm.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnSlcGroundedAlarm.setStatus(
        "current"
    )

zxAnSlcGroundedRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 103)
)
zxAnSlcGroundedRestore.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnSlcGroundedRestore.setStatus(
        "current"
    )

zxAnSlcContactedWithPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 104)
)
zxAnSlcContactedWithPower.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnSlcContactedWithPower.setStatus(
        "current"
    )

zxAnDsx1ProtectionGroupSwapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 105)
)
zxAnDsx1ProtectionGroupSwapped.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnDsx1ProtectionGroupName"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnDsx1MasterDsx1Rack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnDsx1MasterDsx1Shelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnDsx1MasterDsx1Slot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnDsx1MasterDsx1LinkNo"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnDsx1StandbyDsx1Rack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnDsx1StandbyDsx1Shelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnDsx1StandbyDsx1Slot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnDsx1StandbyDsx1LinkNo"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnDsx1CurrWorkingDsx1"))
)
if mibBuilder.loadTexts:
    zxAnDsx1ProtectionGroupSwapped.setStatus(
        "current"
    )

zxAnIsdnUInterfaceLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 106)
)
zxAnIsdnUInterfaceLinkDown.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnIsdnUInterfaceLinkDown.setStatus(
        "current"
    )

zxAnIsdnUInterfaceLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 107)
)
zxAnIsdnUInterfaceLinkUp.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnIsdnUInterfaceLinkUp.setStatus(
        "current"
    )

zxAnSlcContactedWithPowerClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 108)
)
zxAnSlcContactedWithPowerClr.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnSlcContactedWithPowerClr.setStatus(
        "current"
    )

zxAnHwTsUsageAboveThresholdAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 109)
)
zxAnHwTsUsageAboveThresholdAlm.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnHwTimeSlotUsageThreshold"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnHwTimeSlotUsage"))
)
if mibBuilder.loadTexts:
    zxAnHwTsUsageAboveThresholdAlm.setStatus(
        "current"
    )

zxAnHwTsUsageAboveThresholdClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 110)
)
zxAnHwTsUsageAboveThresholdClr.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnHwTimeSlotUsageThreshold"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnHwTimeSlotUsage"))
)
if mibBuilder.loadTexts:
    zxAnHwTsUsageAboveThresholdClr.setStatus(
        "current"
    )

zxAnVoicePortLockoutAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 111)
)
zxAnVoicePortLockoutAlm.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnVoicePortLockoutAlm.setStatus(
        "current"
    )

zxAnVoicePortLockoutClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 112)
)
zxAnVoicePortLockoutClr.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnVoicePortLockoutClr.setStatus(
        "current"
    )

zxAnDdiSubscriberLineBrokenAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 113)
)
zxAnDdiSubscriberLineBrokenAlm.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnDdiSubscriberLineBrokenAlm.setStatus(
        "current"
    )

zxAnDdiSubscriberLineBrokenClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 114)
)
zxAnDdiSubscriberLineBrokenClr.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnDdiSubscriberLineBrokenClr.setStatus(
        "current"
    )

zxAnVoicePortHighAcVoltageAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 115)
)
zxAnVoicePortHighAcVoltageAlm.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnVoicePortHighAcVoltageAlm.setStatus(
        "current"
    )

zxAnVoicePortHighAcVoltageClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 116)
)
zxAnVoicePortHighAcVoltageClr.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnVoicePortHighAcVoltageClr.setStatus(
        "current"
    )

zxAnVoicePortHighDcVoltageAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 117)
)
zxAnVoicePortHighDcVoltageAlm.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnVoicePortHighDcVoltageAlm.setStatus(
        "current"
    )

zxAnVoicePortHighDcVoltageClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 10, 1, 118)
)
zxAnVoicePortHighDcVoltageClr.setObjects(
      *(("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapRack"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapShelf"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapSlot"),
        ("ZTE-AN-VOIP-BASE-MIB", "zxAnTrapPort"))
)
if mibBuilder.loadTexts:
    zxAnVoicePortHighDcVoltageClr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-VOIP-BASE-MIB",
    **{"A200ShelfTypes": A200ShelfTypes,
       "A200BoardTypes": A200BoardTypes,
       "zte": zte,
       "msag": msag,
       "zxAnVoipBaseMib": zxAnVoipBaseMib,
       "msagmajorVersion": msagmajorVersion,
       "msagGlobalConfig": msagGlobalConfig,
       "a200MgCfgTable": a200MgCfgTable,
       "a200MgCfgEntry": a200MgCfgEntry,
       "a200mgid": a200mgid,
       "a200protype": a200protype,
       "a200version": a200version,
       "a200encodetp": a200encodetp,
       "a200mgport": a200mgport,
       "a200translay": a200translay,
       "a200transpro": a200transpro,
       "a200mgDomainName": a200mgDomainName,
       "a200mgInfo": a200mgInfo,
       "a200mgcid1": a200mgcid1,
       "a200mgcid2": a200mgcid2,
       "a200mgcid3": a200mgcid3,
       "a200mgcid4": a200mgcid4,
       "a200selfexchange": a200selfexchange,
       "a200protectcall": a200protectcall,
       "a200disasterprot": a200disasterprot,
       "a200mgRowStatus": a200mgRowStatus,
       "a200tractnum": a200tractnum,
       "a200sdpcho": a200sdpcho,
       "a200retrannum": a200retrannum,
       "a200resdelay": a200resdelay,
       "a200retranmin": a200retranmin,
       "a200lkpttime": a200lkpttime,
       "a200pendtime": a200pendtime,
       "a200pendcount": a200pendcount,
       "a200kprestime": a200kprestime,
       "a200tranidmax": a200tranidmax,
       "a200tranidmin": a200tranidmin,
       "a200rtpFaxPri1": a200rtpFaxPri1,
       "a200rtpFaxPri2": a200rtpFaxPri2,
       "a200subsuspendrtp": a200subsuspendrtp,
       "a200hotlinewithspace": a200hotlinewithspace,
       "a200rtp2833Type": a200rtp2833Type,
       "a200ipsThreshold": a200ipsThreshold,
       "a200congesttime": a200congesttime,
       "a200congesttone": a200congesttone,
       "a200callmatchtype": a200callmatchtype,
       "a200currentmgcid": a200currentmgcid,
       "a200mgSigTos": a200mgSigTos,
       "a200mgPSTNMediaVoiceTos": a200mgPSTNMediaVoiceTos,
       "a200mgPSTNMediaFaxTos": a200mgPSTNMediaFaxTos,
       "a200mgPSTNMediaModemTos": a200mgPSTNMediaModemTos,
       "a200mgPSTNMediaDataTos": a200mgPSTNMediaDataTos,
       "a200mgISDNMediaVoiceTos": a200mgISDNMediaVoiceTos,
       "a200mgISDNMediaFaxTos": a200mgISDNMediaFaxTos,
       "a200mgISDNMediaModemTos": a200mgISDNMediaModemTos,
       "a200mgISDNMediaDataTos": a200mgISDNMediaDataTos,
       "a200ringprofile": a200ringprofile,
       "a200toneprofile": a200toneprofile,
       "a200flashprofile": a200flashprofile,
       "a200chg16kcwidth": a200chg16kcwidth,
       "a200chg16kcinterval": a200chg16kcinterval,
       "a200charge16kcvol": a200charge16kcvol,
       "a200kcflag": a200kcflag,
       "a200ExternalSelfswitchEnable": a200ExternalSelfswitchEnable,
       "zxAnIpsUsage": zxAnIpsUsage,
       "a200MgCallEscapeMode": a200MgCallEscapeMode,
       "a200mgccfgTable": a200mgccfgTable,
       "a200mgccfgEntry": a200mgccfgEntry,
       "a200mgcmgcid": a200mgcmgcid,
       "a200mgctypeid": a200mgctypeid,
       "a200mgcip": a200mgcip,
       "a200mgcport": a200mgcport,
       "a200mgcdomain": a200mgcdomain,
       "a200mgcinfo": a200mgcinfo,
       "a200mgcMD5Info": a200mgcMD5Info,
       "a200mgcRowStatus": a200mgcRowStatus,
       "a200MgcTypeTable": a200MgcTypeTable,
       "a200MgcTypeEntry": a200MgcTypeEntry,
       "a200MgcTypeId": a200MgcTypeId,
       "a200MgcTypeDesc": a200MgcTypeDesc,
       "a200MgcTypeMaxTransPkg": a200MgcTypeMaxTransPkg,
       "a200MgcTypeReasonQuote": a200MgcTypeReasonQuote,
       "a200MgcTypeQueryStatus": a200MgcTypeQueryStatus,
       "a200MgcTypeHeartBeat": a200MgcTypeHeartBeat,
       "a200MgcTypeDmLong": a200MgcTypeDmLong,
       "a200MgcTypeDmShort": a200MgcTypeDmShort,
       "a200MgcTypeDmStart": a200MgcTypeDmStart,
       "a200MgcTypeWithTime": a200MgcTypeWithTime,
       "a200MgcTypeWithDelay": a200MgcTypeWithDelay,
       "a200MgcTypeProfileName": a200MgcTypeProfileName,
       "a200MgcTypeUserOut": a200MgcTypeUserOut,
       "a200MgcTypeAgOut": a200MgcTypeAgOut,
       "a200MgcTypeHeartId": a200MgcTypeHeartId,
       "a200MgcTypeAgRegOldMT": a200MgcTypeAgRegOldMT,
       "a200MgcTypeCanclerror": a200MgcTypeCanclerror,
       "a200MgcTypeRowStatus": a200MgcTypeRowStatus,
       "a200MedNatTable": a200MedNatTable,
       "a200MedNatEntry": a200MedNatEntry,
       "a200mednatIpsRack": a200mednatIpsRack,
       "a200mednatIpsShelf": a200mednatIpsShelf,
       "a200mednatIpsSlot": a200mednatIpsSlot,
       "a200mednatSubCard": a200mednatSubCard,
       "a200mednatNicRack": a200mednatNicRack,
       "a200mednatNicShelf": a200mednatNicShelf,
       "a200mednatNicSlot": a200mednatNicSlot,
       "a200mednatInPhyPort": a200mednatInPhyPort,
       "a200mednatExPhyPort": a200mednatExPhyPort,
       "a200mednatExIp": a200mednatExIp,
       "a200mednatUdpPort": a200mednatUdpPort,
       "a200mednatRowStatus": a200mednatRowStatus,
       "a200natCtrlId": a200natCtrlId,
       "a200QovsTable": a200QovsTable,
       "a200QovsEntry": a200QovsEntry,
       "a200QovsId": a200QovsId,
       "a200QovsLoss": a200QovsLoss,
       "a200QovsDelay": a200QovsDelay,
       "a200QovsJitter": a200QovsJitter,
       "a200QovsRowStatus": a200QovsRowStatus,
       "a200MiscTable": a200MiscTable,
       "a200MiscEntry": a200MiscEntry,
       "a200MiscIndex": a200MiscIndex,
       "a200MiscFlashDelay": a200MiscFlashDelay,
       "a200MiscCalledPartyReanwer": a200MiscCalledPartyReanwer,
       "a200MiscH248BusyStatus": a200MiscH248BusyStatus,
       "a200MiscHowlTone": a200MiscHowlTone,
       "a200MiscH248Short": a200MiscH248Short,
       "a200MiscH248Long": a200MiscH248Long,
       "a200MiscRTPtimer": a200MiscRTPtimer,
       "a200MiscH248RingPattern": a200MiscH248RingPattern,
       "a200MiscCallAlarm": a200MiscCallAlarm,
       "a200MiscInterCallAlarm": a200MiscInterCallAlarm,
       "a200MiscFreshTnet": a200MiscFreshTnet,
       "a200MiscCheckContext": a200MiscCheckContext,
       "a200MiscUpPort": a200MiscUpPort,
       "a200MiscResReportPeriod": a200MiscResReportPeriod,
       "a200MiscAgMustDetOvrLd": a200MiscAgMustDetOvrLd,
       "a200MiscErrReplyInformSSEn": a200MiscErrReplyInformSSEn,
       "a200MiscCookieEchoFormat": a200MiscCookieEchoFormat,
       "a200MiscCheckSumFormat": a200MiscCheckSumFormat,
       "a200MiscIuaIsdnHwFormat": a200MiscIuaIsdnHwFormat,
       "a200DigitMapTable": a200DigitMapTable,
       "a200DigitMapEntry": a200DigitMapEntry,
       "a200DigitMapDas": a200DigitMapDas,
       "a200DigitMapMgid": a200DigitMapMgid,
       "a200DigitMapSrvType": a200DigitMapSrvType,
       "a200DigitMapDgtName": a200DigitMapDgtName,
       "a200DigitMapDgtMap": a200DigitMapDgtMap,
       "a200DigitMapRowStatus": a200DigitMapRowStatus,
       "a200VoipRouteTable": a200VoipRouteTable,
       "a200VoipRouteEntry": a200VoipRouteEntry,
       "a200VoipRouteMgId": a200VoipRouteMgId,
       "a200VoipRouteType": a200VoipRouteType,
       "a200VoipRouteDestIp": a200VoipRouteDestIp,
       "a200VoipRouteDestMask": a200VoipRouteDestMask,
       "a200VoipRouteNexthop": a200VoipRouteNexthop,
       "a200VoipRouteNexthopMac": a200VoipRouteNexthopMac,
       "a200VoipRouteArpTime": a200VoipRouteArpTime,
       "a200VoipRouteRowStatus": a200VoipRouteRowStatus,
       "a200CtlPortTable": a200CtlPortTable,
       "a200CtlPortEntry": a200CtlPortEntry,
       "a200CtlPortCtlId": a200CtlPortCtlId,
       "a200CtlPortInfo": a200CtlPortInfo,
       "a200CtlPortUdpPort": a200CtlPortUdpPort,
       "a200CtlPortRowStatus": a200CtlPortRowStatus,
       "callOptimizeTable": callOptimizeTable,
       "callOptimizeEntry": callOptimizeEntry,
       "calloptIndex": calloptIndex,
       "calloptOpenMsgAck": calloptOpenMsgAck,
       "calloptPlayToneAck": calloptPlayToneAck,
       "calloptSubPriority": calloptSubPriority,
       "calloptNumMax": calloptNumMax,
       "calloptH248MsgAck": calloptH248MsgAck,
       "calloptH248MsgPn": calloptH248MsgPn,
       "calloptH248Statistic": calloptH248Statistic,
       "calloptH248HookOffEvent": calloptH248HookOffEvent,
       "calloptH248HookOnEvent": calloptH248HookOnEvent,
       "calloptServiceAbnormal": calloptServiceAbnormal,
       "calloptMgProtocolErr": calloptMgProtocolErr,
       "calloptMgcProtocolErr": calloptMgcProtocolErr,
       "calloptMgInsideErr": calloptMgInsideErr,
       "calloptHookOffLimiteCycle": calloptHookOffLimiteCycle,
       "calloptHookOffLimiteBlock": calloptHookOffLimiteBlock,
       "calloptHookOffLimiteUnblock": calloptHookOffLimiteUnblock,
       "calloptMgcCallWaitTone": calloptMgcCallWaitTone,
       "calloptToneArea": calloptToneArea,
       "calloptH248LinkBreakTone": calloptH248LinkBreakTone,
       "msagLoadDefaultRingProfile": msagLoadDefaultRingProfile,
       "zxAnVoipInterfaceTable": zxAnVoipInterfaceTable,
       "zxAnVoipInterfaceEntry": zxAnVoipInterfaceEntry,
       "zxAnMgId": zxAnMgId,
       "zxAnVoipCtrlIpAddr": zxAnVoipCtrlIpAddr,
       "zxAnVoipCtrlIpMask": zxAnVoipCtrlIpMask,
       "zxAnVoipMediaIpaddr": zxAnVoipMediaIpaddr,
       "zxAnVoipMediaIpMask": zxAnVoipMediaIpMask,
       "zxAnVoipInterfaceRowStatus": zxAnVoipInterfaceRowStatus,
       "zxAnVoipBaseGlobalObjects": zxAnVoipBaseGlobalObjects,
       "zxAnVoipBaseCapabilities": zxAnVoipBaseCapabilities,
       "zxAnSelfswitchTktObjects": zxAnSelfswitchTktObjects,
       "zxAnSelfswitchTktEnable": zxAnSelfswitchTktEnable,
       "zxAnSelfswitchTktUploadInterval": zxAnSelfswitchTktUploadInterval,
       "zxAnSelfswitchTktSizeThreshold": zxAnSelfswitchTktSizeThreshold,
       "zxAnSelfswitchTelLoadObjects": zxAnSelfswitchTelLoadObjects,
       "zxAnSelfswitchTelLoadFileName": zxAnSelfswitchTelLoadFileName,
       "zxAnSelfswitchTelLoadStatus": zxAnSelfswitchTelLoadStatus,
       "zxAnSelfswitchTelLoadFailReason": zxAnSelfswitchTelLoadFailReason,
       "zxAnVoicePortLockoutTrapEnable": zxAnVoicePortLockoutTrapEnable,
       "zxAnSelfswitchTktFtpTable": zxAnSelfswitchTktFtpTable,
       "zxAnSelfswitchTktFtpEntry": zxAnSelfswitchTktFtpEntry,
       "zxAnSelfswitchTktFtpServerId": zxAnSelfswitchTktFtpServerId,
       "zxAnSelfswitchTktFtpServerIpType": zxAnSelfswitchTktFtpServerIpType,
       "zxAnSelfswitchTktFtpServerIp": zxAnSelfswitchTktFtpServerIp,
       "zxAnSelfswitchTktFtpUserName": zxAnSelfswitchTktFtpUserName,
       "zxAnSelfswitchTktFtpUserPwd": zxAnSelfswitchTktFtpUserPwd,
       "zxAnSelfswitchTktFtpServerPath": zxAnSelfswitchTktFtpServerPath,
       "zxAnSelfswitchTktFtpRowStatus": zxAnSelfswitchTktFtpRowStatus,
       "zxAnDsx1ProtectionGroupTable": zxAnDsx1ProtectionGroupTable,
       "zxAnDsx1ProtectionGroupEntry": zxAnDsx1ProtectionGroupEntry,
       "zxAnDsx1ProtectionGroupId": zxAnDsx1ProtectionGroupId,
       "zxAnDsx1ProtectionGroupName": zxAnDsx1ProtectionGroupName,
       "zxAnDsx1MasterDsx1Rack": zxAnDsx1MasterDsx1Rack,
       "zxAnDsx1MasterDsx1Shelf": zxAnDsx1MasterDsx1Shelf,
       "zxAnDsx1MasterDsx1Slot": zxAnDsx1MasterDsx1Slot,
       "zxAnDsx1MasterDsx1LinkNo": zxAnDsx1MasterDsx1LinkNo,
       "zxAnDsx1StandbyDsx1Rack": zxAnDsx1StandbyDsx1Rack,
       "zxAnDsx1StandbyDsx1Shelf": zxAnDsx1StandbyDsx1Shelf,
       "zxAnDsx1StandbyDsx1Slot": zxAnDsx1StandbyDsx1Slot,
       "zxAnDsx1StandbyDsx1LinkNo": zxAnDsx1StandbyDsx1LinkNo,
       "zxAnDsx1CurrWorkingDsx1": zxAnDsx1CurrWorkingDsx1,
       "zxAnDsx1ProtectionGroupRowStatus": zxAnDsx1ProtectionGroupRowStatus,
       "zxAnHwTimeSlotUsageObjects": zxAnHwTimeSlotUsageObjects,
       "zxAnHwTimeSlotUsageGlobalObjects": zxAnHwTimeSlotUsageGlobalObjects,
       "zxAnHwTimeSlotUsageThreshold": zxAnHwTimeSlotUsageThreshold,
       "zxAnHwTimeSlotUsageTable": zxAnHwTimeSlotUsageTable,
       "zxAnHwTimeSlotUsageEntry": zxAnHwTimeSlotUsageEntry,
       "zxAnHwTimeSlotUsageRack": zxAnHwTimeSlotUsageRack,
       "zxAnHwTimeSlotUsageShelf": zxAnHwTimeSlotUsageShelf,
       "zxAnHwTimeSlotUsage": zxAnHwTimeSlotUsage,
       "msagResource": msagResource,
       "a200SlcTermIDTable": a200SlcTermIDTable,
       "a200SlcTermIDEntry": a200SlcTermIDEntry,
       "a200slcTermIDrackno": a200slcTermIDrackno,
       "a200slcTermIDshelfno": a200slcTermIDshelfno,
       "a200slcTermIDslotno": a200slcTermIDslotno,
       "a200slcTermIDBeginIndex": a200slcTermIDBeginIndex,
       "a200slcTermIDOperSum": a200slcTermIDOperSum,
       "a200slcTermIDTMID": a200slcTermIDTMID,
       "a200slcTermIDType": a200slcTermIDType,
       "a200slcTermIDBeginNo": a200slcTermIDBeginNo,
       "a200slcTermIDDigitLen": a200slcTermIDDigitLen,
       "a200slcTermIDMgId": a200slcTermIDMgId,
       "a200slcTerminationID": a200slcTerminationID,
       "a200slcTermIDRowStatus": a200slcTermIDRowStatus,
       "a200IpsTermIDTable": a200IpsTermIDTable,
       "a200IpsTermIDEntry": a200IpsTermIDEntry,
       "a200IpsTermIDSeqNo": a200IpsTermIDSeqNo,
       "a200IpsTermIDDeltag": a200IpsTermIDDeltag,
       "a200IpsTermIDBeginSeqNo": a200IpsTermIDBeginSeqNo,
       "a200IpsTermIDOperNum": a200IpsTermIDOperNum,
       "a200IpsTermIDTMIDFix": a200IpsTermIDTMIDFix,
       "a200IpsTermIDType": a200IpsTermIDType,
       "a200IpsTermIDDigitLen": a200IpsTermIDDigitLen,
       "a200IpsTermIDBeginNo": a200IpsTermIDBeginNo,
       "a200IpsTermIDMgId": a200IpsTermIDMgId,
       "a200IpsTerminationID": a200IpsTerminationID,
       "a200IpsTermIDRowStatus": a200IpsTermIDRowStatus,
       "a200RtpParTable": a200RtpParTable,
       "a200RtpParEntry": a200RtpParEntry,
       "a200rtpparparid": a200rtpparparid,
       "a200rtpparvadval": a200rtpparvadval,
       "a200rtppardtmfrlmod": a200rtppardtmfrlmod,
       "a200rtpparpcmlaw": a200rtpparpcmlaw,
       "a200rtpparsiltopcm": a200rtpparsiltopcm,
       "a200rtppardcfilter": a200rtppardcfilter,
       "a200rtpparpcmtopkggain": a200rtpparpcmtopkggain,
       "a200rtpparpkgtopcmgain": a200rtpparpkgtopcmgain,
       "a200rtpparconceal": a200rtpparconceal,
       "a200rtpparecmdisabl": a200rtpparecmdisabl,
       "a200rtpparspeedlim": a200rtpparspeedlim,
       "a200rtpparerrrecov": a200rtpparerrrecov,
       "a200rtppartcfproc": a200rtppartcfproc,
       "a200rtppart38enable": a200rtppart38enable,
       "a200rtppardtmfduplex": a200rtppardtmfduplex,
       "a200rtpparNumBeforeOff": a200rtpparNumBeforeOff,
       "a200rtpparIgnoreA": a200rtpparIgnoreA,
       "a200rtpparToneDuplex": a200rtpparToneDuplex,
       "a200rtppardecodadapt": a200rtppardecodadapt,
       "a200rtpparg723rate": a200rtpparg723rate,
       "a200rtpparpckgendis": a200rtpparpckgendis,
       "a200rtppardtmfpyld": a200rtppardtmfpyld,
       "a200rtppardtmfredpyld": a200rtppardtmfredpyld,
       "a200rtpparfaxdatared": a200rtpparfaxdatared,
       "a200rtppart30msgred": a200rtppart30msgred,
       "a200rtpparmasecenal": a200rtpparmasecenal,
       "a200rtpparhdwecdis": a200rtpparhdwecdis,
       "a200rtpparhecfrz": a200rtpparhecfrz,
       "a200rtpparectxf": a200rtpparectxf,
       "a200rtpparectxm": a200rtpparectxm,
       "a200rtpparecrxm": a200rtpparecrxm,
       "a200rtpparheclen": a200rtpparheclen,
       "a200rtpparlpwmin": a200rtpparlpwmin,
       "a200rtpparlpwmax": a200rtpparlpwmax,
       "a200rtpparlpwinit": a200rtpparlpwinit,
       "a200rtpparlpr": a200rtpparlpr,
       "a200rtpparfsklevel": a200rtpparfsklevel,
       "a200rtpparg711redund": a200rtpparg711redund,
       "a200rtpparmodemmode": a200rtpparmodemmode,
       "a200rtpparap": a200rtpparap,
       "a200rtppardeletmode": a200rtppardeletmode,
       "a200rtpparnortptime": a200rtpparnortptime,
       "a200rtpparfaxswtime": a200rtpparfaxswtime,
       "a200rtppardtmfcidelec": a200rtppardtmfcidelec,
       "msagCallCtrl": msagCallCtrl,
       "upPortTable": upPortTable,
       "upPortEntry": upPortEntry,
       "upportid": upportid,
       "upportrack": upportrack,
       "upportshelf": upportshelf,
       "upportslot": upportslot,
       "upportport": upportport,
       "upportsendrateth": upportsendrateth,
       "upportreceiverateth": upportreceiverateth,
       "upportRowStatus": upportRowStatus,
       "toneTable": toneTable,
       "toneEntry": toneEntry,
       "tonemgid": tonemgid,
       "tonefaxcngtone": tonefaxcngtone,
       "tonev21flagstone": tonev21flagstone,
       "tonet38faxend": tonet38faxend,
       "toneansamwitone": toneansamwitone,
       "toneansamwotone": toneansamwotone,
       "toneanswitone": toneanswitone,
       "toneanswotone": toneanswotone,
       "tonefixtonechip": tonefixtonechip,
       "msagH248Perform": msagH248Perform,
       "msagH248PSRecMsg": msagH248PSRecMsg,
       "msagH248PSSendMsg": msagH248PSSendMsg,
       "msagH248PSRecMsgByte": msagH248PSRecMsgByte,
       "msagH248PSSendMsgByte": msagH248PSSendMsgByte,
       "msagH248PSProtocolError": msagH248PSProtocolError,
       "msagH248PSTimerOut": msagH248PSTimerOut,
       "msagH248PSDisconnect": msagH248PSDisconnect,
       "msagH248PSMGCChange": msagH248PSMGCChange,
       "msagH248PSTransmitError": msagH248PSTransmitError,
       "calllimitipsthruput": calllimitipsthruput,
       "calllimitnicthruput": calllimitnicthruput,
       "calllimitcalllimit": calllimitcalllimit,
       "calllimitcpubusylimit": calllimitcpubusylimit,
       "calllimitupportlimit": calllimitupportlimit,
       "calllimitipslimit": calllimitipslimit,
       "calllimitniclimit": calllimitniclimit,
       "msagTrap": msagTrap,
       "msagTrapId": msagTrapId,
       "zxAnNarrowbandResAvailable": zxAnNarrowbandResAvailable,
       "zxAnNarrowbandResUnavailable": zxAnNarrowbandResUnavailable,
       "zxAnIpsResource": zxAnIpsResource,
       "zxAnIpsResourceRestore": zxAnIpsResourceRestore,
       "zxAnIpsChannelFault": zxAnIpsChannelFault,
       "zxAnIpsChannelFaultRestore": zxAnIpsChannelFaultRestore,
       "zxMsagH248Link": zxMsagH248Link,
       "zxMsagH248LinkRestore": zxMsagH248LinkRestore,
       "zxMsagH248ErrorCode": zxMsagH248ErrorCode,
       "zxAnDlccNT1Los": zxAnDlccNT1Los,
       "zxMsagMgcpLink": zxMsagMgcpLink,
       "zxMsagMgcpLinkRestore": zxMsagMgcpLinkRestore,
       "zxMsagMgcpAbnormal": zxMsagMgcpAbnormal,
       "zxMsagMgcpAbnormalRestore": zxMsagMgcpAbnormalRestore,
       "zxMsagV5Pcm": zxMsagV5Pcm,
       "zxMsagV5PcmRestore": zxMsagV5PcmRestore,
       "zxMsagV5Proto": zxMsagV5Proto,
       "zxMsagV5ProtoRestore": zxMsagV5ProtoRestore,
       "zxMsagISDNSctpInform": zxMsagISDNSctpInform,
       "zxMsagISDNSctpAlarm": zxMsagISDNSctpAlarm,
       "zxMsagIUAInform": zxMsagIUAInform,
       "zxMsagIUAAlarm": zxMsagIUAAlarm,
       "zxMsagIUAAlarmRestore": zxMsagIUAAlarmRestore,
       "zxMsagCallAllocMemoryErrorAlarm": zxMsagCallAllocMemoryErrorAlarm,
       "zxMsagQosPoorAlarm": zxMsagQosPoorAlarm,
       "zxMsagQosPoorRestore": zxMsagQosPoorRestore,
       "zxAnSlcFreqOffOnHookAlarm": zxAnSlcFreqOffOnHookAlarm,
       "zxAnSlcFreqOffOnHookAlarmRestore": zxAnSlcFreqOffOnHookAlarmRestore,
       "zxAnSlcGroundedAlarm": zxAnSlcGroundedAlarm,
       "zxAnSlcGroundedRestore": zxAnSlcGroundedRestore,
       "zxAnSlcContactedWithPower": zxAnSlcContactedWithPower,
       "zxAnDsx1ProtectionGroupSwapped": zxAnDsx1ProtectionGroupSwapped,
       "zxAnIsdnUInterfaceLinkDown": zxAnIsdnUInterfaceLinkDown,
       "zxAnIsdnUInterfaceLinkUp": zxAnIsdnUInterfaceLinkUp,
       "zxAnSlcContactedWithPowerClr": zxAnSlcContactedWithPowerClr,
       "zxAnHwTsUsageAboveThresholdAlm": zxAnHwTsUsageAboveThresholdAlm,
       "zxAnHwTsUsageAboveThresholdClr": zxAnHwTsUsageAboveThresholdClr,
       "zxAnVoicePortLockoutAlm": zxAnVoicePortLockoutAlm,
       "zxAnVoicePortLockoutClr": zxAnVoicePortLockoutClr,
       "zxAnDdiSubscriberLineBrokenAlm": zxAnDdiSubscriberLineBrokenAlm,
       "zxAnDdiSubscriberLineBrokenClr": zxAnDdiSubscriberLineBrokenClr,
       "zxAnVoicePortHighAcVoltageAlm": zxAnVoicePortHighAcVoltageAlm,
       "zxAnVoicePortHighAcVoltageClr": zxAnVoicePortHighAcVoltageClr,
       "zxAnVoicePortHighDcVoltageAlm": zxAnVoicePortHighDcVoltageAlm,
       "zxAnVoicePortHighDcVoltageClr": zxAnVoicePortHighDcVoltageClr,
       "msagTrapObjectMib": msagTrapObjectMib,
       "zxAnNarrowbandResCfgType": zxAnNarrowbandResCfgType,
       "zxAnNarrowbandResActType": zxAnNarrowbandResActType,
       "zxAnIpsResourceAlarmReason": zxAnIpsResourceAlarmReason,
       "zxAnTrapRack": zxAnTrapRack,
       "zxAnTrapShelf": zxAnTrapShelf,
       "zxAnTrapSlot": zxAnTrapSlot,
       "zxAnTrapUnit": zxAnTrapUnit,
       "zxAnTrapSunit": zxAnTrapSunit,
       "zxAnTrapPort": zxAnTrapPort,
       "msagTrapReason": msagTrapReason,
       "msagTrapLinkState": msagTrapLinkState,
       "msagTrapMgcNo": msagTrapMgcNo,
       "msagTrapSLN": msagTrapSLN,
       "msagTrapFlag": msagTrapFlag,
       "msagTrapErrcode": msagTrapErrcode,
       "msagTrapIpAddress": msagTrapIpAddress,
       "msagTrapBETime": msagTrapBETime,
       "zxAnTrapInfoType": zxAnTrapInfoType,
       "msagTrapUnitNo": msagTrapUnitNo,
       "msagTrapPcmNo": msagTrapPcmNo,
       "msagTrapReasionValue": msagTrapReasionValue,
       "msagTrapRack": msagTrapRack,
       "msagTrapShelf": msagTrapShelf,
       "msagTrapSlot": msagTrapSlot,
       "msagTrapV5InterId": msagTrapV5InterId,
       "msagTrapDLProType": msagTrapDLProType,
       "msagTrapCurEvent": msagTrapCurEvent,
       "msagTrapCurState": msagTrapCurState,
       "msagTrapParaLinkId": msagTrapParaLinkId,
       "msagQosAlarmType": msagQosAlarmType,
       "msagQosAlarmDetail": msagQosAlarmDetail,
       "msagTrapPort": msagTrapPort,
       "zxAnVoipCallTest": zxAnVoipCallTest,
       "zxAnVoipCalleeTestTable": zxAnVoipCalleeTestTable,
       "zxAnVoipCalleeTestEntry": zxAnVoipCalleeTestEntry,
       "zxAnVoipCalleeTestRack": zxAnVoipCalleeTestRack,
       "zxAnVoipCalleeTestShelf": zxAnVoipCalleeTestShelf,
       "zxAnVoipCalleeTestSlot": zxAnVoipCalleeTestSlot,
       "zxAnVoipCalleeTestPort": zxAnVoipCalleeTestPort,
       "zxAnVoipCalleeTestOnu": zxAnVoipCalleeTestOnu,
       "zxAnVoipCalleeTestCircuitType": zxAnVoipCalleeTestCircuitType,
       "zxAnVoipCalleeTestLogicalId": zxAnVoipCalleeTestLogicalId,
       "zxAnVoipCalleeTestAction": zxAnVoipCalleeTestAction,
       "zxAnVoipCalleeTestTimeout": zxAnVoipCalleeTestTimeout,
       "zxAnVoipCalleeTestStatus": zxAnVoipCalleeTestStatus,
       "zxAnVoipCalleeTestPortStatus": zxAnVoipCalleeTestPortStatus,
       "zxAnVoipCalleeTestFailReason": zxAnVoipCalleeTestFailReason,
       "zxAnVoipCalleeTestFailDetail": zxAnVoipCalleeTestFailDetail,
       "zxAnVoipCalleeTestRowStatus": zxAnVoipCalleeTestRowStatus,
       "zxAnVoipCallerTestTable": zxAnVoipCallerTestTable,
       "zxAnVoipCallerTestEntry": zxAnVoipCallerTestEntry,
       "zxAnVoipCallerTestRack": zxAnVoipCallerTestRack,
       "zxAnVoipCallerTestShelf": zxAnVoipCallerTestShelf,
       "zxAnVoipCallerTestSlot": zxAnVoipCallerTestSlot,
       "zxAnVoipCallerTestPort": zxAnVoipCallerTestPort,
       "zxAnVoipCallerTestOnu": zxAnVoipCallerTestOnu,
       "zxAnVoipCallerTestCircuitType": zxAnVoipCallerTestCircuitType,
       "zxAnVoipCallerTestLogicalId": zxAnVoipCallerTestLogicalId,
       "zxAnVoipCallerTestAction": zxAnVoipCallerTestAction,
       "zxAnVoipCallerTestTimeout": zxAnVoipCallerTestTimeout,
       "zxAnVoipCallerTestDialedNumber": zxAnVoipCallerTestDialedNumber,
       "zxAnVoipCallerTestStatus": zxAnVoipCallerTestStatus,
       "zxAnVoipCallerTestPortStatus": zxAnVoipCallerTestPortStatus,
       "zxAnVoipCallerTestFailReason": zxAnVoipCallerTestFailReason,
       "zxAnVoipCallerTestFailDetail": zxAnVoipCallerTestFailDetail,
       "zxAnVoipCallerTestSipFailReason": zxAnVoipCallerTestSipFailReason,
       "zxAnVoipCallerTestSipErrorCode": zxAnVoipCallerTestSipErrorCode,
       "zxAnVoipCallerTestSipDelay": zxAnVoipCallerTestSipDelay,
       "zxAnVoipCallerTestMode": zxAnVoipCallerTestMode,
       "zxAnVoipCallerTestRowStatus": zxAnVoipCallerTestRowStatus}
)
