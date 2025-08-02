_q='alaPimBsrDiagnosticsGroup'
_p='alaPimBsrObjectGroup'
_o='alaPimBsrCandidateBSRWinElection'
_n='alaPimBsrElectedBSRLostElection'
_m='alaPimBsrElectedBSRExpiryTime'
_l='alaPimBsrElectedBSRHashMaskLength'
_k='alaPimBsrElectedBSRPriority'
_j='alaPimBsrElectedBSRAddress'
_i='alaPimBsrCandidateBSRStatus'
_h='alaPimBsrCandidateBSRBootstrapTimer'
_g='alaPimBsrCandidateBSRHashMaskLength'
_f='alaPimBsrCandidateBSRPriority'
_e='alaPimBsrCandidateBSRAddress'
_d='alaPimBsrElectedBSRRPSetGrpBidir'
_c='alaPimBsrElectedBSRRPSetExpiryTime'
_b='alaPimBsrElectedBSRRPSetHoldtime'
_a='alaPimBsrElectedBSRRPSetPriority'
_Z='alaPimBsrCandidateRPStatus'
_Y='alaPimBsrCandidateRPHoldtime'
_X='alaPimBsrCandidateRPAdvInterval'
_W='alaPimBsrCandidateRPPriority'
_V='alaPimBsrCandidateRPAdvTimer'
_U='alaPimBsrCandidateRPBidir'
_T='alaPimBsrElectedBSRAddressType'
_S='alaPimBsrCandidateBSRAddressType'
_R='alaPimBsrElectedBSRGrpMappingRPAddr'
_Q='alaPimBsrElectedBSRGrpMappingGrpPrefixLen'
_P='alaPimBsrElectedBSRGrpMappingGrpAddr'
_O='alaPimBsrElectedBSRGrpMappingAddrType'
_N='alaPimBsrCandidateRPGroupPrefixLength'
_M='alaPimBsrCandidateRPGroupAddress'
_L='alaPimBsrCandidateRPAddress'
_K='alaPimBsrCandidateRPAddressType'
_J='TruthValue'
_I='InetAddressPrefixLength'
_H='alaPimBsrCandidateBSRElectedBSR'
_G='InetAddress'
_F='read-create'
_E='not-accessible'
_D='Unsigned32'
_C='read-only'
_B='ALCATEL-IND1-PIM-BSR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Pim,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1Pim')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,_I,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
alaPimBsrMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,3))
if mibBuilder.loadTexts:alaPimBsrMIB.setRevisions(('2007-07-02 00:00',))
_AlaPimBsrNotifications_ObjectIdentity=ObjectIdentity
alaPimBsrNotifications=_AlaPimBsrNotifications_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,0))
_AlaPimBsrObjects_ObjectIdentity=ObjectIdentity
alaPimBsrObjects=_AlaPimBsrObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1))
_AlaPimBsrCandidateRPTable_Object=MibTable
alaPimBsrCandidateRPTable=_AlaPimBsrCandidateRPTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,1))
if mibBuilder.loadTexts:alaPimBsrCandidateRPTable.setStatus(_A)
_AlaPimBsrCandidateRPEntry_Object=MibTableRow
alaPimBsrCandidateRPEntry=_AlaPimBsrCandidateRPEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,1,1))
alaPimBsrCandidateRPEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:alaPimBsrCandidateRPEntry.setStatus(_A)
_AlaPimBsrCandidateRPAddressType_Type=InetAddressType
_AlaPimBsrCandidateRPAddressType_Object=MibTableColumn
alaPimBsrCandidateRPAddressType=_AlaPimBsrCandidateRPAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,1,1,1),_AlaPimBsrCandidateRPAddressType_Type())
alaPimBsrCandidateRPAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPimBsrCandidateRPAddressType.setStatus(_A)
class _AlaPimBsrCandidateRPAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaPimBsrCandidateRPAddress_Type.__name__=_G
_AlaPimBsrCandidateRPAddress_Object=MibTableColumn
alaPimBsrCandidateRPAddress=_AlaPimBsrCandidateRPAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,1,1,2),_AlaPimBsrCandidateRPAddress_Type())
alaPimBsrCandidateRPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPimBsrCandidateRPAddress.setStatus(_A)
class _AlaPimBsrCandidateRPGroupAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaPimBsrCandidateRPGroupAddress_Type.__name__=_G
_AlaPimBsrCandidateRPGroupAddress_Object=MibTableColumn
alaPimBsrCandidateRPGroupAddress=_AlaPimBsrCandidateRPGroupAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,1,1,3),_AlaPimBsrCandidateRPGroupAddress_Type())
alaPimBsrCandidateRPGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPimBsrCandidateRPGroupAddress.setStatus(_A)
class _AlaPimBsrCandidateRPGroupPrefixLength_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,128))
_AlaPimBsrCandidateRPGroupPrefixLength_Type.__name__=_I
_AlaPimBsrCandidateRPGroupPrefixLength_Object=MibTableColumn
alaPimBsrCandidateRPGroupPrefixLength=_AlaPimBsrCandidateRPGroupPrefixLength_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,1,1,4),_AlaPimBsrCandidateRPGroupPrefixLength_Type())
alaPimBsrCandidateRPGroupPrefixLength.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPimBsrCandidateRPGroupPrefixLength.setStatus(_A)
class _AlaPimBsrCandidateRPBidir_Type(TruthValue):defaultValue=2
_AlaPimBsrCandidateRPBidir_Type.__name__=_J
_AlaPimBsrCandidateRPBidir_Object=MibTableColumn
alaPimBsrCandidateRPBidir=_AlaPimBsrCandidateRPBidir_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,1,1,5),_AlaPimBsrCandidateRPBidir_Type())
alaPimBsrCandidateRPBidir.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPimBsrCandidateRPBidir.setStatus(_A)
_AlaPimBsrCandidateRPAdvTimer_Type=TimeTicks
_AlaPimBsrCandidateRPAdvTimer_Object=MibTableColumn
alaPimBsrCandidateRPAdvTimer=_AlaPimBsrCandidateRPAdvTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,1,1,6),_AlaPimBsrCandidateRPAdvTimer_Type())
alaPimBsrCandidateRPAdvTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimBsrCandidateRPAdvTimer.setStatus(_A)
class _AlaPimBsrCandidateRPPriority_Type(Unsigned32):defaultValue=192;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaPimBsrCandidateRPPriority_Type.__name__=_D
_AlaPimBsrCandidateRPPriority_Object=MibTableColumn
alaPimBsrCandidateRPPriority=_AlaPimBsrCandidateRPPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,1,1,7),_AlaPimBsrCandidateRPPriority_Type())
alaPimBsrCandidateRPPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPimBsrCandidateRPPriority.setStatus(_A)
class _AlaPimBsrCandidateRPAdvInterval_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,26214))
_AlaPimBsrCandidateRPAdvInterval_Type.__name__=_D
_AlaPimBsrCandidateRPAdvInterval_Object=MibTableColumn
alaPimBsrCandidateRPAdvInterval=_AlaPimBsrCandidateRPAdvInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,1,1,8),_AlaPimBsrCandidateRPAdvInterval_Type())
alaPimBsrCandidateRPAdvInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPimBsrCandidateRPAdvInterval.setStatus(_A)
class _AlaPimBsrCandidateRPHoldtime_Type(Unsigned32):defaultValue=150;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaPimBsrCandidateRPHoldtime_Type.__name__=_D
_AlaPimBsrCandidateRPHoldtime_Object=MibTableColumn
alaPimBsrCandidateRPHoldtime=_AlaPimBsrCandidateRPHoldtime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,1,1,9),_AlaPimBsrCandidateRPHoldtime_Type())
alaPimBsrCandidateRPHoldtime.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPimBsrCandidateRPHoldtime.setStatus(_A)
_AlaPimBsrCandidateRPStatus_Type=RowStatus
_AlaPimBsrCandidateRPStatus_Object=MibTableColumn
alaPimBsrCandidateRPStatus=_AlaPimBsrCandidateRPStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,1,1,10),_AlaPimBsrCandidateRPStatus_Type())
alaPimBsrCandidateRPStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPimBsrCandidateRPStatus.setStatus(_A)
_AlaPimBsrElectedBSRRPSetTable_Object=MibTable
alaPimBsrElectedBSRRPSetTable=_AlaPimBsrElectedBSRRPSetTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,2))
if mibBuilder.loadTexts:alaPimBsrElectedBSRRPSetTable.setStatus(_A)
_AlaPimBsrElectedBSRRPSetEntry_Object=MibTableRow
alaPimBsrElectedBSRRPSetEntry=_AlaPimBsrElectedBSRRPSetEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,2,1))
alaPimBsrElectedBSRRPSetEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:alaPimBsrElectedBSRRPSetEntry.setStatus(_A)
_AlaPimBsrElectedBSRGrpMappingAddrType_Type=InetAddressType
_AlaPimBsrElectedBSRGrpMappingAddrType_Object=MibTableColumn
alaPimBsrElectedBSRGrpMappingAddrType=_AlaPimBsrElectedBSRGrpMappingAddrType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,2,1,2),_AlaPimBsrElectedBSRGrpMappingAddrType_Type())
alaPimBsrElectedBSRGrpMappingAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPimBsrElectedBSRGrpMappingAddrType.setStatus(_A)
class _AlaPimBsrElectedBSRGrpMappingGrpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaPimBsrElectedBSRGrpMappingGrpAddr_Type.__name__=_G
_AlaPimBsrElectedBSRGrpMappingGrpAddr_Object=MibTableColumn
alaPimBsrElectedBSRGrpMappingGrpAddr=_AlaPimBsrElectedBSRGrpMappingGrpAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,2,1,3),_AlaPimBsrElectedBSRGrpMappingGrpAddr_Type())
alaPimBsrElectedBSRGrpMappingGrpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPimBsrElectedBSRGrpMappingGrpAddr.setStatus(_A)
class _AlaPimBsrElectedBSRGrpMappingGrpPrefixLen_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,128))
_AlaPimBsrElectedBSRGrpMappingGrpPrefixLen_Type.__name__=_I
_AlaPimBsrElectedBSRGrpMappingGrpPrefixLen_Object=MibTableColumn
alaPimBsrElectedBSRGrpMappingGrpPrefixLen=_AlaPimBsrElectedBSRGrpMappingGrpPrefixLen_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,2,1,4),_AlaPimBsrElectedBSRGrpMappingGrpPrefixLen_Type())
alaPimBsrElectedBSRGrpMappingGrpPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPimBsrElectedBSRGrpMappingGrpPrefixLen.setStatus(_A)
class _AlaPimBsrElectedBSRGrpMappingRPAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaPimBsrElectedBSRGrpMappingRPAddr_Type.__name__=_G
_AlaPimBsrElectedBSRGrpMappingRPAddr_Object=MibTableColumn
alaPimBsrElectedBSRGrpMappingRPAddr=_AlaPimBsrElectedBSRGrpMappingRPAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,2,1,5),_AlaPimBsrElectedBSRGrpMappingRPAddr_Type())
alaPimBsrElectedBSRGrpMappingRPAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPimBsrElectedBSRGrpMappingRPAddr.setStatus(_A)
class _AlaPimBsrElectedBSRRPSetPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaPimBsrElectedBSRRPSetPriority_Type.__name__=_D
_AlaPimBsrElectedBSRRPSetPriority_Object=MibTableColumn
alaPimBsrElectedBSRRPSetPriority=_AlaPimBsrElectedBSRRPSetPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,2,1,6),_AlaPimBsrElectedBSRRPSetPriority_Type())
alaPimBsrElectedBSRRPSetPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimBsrElectedBSRRPSetPriority.setStatus(_A)
class _AlaPimBsrElectedBSRRPSetHoldtime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaPimBsrElectedBSRRPSetHoldtime_Type.__name__=_D
_AlaPimBsrElectedBSRRPSetHoldtime_Object=MibTableColumn
alaPimBsrElectedBSRRPSetHoldtime=_AlaPimBsrElectedBSRRPSetHoldtime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,2,1,7),_AlaPimBsrElectedBSRRPSetHoldtime_Type())
alaPimBsrElectedBSRRPSetHoldtime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimBsrElectedBSRRPSetHoldtime.setStatus(_A)
if mibBuilder.loadTexts:alaPimBsrElectedBSRRPSetHoldtime.setUnits('seconds')
_AlaPimBsrElectedBSRRPSetExpiryTime_Type=TimeTicks
_AlaPimBsrElectedBSRRPSetExpiryTime_Object=MibTableColumn
alaPimBsrElectedBSRRPSetExpiryTime=_AlaPimBsrElectedBSRRPSetExpiryTime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,2,1,8),_AlaPimBsrElectedBSRRPSetExpiryTime_Type())
alaPimBsrElectedBSRRPSetExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimBsrElectedBSRRPSetExpiryTime.setStatus(_A)
_AlaPimBsrElectedBSRRPSetGrpBidir_Type=TruthValue
_AlaPimBsrElectedBSRRPSetGrpBidir_Object=MibTableColumn
alaPimBsrElectedBSRRPSetGrpBidir=_AlaPimBsrElectedBSRRPSetGrpBidir_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,2,1,9),_AlaPimBsrElectedBSRRPSetGrpBidir_Type())
alaPimBsrElectedBSRRPSetGrpBidir.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimBsrElectedBSRRPSetGrpBidir.setStatus(_A)
_AlaPimBsrCandidateBSRTable_Object=MibTable
alaPimBsrCandidateBSRTable=_AlaPimBsrCandidateBSRTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,3))
if mibBuilder.loadTexts:alaPimBsrCandidateBSRTable.setStatus(_A)
_AlaPimBsrCandidateBSREntry_Object=MibTableRow
alaPimBsrCandidateBSREntry=_AlaPimBsrCandidateBSREntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,3,1))
alaPimBsrCandidateBSREntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:alaPimBsrCandidateBSREntry.setStatus(_A)
_AlaPimBsrCandidateBSRAddressType_Type=InetAddressType
_AlaPimBsrCandidateBSRAddressType_Object=MibTableColumn
alaPimBsrCandidateBSRAddressType=_AlaPimBsrCandidateBSRAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,3,1,1),_AlaPimBsrCandidateBSRAddressType_Type())
alaPimBsrCandidateBSRAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPimBsrCandidateBSRAddressType.setStatus(_A)
_AlaPimBsrCandidateBSRAddress_Type=InetAddress
_AlaPimBsrCandidateBSRAddress_Object=MibTableColumn
alaPimBsrCandidateBSRAddress=_AlaPimBsrCandidateBSRAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,3,1,2),_AlaPimBsrCandidateBSRAddress_Type())
alaPimBsrCandidateBSRAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPimBsrCandidateBSRAddress.setStatus(_A)
class _AlaPimBsrCandidateBSRPriority_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaPimBsrCandidateBSRPriority_Type.__name__=_D
_AlaPimBsrCandidateBSRPriority_Object=MibTableColumn
alaPimBsrCandidateBSRPriority=_AlaPimBsrCandidateBSRPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,3,1,3),_AlaPimBsrCandidateBSRPriority_Type())
alaPimBsrCandidateBSRPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPimBsrCandidateBSRPriority.setStatus(_A)
class _AlaPimBsrCandidateBSRHashMaskLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaPimBsrCandidateBSRHashMaskLength_Type.__name__=_D
_AlaPimBsrCandidateBSRHashMaskLength_Object=MibTableColumn
alaPimBsrCandidateBSRHashMaskLength=_AlaPimBsrCandidateBSRHashMaskLength_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,3,1,4),_AlaPimBsrCandidateBSRHashMaskLength_Type())
alaPimBsrCandidateBSRHashMaskLength.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPimBsrCandidateBSRHashMaskLength.setStatus(_A)
_AlaPimBsrCandidateBSRElectedBSR_Type=TruthValue
_AlaPimBsrCandidateBSRElectedBSR_Object=MibTableColumn
alaPimBsrCandidateBSRElectedBSR=_AlaPimBsrCandidateBSRElectedBSR_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,3,1,5),_AlaPimBsrCandidateBSRElectedBSR_Type())
alaPimBsrCandidateBSRElectedBSR.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimBsrCandidateBSRElectedBSR.setStatus(_A)
_AlaPimBsrCandidateBSRBootstrapTimer_Type=TimeTicks
_AlaPimBsrCandidateBSRBootstrapTimer_Object=MibTableColumn
alaPimBsrCandidateBSRBootstrapTimer=_AlaPimBsrCandidateBSRBootstrapTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,3,1,6),_AlaPimBsrCandidateBSRBootstrapTimer_Type())
alaPimBsrCandidateBSRBootstrapTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimBsrCandidateBSRBootstrapTimer.setStatus(_A)
_AlaPimBsrCandidateBSRStatus_Type=RowStatus
_AlaPimBsrCandidateBSRStatus_Object=MibTableColumn
alaPimBsrCandidateBSRStatus=_AlaPimBsrCandidateBSRStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,3,1,7),_AlaPimBsrCandidateBSRStatus_Type())
alaPimBsrCandidateBSRStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPimBsrCandidateBSRStatus.setStatus(_A)
_AlaPimBsrElectedBSRTable_Object=MibTable
alaPimBsrElectedBSRTable=_AlaPimBsrElectedBSRTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,4))
if mibBuilder.loadTexts:alaPimBsrElectedBSRTable.setStatus(_A)
_AlaPimBsrElectedBSREntry_Object=MibTableRow
alaPimBsrElectedBSREntry=_AlaPimBsrElectedBSREntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,4,1))
alaPimBsrElectedBSREntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:alaPimBsrElectedBSREntry.setStatus(_A)
_AlaPimBsrElectedBSRAddressType_Type=InetAddressType
_AlaPimBsrElectedBSRAddressType_Object=MibTableColumn
alaPimBsrElectedBSRAddressType=_AlaPimBsrElectedBSRAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,4,1,1),_AlaPimBsrElectedBSRAddressType_Type())
alaPimBsrElectedBSRAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPimBsrElectedBSRAddressType.setStatus(_A)
class _AlaPimBsrElectedBSRAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaPimBsrElectedBSRAddress_Type.__name__=_G
_AlaPimBsrElectedBSRAddress_Object=MibTableColumn
alaPimBsrElectedBSRAddress=_AlaPimBsrElectedBSRAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,4,1,2),_AlaPimBsrElectedBSRAddress_Type())
alaPimBsrElectedBSRAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimBsrElectedBSRAddress.setStatus(_A)
class _AlaPimBsrElectedBSRPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaPimBsrElectedBSRPriority_Type.__name__=_D
_AlaPimBsrElectedBSRPriority_Object=MibTableColumn
alaPimBsrElectedBSRPriority=_AlaPimBsrElectedBSRPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,4,1,3),_AlaPimBsrElectedBSRPriority_Type())
alaPimBsrElectedBSRPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimBsrElectedBSRPriority.setStatus(_A)
class _AlaPimBsrElectedBSRHashMaskLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaPimBsrElectedBSRHashMaskLength_Type.__name__=_D
_AlaPimBsrElectedBSRHashMaskLength_Object=MibTableColumn
alaPimBsrElectedBSRHashMaskLength=_AlaPimBsrElectedBSRHashMaskLength_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,4,1,4),_AlaPimBsrElectedBSRHashMaskLength_Type())
alaPimBsrElectedBSRHashMaskLength.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimBsrElectedBSRHashMaskLength.setStatus(_A)
_AlaPimBsrElectedBSRExpiryTime_Type=TimeTicks
_AlaPimBsrElectedBSRExpiryTime_Object=MibTableColumn
alaPimBsrElectedBSRExpiryTime=_AlaPimBsrElectedBSRExpiryTime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,1,4,1,5),_AlaPimBsrElectedBSRExpiryTime_Type())
alaPimBsrElectedBSRExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPimBsrElectedBSRExpiryTime.setStatus(_A)
_AlaPimBsrConformance_ObjectIdentity=ObjectIdentity
alaPimBsrConformance=_AlaPimBsrConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,2))
_AlaPimBsrCompliances_ObjectIdentity=ObjectIdentity
alaPimBsrCompliances=_AlaPimBsrCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,2,1))
_AlaPimBsrGroups_ObjectIdentity=ObjectIdentity
alaPimBsrGroups=_AlaPimBsrGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,2,2))
alaPimBsrObjectGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,2,2,1))
alaPimBsrObjectGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_H),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:alaPimBsrObjectGroup.setStatus(_A)
alaPimBsrElectedBSRLostElection=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,0,1))
alaPimBsrElectedBSRLostElection.setObjects((_B,_H))
if mibBuilder.loadTexts:alaPimBsrElectedBSRLostElection.setStatus(_A)
alaPimBsrCandidateBSRWinElection=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,0,2))
alaPimBsrCandidateBSRWinElection.setObjects((_B,_H))
if mibBuilder.loadTexts:alaPimBsrCandidateBSRWinElection.setStatus(_A)
alaPimBsrDiagnosticsGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,2,2,2))
alaPimBsrDiagnosticsGroup.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:alaPimBsrDiagnosticsGroup.setStatus(_A)
alaPimBsrCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,6,3,2,1,1))
alaPimBsrCompliance.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:alaPimBsrCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alaPimBsrMIB':alaPimBsrMIB,'alaPimBsrNotifications':alaPimBsrNotifications,_n:alaPimBsrElectedBSRLostElection,_o:alaPimBsrCandidateBSRWinElection,'alaPimBsrObjects':alaPimBsrObjects,'alaPimBsrCandidateRPTable':alaPimBsrCandidateRPTable,'alaPimBsrCandidateRPEntry':alaPimBsrCandidateRPEntry,_K:alaPimBsrCandidateRPAddressType,_L:alaPimBsrCandidateRPAddress,_M:alaPimBsrCandidateRPGroupAddress,_N:alaPimBsrCandidateRPGroupPrefixLength,_U:alaPimBsrCandidateRPBidir,_V:alaPimBsrCandidateRPAdvTimer,_W:alaPimBsrCandidateRPPriority,_X:alaPimBsrCandidateRPAdvInterval,_Y:alaPimBsrCandidateRPHoldtime,_Z:alaPimBsrCandidateRPStatus,'alaPimBsrElectedBSRRPSetTable':alaPimBsrElectedBSRRPSetTable,'alaPimBsrElectedBSRRPSetEntry':alaPimBsrElectedBSRRPSetEntry,_O:alaPimBsrElectedBSRGrpMappingAddrType,_P:alaPimBsrElectedBSRGrpMappingGrpAddr,_Q:alaPimBsrElectedBSRGrpMappingGrpPrefixLen,_R:alaPimBsrElectedBSRGrpMappingRPAddr,_a:alaPimBsrElectedBSRRPSetPriority,_b:alaPimBsrElectedBSRRPSetHoldtime,_c:alaPimBsrElectedBSRRPSetExpiryTime,_d:alaPimBsrElectedBSRRPSetGrpBidir,'alaPimBsrCandidateBSRTable':alaPimBsrCandidateBSRTable,'alaPimBsrCandidateBSREntry':alaPimBsrCandidateBSREntry,_S:alaPimBsrCandidateBSRAddressType,_e:alaPimBsrCandidateBSRAddress,_f:alaPimBsrCandidateBSRPriority,_g:alaPimBsrCandidateBSRHashMaskLength,_H:alaPimBsrCandidateBSRElectedBSR,_h:alaPimBsrCandidateBSRBootstrapTimer,_i:alaPimBsrCandidateBSRStatus,'alaPimBsrElectedBSRTable':alaPimBsrElectedBSRTable,'alaPimBsrElectedBSREntry':alaPimBsrElectedBSREntry,_T:alaPimBsrElectedBSRAddressType,_j:alaPimBsrElectedBSRAddress,_k:alaPimBsrElectedBSRPriority,_l:alaPimBsrElectedBSRHashMaskLength,_m:alaPimBsrElectedBSRExpiryTime,'alaPimBsrConformance':alaPimBsrConformance,'alaPimBsrCompliances':alaPimBsrCompliances,'alaPimBsrCompliance':alaPimBsrCompliance,'alaPimBsrGroups':alaPimBsrGroups,_p:alaPimBsrObjectGroup,_q:alaPimBsrDiagnosticsGroup})