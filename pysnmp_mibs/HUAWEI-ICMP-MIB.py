_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huawei,hwInternetProtocol,hwLocal=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','huawei','hwInternetProtocol','hwLocal')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_RIcmp_ObjectIdentity=ObjectIdentity
rIcmp=_RIcmp_ObjectIdentity((1,3,6,1,4,1,2011,1,3,2))
_IcmpInBadCode_Type=Counter32
_IcmpInBadCode_Object=MibScalar
icmpInBadCode=_IcmpInBadCode_Object((1,3,6,1,4,1,2011,1,3,2,1),_IcmpInBadCode_Type())
icmpInBadCode.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInBadCode.setStatus(_B)
_IcmpInBadLen_Type=Counter32
_IcmpInBadLen_Object=MibScalar
icmpInBadLen=_IcmpInBadLen_Object((1,3,6,1,4,1,2011,1,3,2,2),_IcmpInBadLen_Type())
icmpInBadLen.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInBadLen.setStatus(_B)
_IcmpInChecksum_Type=Counter32
_IcmpInChecksum_Object=MibScalar
icmpInChecksum=_IcmpInChecksum_Object((1,3,6,1,4,1,2011,1,3,2,3),_IcmpInChecksum_Type())
icmpInChecksum.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInChecksum.setStatus(_B)
_IcmpInTooShort_Type=Counter32
_IcmpInTooShort_Object=MibScalar
icmpInTooShort=_IcmpInTooShort_Object((1,3,6,1,4,1,2011,1,3,2,4),_IcmpInTooShort_Type())
icmpInTooShort.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInTooShort.setStatus(_B)
_IcmpOutOldIcmp_Type=Counter32
_IcmpOutOldIcmp_Object=MibScalar
icmpOutOldIcmp=_IcmpOutOldIcmp_Object((1,3,6,1,4,1,2011,1,3,2,5),_IcmpOutOldIcmp_Type())
icmpOutOldIcmp.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutOldIcmp.setStatus(_B)
_IcmpOutShort_Type=Counter32
_IcmpOutShort_Object=MibScalar
icmpOutShort=_IcmpOutShort_Object((1,3,6,1,4,1,2011,1,3,2,6),_IcmpOutShort_Type())
icmpOutShort.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutShort.setStatus(_B)
mibBuilder.exportSymbols('HUAWEI-ICMP-MIB',**{'rIcmp':rIcmp,'icmpInBadCode':icmpInBadCode,'icmpInBadLen':icmpInBadLen,'icmpInChecksum':icmpInChecksum,'icmpInTooShort':icmpInTooShort,'icmpOutOldIcmp':icmpOutOldIcmp,'icmpOutShort':icmpOutShort})