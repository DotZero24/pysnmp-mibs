_R='eltexMsdpSAFilterIndex'
_Q='eltexMsdpSAFilterDirection'
_P='eltexMsdpSAFilterPeerRemoteAddress'
_O='eltexMsdpMeshGroupPeerAddress'
_N='eltexMsdpMeshGroupName'
_M='eltexMsdpPeerRemoteAddress'
_L='eltexMsdpSACacheSourceAddr'
_K='eltexMsdpSACacheGroupAddr'
_J='Unsigned32'
_I='read-create'
_H='seconds'
_G='DisplayString'
_F='Integer32'
_E='not-accessible'
_D='ELTEX-MSDP-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
eltexMsdpMIB=ModuleIdentity((1,3,6,1,4,1,35265,51))
class EltexMsdpSAFilterDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
class EltexMsdpSAFilterAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_EltexMsdpObjects_ObjectIdentity=ObjectIdentity
eltexMsdpObjects=_EltexMsdpObjects_ObjectIdentity((1,3,6,1,4,1,35265,51,1))
_EltexMsdp_ObjectIdentity=ObjectIdentity
eltexMsdp=_EltexMsdp_ObjectIdentity((1,3,6,1,4,1,35265,51,1,1))
_EltexMsdpTraps_ObjectIdentity=ObjectIdentity
eltexMsdpTraps=_EltexMsdpTraps_ObjectIdentity((1,3,6,1,4,1,35265,51,1,1,0))
class _EltexMsdpCacheLifetime_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(150,3600))
_EltexMsdpCacheLifetime_Type.__name__=_F
_EltexMsdpCacheLifetime_Object=MibScalar
eltexMsdpCacheLifetime=_EltexMsdpCacheLifetime_Object((1,3,6,1,4,1,35265,51,1,1,2),_EltexMsdpCacheLifetime_Type())
eltexMsdpCacheLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpCacheLifetime.setStatus(_A)
if mibBuilder.loadTexts:eltexMsdpCacheLifetime.setUnits(_H)
_EltexMsdpSACacheTable_Object=MibTable
eltexMsdpSACacheTable=_EltexMsdpSACacheTable_Object((1,3,6,1,4,1,35265,51,1,1,6))
if mibBuilder.loadTexts:eltexMsdpSACacheTable.setStatus(_A)
_EltexMsdpSACacheEntry_Object=MibTableRow
eltexMsdpSACacheEntry=_EltexMsdpSACacheEntry_Object((1,3,6,1,4,1,35265,51,1,1,6,1))
eltexMsdpSACacheEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:eltexMsdpSACacheEntry.setStatus(_A)
_EltexMsdpSACacheGroupAddr_Type=IpAddress
_EltexMsdpSACacheGroupAddr_Object=MibTableColumn
eltexMsdpSACacheGroupAddr=_EltexMsdpSACacheGroupAddr_Object((1,3,6,1,4,1,35265,51,1,1,6,1,1),_EltexMsdpSACacheGroupAddr_Type())
eltexMsdpSACacheGroupAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexMsdpSACacheGroupAddr.setStatus(_A)
_EltexMsdpSACacheSourceAddr_Type=IpAddress
_EltexMsdpSACacheSourceAddr_Object=MibTableColumn
eltexMsdpSACacheSourceAddr=_EltexMsdpSACacheSourceAddr_Object((1,3,6,1,4,1,35265,51,1,1,6,1,2),_EltexMsdpSACacheSourceAddr_Type())
eltexMsdpSACacheSourceAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexMsdpSACacheSourceAddr.setStatus(_A)
_EltexMsdpSACacheOriginRP_Type=IpAddress
_EltexMsdpSACacheOriginRP_Object=MibTableColumn
eltexMsdpSACacheOriginRP=_EltexMsdpSACacheOriginRP_Object((1,3,6,1,4,1,35265,51,1,1,6,1,3),_EltexMsdpSACacheOriginRP_Type())
eltexMsdpSACacheOriginRP.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpSACacheOriginRP.setStatus(_A)
_EltexMsdpSACachePeerLearnedFrom_Type=IpAddress
_EltexMsdpSACachePeerLearnedFrom_Object=MibTableColumn
eltexMsdpSACachePeerLearnedFrom=_EltexMsdpSACachePeerLearnedFrom_Object((1,3,6,1,4,1,35265,51,1,1,6,1,4),_EltexMsdpSACachePeerLearnedFrom_Type())
eltexMsdpSACachePeerLearnedFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpSACachePeerLearnedFrom.setStatus(_A)
_EltexMsdpSACacheUpTime_Type=TimeTicks
_EltexMsdpSACacheUpTime_Object=MibTableColumn
eltexMsdpSACacheUpTime=_EltexMsdpSACacheUpTime_Object((1,3,6,1,4,1,35265,51,1,1,6,1,8),_EltexMsdpSACacheUpTime_Type())
eltexMsdpSACacheUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpSACacheUpTime.setStatus(_A)
_EltexMsdpPeerTable_Object=MibTable
eltexMsdpPeerTable=_EltexMsdpPeerTable_Object((1,3,6,1,4,1,35265,51,1,1,10))
if mibBuilder.loadTexts:eltexMsdpPeerTable.setStatus(_A)
_EltexMsdpPeerEntry_Object=MibTableRow
eltexMsdpPeerEntry=_EltexMsdpPeerEntry_Object((1,3,6,1,4,1,35265,51,1,1,10,1))
eltexMsdpPeerEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:eltexMsdpPeerEntry.setStatus(_A)
_EltexMsdpPeerRemoteAddress_Type=IpAddress
_EltexMsdpPeerRemoteAddress_Object=MibTableColumn
eltexMsdpPeerRemoteAddress=_EltexMsdpPeerRemoteAddress_Object((1,3,6,1,4,1,35265,51,1,1,10,1,1),_EltexMsdpPeerRemoteAddress_Type())
eltexMsdpPeerRemoteAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexMsdpPeerRemoteAddress.setStatus(_A)
class _EltexMsdpPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inactive',1),('listen',2),('connecting',3),('established',4),('disabled',5)))
_EltexMsdpPeerState_Type.__name__=_F
_EltexMsdpPeerState_Object=MibTableColumn
eltexMsdpPeerState=_EltexMsdpPeerState_Object((1,3,6,1,4,1,35265,51,1,1,10,1,3),_EltexMsdpPeerState_Type())
eltexMsdpPeerState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerState.setStatus(_A)
_EltexMsdpPeerRPFFailures_Type=Counter32
_EltexMsdpPeerRPFFailures_Object=MibTableColumn
eltexMsdpPeerRPFFailures=_EltexMsdpPeerRPFFailures_Object((1,3,6,1,4,1,35265,51,1,1,10,1,4),_EltexMsdpPeerRPFFailures_Type())
eltexMsdpPeerRPFFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerRPFFailures.setStatus(_A)
_EltexMsdpPeerInSAs_Type=Counter32
_EltexMsdpPeerInSAs_Object=MibTableColumn
eltexMsdpPeerInSAs=_EltexMsdpPeerInSAs_Object((1,3,6,1,4,1,35265,51,1,1,10,1,5),_EltexMsdpPeerInSAs_Type())
eltexMsdpPeerInSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerInSAs.setStatus(_A)
_EltexMsdpPeerOutSAs_Type=Counter32
_EltexMsdpPeerOutSAs_Object=MibTableColumn
eltexMsdpPeerOutSAs=_EltexMsdpPeerOutSAs_Object((1,3,6,1,4,1,35265,51,1,1,10,1,6),_EltexMsdpPeerOutSAs_Type())
eltexMsdpPeerOutSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerOutSAs.setStatus(_A)
_EltexMsdpPeerInSARequests_Type=Counter32
_EltexMsdpPeerInSARequests_Object=MibTableColumn
eltexMsdpPeerInSARequests=_EltexMsdpPeerInSARequests_Object((1,3,6,1,4,1,35265,51,1,1,10,1,7),_EltexMsdpPeerInSARequests_Type())
eltexMsdpPeerInSARequests.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerInSARequests.setStatus(_A)
_EltexMsdpPeerOutSARequests_Type=Counter32
_EltexMsdpPeerOutSARequests_Object=MibTableColumn
eltexMsdpPeerOutSARequests=_EltexMsdpPeerOutSARequests_Object((1,3,6,1,4,1,35265,51,1,1,10,1,8),_EltexMsdpPeerOutSARequests_Type())
eltexMsdpPeerOutSARequests.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerOutSARequests.setStatus(_A)
_EltexMsdpPeerInSAResponses_Type=Counter32
_EltexMsdpPeerInSAResponses_Object=MibTableColumn
eltexMsdpPeerInSAResponses=_EltexMsdpPeerInSAResponses_Object((1,3,6,1,4,1,35265,51,1,1,10,1,9),_EltexMsdpPeerInSAResponses_Type())
eltexMsdpPeerInSAResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerInSAResponses.setStatus(_A)
_EltexMsdpPeerOutSAResponses_Type=Counter32
_EltexMsdpPeerOutSAResponses_Object=MibTableColumn
eltexMsdpPeerOutSAResponses=_EltexMsdpPeerOutSAResponses_Object((1,3,6,1,4,1,35265,51,1,1,10,1,10),_EltexMsdpPeerOutSAResponses_Type())
eltexMsdpPeerOutSAResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerOutSAResponses.setStatus(_A)
_EltexMsdpPeerInControlMessages_Type=Counter32
_EltexMsdpPeerInControlMessages_Object=MibTableColumn
eltexMsdpPeerInControlMessages=_EltexMsdpPeerInControlMessages_Object((1,3,6,1,4,1,35265,51,1,1,10,1,11),_EltexMsdpPeerInControlMessages_Type())
eltexMsdpPeerInControlMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerInControlMessages.setStatus(_A)
_EltexMsdpPeerOutControlMessages_Type=Counter32
_EltexMsdpPeerOutControlMessages_Object=MibTableColumn
eltexMsdpPeerOutControlMessages=_EltexMsdpPeerOutControlMessages_Object((1,3,6,1,4,1,35265,51,1,1,10,1,12),_EltexMsdpPeerOutControlMessages_Type())
eltexMsdpPeerOutControlMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerOutControlMessages.setStatus(_A)
_EltexMsdpPeerFsmEstablishedTime_Type=TimeStamp
_EltexMsdpPeerFsmEstablishedTime_Object=MibTableColumn
eltexMsdpPeerFsmEstablishedTime=_EltexMsdpPeerFsmEstablishedTime_Object((1,3,6,1,4,1,35265,51,1,1,10,1,16),_EltexMsdpPeerFsmEstablishedTime_Type())
eltexMsdpPeerFsmEstablishedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerFsmEstablishedTime.setStatus(_A)
_EltexMsdpPeerInMessageTime_Type=TimeStamp
_EltexMsdpPeerInMessageTime_Object=MibTableColumn
eltexMsdpPeerInMessageTime=_EltexMsdpPeerInMessageTime_Object((1,3,6,1,4,1,35265,51,1,1,10,1,17),_EltexMsdpPeerInMessageTime_Type())
eltexMsdpPeerInMessageTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerInMessageTime.setStatus(_A)
_EltexMsdpPeerLocalAddress_Type=IpAddress
_EltexMsdpPeerLocalAddress_Object=MibTableColumn
eltexMsdpPeerLocalAddress=_EltexMsdpPeerLocalAddress_Object((1,3,6,1,4,1,35265,51,1,1,10,1,18),_EltexMsdpPeerLocalAddress_Type())
eltexMsdpPeerLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpPeerLocalAddress.setStatus(_A)
_EltexMsdpPeerRowStatus_Type=RowStatus
_EltexMsdpPeerRowStatus_Object=MibTableColumn
eltexMsdpPeerRowStatus=_EltexMsdpPeerRowStatus_Object((1,3,6,1,4,1,35265,51,1,1,10,1,25),_EltexMsdpPeerRowStatus_Type())
eltexMsdpPeerRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexMsdpPeerRowStatus.setStatus(_A)
_EltexMsdpPeerConnectionAttempts_Type=Counter32
_EltexMsdpPeerConnectionAttempts_Object=MibTableColumn
eltexMsdpPeerConnectionAttempts=_EltexMsdpPeerConnectionAttempts_Object((1,3,6,1,4,1,35265,51,1,1,10,1,30),_EltexMsdpPeerConnectionAttempts_Type())
eltexMsdpPeerConnectionAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerConnectionAttempts.setStatus(_A)
_EltexMsdpPeerEnabled_Type=TruthValue
_EltexMsdpPeerEnabled_Object=MibTableColumn
eltexMsdpPeerEnabled=_EltexMsdpPeerEnabled_Object((1,3,6,1,4,1,35265,51,1,1,10,1,100),_EltexMsdpPeerEnabled_Type())
eltexMsdpPeerEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpPeerEnabled.setStatus(_A)
class _EltexMsdpPeerDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_EltexMsdpPeerDescription_Type.__name__=_G
_EltexMsdpPeerDescription_Object=MibTableColumn
eltexMsdpPeerDescription=_EltexMsdpPeerDescription_Object((1,3,6,1,4,1,35265,51,1,1,10,1,101),_EltexMsdpPeerDescription_Type())
eltexMsdpPeerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpPeerDescription.setStatus(_A)
_EltexMsdpPeerFsmLastChangeTime_Type=TimeStamp
_EltexMsdpPeerFsmLastChangeTime_Object=MibTableColumn
eltexMsdpPeerFsmLastChangeTime=_EltexMsdpPeerFsmLastChangeTime_Object((1,3,6,1,4,1,35265,51,1,1,10,1,102),_EltexMsdpPeerFsmLastChangeTime_Type())
eltexMsdpPeerFsmLastChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerFsmLastChangeTime.setStatus(_A)
_EltexMsdpPeerNumSACacheEntries_Type=Gauge32
_EltexMsdpPeerNumSACacheEntries_Object=MibTableColumn
eltexMsdpPeerNumSACacheEntries=_EltexMsdpPeerNumSACacheEntries_Object((1,3,6,1,4,1,35265,51,1,1,10,1,103),_EltexMsdpPeerNumSACacheEntries_Type())
eltexMsdpPeerNumSACacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexMsdpPeerNumSACacheEntries.setStatus(_A)
_EltexMsdpRPAddress_Type=IpAddress
_EltexMsdpRPAddress_Object=MibScalar
eltexMsdpRPAddress=_EltexMsdpRPAddress_Object((1,3,6,1,4,1,35265,51,1,1,11),_EltexMsdpRPAddress_Type())
eltexMsdpRPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpRPAddress.setStatus(_A)
_EltexMsdpMeshGroupTable_Object=MibTable
eltexMsdpMeshGroupTable=_EltexMsdpMeshGroupTable_Object((1,3,6,1,4,1,35265,51,1,1,12))
if mibBuilder.loadTexts:eltexMsdpMeshGroupTable.setStatus(_A)
_EltexMsdpMeshGroupEntry_Object=MibTableRow
eltexMsdpMeshGroupEntry=_EltexMsdpMeshGroupEntry_Object((1,3,6,1,4,1,35265,51,1,1,12,1))
eltexMsdpMeshGroupEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:eltexMsdpMeshGroupEntry.setStatus(_A)
class _EltexMsdpMeshGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_EltexMsdpMeshGroupName_Type.__name__=_G
_EltexMsdpMeshGroupName_Object=MibTableColumn
eltexMsdpMeshGroupName=_EltexMsdpMeshGroupName_Object((1,3,6,1,4,1,35265,51,1,1,12,1,1),_EltexMsdpMeshGroupName_Type())
eltexMsdpMeshGroupName.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexMsdpMeshGroupName.setStatus(_A)
_EltexMsdpMeshGroupPeerAddress_Type=IpAddress
_EltexMsdpMeshGroupPeerAddress_Object=MibTableColumn
eltexMsdpMeshGroupPeerAddress=_EltexMsdpMeshGroupPeerAddress_Object((1,3,6,1,4,1,35265,51,1,1,12,1,2),_EltexMsdpMeshGroupPeerAddress_Type())
eltexMsdpMeshGroupPeerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexMsdpMeshGroupPeerAddress.setStatus(_A)
_EltexMsdpMeshGroupRowStatus_Type=RowStatus
_EltexMsdpMeshGroupRowStatus_Object=MibTableColumn
eltexMsdpMeshGroupRowStatus=_EltexMsdpMeshGroupRowStatus_Object((1,3,6,1,4,1,35265,51,1,1,12,1,3),_EltexMsdpMeshGroupRowStatus_Type())
eltexMsdpMeshGroupRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexMsdpMeshGroupRowStatus.setStatus(_A)
class _EltexMsdpHoldTime_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,150))
_EltexMsdpHoldTime_Type.__name__=_F
_EltexMsdpHoldTime_Object=MibScalar
eltexMsdpHoldTime=_EltexMsdpHoldTime_Object((1,3,6,1,4,1,35265,51,1,1,100),_EltexMsdpHoldTime_Type())
eltexMsdpHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpHoldTime.setStatus(_A)
if mibBuilder.loadTexts:eltexMsdpHoldTime.setUnits(_H)
class _EltexMsdpKeepAlive_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_EltexMsdpKeepAlive_Type.__name__=_F
_EltexMsdpKeepAlive_Object=MibScalar
eltexMsdpKeepAlive=_EltexMsdpKeepAlive_Object((1,3,6,1,4,1,35265,51,1,1,101),_EltexMsdpKeepAlive_Type())
eltexMsdpKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpKeepAlive.setStatus(_A)
if mibBuilder.loadTexts:eltexMsdpKeepAlive.setUnits(_H)
_EltexMsdpLocalAddress_Type=IpAddress
_EltexMsdpLocalAddress_Object=MibScalar
eltexMsdpLocalAddress=_EltexMsdpLocalAddress_Object((1,3,6,1,4,1,35265,51,1,1,102),_EltexMsdpLocalAddress_Type())
eltexMsdpLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpLocalAddress.setStatus(_A)
_EltexMsdpPeerCountersClear_Type=IpAddress
_EltexMsdpPeerCountersClear_Object=MibScalar
eltexMsdpPeerCountersClear=_EltexMsdpPeerCountersClear_Object((1,3,6,1,4,1,35265,51,1,1,103),_EltexMsdpPeerCountersClear_Type())
eltexMsdpPeerCountersClear.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpPeerCountersClear.setStatus(_A)
_EltexMsdpSAFilterTable_Object=MibTable
eltexMsdpSAFilterTable=_EltexMsdpSAFilterTable_Object((1,3,6,1,4,1,35265,51,1,1,104))
if mibBuilder.loadTexts:eltexMsdpSAFilterTable.setStatus(_A)
_EltexMsdpSAFilterEntry_Object=MibTableRow
eltexMsdpSAFilterEntry=_EltexMsdpSAFilterEntry_Object((1,3,6,1,4,1,35265,51,1,1,104,1))
eltexMsdpSAFilterEntry.setIndexNames((0,_D,_P),(0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:eltexMsdpSAFilterEntry.setStatus(_A)
_EltexMsdpSAFilterPeerRemoteAddress_Type=IpAddress
_EltexMsdpSAFilterPeerRemoteAddress_Object=MibTableColumn
eltexMsdpSAFilterPeerRemoteAddress=_EltexMsdpSAFilterPeerRemoteAddress_Object((1,3,6,1,4,1,35265,51,1,1,104,1,1),_EltexMsdpSAFilterPeerRemoteAddress_Type())
eltexMsdpSAFilterPeerRemoteAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexMsdpSAFilterPeerRemoteAddress.setStatus(_A)
_EltexMsdpSAFilterDirection_Type=EltexMsdpSAFilterDirection
_EltexMsdpSAFilterDirection_Object=MibTableColumn
eltexMsdpSAFilterDirection=_EltexMsdpSAFilterDirection_Object((1,3,6,1,4,1,35265,51,1,1,104,1,2),_EltexMsdpSAFilterDirection_Type())
eltexMsdpSAFilterDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexMsdpSAFilterDirection.setStatus(_A)
class _EltexMsdpSAFilterIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967294))
_EltexMsdpSAFilterIndex_Type.__name__=_J
_EltexMsdpSAFilterIndex_Object=MibTableColumn
eltexMsdpSAFilterIndex=_EltexMsdpSAFilterIndex_Object((1,3,6,1,4,1,35265,51,1,1,104,1,3),_EltexMsdpSAFilterIndex_Type())
eltexMsdpSAFilterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexMsdpSAFilterIndex.setStatus(_A)
_EltexMsdpSAFilterAction_Type=EltexMsdpSAFilterAction
_EltexMsdpSAFilterAction_Object=MibTableColumn
eltexMsdpSAFilterAction=_EltexMsdpSAFilterAction_Object((1,3,6,1,4,1,35265,51,1,1,104,1,4),_EltexMsdpSAFilterAction_Type())
eltexMsdpSAFilterAction.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpSAFilterAction.setStatus(_A)
_EltexMsdpSAFilterGroupAddr_Type=IpAddress
_EltexMsdpSAFilterGroupAddr_Object=MibTableColumn
eltexMsdpSAFilterGroupAddr=_EltexMsdpSAFilterGroupAddr_Object((1,3,6,1,4,1,35265,51,1,1,104,1,5),_EltexMsdpSAFilterGroupAddr_Type())
eltexMsdpSAFilterGroupAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpSAFilterGroupAddr.setStatus(_A)
_EltexMsdpSAFilterGroupAddrPrefixLen_Type=Integer32
_EltexMsdpSAFilterGroupAddrPrefixLen_Object=MibTableColumn
eltexMsdpSAFilterGroupAddrPrefixLen=_EltexMsdpSAFilterGroupAddrPrefixLen_Object((1,3,6,1,4,1,35265,51,1,1,104,1,6),_EltexMsdpSAFilterGroupAddrPrefixLen_Type())
eltexMsdpSAFilterGroupAddrPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpSAFilterGroupAddrPrefixLen.setStatus(_A)
_EltexMsdpSAFilterSourceAddr_Type=IpAddress
_EltexMsdpSAFilterSourceAddr_Object=MibTableColumn
eltexMsdpSAFilterSourceAddr=_EltexMsdpSAFilterSourceAddr_Object((1,3,6,1,4,1,35265,51,1,1,104,1,7),_EltexMsdpSAFilterSourceAddr_Type())
eltexMsdpSAFilterSourceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpSAFilterSourceAddr.setStatus(_A)
_EltexMsdpSAFilterSourceAddrPrefixLen_Type=Integer32
_EltexMsdpSAFilterSourceAddrPrefixLen_Object=MibTableColumn
eltexMsdpSAFilterSourceAddrPrefixLen=_EltexMsdpSAFilterSourceAddrPrefixLen_Object((1,3,6,1,4,1,35265,51,1,1,104,1,8),_EltexMsdpSAFilterSourceAddrPrefixLen_Type())
eltexMsdpSAFilterSourceAddrPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpSAFilterSourceAddrPrefixLen.setStatus(_A)
_EltexMsdpSAFilterOriginRP_Type=IpAddress
_EltexMsdpSAFilterOriginRP_Object=MibTableColumn
eltexMsdpSAFilterOriginRP=_EltexMsdpSAFilterOriginRP_Object((1,3,6,1,4,1,35265,51,1,1,104,1,9),_EltexMsdpSAFilterOriginRP_Type())
eltexMsdpSAFilterOriginRP.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpSAFilterOriginRP.setStatus(_A)
_EltexMsdpSAFilterOriginRPPrefixLen_Type=Integer32
_EltexMsdpSAFilterOriginRPPrefixLen_Object=MibTableColumn
eltexMsdpSAFilterOriginRPPrefixLen=_EltexMsdpSAFilterOriginRPPrefixLen_Object((1,3,6,1,4,1,35265,51,1,1,104,1,10),_EltexMsdpSAFilterOriginRPPrefixLen_Type())
eltexMsdpSAFilterOriginRPPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMsdpSAFilterOriginRPPrefixLen.setStatus(_A)
_EltexMsdpSAFilterRowStatus_Type=RowStatus
_EltexMsdpSAFilterRowStatus_Object=MibTableColumn
eltexMsdpSAFilterRowStatus=_EltexMsdpSAFilterRowStatus_Object((1,3,6,1,4,1,35265,51,1,1,104,1,11),_EltexMsdpSAFilterRowStatus_Type())
eltexMsdpSAFilterRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexMsdpSAFilterRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'EltexMsdpSAFilterDirection':EltexMsdpSAFilterDirection,'EltexMsdpSAFilterAction':EltexMsdpSAFilterAction,'eltexMsdpMIB':eltexMsdpMIB,'eltexMsdpObjects':eltexMsdpObjects,'eltexMsdp':eltexMsdp,'eltexMsdpTraps':eltexMsdpTraps,'eltexMsdpCacheLifetime':eltexMsdpCacheLifetime,'eltexMsdpSACacheTable':eltexMsdpSACacheTable,'eltexMsdpSACacheEntry':eltexMsdpSACacheEntry,_K:eltexMsdpSACacheGroupAddr,_L:eltexMsdpSACacheSourceAddr,'eltexMsdpSACacheOriginRP':eltexMsdpSACacheOriginRP,'eltexMsdpSACachePeerLearnedFrom':eltexMsdpSACachePeerLearnedFrom,'eltexMsdpSACacheUpTime':eltexMsdpSACacheUpTime,'eltexMsdpPeerTable':eltexMsdpPeerTable,'eltexMsdpPeerEntry':eltexMsdpPeerEntry,_M:eltexMsdpPeerRemoteAddress,'eltexMsdpPeerState':eltexMsdpPeerState,'eltexMsdpPeerRPFFailures':eltexMsdpPeerRPFFailures,'eltexMsdpPeerInSAs':eltexMsdpPeerInSAs,'eltexMsdpPeerOutSAs':eltexMsdpPeerOutSAs,'eltexMsdpPeerInSARequests':eltexMsdpPeerInSARequests,'eltexMsdpPeerOutSARequests':eltexMsdpPeerOutSARequests,'eltexMsdpPeerInSAResponses':eltexMsdpPeerInSAResponses,'eltexMsdpPeerOutSAResponses':eltexMsdpPeerOutSAResponses,'eltexMsdpPeerInControlMessages':eltexMsdpPeerInControlMessages,'eltexMsdpPeerOutControlMessages':eltexMsdpPeerOutControlMessages,'eltexMsdpPeerFsmEstablishedTime':eltexMsdpPeerFsmEstablishedTime,'eltexMsdpPeerInMessageTime':eltexMsdpPeerInMessageTime,'eltexMsdpPeerLocalAddress':eltexMsdpPeerLocalAddress,'eltexMsdpPeerRowStatus':eltexMsdpPeerRowStatus,'eltexMsdpPeerConnectionAttempts':eltexMsdpPeerConnectionAttempts,'eltexMsdpPeerEnabled':eltexMsdpPeerEnabled,'eltexMsdpPeerDescription':eltexMsdpPeerDescription,'eltexMsdpPeerFsmLastChangeTime':eltexMsdpPeerFsmLastChangeTime,'eltexMsdpPeerNumSACacheEntries':eltexMsdpPeerNumSACacheEntries,'eltexMsdpRPAddress':eltexMsdpRPAddress,'eltexMsdpMeshGroupTable':eltexMsdpMeshGroupTable,'eltexMsdpMeshGroupEntry':eltexMsdpMeshGroupEntry,_N:eltexMsdpMeshGroupName,_O:eltexMsdpMeshGroupPeerAddress,'eltexMsdpMeshGroupRowStatus':eltexMsdpMeshGroupRowStatus,'eltexMsdpHoldTime':eltexMsdpHoldTime,'eltexMsdpKeepAlive':eltexMsdpKeepAlive,'eltexMsdpLocalAddress':eltexMsdpLocalAddress,'eltexMsdpPeerCountersClear':eltexMsdpPeerCountersClear,'eltexMsdpSAFilterTable':eltexMsdpSAFilterTable,'eltexMsdpSAFilterEntry':eltexMsdpSAFilterEntry,_P:eltexMsdpSAFilterPeerRemoteAddress,_Q:eltexMsdpSAFilterDirection,_R:eltexMsdpSAFilterIndex,'eltexMsdpSAFilterAction':eltexMsdpSAFilterAction,'eltexMsdpSAFilterGroupAddr':eltexMsdpSAFilterGroupAddr,'eltexMsdpSAFilterGroupAddrPrefixLen':eltexMsdpSAFilterGroupAddrPrefixLen,'eltexMsdpSAFilterSourceAddr':eltexMsdpSAFilterSourceAddr,'eltexMsdpSAFilterSourceAddrPrefixLen':eltexMsdpSAFilterSourceAddrPrefixLen,'eltexMsdpSAFilterOriginRP':eltexMsdpSAFilterOriginRP,'eltexMsdpSAFilterOriginRPPrefixLen':eltexMsdpSAFilterOriginRPPrefixLen,'eltexMsdpSAFilterRowStatus':eltexMsdpSAFilterRowStatus})