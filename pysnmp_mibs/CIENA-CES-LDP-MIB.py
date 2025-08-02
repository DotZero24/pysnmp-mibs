_L='cienaCesLdpHelloAdjacencyIndex'
_K='seconds'
_J='cienaCesLdpPeerLdpId'
_I='cienaCesLdpEntityIndex'
_H='cienaCesLdpEntityLdpId'
_G='Integer32'
_F='not-accessible'
_E='milliseconds'
_D='CIENA-CES-LDP-MIB'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaCesConfig,cienaCesNotifications=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications')
CienaGlobalState,=mibBuilder.importSymbols('CIENA-TC','CienaGlobalState')
MplsLdpIdentifier,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsLdpIdentifier')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
cienaCesLdpMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,17))
if mibBuilder.loadTexts:cienaCesLdpMIB.setRevisions(('2017-06-07 00:00','2016-07-15 00:00','2016-07-13 00:00','2013-04-18 00:00','2011-02-02 00:00'))
_CienaCesLdpMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesLdpMIBObjects=_CienaCesLdpMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,17,1))
_CienaCesLdpObjects_ObjectIdentity=ObjectIdentity
cienaCesLdpObjects=_CienaCesLdpObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,17,1,1))
_CienaCesLdpAdminStatus_Type=CienaGlobalState
_CienaCesLdpAdminStatus_Object=MibScalar
cienaCesLdpAdminStatus=_CienaCesLdpAdminStatus_Object((1,3,6,1,4,1,1271,2,1,17,1,1,1),_CienaCesLdpAdminStatus_Type())
cienaCesLdpAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpAdminStatus.setStatus(_A)
class _CienaCesLdpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('up',1),('down',2)))
_CienaCesLdpOperStatus_Type.__name__=_G
_CienaCesLdpOperStatus_Object=MibScalar
cienaCesLdpOperStatus=_CienaCesLdpOperStatus_Object((1,3,6,1,4,1,1271,2,1,17,1,1,2),_CienaCesLdpOperStatus_Type())
cienaCesLdpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpOperStatus.setStatus(_A)
class _CienaCesLdpHelloHoldTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesLdpHelloHoldTime_Type.__name__=_C
_CienaCesLdpHelloHoldTime_Object=MibScalar
cienaCesLdpHelloHoldTime=_CienaCesLdpHelloHoldTime_Object((1,3,6,1,4,1,1271,2,1,17,1,1,3),_CienaCesLdpHelloHoldTime_Type())
cienaCesLdpHelloHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpHelloHoldTime.setStatus(_A)
if mibBuilder.loadTexts:cienaCesLdpHelloHoldTime.setUnits(_K)
class _CienaCesLdpKeepAliveHoldTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesLdpKeepAliveHoldTime_Type.__name__=_C
_CienaCesLdpKeepAliveHoldTime_Object=MibScalar
cienaCesLdpKeepAliveHoldTime=_CienaCesLdpKeepAliveHoldTime_Object((1,3,6,1,4,1,1271,2,1,17,1,1,4),_CienaCesLdpKeepAliveHoldTime_Type())
cienaCesLdpKeepAliveHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpKeepAliveHoldTime.setStatus(_A)
if mibBuilder.loadTexts:cienaCesLdpKeepAliveHoldTime.setUnits(_K)
_CienaCesLdpGRAdminStatus_Type=CienaGlobalState
_CienaCesLdpGRAdminStatus_Object=MibScalar
cienaCesLdpGRAdminStatus=_CienaCesLdpGRAdminStatus_Object((1,3,6,1,4,1,1271,2,1,17,1,1,5),_CienaCesLdpGRAdminStatus_Type())
cienaCesLdpGRAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpGRAdminStatus.setStatus(_A)
class _CienaCesLdpGRMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('helpNeighbor',1),('restartCapable',2),('notApplicable',3)))
_CienaCesLdpGRMode_Type.__name__=_G
_CienaCesLdpGRMode_Object=MibScalar
cienaCesLdpGRMode=_CienaCesLdpGRMode_Object((1,3,6,1,4,1,1271,2,1,17,1,1,6),_CienaCesLdpGRMode_Type())
cienaCesLdpGRMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpGRMode.setStatus(_A)
class _CienaCesLdpReconnectTime_Type(Unsigned32):defaultValue=60000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600000))
_CienaCesLdpReconnectTime_Type.__name__=_C
_CienaCesLdpReconnectTime_Object=MibScalar
cienaCesLdpReconnectTime=_CienaCesLdpReconnectTime_Object((1,3,6,1,4,1,1271,2,1,17,1,1,7),_CienaCesLdpReconnectTime_Type())
cienaCesLdpReconnectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpReconnectTime.setStatus(_A)
if mibBuilder.loadTexts:cienaCesLdpReconnectTime.setUnits(_E)
class _CienaCesLdpRecoveryTime_Type(Unsigned32):defaultValue=180000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600000))
_CienaCesLdpRecoveryTime_Type.__name__=_C
_CienaCesLdpRecoveryTime_Object=MibScalar
cienaCesLdpRecoveryTime=_CienaCesLdpRecoveryTime_Object((1,3,6,1,4,1,1271,2,1,17,1,1,8),_CienaCesLdpRecoveryTime_Type())
cienaCesLdpRecoveryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpRecoveryTime.setStatus(_A)
if mibBuilder.loadTexts:cienaCesLdpRecoveryTime.setUnits(_E)
class _CienaCesLdpMaxPeerReconnect_Type(Unsigned32):defaultValue=180000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600000))
_CienaCesLdpMaxPeerReconnect_Type.__name__=_C
_CienaCesLdpMaxPeerReconnect_Object=MibScalar
cienaCesLdpMaxPeerReconnect=_CienaCesLdpMaxPeerReconnect_Object((1,3,6,1,4,1,1271,2,1,17,1,1,9),_CienaCesLdpMaxPeerReconnect_Type())
cienaCesLdpMaxPeerReconnect.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpMaxPeerReconnect.setStatus(_A)
if mibBuilder.loadTexts:cienaCesLdpMaxPeerReconnect.setUnits(_E)
class _CienaCesLdpMaxPeerRecovery_Type(Unsigned32):defaultValue=240000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600000))
_CienaCesLdpMaxPeerRecovery_Type.__name__=_C
_CienaCesLdpMaxPeerRecovery_Object=MibScalar
cienaCesLdpMaxPeerRecovery=_CienaCesLdpMaxPeerRecovery_Object((1,3,6,1,4,1,1271,2,1,17,1,1,10),_CienaCesLdpMaxPeerRecovery_Type())
cienaCesLdpMaxPeerRecovery.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpMaxPeerRecovery.setStatus(_A)
if mibBuilder.loadTexts:cienaCesLdpMaxPeerRecovery.setUnits(_E)
_CienaCesLdp_ObjectIdentity=ObjectIdentity
cienaCesLdp=_CienaCesLdp_ObjectIdentity((1,3,6,1,4,1,1271,2,1,17,1,2))
_CienaCesLdpSessionTable_Object=MibTable
cienaCesLdpSessionTable=_CienaCesLdpSessionTable_Object((1,3,6,1,4,1,1271,2,1,17,1,2,1))
if mibBuilder.loadTexts:cienaCesLdpSessionTable.setStatus(_A)
_CienaCesLdpSessionEntry_Object=MibTableRow
cienaCesLdpSessionEntry=_CienaCesLdpSessionEntry_Object((1,3,6,1,4,1,1271,2,1,17,1,2,1,1))
cienaCesLdpSessionEntry.setIndexNames((0,_D,_H),(0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:cienaCesLdpSessionEntry.setStatus(_A)
_CienaCesLdpEntityLdpId_Type=MplsLdpIdentifier
_CienaCesLdpEntityLdpId_Object=MibTableColumn
cienaCesLdpEntityLdpId=_CienaCesLdpEntityLdpId_Object((1,3,6,1,4,1,1271,2,1,17,1,2,1,1,1),_CienaCesLdpEntityLdpId_Type())
cienaCesLdpEntityLdpId.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesLdpEntityLdpId.setStatus(_A)
_CienaCesLdpEntityIndex_Type=Unsigned32
_CienaCesLdpEntityIndex_Object=MibTableColumn
cienaCesLdpEntityIndex=_CienaCesLdpEntityIndex_Object((1,3,6,1,4,1,1271,2,1,17,1,2,1,1,2),_CienaCesLdpEntityIndex_Type())
cienaCesLdpEntityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesLdpEntityIndex.setStatus(_A)
_CienaCesLdpPeerLdpId_Type=MplsLdpIdentifier
_CienaCesLdpPeerLdpId_Object=MibTableColumn
cienaCesLdpPeerLdpId=_CienaCesLdpPeerLdpId_Object((1,3,6,1,4,1,1271,2,1,17,1,2,1,1,3),_CienaCesLdpPeerLdpId_Type())
cienaCesLdpPeerLdpId.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesLdpPeerLdpId.setStatus(_A)
_CienaCesLdpSessionConfiguredHoldTime_Type=Unsigned32
_CienaCesLdpSessionConfiguredHoldTime_Object=MibTableColumn
cienaCesLdpSessionConfiguredHoldTime=_CienaCesLdpSessionConfiguredHoldTime_Object((1,3,6,1,4,1,1271,2,1,17,1,2,1,1,4),_CienaCesLdpSessionConfiguredHoldTime_Type())
cienaCesLdpSessionConfiguredHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpSessionConfiguredHoldTime.setStatus(_A)
_CienaCesLdpSessionPeerHoldTime_Type=Unsigned32
_CienaCesLdpSessionPeerHoldTime_Object=MibTableColumn
cienaCesLdpSessionPeerHoldTime=_CienaCesLdpSessionPeerHoldTime_Object((1,3,6,1,4,1,1271,2,1,17,1,2,1,1,5),_CienaCesLdpSessionPeerHoldTime_Type())
cienaCesLdpSessionPeerHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpSessionPeerHoldTime.setStatus(_A)
_CienaCesLdpSessionHoldTimeInUse_Type=Unsigned32
_CienaCesLdpSessionHoldTimeInUse_Object=MibTableColumn
cienaCesLdpSessionHoldTimeInUse=_CienaCesLdpSessionHoldTimeInUse_Object((1,3,6,1,4,1,1271,2,1,17,1,2,1,1,6),_CienaCesLdpSessionHoldTimeInUse_Type())
cienaCesLdpSessionHoldTimeInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpSessionHoldTimeInUse.setStatus(_A)
_CienaCesLdpHelloAdjacencyTable_Object=MibTable
cienaCesLdpHelloAdjacencyTable=_CienaCesLdpHelloAdjacencyTable_Object((1,3,6,1,4,1,1271,2,1,17,1,2,2))
if mibBuilder.loadTexts:cienaCesLdpHelloAdjacencyTable.setStatus(_A)
_CienaCesLdpHelloAdjacencyEntry_Object=MibTableRow
cienaCesLdpHelloAdjacencyEntry=_CienaCesLdpHelloAdjacencyEntry_Object((1,3,6,1,4,1,1271,2,1,17,1,2,2,1))
cienaCesLdpHelloAdjacencyEntry.setIndexNames((0,_D,_H),(0,_D,_I),(0,_D,_J),(0,_D,_L))
if mibBuilder.loadTexts:cienaCesLdpHelloAdjacencyEntry.setStatus(_A)
class _CienaCesLdpHelloAdjacencyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CienaCesLdpHelloAdjacencyIndex_Type.__name__=_C
_CienaCesLdpHelloAdjacencyIndex_Object=MibTableColumn
cienaCesLdpHelloAdjacencyIndex=_CienaCesLdpHelloAdjacencyIndex_Object((1,3,6,1,4,1,1271,2,1,17,1,2,2,1,1),_CienaCesLdpHelloAdjacencyIndex_Type())
cienaCesLdpHelloAdjacencyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesLdpHelloAdjacencyIndex.setStatus(_A)
_CienaCesLdpHelloAdjacencyConfiguredHoldTime_Type=Unsigned32
_CienaCesLdpHelloAdjacencyConfiguredHoldTime_Object=MibTableColumn
cienaCesLdpHelloAdjacencyConfiguredHoldTime=_CienaCesLdpHelloAdjacencyConfiguredHoldTime_Object((1,3,6,1,4,1,1271,2,1,17,1,2,2,1,2),_CienaCesLdpHelloAdjacencyConfiguredHoldTime_Type())
cienaCesLdpHelloAdjacencyConfiguredHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpHelloAdjacencyConfiguredHoldTime.setStatus(_A)
_CienaCesLdpHelloAdjacencyPeerHoldTime_Type=Unsigned32
_CienaCesLdpHelloAdjacencyPeerHoldTime_Object=MibTableColumn
cienaCesLdpHelloAdjacencyPeerHoldTime=_CienaCesLdpHelloAdjacencyPeerHoldTime_Object((1,3,6,1,4,1,1271,2,1,17,1,2,2,1,3),_CienaCesLdpHelloAdjacencyPeerHoldTime_Type())
cienaCesLdpHelloAdjacencyPeerHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLdpHelloAdjacencyPeerHoldTime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cienaCesLdpMIB':cienaCesLdpMIB,'cienaCesLdpMIBObjects':cienaCesLdpMIBObjects,'cienaCesLdpObjects':cienaCesLdpObjects,'cienaCesLdpAdminStatus':cienaCesLdpAdminStatus,'cienaCesLdpOperStatus':cienaCesLdpOperStatus,'cienaCesLdpHelloHoldTime':cienaCesLdpHelloHoldTime,'cienaCesLdpKeepAliveHoldTime':cienaCesLdpKeepAliveHoldTime,'cienaCesLdpGRAdminStatus':cienaCesLdpGRAdminStatus,'cienaCesLdpGRMode':cienaCesLdpGRMode,'cienaCesLdpReconnectTime':cienaCesLdpReconnectTime,'cienaCesLdpRecoveryTime':cienaCesLdpRecoveryTime,'cienaCesLdpMaxPeerReconnect':cienaCesLdpMaxPeerReconnect,'cienaCesLdpMaxPeerRecovery':cienaCesLdpMaxPeerRecovery,'cienaCesLdp':cienaCesLdp,'cienaCesLdpSessionTable':cienaCesLdpSessionTable,'cienaCesLdpSessionEntry':cienaCesLdpSessionEntry,_H:cienaCesLdpEntityLdpId,_I:cienaCesLdpEntityIndex,_J:cienaCesLdpPeerLdpId,'cienaCesLdpSessionConfiguredHoldTime':cienaCesLdpSessionConfiguredHoldTime,'cienaCesLdpSessionPeerHoldTime':cienaCesLdpSessionPeerHoldTime,'cienaCesLdpSessionHoldTimeInUse':cienaCesLdpSessionHoldTimeInUse,'cienaCesLdpHelloAdjacencyTable':cienaCesLdpHelloAdjacencyTable,'cienaCesLdpHelloAdjacencyEntry':cienaCesLdpHelloAdjacencyEntry,_L:cienaCesLdpHelloAdjacencyIndex,'cienaCesLdpHelloAdjacencyConfiguredHoldTime':cienaCesLdpHelloAdjacencyConfiguredHoldTime,'cienaCesLdpHelloAdjacencyPeerHoldTime':cienaCesLdpHelloAdjacencyPeerHoldTime})