_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Biboip_ObjectIdentity=ObjectIdentity
biboip=_Biboip_ObjectIdentity((1,3,6,1,4,1,272,4,5))
_OspfErr_ObjectIdentity=ObjectIdentity
ospfErr=_OspfErr_ObjectIdentity((1,3,6,1,4,1,272,4,5,11))
_OspfErrOspfBadVersion_Type=Counter32
_OspfErrOspfBadVersion_Object=MibScalar
ospfErrOspfBadVersion=_OspfErrOspfBadVersion_Object((1,3,6,1,4,1,272,4,5,11,1),_OspfErrOspfBadVersion_Type())
ospfErrOspfBadVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrOspfBadVersion.setStatus(_B)
_OspfErrOspfBadPacketType_Type=Counter32
_OspfErrOspfBadPacketType_Object=MibScalar
ospfErrOspfBadPacketType=_OspfErrOspfBadPacketType_Object((1,3,6,1,4,1,272,4,5,11,2),_OspfErrOspfBadPacketType_Type())
ospfErrOspfBadPacketType.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrOspfBadPacketType.setStatus(_B)
_OspfErrOspfBadChecksum_Type=Counter32
_OspfErrOspfBadChecksum_Object=MibScalar
ospfErrOspfBadChecksum=_OspfErrOspfBadChecksum_Object((1,3,6,1,4,1,272,4,5,11,3),_OspfErrOspfBadChecksum_Type())
ospfErrOspfBadChecksum.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrOspfBadChecksum.setStatus(_B)
_OspfErrIpBadDestination_Type=Counter32
_OspfErrIpBadDestination_Object=MibScalar
ospfErrIpBadDestination=_OspfErrIpBadDestination_Object((1,3,6,1,4,1,272,4,5,11,4),_OspfErrIpBadDestination_Type())
ospfErrIpBadDestination.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrIpBadDestination.setStatus(_B)
_OspfErrOspfBadAreaId_Type=Counter32
_OspfErrOspfBadAreaId_Object=MibScalar
ospfErrOspfBadAreaId=_OspfErrOspfBadAreaId_Object((1,3,6,1,4,1,272,4,5,11,5),_OspfErrOspfBadAreaId_Type())
ospfErrOspfBadAreaId.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrOspfBadAreaId.setStatus(_B)
_OspfErrOspfAuthenticationFailed_Type=Counter32
_OspfErrOspfAuthenticationFailed_Object=MibScalar
ospfErrOspfAuthenticationFailed=_OspfErrOspfAuthenticationFailed_Object((1,3,6,1,4,1,272,4,5,11,6),_OspfErrOspfAuthenticationFailed_Type())
ospfErrOspfAuthenticationFailed.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrOspfAuthenticationFailed.setStatus(_B)
_OspfErrOspfUnknownNeighbor_Type=Counter32
_OspfErrOspfUnknownNeighbor_Object=MibScalar
ospfErrOspfUnknownNeighbor=_OspfErrOspfUnknownNeighbor_Object((1,3,6,1,4,1,272,4,5,11,7),_OspfErrOspfUnknownNeighbor_Type())
ospfErrOspfUnknownNeighbor.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrOspfUnknownNeighbor.setStatus(_B)
_OspfErrHelloNetmaskMismatch_Type=Counter32
_OspfErrHelloNetmaskMismatch_Object=MibScalar
ospfErrHelloNetmaskMismatch=_OspfErrHelloNetmaskMismatch_Object((1,3,6,1,4,1,272,4,5,11,8),_OspfErrHelloNetmaskMismatch_Type())
ospfErrHelloNetmaskMismatch.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrHelloNetmaskMismatch.setStatus(_B)
_OspfErrHelloDeadTimerMismatch_Type=Counter32
_OspfErrHelloDeadTimerMismatch_Object=MibScalar
ospfErrHelloDeadTimerMismatch=_OspfErrHelloDeadTimerMismatch_Object((1,3,6,1,4,1,272,4,5,11,9),_OspfErrHelloDeadTimerMismatch_Type())
ospfErrHelloDeadTimerMismatch.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrHelloDeadTimerMismatch.setStatus(_B)
_OspfErrHelloTimerMismatch_Type=Counter32
_OspfErrHelloTimerMismatch_Object=MibScalar
ospfErrHelloTimerMismatch=_OspfErrHelloTimerMismatch_Object((1,3,6,1,4,1,272,4,5,11,10),_OspfErrHelloTimerMismatch_Type())
ospfErrHelloTimerMismatch.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrHelloTimerMismatch.setStatus(_B)
_OspfErrHelloOptionMismatch_Type=Counter32
_OspfErrHelloOptionMismatch_Object=MibScalar
ospfErrHelloOptionMismatch=_OspfErrHelloOptionMismatch_Object((1,3,6,1,4,1,272,4,5,11,11),_OspfErrHelloOptionMismatch_Type())
ospfErrHelloOptionMismatch.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrHelloOptionMismatch.setStatus(_B)
_OspfErrOspfRouterIdConfusion_Type=Counter32
_OspfErrOspfRouterIdConfusion_Object=MibScalar
ospfErrOspfRouterIdConfusion=_OspfErrOspfRouterIdConfusion_Object((1,3,6,1,4,1,272,4,5,11,12),_OspfErrOspfRouterIdConfusion_Type())
ospfErrOspfRouterIdConfusion.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrOspfRouterIdConfusion.setStatus(_B)
_OspfErrOspfUnknownLsaType_Type=Counter32
_OspfErrOspfUnknownLsaType_Object=MibScalar
ospfErrOspfUnknownLsaType=_OspfErrOspfUnknownLsaType_Object((1,3,6,1,4,1,272,4,5,11,13),_OspfErrOspfUnknownLsaType_Type())
ospfErrOspfUnknownLsaType.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrOspfUnknownLsaType.setStatus(_B)
_OspfErrDdOptionMismatch_Type=Counter32
_OspfErrDdOptionMismatch_Object=MibScalar
ospfErrDdOptionMismatch=_OspfErrDdOptionMismatch_Object((1,3,6,1,4,1,272,4,5,11,14),_OspfErrDdOptionMismatch_Type())
ospfErrDdOptionMismatch.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrDdOptionMismatch.setStatus(_B)
_OspfErrDdNeighborStateLow_Type=Counter32
_OspfErrDdNeighborStateLow_Object=MibScalar
ospfErrDdNeighborStateLow=_OspfErrDdNeighborStateLow_Object((1,3,6,1,4,1,272,4,5,11,15),_OspfErrDdNeighborStateLow_Type())
ospfErrDdNeighborStateLow.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrDdNeighborStateLow.setStatus(_B)
_OspfErrLsackBadAck_Type=Counter32
_OspfErrLsackBadAck_Object=MibScalar
ospfErrLsackBadAck=_OspfErrLsackBadAck_Object((1,3,6,1,4,1,272,4,5,11,16),_OspfErrLsackBadAck_Type())
ospfErrLsackBadAck.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrLsackBadAck.setStatus(_B)
_OspfErrLsackDuplicateAck_Type=Counter32
_OspfErrLsackDuplicateAck_Object=MibScalar
ospfErrLsackDuplicateAck=_OspfErrLsackDuplicateAck_Object((1,3,6,1,4,1,272,4,5,11,17),_OspfErrLsackDuplicateAck_Type())
ospfErrLsackDuplicateAck.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrLsackDuplicateAck.setStatus(_B)
_OspfErrLsreqBadRequest_Type=Counter32
_OspfErrLsreqBadRequest_Object=MibScalar
ospfErrLsreqBadRequest=_OspfErrLsreqBadRequest_Object((1,3,6,1,4,1,272,4,5,11,18),_OspfErrLsreqBadRequest_Type())
ospfErrLsreqBadRequest.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrLsreqBadRequest.setStatus(_B)
_OspfErrLsreqNeighborStateLow_Type=Counter32
_OspfErrLsreqNeighborStateLow_Object=MibScalar
ospfErrLsreqNeighborStateLow=_OspfErrLsreqNeighborStateLow_Object((1,3,6,1,4,1,272,4,5,11,19),_OspfErrLsreqNeighborStateLow_Type())
ospfErrLsreqNeighborStateLow.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrLsreqNeighborStateLow.setStatus(_B)
_OspfErrLsupdNeighborStateLow_Type=Counter32
_OspfErrLsupdNeighborStateLow_Object=MibScalar
ospfErrLsupdNeighborStateLow=_OspfErrLsupdNeighborStateLow_Object((1,3,6,1,4,1,272,4,5,11,20),_OspfErrLsupdNeighborStateLow_Type())
ospfErrLsupdNeighborStateLow.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrLsupdNeighborStateLow.setStatus(_B)
_OspfErrLsupdBadLsaChecksum_Type=Counter32
_OspfErrLsupdBadLsaChecksum_Object=MibScalar
ospfErrLsupdBadLsaChecksum=_OspfErrLsupdBadLsaChecksum_Object((1,3,6,1,4,1,272,4,5,11,21),_OspfErrLsupdBadLsaChecksum_Type())
ospfErrLsupdBadLsaChecksum.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrLsupdBadLsaChecksum.setStatus(_B)
_OspfErrLsupdNewerSelfgenLsa_Type=Counter32
_OspfErrLsupdNewerSelfgenLsa_Object=MibScalar
ospfErrLsupdNewerSelfgenLsa=_OspfErrLsupdNewerSelfgenLsa_Object((1,3,6,1,4,1,272,4,5,11,22),_OspfErrLsupdNewerSelfgenLsa_Type())
ospfErrLsupdNewerSelfgenLsa.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrLsupdNewerSelfgenLsa.setStatus(_B)
_OspfErrLsupdLessRecentLsa_Type=Counter32
_OspfErrLsupdLessRecentLsa_Object=MibScalar
ospfErrLsupdLessRecentLsa=_OspfErrLsupdLessRecentLsa_Object((1,3,6,1,4,1,272,4,5,11,23),_OspfErrLsupdLessRecentLsa_Type())
ospfErrLsupdLessRecentLsa.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfErrLsupdLessRecentLsa.setStatus(_B)
mibBuilder.exportSymbols('BIANCA-BRICK-OSPF-ERR-MIB',**{'bintec':bintec,'bibo':bibo,'biboip':biboip,'ospfErr':ospfErr,'ospfErrOspfBadVersion':ospfErrOspfBadVersion,'ospfErrOspfBadPacketType':ospfErrOspfBadPacketType,'ospfErrOspfBadChecksum':ospfErrOspfBadChecksum,'ospfErrIpBadDestination':ospfErrIpBadDestination,'ospfErrOspfBadAreaId':ospfErrOspfBadAreaId,'ospfErrOspfAuthenticationFailed':ospfErrOspfAuthenticationFailed,'ospfErrOspfUnknownNeighbor':ospfErrOspfUnknownNeighbor,'ospfErrHelloNetmaskMismatch':ospfErrHelloNetmaskMismatch,'ospfErrHelloDeadTimerMismatch':ospfErrHelloDeadTimerMismatch,'ospfErrHelloTimerMismatch':ospfErrHelloTimerMismatch,'ospfErrHelloOptionMismatch':ospfErrHelloOptionMismatch,'ospfErrOspfRouterIdConfusion':ospfErrOspfRouterIdConfusion,'ospfErrOspfUnknownLsaType':ospfErrOspfUnknownLsaType,'ospfErrDdOptionMismatch':ospfErrDdOptionMismatch,'ospfErrDdNeighborStateLow':ospfErrDdNeighborStateLow,'ospfErrLsackBadAck':ospfErrLsackBadAck,'ospfErrLsackDuplicateAck':ospfErrLsackDuplicateAck,'ospfErrLsreqBadRequest':ospfErrLsreqBadRequest,'ospfErrLsreqNeighborStateLow':ospfErrLsreqNeighborStateLow,'ospfErrLsupdNeighborStateLow':ospfErrLsupdNeighborStateLow,'ospfErrLsupdBadLsaChecksum':ospfErrLsupdBadLsaChecksum,'ospfErrLsupdNewerSelfgenLsa':ospfErrLsupdNewerSelfgenLsa,'ospfErrLsupdLessRecentLsa':ospfErrLsupdLessRecentLsa})