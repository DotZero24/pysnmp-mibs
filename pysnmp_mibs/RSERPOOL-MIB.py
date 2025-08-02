_Aa='rserpoolPUGroup'
_AZ='rserpoolPEGroup'
_AY='rserpoolENRPGroup'
_AX='rserpoolPUUptime'
_AW='rserpoolPUDescription'
_AV='rserpoolPUPoolHandle'
_AU='rserpoolPUOperationScope'
_AT='rserpoolPEUserL3Opaque'
_AS='rserpoolPEUserL3Addr'
_AR='rserpoolPEUserL3Type'
_AQ='rserpoolPEASAPL3Addr'
_AP='rserpoolPEASAPL3Type'
_AO='rserpoolPEHomeENRPServer'
_AN='rserpoolPERegistrationLife'
_AM='rserpoolPEPolicyLoadDeg'
_AL='rserpoolPEPolicyLoad'
_AK='rserpoolPEPolicyWeight'
_AJ='rserpoolPEPolicyDescription'
_AI='rserpoolPEPolicyID'
_AH='rserpoolPEUserTransportUse'
_AG='rserpoolPEUserTransportPort'
_AF='rserpoolPEUserTransportProto'
_AE='rserpoolPEASAPTransportPort'
_AD='rserpoolPEUptime'
_AC='rserpoolPEDescription'
_AB='rserpoolPEIdentifier'
_AA='rserpoolPEPoolHandle'
_A9='rserpoolPEOperationScope'
_A8='rserpoolENRPPeerL3Addr'
_A7='rserpoolENRPPeerL3Type'
_A6='rserpoolENRPPeerLastHeard'
_A5='rserpoolENRPPeerPort'
_A4='rserpoolENRPPeerIdentifier'
_A3='rserpoolENRPENRPL3Addr'
_A2='rserpoolENRPENRPL3Type'
_A1='rserpoolENRPUserL3Opaque'
_A0='rserpoolENRPUserL3Addr'
_z='rserpoolENRPUserL3Type'
_y='rserpoolENRPASAPL3Addr'
_x='rserpoolENRPASAPL3Type'
_w='rserpoolENRPHomeENRPServer'
_v='rserpoolENRPRegistrationLife'
_u='rserpoolENRPPolicyLoadDeg'
_t='rserpoolENRPPolicyLoad'
_s='rserpoolENRPPolicyWeight'
_r='rserpoolENRPPolicyDescription'
_q='rserpoolENRPPolicyID'
_p='rserpoolENRPUserTransportPort'
_o='rserpoolENRPUserTransportUse'
_n='rserpoolENRPUserTransportProto'
_m='rserpoolENRPASAPTransportPort'
_l='rserpoolENRPPoolElementID'
_k='rserpoolENRPPoolHandle'
_j='rserpoolENRPENRPAnnounceAddr'
_i='rserpoolENRPENRPAnnouncePort'
_h='rserpoolENRPENRPAnnounceAddrType'
_g='rserpoolENRPASAPAnnounceAddrType'
_f='rserpoolENRPASAPAnnounceAddr'
_e='rserpoolENRPASAPAnnouncePort'
_d='rserpoolENRPPort'
_c='rserpoolENRPUptime'
_b='rserpoolENRPDescription'
_a='rserpoolENRPIdentifier'
_Z='rserpoolENRPOperationScope'
_Y='rserpoolPUIndex'
_X='rserpoolPEUserAddrTableIndex'
_W='rserpoolPEASAPAddrTableIndex'
_V='rserpoolENRPPeerAddrTableIndex'
_U='rserpoolENRPENRPAddrTableIndex'
_T='unknown'
_S='rserpoolENRPUserAddrTableIndex'
_R='rserpoolENRPASAPAddrTableIndex'
_Q='rserpoolENRPPeerIndex'
_P='1024t'
_O='rserpoolPEIndex'
_N='rserpoolENRPPoolElementIndex'
_M='rserpoolENRPPoolIndex'
_L='OctetString'
_K='rserpoolENRPIndex'
_J='ipv6'
_I='ipv4'
_H='InetAddressType'
_G='InetAddress'
_F='read-write'
_E='not-accessible'
_D='Unsigned32'
_C='read-only'
_B='RSERPOOL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,_H,'InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'experimental','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rserpoolMIB=ModuleIdentity((1,3,6,1,3,125))
if mibBuilder.loadTexts:rserpoolMIB.setRevisions(('2009-04-07 00:00',))
class RSerPoolENRPServerIdentifierTC(TextualConvention,Unsigned32):status=_A;displayHint='x';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class RSerPoolOperationScopeTC(TextualConvention,OctetString):status=_A;displayHint=_P;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
class RSerPoolPoolHandleTC(TextualConvention,OctetString):status=_A;displayHint=_P;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
class RserpoolPoolElementIdentifierTC(TextualConvention,Unsigned32):status=_A;displayHint='x';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class RSerPoolPolicyIdentifierTC(TextualConvention,Unsigned32):status=_A;displayHint='x';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class RSerPoolPolicyLoadTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class RSerPoolPolicyWeightTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class RSerPoolTransportUseTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dataOnly',0),('dataPlusControl',1)))
class RSerPoolOpaqueAddressTC(TextualConvention,OctetString):status=_A;displayHint=_P;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_RserpoolMIBObjects_ObjectIdentity=ObjectIdentity
rserpoolMIBObjects=_RserpoolMIBObjects_ObjectIdentity((1,3,6,1,3,125,1))
_RserpoolENRPServers_ObjectIdentity=ObjectIdentity
rserpoolENRPServers=_RserpoolENRPServers_ObjectIdentity((1,3,6,1,3,125,1,1))
_RserpoolENRPTable_Object=MibTable
rserpoolENRPTable=_RserpoolENRPTable_Object((1,3,6,1,3,125,1,1,1))
if mibBuilder.loadTexts:rserpoolENRPTable.setStatus(_A)
_RserpoolENRPEntry_Object=MibTableRow
rserpoolENRPEntry=_RserpoolENRPEntry_Object((1,3,6,1,3,125,1,1,1,1))
rserpoolENRPEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:rserpoolENRPEntry.setStatus(_A)
class _RserpoolENRPIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RserpoolENRPIndex_Type.__name__=_D
_RserpoolENRPIndex_Object=MibTableColumn
rserpoolENRPIndex=_RserpoolENRPIndex_Object((1,3,6,1,3,125,1,1,1,1,1),_RserpoolENRPIndex_Type())
rserpoolENRPIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rserpoolENRPIndex.setStatus(_A)
_RserpoolENRPOperationScope_Type=RSerPoolOperationScopeTC
_RserpoolENRPOperationScope_Object=MibTableColumn
rserpoolENRPOperationScope=_RserpoolENRPOperationScope_Object((1,3,6,1,3,125,1,1,1,1,2),_RserpoolENRPOperationScope_Type())
rserpoolENRPOperationScope.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPOperationScope.setStatus(_A)
_RserpoolENRPIdentifier_Type=RSerPoolENRPServerIdentifierTC
_RserpoolENRPIdentifier_Object=MibTableColumn
rserpoolENRPIdentifier=_RserpoolENRPIdentifier_Object((1,3,6,1,3,125,1,1,1,1,3),_RserpoolENRPIdentifier_Type())
rserpoolENRPIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPIdentifier.setStatus(_A)
class _RserpoolENRPDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RserpoolENRPDescription_Type.__name__=_L
_RserpoolENRPDescription_Object=MibTableColumn
rserpoolENRPDescription=_RserpoolENRPDescription_Object((1,3,6,1,3,125,1,1,1,1,4),_RserpoolENRPDescription_Type())
rserpoolENRPDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:rserpoolENRPDescription.setStatus(_A)
_RserpoolENRPUptime_Type=TimeTicks
_RserpoolENRPUptime_Object=MibTableColumn
rserpoolENRPUptime=_RserpoolENRPUptime_Object((1,3,6,1,3,125,1,1,1,1,5),_RserpoolENRPUptime_Type())
rserpoolENRPUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPUptime.setStatus(_A)
_RserpoolENRPPort_Type=InetPortNumber
_RserpoolENRPPort_Object=MibTableColumn
rserpoolENRPPort=_RserpoolENRPPort_Object((1,3,6,1,3,125,1,1,1,1,6),_RserpoolENRPPort_Type())
rserpoolENRPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPort.setStatus(_A)
_RserpoolENRPASAPAnnouncePort_Type=InetPortNumber
_RserpoolENRPASAPAnnouncePort_Object=MibTableColumn
rserpoolENRPASAPAnnouncePort=_RserpoolENRPASAPAnnouncePort_Object((1,3,6,1,3,125,1,1,1,1,7),_RserpoolENRPASAPAnnouncePort_Type())
rserpoolENRPASAPAnnouncePort.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPASAPAnnouncePort.setStatus(_A)
class _RserpoolENRPASAPAnnounceAddrType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RserpoolENRPASAPAnnounceAddrType_Type.__name__=_H
_RserpoolENRPASAPAnnounceAddrType_Object=MibTableColumn
rserpoolENRPASAPAnnounceAddrType=_RserpoolENRPASAPAnnounceAddrType_Object((1,3,6,1,3,125,1,1,1,1,8),_RserpoolENRPASAPAnnounceAddrType_Type())
rserpoolENRPASAPAnnounceAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPASAPAnnounceAddrType.setStatus(_A)
class _RserpoolENRPASAPAnnounceAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_RserpoolENRPASAPAnnounceAddr_Type.__name__=_G
_RserpoolENRPASAPAnnounceAddr_Object=MibTableColumn
rserpoolENRPASAPAnnounceAddr=_RserpoolENRPASAPAnnounceAddr_Object((1,3,6,1,3,125,1,1,1,1,9),_RserpoolENRPASAPAnnounceAddr_Type())
rserpoolENRPASAPAnnounceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPASAPAnnounceAddr.setStatus(_A)
_RserpoolENRPENRPAnnouncePort_Type=InetPortNumber
_RserpoolENRPENRPAnnouncePort_Object=MibTableColumn
rserpoolENRPENRPAnnouncePort=_RserpoolENRPENRPAnnouncePort_Object((1,3,6,1,3,125,1,1,1,1,10),_RserpoolENRPENRPAnnouncePort_Type())
rserpoolENRPENRPAnnouncePort.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPENRPAnnouncePort.setStatus(_A)
class _RserpoolENRPENRPAnnounceAddrType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RserpoolENRPENRPAnnounceAddrType_Type.__name__=_H
_RserpoolENRPENRPAnnounceAddrType_Object=MibTableColumn
rserpoolENRPENRPAnnounceAddrType=_RserpoolENRPENRPAnnounceAddrType_Object((1,3,6,1,3,125,1,1,1,1,11),_RserpoolENRPENRPAnnounceAddrType_Type())
rserpoolENRPENRPAnnounceAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPENRPAnnounceAddrType.setStatus(_A)
class _RserpoolENRPENRPAnnounceAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_RserpoolENRPENRPAnnounceAddr_Type.__name__=_G
_RserpoolENRPENRPAnnounceAddr_Object=MibTableColumn
rserpoolENRPENRPAnnounceAddr=_RserpoolENRPENRPAnnounceAddr_Object((1,3,6,1,3,125,1,1,1,1,12),_RserpoolENRPENRPAnnounceAddr_Type())
rserpoolENRPENRPAnnounceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPENRPAnnounceAddr.setStatus(_A)
_RserpoolENRPPoolTable_Object=MibTable
rserpoolENRPPoolTable=_RserpoolENRPPoolTable_Object((1,3,6,1,3,125,1,1,3))
if mibBuilder.loadTexts:rserpoolENRPPoolTable.setStatus(_A)
_RserpoolENRPPoolEntry_Object=MibTableRow
rserpoolENRPPoolEntry=_RserpoolENRPPoolEntry_Object((1,3,6,1,3,125,1,1,3,1))
rserpoolENRPPoolEntry.setIndexNames((0,_B,_K),(0,_B,_M))
if mibBuilder.loadTexts:rserpoolENRPPoolEntry.setStatus(_A)
class _RserpoolENRPPoolIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RserpoolENRPPoolIndex_Type.__name__=_D
_RserpoolENRPPoolIndex_Object=MibTableColumn
rserpoolENRPPoolIndex=_RserpoolENRPPoolIndex_Object((1,3,6,1,3,125,1,1,3,1,1),_RserpoolENRPPoolIndex_Type())
rserpoolENRPPoolIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rserpoolENRPPoolIndex.setStatus(_A)
_RserpoolENRPPoolHandle_Type=RSerPoolPoolHandleTC
_RserpoolENRPPoolHandle_Object=MibTableColumn
rserpoolENRPPoolHandle=_RserpoolENRPPoolHandle_Object((1,3,6,1,3,125,1,1,3,1,2),_RserpoolENRPPoolHandle_Type())
rserpoolENRPPoolHandle.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPoolHandle.setStatus(_A)
_RserpoolENRPPoolElementTable_Object=MibTable
rserpoolENRPPoolElementTable=_RserpoolENRPPoolElementTable_Object((1,3,6,1,3,125,1,1,4))
if mibBuilder.loadTexts:rserpoolENRPPoolElementTable.setStatus(_A)
_RserpoolENRPPoolElementEntry_Object=MibTableRow
rserpoolENRPPoolElementEntry=_RserpoolENRPPoolElementEntry_Object((1,3,6,1,3,125,1,1,4,1))
rserpoolENRPPoolElementEntry.setIndexNames((0,_B,_K),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:rserpoolENRPPoolElementEntry.setStatus(_A)
class _RserpoolENRPPoolElementIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RserpoolENRPPoolElementIndex_Type.__name__=_D
_RserpoolENRPPoolElementIndex_Object=MibTableColumn
rserpoolENRPPoolElementIndex=_RserpoolENRPPoolElementIndex_Object((1,3,6,1,3,125,1,1,4,1,1),_RserpoolENRPPoolElementIndex_Type())
rserpoolENRPPoolElementIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rserpoolENRPPoolElementIndex.setStatus(_A)
_RserpoolENRPPoolElementID_Type=RserpoolPoolElementIdentifierTC
_RserpoolENRPPoolElementID_Object=MibTableColumn
rserpoolENRPPoolElementID=_RserpoolENRPPoolElementID_Object((1,3,6,1,3,125,1,1,4,1,2),_RserpoolENRPPoolElementID_Type())
rserpoolENRPPoolElementID.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPoolElementID.setStatus(_A)
_RserpoolENRPASAPTransportPort_Type=InetPortNumber
_RserpoolENRPASAPTransportPort_Object=MibTableColumn
rserpoolENRPASAPTransportPort=_RserpoolENRPASAPTransportPort_Object((1,3,6,1,3,125,1,1,4,1,3),_RserpoolENRPASAPTransportPort_Type())
rserpoolENRPASAPTransportPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPASAPTransportPort.setStatus(_A)
class _RserpoolENRPUserTransportProto_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RserpoolENRPUserTransportProto_Type.__name__=_D
_RserpoolENRPUserTransportProto_Object=MibTableColumn
rserpoolENRPUserTransportProto=_RserpoolENRPUserTransportProto_Object((1,3,6,1,3,125,1,1,4,1,4),_RserpoolENRPUserTransportProto_Type())
rserpoolENRPUserTransportProto.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPUserTransportProto.setStatus(_A)
_RserpoolENRPUserTransportPort_Type=InetPortNumber
_RserpoolENRPUserTransportPort_Object=MibTableColumn
rserpoolENRPUserTransportPort=_RserpoolENRPUserTransportPort_Object((1,3,6,1,3,125,1,1,4,1,5),_RserpoolENRPUserTransportPort_Type())
rserpoolENRPUserTransportPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPUserTransportPort.setStatus(_A)
_RserpoolENRPUserTransportUse_Type=RSerPoolTransportUseTypeTC
_RserpoolENRPUserTransportUse_Object=MibTableColumn
rserpoolENRPUserTransportUse=_RserpoolENRPUserTransportUse_Object((1,3,6,1,3,125,1,1,4,1,6),_RserpoolENRPUserTransportUse_Type())
rserpoolENRPUserTransportUse.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPUserTransportUse.setStatus(_A)
_RserpoolENRPPolicyID_Type=RSerPoolPolicyIdentifierTC
_RserpoolENRPPolicyID_Object=MibTableColumn
rserpoolENRPPolicyID=_RserpoolENRPPolicyID_Object((1,3,6,1,3,125,1,1,4,1,7),_RserpoolENRPPolicyID_Type())
rserpoolENRPPolicyID.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPolicyID.setStatus(_A)
class _RserpoolENRPPolicyDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RserpoolENRPPolicyDescription_Type.__name__=_L
_RserpoolENRPPolicyDescription_Object=MibTableColumn
rserpoolENRPPolicyDescription=_RserpoolENRPPolicyDescription_Object((1,3,6,1,3,125,1,1,4,1,8),_RserpoolENRPPolicyDescription_Type())
rserpoolENRPPolicyDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPolicyDescription.setStatus(_A)
_RserpoolENRPPolicyWeight_Type=RSerPoolPolicyWeightTC
_RserpoolENRPPolicyWeight_Object=MibTableColumn
rserpoolENRPPolicyWeight=_RserpoolENRPPolicyWeight_Object((1,3,6,1,3,125,1,1,4,1,9),_RserpoolENRPPolicyWeight_Type())
rserpoolENRPPolicyWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPolicyWeight.setStatus(_A)
_RserpoolENRPPolicyLoad_Type=RSerPoolPolicyLoadTC
_RserpoolENRPPolicyLoad_Object=MibTableColumn
rserpoolENRPPolicyLoad=_RserpoolENRPPolicyLoad_Object((1,3,6,1,3,125,1,1,4,1,10),_RserpoolENRPPolicyLoad_Type())
rserpoolENRPPolicyLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPolicyLoad.setStatus(_A)
_RserpoolENRPPolicyLoadDeg_Type=RSerPoolPolicyLoadTC
_RserpoolENRPPolicyLoadDeg_Object=MibTableColumn
rserpoolENRPPolicyLoadDeg=_RserpoolENRPPolicyLoadDeg_Object((1,3,6,1,3,125,1,1,4,1,11),_RserpoolENRPPolicyLoadDeg_Type())
rserpoolENRPPolicyLoadDeg.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPolicyLoadDeg.setStatus(_A)
_RserpoolENRPRegistrationLife_Type=TimeTicks
_RserpoolENRPRegistrationLife_Object=MibTableColumn
rserpoolENRPRegistrationLife=_RserpoolENRPRegistrationLife_Object((1,3,6,1,3,125,1,1,4,1,12),_RserpoolENRPRegistrationLife_Type())
rserpoolENRPRegistrationLife.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPRegistrationLife.setStatus(_A)
_RserpoolENRPHomeENRPServer_Type=RSerPoolENRPServerIdentifierTC
_RserpoolENRPHomeENRPServer_Object=MibTableColumn
rserpoolENRPHomeENRPServer=_RserpoolENRPHomeENRPServer_Object((1,3,6,1,3,125,1,1,4,1,13),_RserpoolENRPHomeENRPServer_Type())
rserpoolENRPHomeENRPServer.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPHomeENRPServer.setStatus(_A)
_RserpoolENRPASAPAddrTable_Object=MibTable
rserpoolENRPASAPAddrTable=_RserpoolENRPASAPAddrTable_Object((1,3,6,1,3,125,1,1,5))
if mibBuilder.loadTexts:rserpoolENRPASAPAddrTable.setStatus(_A)
_RserpoolENRPASAPAddrTableEntry_Object=MibTableRow
rserpoolENRPASAPAddrTableEntry=_RserpoolENRPASAPAddrTableEntry_Object((1,3,6,1,3,125,1,1,5,1))
rserpoolENRPASAPAddrTableEntry.setIndexNames((0,_B,_K),(0,_B,_M),(0,_B,_N),(0,_B,_R))
if mibBuilder.loadTexts:rserpoolENRPASAPAddrTableEntry.setStatus(_A)
class _RserpoolENRPASAPAddrTableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RserpoolENRPASAPAddrTableIndex_Type.__name__=_D
_RserpoolENRPASAPAddrTableIndex_Object=MibTableColumn
rserpoolENRPASAPAddrTableIndex=_RserpoolENRPASAPAddrTableIndex_Object((1,3,6,1,3,125,1,1,5,1,1),_RserpoolENRPASAPAddrTableIndex_Type())
rserpoolENRPASAPAddrTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rserpoolENRPASAPAddrTableIndex.setStatus(_A)
class _RserpoolENRPASAPL3Type_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RserpoolENRPASAPL3Type_Type.__name__=_H
_RserpoolENRPASAPL3Type_Object=MibTableColumn
rserpoolENRPASAPL3Type=_RserpoolENRPASAPL3Type_Object((1,3,6,1,3,125,1,1,5,1,2),_RserpoolENRPASAPL3Type_Type())
rserpoolENRPASAPL3Type.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPASAPL3Type.setStatus(_A)
class _RserpoolENRPASAPL3Addr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_RserpoolENRPASAPL3Addr_Type.__name__=_G
_RserpoolENRPASAPL3Addr_Object=MibTableColumn
rserpoolENRPASAPL3Addr=_RserpoolENRPASAPL3Addr_Object((1,3,6,1,3,125,1,1,5,1,3),_RserpoolENRPASAPL3Addr_Type())
rserpoolENRPASAPL3Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPASAPL3Addr.setStatus(_A)
_RserpoolENRPUserAddrTable_Object=MibTable
rserpoolENRPUserAddrTable=_RserpoolENRPUserAddrTable_Object((1,3,6,1,3,125,1,1,6))
if mibBuilder.loadTexts:rserpoolENRPUserAddrTable.setStatus(_A)
_RserpoolENRPUserAddrTableEntry_Object=MibTableRow
rserpoolENRPUserAddrTableEntry=_RserpoolENRPUserAddrTableEntry_Object((1,3,6,1,3,125,1,1,6,1))
rserpoolENRPUserAddrTableEntry.setIndexNames((0,_B,_K),(0,_B,_M),(0,_B,_N),(0,_B,_S))
if mibBuilder.loadTexts:rserpoolENRPUserAddrTableEntry.setStatus(_A)
class _RserpoolENRPUserAddrTableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RserpoolENRPUserAddrTableIndex_Type.__name__=_D
_RserpoolENRPUserAddrTableIndex_Object=MibTableColumn
rserpoolENRPUserAddrTableIndex=_RserpoolENRPUserAddrTableIndex_Object((1,3,6,1,3,125,1,1,6,1,1),_RserpoolENRPUserAddrTableIndex_Type())
rserpoolENRPUserAddrTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rserpoolENRPUserAddrTableIndex.setStatus(_A)
class _RserpoolENRPUserL3Type_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),(_I,1),(_J,2)))
_RserpoolENRPUserL3Type_Type.__name__=_H
_RserpoolENRPUserL3Type_Object=MibTableColumn
rserpoolENRPUserL3Type=_RserpoolENRPUserL3Type_Object((1,3,6,1,3,125,1,1,6,1,2),_RserpoolENRPUserL3Type_Type())
rserpoolENRPUserL3Type.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPUserL3Type.setStatus(_A)
class _RserpoolENRPUserL3Addr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_RserpoolENRPUserL3Addr_Type.__name__=_G
_RserpoolENRPUserL3Addr_Object=MibTableColumn
rserpoolENRPUserL3Addr=_RserpoolENRPUserL3Addr_Object((1,3,6,1,3,125,1,1,6,1,3),_RserpoolENRPUserL3Addr_Type())
rserpoolENRPUserL3Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPUserL3Addr.setStatus(_A)
_RserpoolENRPUserL3Opaque_Type=RSerPoolOpaqueAddressTC
_RserpoolENRPUserL3Opaque_Object=MibTableColumn
rserpoolENRPUserL3Opaque=_RserpoolENRPUserL3Opaque_Object((1,3,6,1,3,125,1,1,6,1,4),_RserpoolENRPUserL3Opaque_Type())
rserpoolENRPUserL3Opaque.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPUserL3Opaque.setStatus(_A)
_RserpoolENRPENRPAddrTable_Object=MibTable
rserpoolENRPENRPAddrTable=_RserpoolENRPENRPAddrTable_Object((1,3,6,1,3,125,1,1,7))
if mibBuilder.loadTexts:rserpoolENRPENRPAddrTable.setStatus(_A)
_RserpoolENRPENRPAddrTableEntry_Object=MibTableRow
rserpoolENRPENRPAddrTableEntry=_RserpoolENRPENRPAddrTableEntry_Object((1,3,6,1,3,125,1,1,7,1))
rserpoolENRPENRPAddrTableEntry.setIndexNames((0,_B,_K),(0,_B,_U))
if mibBuilder.loadTexts:rserpoolENRPENRPAddrTableEntry.setStatus(_A)
class _RserpoolENRPENRPAddrTableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RserpoolENRPENRPAddrTableIndex_Type.__name__=_D
_RserpoolENRPENRPAddrTableIndex_Object=MibTableColumn
rserpoolENRPENRPAddrTableIndex=_RserpoolENRPENRPAddrTableIndex_Object((1,3,6,1,3,125,1,1,7,1,1),_RserpoolENRPENRPAddrTableIndex_Type())
rserpoolENRPENRPAddrTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rserpoolENRPENRPAddrTableIndex.setStatus(_A)
class _RserpoolENRPENRPL3Type_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RserpoolENRPENRPL3Type_Type.__name__=_H
_RserpoolENRPENRPL3Type_Object=MibTableColumn
rserpoolENRPENRPL3Type=_RserpoolENRPENRPL3Type_Object((1,3,6,1,3,125,1,1,7,1,2),_RserpoolENRPENRPL3Type_Type())
rserpoolENRPENRPL3Type.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPENRPL3Type.setStatus(_A)
class _RserpoolENRPENRPL3Addr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_RserpoolENRPENRPL3Addr_Type.__name__=_G
_RserpoolENRPENRPL3Addr_Object=MibTableColumn
rserpoolENRPENRPL3Addr=_RserpoolENRPENRPL3Addr_Object((1,3,6,1,3,125,1,1,7,1,3),_RserpoolENRPENRPL3Addr_Type())
rserpoolENRPENRPL3Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPENRPL3Addr.setStatus(_A)
_RserpoolENRPPeerTable_Object=MibTable
rserpoolENRPPeerTable=_RserpoolENRPPeerTable_Object((1,3,6,1,3,125,1,1,8))
if mibBuilder.loadTexts:rserpoolENRPPeerTable.setStatus(_A)
_RserpoolENRPPeerEntry_Object=MibTableRow
rserpoolENRPPeerEntry=_RserpoolENRPPeerEntry_Object((1,3,6,1,3,125,1,1,8,1))
rserpoolENRPPeerEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:rserpoolENRPPeerEntry.setStatus(_A)
class _RserpoolENRPPeerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RserpoolENRPPeerIndex_Type.__name__=_D
_RserpoolENRPPeerIndex_Object=MibTableColumn
rserpoolENRPPeerIndex=_RserpoolENRPPeerIndex_Object((1,3,6,1,3,125,1,1,8,1,1),_RserpoolENRPPeerIndex_Type())
rserpoolENRPPeerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rserpoolENRPPeerIndex.setStatus(_A)
_RserpoolENRPPeerIdentifier_Type=RSerPoolENRPServerIdentifierTC
_RserpoolENRPPeerIdentifier_Object=MibTableColumn
rserpoolENRPPeerIdentifier=_RserpoolENRPPeerIdentifier_Object((1,3,6,1,3,125,1,1,8,1,2),_RserpoolENRPPeerIdentifier_Type())
rserpoolENRPPeerIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPeerIdentifier.setStatus(_A)
_RserpoolENRPPeerPort_Type=InetPortNumber
_RserpoolENRPPeerPort_Object=MibTableColumn
rserpoolENRPPeerPort=_RserpoolENRPPeerPort_Object((1,3,6,1,3,125,1,1,8,1,3),_RserpoolENRPPeerPort_Type())
rserpoolENRPPeerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPeerPort.setStatus(_A)
_RserpoolENRPPeerLastHeard_Type=TimeTicks
_RserpoolENRPPeerLastHeard_Object=MibTableColumn
rserpoolENRPPeerLastHeard=_RserpoolENRPPeerLastHeard_Object((1,3,6,1,3,125,1,1,8,1,4),_RserpoolENRPPeerLastHeard_Type())
rserpoolENRPPeerLastHeard.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPeerLastHeard.setStatus(_A)
_RserpoolENRPPeerAddrTable_Object=MibTable
rserpoolENRPPeerAddrTable=_RserpoolENRPPeerAddrTable_Object((1,3,6,1,3,125,1,1,9))
if mibBuilder.loadTexts:rserpoolENRPPeerAddrTable.setStatus(_A)
_RserpoolENRPPeerAddrTableEntry_Object=MibTableRow
rserpoolENRPPeerAddrTableEntry=_RserpoolENRPPeerAddrTableEntry_Object((1,3,6,1,3,125,1,1,9,1))
rserpoolENRPPeerAddrTableEntry.setIndexNames((0,_B,_Q),(0,_B,_V))
if mibBuilder.loadTexts:rserpoolENRPPeerAddrTableEntry.setStatus(_A)
class _RserpoolENRPPeerAddrTableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RserpoolENRPPeerAddrTableIndex_Type.__name__=_D
_RserpoolENRPPeerAddrTableIndex_Object=MibTableColumn
rserpoolENRPPeerAddrTableIndex=_RserpoolENRPPeerAddrTableIndex_Object((1,3,6,1,3,125,1,1,9,1,1),_RserpoolENRPPeerAddrTableIndex_Type())
rserpoolENRPPeerAddrTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rserpoolENRPPeerAddrTableIndex.setStatus(_A)
class _RserpoolENRPPeerL3Type_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RserpoolENRPPeerL3Type_Type.__name__=_H
_RserpoolENRPPeerL3Type_Object=MibTableColumn
rserpoolENRPPeerL3Type=_RserpoolENRPPeerL3Type_Object((1,3,6,1,3,125,1,1,9,1,2),_RserpoolENRPPeerL3Type_Type())
rserpoolENRPPeerL3Type.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPeerL3Type.setStatus(_A)
class _RserpoolENRPPeerL3Addr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_RserpoolENRPPeerL3Addr_Type.__name__=_G
_RserpoolENRPPeerL3Addr_Object=MibTableColumn
rserpoolENRPPeerL3Addr=_RserpoolENRPPeerL3Addr_Object((1,3,6,1,3,125,1,1,9,1,3),_RserpoolENRPPeerL3Addr_Type())
rserpoolENRPPeerL3Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolENRPPeerL3Addr.setStatus(_A)
_RserpoolPoolElements_ObjectIdentity=ObjectIdentity
rserpoolPoolElements=_RserpoolPoolElements_ObjectIdentity((1,3,6,1,3,125,1,2))
_RserpoolPETable_Object=MibTable
rserpoolPETable=_RserpoolPETable_Object((1,3,6,1,3,125,1,2,1))
if mibBuilder.loadTexts:rserpoolPETable.setStatus(_A)
_RserpoolPEEntry_Object=MibTableRow
rserpoolPEEntry=_RserpoolPEEntry_Object((1,3,6,1,3,125,1,2,1,1))
rserpoolPEEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:rserpoolPEEntry.setStatus(_A)
class _RserpoolPEIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RserpoolPEIndex_Type.__name__=_D
_RserpoolPEIndex_Object=MibTableColumn
rserpoolPEIndex=_RserpoolPEIndex_Object((1,3,6,1,3,125,1,2,1,1,1),_RserpoolPEIndex_Type())
rserpoolPEIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rserpoolPEIndex.setStatus(_A)
_RserpoolPEOperationScope_Type=RSerPoolOperationScopeTC
_RserpoolPEOperationScope_Object=MibTableColumn
rserpoolPEOperationScope=_RserpoolPEOperationScope_Object((1,3,6,1,3,125,1,2,1,1,2),_RserpoolPEOperationScope_Type())
rserpoolPEOperationScope.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEOperationScope.setStatus(_A)
_RserpoolPEPoolHandle_Type=RSerPoolPoolHandleTC
_RserpoolPEPoolHandle_Object=MibTableColumn
rserpoolPEPoolHandle=_RserpoolPEPoolHandle_Object((1,3,6,1,3,125,1,2,1,1,3),_RserpoolPEPoolHandle_Type())
rserpoolPEPoolHandle.setMaxAccess(_F)
if mibBuilder.loadTexts:rserpoolPEPoolHandle.setStatus(_A)
_RserpoolPEIdentifier_Type=RserpoolPoolElementIdentifierTC
_RserpoolPEIdentifier_Object=MibTableColumn
rserpoolPEIdentifier=_RserpoolPEIdentifier_Object((1,3,6,1,3,125,1,2,1,1,4),_RserpoolPEIdentifier_Type())
rserpoolPEIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEIdentifier.setStatus(_A)
class _RserpoolPEDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RserpoolPEDescription_Type.__name__=_L
_RserpoolPEDescription_Object=MibTableColumn
rserpoolPEDescription=_RserpoolPEDescription_Object((1,3,6,1,3,125,1,2,1,1,5),_RserpoolPEDescription_Type())
rserpoolPEDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:rserpoolPEDescription.setStatus(_A)
_RserpoolPEUptime_Type=TimeTicks
_RserpoolPEUptime_Object=MibTableColumn
rserpoolPEUptime=_RserpoolPEUptime_Object((1,3,6,1,3,125,1,2,1,1,6),_RserpoolPEUptime_Type())
rserpoolPEUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEUptime.setStatus(_A)
_RserpoolPEASAPTransportPort_Type=InetPortNumber
_RserpoolPEASAPTransportPort_Object=MibTableColumn
rserpoolPEASAPTransportPort=_RserpoolPEASAPTransportPort_Object((1,3,6,1,3,125,1,2,1,1,7),_RserpoolPEASAPTransportPort_Type())
rserpoolPEASAPTransportPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEASAPTransportPort.setStatus(_A)
class _RserpoolPEUserTransportProto_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RserpoolPEUserTransportProto_Type.__name__=_D
_RserpoolPEUserTransportProto_Object=MibTableColumn
rserpoolPEUserTransportProto=_RserpoolPEUserTransportProto_Object((1,3,6,1,3,125,1,2,1,1,8),_RserpoolPEUserTransportProto_Type())
rserpoolPEUserTransportProto.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEUserTransportProto.setStatus(_A)
_RserpoolPEUserTransportPort_Type=InetPortNumber
_RserpoolPEUserTransportPort_Object=MibTableColumn
rserpoolPEUserTransportPort=_RserpoolPEUserTransportPort_Object((1,3,6,1,3,125,1,2,1,1,9),_RserpoolPEUserTransportPort_Type())
rserpoolPEUserTransportPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEUserTransportPort.setStatus(_A)
_RserpoolPEUserTransportUse_Type=RSerPoolTransportUseTypeTC
_RserpoolPEUserTransportUse_Object=MibTableColumn
rserpoolPEUserTransportUse=_RserpoolPEUserTransportUse_Object((1,3,6,1,3,125,1,2,1,1,10),_RserpoolPEUserTransportUse_Type())
rserpoolPEUserTransportUse.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEUserTransportUse.setStatus(_A)
_RserpoolPEPolicyID_Type=RSerPoolPolicyIdentifierTC
_RserpoolPEPolicyID_Object=MibTableColumn
rserpoolPEPolicyID=_RserpoolPEPolicyID_Object((1,3,6,1,3,125,1,2,1,1,11),_RserpoolPEPolicyID_Type())
rserpoolPEPolicyID.setMaxAccess(_F)
if mibBuilder.loadTexts:rserpoolPEPolicyID.setStatus(_A)
class _RserpoolPEPolicyDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RserpoolPEPolicyDescription_Type.__name__=_L
_RserpoolPEPolicyDescription_Object=MibTableColumn
rserpoolPEPolicyDescription=_RserpoolPEPolicyDescription_Object((1,3,6,1,3,125,1,2,1,1,12),_RserpoolPEPolicyDescription_Type())
rserpoolPEPolicyDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:rserpoolPEPolicyDescription.setStatus(_A)
_RserpoolPEPolicyWeight_Type=RSerPoolPolicyWeightTC
_RserpoolPEPolicyWeight_Object=MibTableColumn
rserpoolPEPolicyWeight=_RserpoolPEPolicyWeight_Object((1,3,6,1,3,125,1,2,1,1,13),_RserpoolPEPolicyWeight_Type())
rserpoolPEPolicyWeight.setMaxAccess(_F)
if mibBuilder.loadTexts:rserpoolPEPolicyWeight.setStatus(_A)
_RserpoolPEPolicyLoad_Type=RSerPoolPolicyLoadTC
_RserpoolPEPolicyLoad_Object=MibTableColumn
rserpoolPEPolicyLoad=_RserpoolPEPolicyLoad_Object((1,3,6,1,3,125,1,2,1,1,14),_RserpoolPEPolicyLoad_Type())
rserpoolPEPolicyLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEPolicyLoad.setStatus(_A)
_RserpoolPEPolicyLoadDeg_Type=RSerPoolPolicyLoadTC
_RserpoolPEPolicyLoadDeg_Object=MibTableColumn
rserpoolPEPolicyLoadDeg=_RserpoolPEPolicyLoadDeg_Object((1,3,6,1,3,125,1,2,1,1,15),_RserpoolPEPolicyLoadDeg_Type())
rserpoolPEPolicyLoadDeg.setMaxAccess(_F)
if mibBuilder.loadTexts:rserpoolPEPolicyLoadDeg.setStatus(_A)
_RserpoolPERegistrationLife_Type=TimeTicks
_RserpoolPERegistrationLife_Object=MibTableColumn
rserpoolPERegistrationLife=_RserpoolPERegistrationLife_Object((1,3,6,1,3,125,1,2,1,1,16),_RserpoolPERegistrationLife_Type())
rserpoolPERegistrationLife.setMaxAccess(_F)
if mibBuilder.loadTexts:rserpoolPERegistrationLife.setStatus(_A)
_RserpoolPEHomeENRPServer_Type=RSerPoolENRPServerIdentifierTC
_RserpoolPEHomeENRPServer_Object=MibTableColumn
rserpoolPEHomeENRPServer=_RserpoolPEHomeENRPServer_Object((1,3,6,1,3,125,1,2,1,1,17),_RserpoolPEHomeENRPServer_Type())
rserpoolPEHomeENRPServer.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEHomeENRPServer.setStatus(_A)
_RserpoolPEASAPAddrTable_Object=MibTable
rserpoolPEASAPAddrTable=_RserpoolPEASAPAddrTable_Object((1,3,6,1,3,125,1,2,2))
if mibBuilder.loadTexts:rserpoolPEASAPAddrTable.setStatus(_A)
_RserpoolPEASAPAddrTableEntry_Object=MibTableRow
rserpoolPEASAPAddrTableEntry=_RserpoolPEASAPAddrTableEntry_Object((1,3,6,1,3,125,1,2,2,1))
rserpoolPEASAPAddrTableEntry.setIndexNames((0,_B,_O),(0,_B,_W))
if mibBuilder.loadTexts:rserpoolPEASAPAddrTableEntry.setStatus(_A)
class _RserpoolPEASAPAddrTableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RserpoolPEASAPAddrTableIndex_Type.__name__=_D
_RserpoolPEASAPAddrTableIndex_Object=MibTableColumn
rserpoolPEASAPAddrTableIndex=_RserpoolPEASAPAddrTableIndex_Object((1,3,6,1,3,125,1,2,2,1,1),_RserpoolPEASAPAddrTableIndex_Type())
rserpoolPEASAPAddrTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rserpoolPEASAPAddrTableIndex.setStatus(_A)
class _RserpoolPEASAPL3Type_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RserpoolPEASAPL3Type_Type.__name__=_H
_RserpoolPEASAPL3Type_Object=MibTableColumn
rserpoolPEASAPL3Type=_RserpoolPEASAPL3Type_Object((1,3,6,1,3,125,1,2,2,1,2),_RserpoolPEASAPL3Type_Type())
rserpoolPEASAPL3Type.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEASAPL3Type.setStatus(_A)
class _RserpoolPEASAPL3Addr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_RserpoolPEASAPL3Addr_Type.__name__=_G
_RserpoolPEASAPL3Addr_Object=MibTableColumn
rserpoolPEASAPL3Addr=_RserpoolPEASAPL3Addr_Object((1,3,6,1,3,125,1,2,2,1,3),_RserpoolPEASAPL3Addr_Type())
rserpoolPEASAPL3Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEASAPL3Addr.setStatus(_A)
_RserpoolPEUserAddrTable_Object=MibTable
rserpoolPEUserAddrTable=_RserpoolPEUserAddrTable_Object((1,3,6,1,3,125,1,2,6))
if mibBuilder.loadTexts:rserpoolPEUserAddrTable.setStatus(_A)
_RserpoolPEUserAddrTableEntry_Object=MibTableRow
rserpoolPEUserAddrTableEntry=_RserpoolPEUserAddrTableEntry_Object((1,3,6,1,3,125,1,2,6,1))
rserpoolPEUserAddrTableEntry.setIndexNames((0,_B,_O),(0,_B,_X))
if mibBuilder.loadTexts:rserpoolPEUserAddrTableEntry.setStatus(_A)
class _RserpoolPEUserAddrTableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RserpoolPEUserAddrTableIndex_Type.__name__=_D
_RserpoolPEUserAddrTableIndex_Object=MibTableColumn
rserpoolPEUserAddrTableIndex=_RserpoolPEUserAddrTableIndex_Object((1,3,6,1,3,125,1,2,6,1,1),_RserpoolPEUserAddrTableIndex_Type())
rserpoolPEUserAddrTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rserpoolPEUserAddrTableIndex.setStatus(_A)
class _RserpoolPEUserL3Type_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),(_I,1),(_J,2)))
_RserpoolPEUserL3Type_Type.__name__=_H
_RserpoolPEUserL3Type_Object=MibTableColumn
rserpoolPEUserL3Type=_RserpoolPEUserL3Type_Object((1,3,6,1,3,125,1,2,6,1,2),_RserpoolPEUserL3Type_Type())
rserpoolPEUserL3Type.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEUserL3Type.setStatus(_A)
class _RserpoolPEUserL3Addr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_RserpoolPEUserL3Addr_Type.__name__=_G
_RserpoolPEUserL3Addr_Object=MibTableColumn
rserpoolPEUserL3Addr=_RserpoolPEUserL3Addr_Object((1,3,6,1,3,125,1,2,6,1,3),_RserpoolPEUserL3Addr_Type())
rserpoolPEUserL3Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEUserL3Addr.setStatus(_A)
_RserpoolPEUserL3Opaque_Type=RSerPoolOpaqueAddressTC
_RserpoolPEUserL3Opaque_Object=MibTableColumn
rserpoolPEUserL3Opaque=_RserpoolPEUserL3Opaque_Object((1,3,6,1,3,125,1,2,6,1,4),_RserpoolPEUserL3Opaque_Type())
rserpoolPEUserL3Opaque.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPEUserL3Opaque.setStatus(_A)
_RserpoolPoolUsers_ObjectIdentity=ObjectIdentity
rserpoolPoolUsers=_RserpoolPoolUsers_ObjectIdentity((1,3,6,1,3,125,1,3))
_RserpoolPUTable_Object=MibTable
rserpoolPUTable=_RserpoolPUTable_Object((1,3,6,1,3,125,1,3,1))
if mibBuilder.loadTexts:rserpoolPUTable.setStatus(_A)
_RserpoolPUEntry_Object=MibTableRow
rserpoolPUEntry=_RserpoolPUEntry_Object((1,3,6,1,3,125,1,3,1,1))
rserpoolPUEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:rserpoolPUEntry.setStatus(_A)
class _RserpoolPUIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RserpoolPUIndex_Type.__name__=_D
_RserpoolPUIndex_Object=MibTableColumn
rserpoolPUIndex=_RserpoolPUIndex_Object((1,3,6,1,3,125,1,3,1,1,1),_RserpoolPUIndex_Type())
rserpoolPUIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rserpoolPUIndex.setStatus(_A)
_RserpoolPUOperationScope_Type=RSerPoolOperationScopeTC
_RserpoolPUOperationScope_Object=MibTableColumn
rserpoolPUOperationScope=_RserpoolPUOperationScope_Object((1,3,6,1,3,125,1,3,1,1,2),_RserpoolPUOperationScope_Type())
rserpoolPUOperationScope.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPUOperationScope.setStatus(_A)
_RserpoolPUPoolHandle_Type=RSerPoolPoolHandleTC
_RserpoolPUPoolHandle_Object=MibTableColumn
rserpoolPUPoolHandle=_RserpoolPUPoolHandle_Object((1,3,6,1,3,125,1,3,1,1,3),_RserpoolPUPoolHandle_Type())
rserpoolPUPoolHandle.setMaxAccess(_F)
if mibBuilder.loadTexts:rserpoolPUPoolHandle.setStatus(_A)
class _RserpoolPUDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RserpoolPUDescription_Type.__name__=_L
_RserpoolPUDescription_Object=MibTableColumn
rserpoolPUDescription=_RserpoolPUDescription_Object((1,3,6,1,3,125,1,3,1,1,4),_RserpoolPUDescription_Type())
rserpoolPUDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:rserpoolPUDescription.setStatus(_A)
_RserpoolPUUptime_Type=TimeTicks
_RserpoolPUUptime_Object=MibTableColumn
rserpoolPUUptime=_RserpoolPUUptime_Object((1,3,6,1,3,125,1,3,1,1,5),_RserpoolPUUptime_Type())
rserpoolPUUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:rserpoolPUUptime.setStatus(_A)
_RserpoolMIBConformance_ObjectIdentity=ObjectIdentity
rserpoolMIBConformance=_RserpoolMIBConformance_ObjectIdentity((1,3,6,1,3,125,2))
_RserpoolMIBCompliances_ObjectIdentity=ObjectIdentity
rserpoolMIBCompliances=_RserpoolMIBCompliances_ObjectIdentity((1,3,6,1,3,125,2,1))
_RserpoolMIBGroups_ObjectIdentity=ObjectIdentity
rserpoolMIBGroups=_RserpoolMIBGroups_ObjectIdentity((1,3,6,1,3,125,2,2))
rserpoolENRPGroup=ObjectGroup((1,3,6,1,3,125,2,2,1))
rserpoolENRPGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:rserpoolENRPGroup.setStatus(_A)
rserpoolPEGroup=ObjectGroup((1,3,6,1,3,125,2,2,2))
rserpoolPEGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:rserpoolPEGroup.setStatus(_A)
rserpoolPUGroup=ObjectGroup((1,3,6,1,3,125,2,2,3))
rserpoolPUGroup.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:rserpoolPUGroup.setStatus(_A)
rserpoolMIBCompliance=ModuleCompliance((1,3,6,1,3,125,2,1,1))
rserpoolMIBCompliance.setObjects(*((_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:rserpoolMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RSerPoolENRPServerIdentifierTC':RSerPoolENRPServerIdentifierTC,'RSerPoolOperationScopeTC':RSerPoolOperationScopeTC,'RSerPoolPoolHandleTC':RSerPoolPoolHandleTC,'RserpoolPoolElementIdentifierTC':RserpoolPoolElementIdentifierTC,'RSerPoolPolicyIdentifierTC':RSerPoolPolicyIdentifierTC,'RSerPoolPolicyLoadTC':RSerPoolPolicyLoadTC,'RSerPoolPolicyWeightTC':RSerPoolPolicyWeightTC,'RSerPoolTransportUseTypeTC':RSerPoolTransportUseTypeTC,'RSerPoolOpaqueAddressTC':RSerPoolOpaqueAddressTC,'rserpoolMIB':rserpoolMIB,'rserpoolMIBObjects':rserpoolMIBObjects,'rserpoolENRPServers':rserpoolENRPServers,'rserpoolENRPTable':rserpoolENRPTable,'rserpoolENRPEntry':rserpoolENRPEntry,_K:rserpoolENRPIndex,_Z:rserpoolENRPOperationScope,_a:rserpoolENRPIdentifier,_b:rserpoolENRPDescription,_c:rserpoolENRPUptime,_d:rserpoolENRPPort,_e:rserpoolENRPASAPAnnouncePort,_g:rserpoolENRPASAPAnnounceAddrType,_f:rserpoolENRPASAPAnnounceAddr,_i:rserpoolENRPENRPAnnouncePort,_h:rserpoolENRPENRPAnnounceAddrType,_j:rserpoolENRPENRPAnnounceAddr,'rserpoolENRPPoolTable':rserpoolENRPPoolTable,'rserpoolENRPPoolEntry':rserpoolENRPPoolEntry,_M:rserpoolENRPPoolIndex,_k:rserpoolENRPPoolHandle,'rserpoolENRPPoolElementTable':rserpoolENRPPoolElementTable,'rserpoolENRPPoolElementEntry':rserpoolENRPPoolElementEntry,_N:rserpoolENRPPoolElementIndex,_l:rserpoolENRPPoolElementID,_m:rserpoolENRPASAPTransportPort,_n:rserpoolENRPUserTransportProto,_p:rserpoolENRPUserTransportPort,_o:rserpoolENRPUserTransportUse,_q:rserpoolENRPPolicyID,_r:rserpoolENRPPolicyDescription,_s:rserpoolENRPPolicyWeight,_t:rserpoolENRPPolicyLoad,_u:rserpoolENRPPolicyLoadDeg,_v:rserpoolENRPRegistrationLife,_w:rserpoolENRPHomeENRPServer,'rserpoolENRPASAPAddrTable':rserpoolENRPASAPAddrTable,'rserpoolENRPASAPAddrTableEntry':rserpoolENRPASAPAddrTableEntry,_R:rserpoolENRPASAPAddrTableIndex,_x:rserpoolENRPASAPL3Type,_y:rserpoolENRPASAPL3Addr,'rserpoolENRPUserAddrTable':rserpoolENRPUserAddrTable,'rserpoolENRPUserAddrTableEntry':rserpoolENRPUserAddrTableEntry,_S:rserpoolENRPUserAddrTableIndex,_z:rserpoolENRPUserL3Type,_A0:rserpoolENRPUserL3Addr,_A1:rserpoolENRPUserL3Opaque,'rserpoolENRPENRPAddrTable':rserpoolENRPENRPAddrTable,'rserpoolENRPENRPAddrTableEntry':rserpoolENRPENRPAddrTableEntry,_U:rserpoolENRPENRPAddrTableIndex,_A2:rserpoolENRPENRPL3Type,_A3:rserpoolENRPENRPL3Addr,'rserpoolENRPPeerTable':rserpoolENRPPeerTable,'rserpoolENRPPeerEntry':rserpoolENRPPeerEntry,_Q:rserpoolENRPPeerIndex,_A4:rserpoolENRPPeerIdentifier,_A5:rserpoolENRPPeerPort,_A6:rserpoolENRPPeerLastHeard,'rserpoolENRPPeerAddrTable':rserpoolENRPPeerAddrTable,'rserpoolENRPPeerAddrTableEntry':rserpoolENRPPeerAddrTableEntry,_V:rserpoolENRPPeerAddrTableIndex,_A7:rserpoolENRPPeerL3Type,_A8:rserpoolENRPPeerL3Addr,'rserpoolPoolElements':rserpoolPoolElements,'rserpoolPETable':rserpoolPETable,'rserpoolPEEntry':rserpoolPEEntry,_O:rserpoolPEIndex,_A9:rserpoolPEOperationScope,_AA:rserpoolPEPoolHandle,_AB:rserpoolPEIdentifier,_AC:rserpoolPEDescription,_AD:rserpoolPEUptime,_AE:rserpoolPEASAPTransportPort,_AF:rserpoolPEUserTransportProto,_AG:rserpoolPEUserTransportPort,_AH:rserpoolPEUserTransportUse,_AI:rserpoolPEPolicyID,_AJ:rserpoolPEPolicyDescription,_AK:rserpoolPEPolicyWeight,_AL:rserpoolPEPolicyLoad,_AM:rserpoolPEPolicyLoadDeg,_AN:rserpoolPERegistrationLife,_AO:rserpoolPEHomeENRPServer,'rserpoolPEASAPAddrTable':rserpoolPEASAPAddrTable,'rserpoolPEASAPAddrTableEntry':rserpoolPEASAPAddrTableEntry,_W:rserpoolPEASAPAddrTableIndex,_AP:rserpoolPEASAPL3Type,_AQ:rserpoolPEASAPL3Addr,'rserpoolPEUserAddrTable':rserpoolPEUserAddrTable,'rserpoolPEUserAddrTableEntry':rserpoolPEUserAddrTableEntry,_X:rserpoolPEUserAddrTableIndex,_AR:rserpoolPEUserL3Type,_AS:rserpoolPEUserL3Addr,_AT:rserpoolPEUserL3Opaque,'rserpoolPoolUsers':rserpoolPoolUsers,'rserpoolPUTable':rserpoolPUTable,'rserpoolPUEntry':rserpoolPUEntry,_Y:rserpoolPUIndex,_AU:rserpoolPUOperationScope,_AV:rserpoolPUPoolHandle,_AW:rserpoolPUDescription,_AX:rserpoolPUUptime,'rserpoolMIBConformance':rserpoolMIBConformance,'rserpoolMIBCompliances':rserpoolMIBCompliances,'rserpoolMIBCompliance':rserpoolMIBCompliance,'rserpoolMIBGroups':rserpoolMIBGroups,_AY:rserpoolENRPGroup,_AZ:rserpoolPEGroup,_Aa:rserpoolPUGroup})