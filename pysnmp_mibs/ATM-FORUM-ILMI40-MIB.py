_AY='atmfVccOperStatus'
_AX='atmfVpcOperStatus'
_AW='atmfAddressRegistrationAdminIndex'
_AV='atmfVccAbrVci'
_AU='atmfVccAbrVpi'
_AT='atmfVccAbrPortIndex'
_AS='rdfOneOver2'
_AR='rdfOneOver4'
_AQ='rdfOneOver8'
_AP='rdfOneOver16'
_AO='rdfOneOver32'
_AN='rdfOneOver64'
_AM='rdfOneOver128'
_AL='rdfOneOver256'
_AK='rdfOneOver512'
_AJ='rdfOneOver1024'
_AI='rdfOneOver2048'
_AH='rdfOneOver4096'
_AG='rdfOneOver8192'
_AF='rdfOneOver16384'
_AE='rdfOneOver32768'
_AD='rifOneOver2'
_AC='rifOneOver4'
_AB='rifOneOver8'
_AA='rifOneOver16'
_A9='rifOneOver32'
_A8='rifOneOver64'
_A7='rifOneOver128'
_A6='rifOneOver256'
_A5='rifOneOver512'
_A4='rifOneOver1024'
_A3='rifOneOver2048'
_A2='rifOneOver4096'
_A1='rifOneOver8192'
_A0='rifOneOver16384'
_z='rifOneOver32768'
_y='cdfOne'
_x='cdfOneOver2'
_w='cdfOneOver4'
_v='cdfOneOver8'
_u='cdfOneOver16'
_t='cdfOneOver32'
_s='cdfOneOver64'
_r='trm100'
_q='trm12point5'
_p='trm6point25'
_o='trm3point125'
_n='trm1point5625'
_m='trm0point78125'
_l='nrm256'
_k='nrm128'
_j='atmfVpcAbrVpi'
_i='atmfVpcAbrPortIndex'
_h='atmfSrvcRegAddressIndex'
_g='atmfSrvcRegServiceID'
_f='atmfSrvcRegPort'
_e='read-write'
_d='atmfAddressAtmAddress'
_c='atmfAddressPort'
_b='unspecified'
_a='statistical'
_Z='deterministic'
_Y='localDown'
_X='localUpEnd2endUnknown'
_W='end2endDown'
_V='end2endUp'
_U='unknown'
_T='atmfAtmStatsIndex'
_S='version4point0'
_R='atmfAtmLayerIndex'
_Q='atmfPortIndex'
_P='NotificationType'
_O='atmfVccVci'
_N='atmfVccVpi'
_M='atmfVccPortIndex'
_L='atmfVpcVpi'
_K='atmfVpcPortIndex'
_J='obsolete'
_I='OctetString'
_H='unsupported'
_G='other'
_F='not-accessible'
_E='deprecated'
_D='ATM-FORUM-ILMI40-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_P,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_P,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class AtmAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class TruthValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
class ClnpAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,21))
class AtmServiceCategory(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('cbr',2),('rtVbr',3),('nrtVbr',4),('abr',5),('ubr',6)))
_AtmForum_ObjectIdentity=ObjectIdentity
atmForum=_AtmForum_ObjectIdentity((1,3,6,1,4,1,353))
_AtmForumAdmin_ObjectIdentity=ObjectIdentity
atmForumAdmin=_AtmForumAdmin_ObjectIdentity((1,3,6,1,4,1,353,1))
_AtmfTransmissionTypes_ObjectIdentity=ObjectIdentity
atmfTransmissionTypes=_AtmfTransmissionTypes_ObjectIdentity((1,3,6,1,4,1,353,1,2))
_AtmfUnknownType_ObjectIdentity=ObjectIdentity
atmfUnknownType=_AtmfUnknownType_ObjectIdentity((1,3,6,1,4,1,353,1,2,1))
_AtmfSonetSTS3c_ObjectIdentity=ObjectIdentity
atmfSonetSTS3c=_AtmfSonetSTS3c_ObjectIdentity((1,3,6,1,4,1,353,1,2,2))
_AtmfDs3_ObjectIdentity=ObjectIdentity
atmfDs3=_AtmfDs3_ObjectIdentity((1,3,6,1,4,1,353,1,2,3))
_Atmf4B5B_ObjectIdentity=ObjectIdentity
atmf4B5B=_Atmf4B5B_ObjectIdentity((1,3,6,1,4,1,353,1,2,4))
_Atmf8B10B_ObjectIdentity=ObjectIdentity
atmf8B10B=_Atmf8B10B_ObjectIdentity((1,3,6,1,4,1,353,1,2,5))
_AtmfSonetSTS12c_ObjectIdentity=ObjectIdentity
atmfSonetSTS12c=_AtmfSonetSTS12c_ObjectIdentity((1,3,6,1,4,1,353,1,2,6))
_AtmfE3_ObjectIdentity=ObjectIdentity
atmfE3=_AtmfE3_ObjectIdentity((1,3,6,1,4,1,353,1,2,7))
_AtmfT1_ObjectIdentity=ObjectIdentity
atmfT1=_AtmfT1_ObjectIdentity((1,3,6,1,4,1,353,1,2,8))
_AtmfE1_ObjectIdentity=ObjectIdentity
atmfE1=_AtmfE1_ObjectIdentity((1,3,6,1,4,1,353,1,2,9))
_AtmfMediaTypes_ObjectIdentity=ObjectIdentity
atmfMediaTypes=_AtmfMediaTypes_ObjectIdentity((1,3,6,1,4,1,353,1,3))
_AtmfMediaUnknownType_ObjectIdentity=ObjectIdentity
atmfMediaUnknownType=_AtmfMediaUnknownType_ObjectIdentity((1,3,6,1,4,1,353,1,3,1))
_AtmfMediaCoaxCable_ObjectIdentity=ObjectIdentity
atmfMediaCoaxCable=_AtmfMediaCoaxCable_ObjectIdentity((1,3,6,1,4,1,353,1,3,2))
_AtmfMediaSingleMode_ObjectIdentity=ObjectIdentity
atmfMediaSingleMode=_AtmfMediaSingleMode_ObjectIdentity((1,3,6,1,4,1,353,1,3,3))
_AtmfMediaMultiMode_ObjectIdentity=ObjectIdentity
atmfMediaMultiMode=_AtmfMediaMultiMode_ObjectIdentity((1,3,6,1,4,1,353,1,3,4))
_AtmfMediaStp_ObjectIdentity=ObjectIdentity
atmfMediaStp=_AtmfMediaStp_ObjectIdentity((1,3,6,1,4,1,353,1,3,5))
_AtmfMediaUtp_ObjectIdentity=ObjectIdentity
atmfMediaUtp=_AtmfMediaUtp_ObjectIdentity((1,3,6,1,4,1,353,1,3,6))
_AtmfTrafficDescrTypes_ObjectIdentity=ObjectIdentity
atmfTrafficDescrTypes=_AtmfTrafficDescrTypes_ObjectIdentity((1,3,6,1,4,1,353,1,4))
_AtmfNoDescriptor_ObjectIdentity=ObjectIdentity
atmfNoDescriptor=_AtmfNoDescriptor_ObjectIdentity((1,3,6,1,4,1,353,1,4,1))
_AtmfPeakRate_ObjectIdentity=ObjectIdentity
atmfPeakRate=_AtmfPeakRate_ObjectIdentity((1,3,6,1,4,1,353,1,4,2))
_AtmfNoClpNoScr_ObjectIdentity=ObjectIdentity
atmfNoClpNoScr=_AtmfNoClpNoScr_ObjectIdentity((1,3,6,1,4,1,353,1,4,3))
_AtmfClpNoTaggingNoScr_ObjectIdentity=ObjectIdentity
atmfClpNoTaggingNoScr=_AtmfClpNoTaggingNoScr_ObjectIdentity((1,3,6,1,4,1,353,1,4,4))
_AtmfClpTaggingNoScr_ObjectIdentity=ObjectIdentity
atmfClpTaggingNoScr=_AtmfClpTaggingNoScr_ObjectIdentity((1,3,6,1,4,1,353,1,4,5))
_AtmfNoClpScr_ObjectIdentity=ObjectIdentity
atmfNoClpScr=_AtmfNoClpScr_ObjectIdentity((1,3,6,1,4,1,353,1,4,6))
_AtmfClpNoTaggingScr_ObjectIdentity=ObjectIdentity
atmfClpNoTaggingScr=_AtmfClpNoTaggingScr_ObjectIdentity((1,3,6,1,4,1,353,1,4,7))
_AtmfClpTaggingScr_ObjectIdentity=ObjectIdentity
atmfClpTaggingScr=_AtmfClpTaggingScr_ObjectIdentity((1,3,6,1,4,1,353,1,4,8))
_AtmfClpNoTaggingMcr_ObjectIdentity=ObjectIdentity
atmfClpNoTaggingMcr=_AtmfClpNoTaggingMcr_ObjectIdentity((1,3,6,1,4,1,353,1,4,9))
_AtmfSrvcRegTypes_ObjectIdentity=ObjectIdentity
atmfSrvcRegTypes=_AtmfSrvcRegTypes_ObjectIdentity((1,3,6,1,4,1,353,1,5))
_AtmfSrvcRegLecs_ObjectIdentity=ObjectIdentity
atmfSrvcRegLecs=_AtmfSrvcRegLecs_ObjectIdentity((1,3,6,1,4,1,353,1,5,1))
_AtmfSrvcRegAns_ObjectIdentity=ObjectIdentity
atmfSrvcRegAns=_AtmfSrvcRegAns_ObjectIdentity((1,3,6,1,4,1,353,1,5,2))
_AtmForumUni_ObjectIdentity=ObjectIdentity
atmForumUni=_AtmForumUni_ObjectIdentity((1,3,6,1,4,1,353,2))
_AtmfPhysicalGroup_ObjectIdentity=ObjectIdentity
atmfPhysicalGroup=_AtmfPhysicalGroup_ObjectIdentity((1,3,6,1,4,1,353,2,1))
_AtmfPortTable_Object=MibTable
atmfPortTable=_AtmfPortTable_Object((1,3,6,1,4,1,353,2,1,1))
if mibBuilder.loadTexts:atmfPortTable.setStatus(_A)
_AtmfPortEntry_Object=MibTableRow
atmfPortEntry=_AtmfPortEntry_Object((1,3,6,1,4,1,353,2,1,1,1))
atmfPortEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:atmfPortEntry.setStatus(_A)
class _AtmfPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfPortIndex_Type.__name__=_C
_AtmfPortIndex_Object=MibTableColumn
atmfPortIndex=_AtmfPortIndex_Object((1,3,6,1,4,1,353,2,1,1,1,1),_AtmfPortIndex_Type())
atmfPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfPortIndex.setStatus(_A)
_AtmfPortAddress_Type=AtmAddress
_AtmfPortAddress_Object=MibTableColumn
atmfPortAddress=_AtmfPortAddress_Object((1,3,6,1,4,1,353,2,1,1,1,2),_AtmfPortAddress_Type())
atmfPortAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfPortAddress.setStatus(_J)
_AtmfPortTransmissionType_Type=ObjectIdentifier
_AtmfPortTransmissionType_Object=MibTableColumn
atmfPortTransmissionType=_AtmfPortTransmissionType_Object((1,3,6,1,4,1,353,2,1,1,1,3),_AtmfPortTransmissionType_Type())
atmfPortTransmissionType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfPortTransmissionType.setStatus(_E)
_AtmfPortMediaType_Type=ObjectIdentifier
_AtmfPortMediaType_Object=MibTableColumn
atmfPortMediaType=_AtmfPortMediaType_Object((1,3,6,1,4,1,353,2,1,1,1,4),_AtmfPortMediaType_Type())
atmfPortMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfPortMediaType.setStatus(_E)
class _AtmfPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('inService',2),('outOfService',3),('loopBack',4)))
_AtmfPortOperStatus_Type.__name__=_C
_AtmfPortOperStatus_Object=MibTableColumn
atmfPortOperStatus=_AtmfPortOperStatus_Object((1,3,6,1,4,1,353,2,1,1,1,5),_AtmfPortOperStatus_Type())
atmfPortOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfPortOperStatus.setStatus(_E)
_AtmfPortSpecific_Type=ObjectIdentifier
_AtmfPortSpecific_Object=MibTableColumn
atmfPortSpecific=_AtmfPortSpecific_Object((1,3,6,1,4,1,353,2,1,1,1,6),_AtmfPortSpecific_Type())
atmfPortSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfPortSpecific.setStatus(_E)
_AtmfPortMyIfName_Type=DisplayString
_AtmfPortMyIfName_Object=MibTableColumn
atmfPortMyIfName=_AtmfPortMyIfName_Object((1,3,6,1,4,1,353,2,1,1,1,7),_AtmfPortMyIfName_Type())
atmfPortMyIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfPortMyIfName.setStatus(_A)
class _AtmfPortMyIfIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfPortMyIfIdentifier_Type.__name__=_C
_AtmfPortMyIfIdentifier_Object=MibTableColumn
atmfPortMyIfIdentifier=_AtmfPortMyIfIdentifier_Object((1,3,6,1,4,1,353,2,1,1,1,8),_AtmfPortMyIfIdentifier_Type())
atmfPortMyIfIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfPortMyIfIdentifier.setStatus(_A)
_AtmfMyIpNmAddress_Type=IpAddress
_AtmfMyIpNmAddress_Object=MibScalar
atmfMyIpNmAddress=_AtmfMyIpNmAddress_Object((1,3,6,1,4,1,353,2,1,2),_AtmfMyIpNmAddress_Type())
atmfMyIpNmAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfMyIpNmAddress.setStatus(_A)
_AtmfMyOsiNmNsapAddress_Type=ClnpAddress
_AtmfMyOsiNmNsapAddress_Object=MibScalar
atmfMyOsiNmNsapAddress=_AtmfMyOsiNmNsapAddress_Object((1,3,6,1,4,1,353,2,1,3),_AtmfMyOsiNmNsapAddress_Type())
atmfMyOsiNmNsapAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfMyOsiNmNsapAddress.setStatus(_A)
class _AtmfMySystemIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AtmfMySystemIdentifier_Type.__name__=_I
_AtmfMySystemIdentifier_Object=MibScalar
atmfMySystemIdentifier=_AtmfMySystemIdentifier_Object((1,3,6,1,4,1,353,2,1,4),_AtmfMySystemIdentifier_Type())
atmfMySystemIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfMySystemIdentifier.setStatus(_A)
_AtmfAtmLayerGroup_ObjectIdentity=ObjectIdentity
atmfAtmLayerGroup=_AtmfAtmLayerGroup_ObjectIdentity((1,3,6,1,4,1,353,2,2))
_AtmfAtmLayerTable_Object=MibTable
atmfAtmLayerTable=_AtmfAtmLayerTable_Object((1,3,6,1,4,1,353,2,2,1))
if mibBuilder.loadTexts:atmfAtmLayerTable.setStatus(_A)
_AtmfAtmLayerEntry_Object=MibTableRow
atmfAtmLayerEntry=_AtmfAtmLayerEntry_Object((1,3,6,1,4,1,353,2,2,1,1))
atmfAtmLayerEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:atmfAtmLayerEntry.setStatus(_A)
class _AtmfAtmLayerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfAtmLayerIndex_Type.__name__=_C
_AtmfAtmLayerIndex_Object=MibTableColumn
atmfAtmLayerIndex=_AtmfAtmLayerIndex_Object((1,3,6,1,4,1,353,2,2,1,1,1),_AtmfAtmLayerIndex_Type())
atmfAtmLayerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerIndex.setStatus(_A)
class _AtmfAtmLayerMaxVPCs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_AtmfAtmLayerMaxVPCs_Type.__name__=_C
_AtmfAtmLayerMaxVPCs_Object=MibTableColumn
atmfAtmLayerMaxVPCs=_AtmfAtmLayerMaxVPCs_Object((1,3,6,1,4,1,353,2,2,1,1,2),_AtmfAtmLayerMaxVPCs_Type())
atmfAtmLayerMaxVPCs.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerMaxVPCs.setStatus(_A)
class _AtmfAtmLayerMaxVCCs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,268435456))
_AtmfAtmLayerMaxVCCs_Type.__name__=_C
_AtmfAtmLayerMaxVCCs_Object=MibTableColumn
atmfAtmLayerMaxVCCs=_AtmfAtmLayerMaxVCCs_Object((1,3,6,1,4,1,353,2,2,1,1,3),_AtmfAtmLayerMaxVCCs_Type())
atmfAtmLayerMaxVCCs.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerMaxVCCs.setStatus(_A)
class _AtmfAtmLayerConfiguredVPCs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_AtmfAtmLayerConfiguredVPCs_Type.__name__=_C
_AtmfAtmLayerConfiguredVPCs_Object=MibTableColumn
atmfAtmLayerConfiguredVPCs=_AtmfAtmLayerConfiguredVPCs_Object((1,3,6,1,4,1,353,2,2,1,1,4),_AtmfAtmLayerConfiguredVPCs_Type())
atmfAtmLayerConfiguredVPCs.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerConfiguredVPCs.setStatus(_A)
class _AtmfAtmLayerConfiguredVCCs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,268435456))
_AtmfAtmLayerConfiguredVCCs_Type.__name__=_C
_AtmfAtmLayerConfiguredVCCs_Object=MibTableColumn
atmfAtmLayerConfiguredVCCs=_AtmfAtmLayerConfiguredVCCs_Object((1,3,6,1,4,1,353,2,2,1,1,5),_AtmfAtmLayerConfiguredVCCs_Type())
atmfAtmLayerConfiguredVCCs.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerConfiguredVCCs.setStatus(_A)
class _AtmfAtmLayerMaxVpiBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_AtmfAtmLayerMaxVpiBits_Type.__name__=_C
_AtmfAtmLayerMaxVpiBits_Object=MibTableColumn
atmfAtmLayerMaxVpiBits=_AtmfAtmLayerMaxVpiBits_Object((1,3,6,1,4,1,353,2,2,1,1,6),_AtmfAtmLayerMaxVpiBits_Type())
atmfAtmLayerMaxVpiBits.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerMaxVpiBits.setStatus(_A)
class _AtmfAtmLayerMaxVciBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AtmfAtmLayerMaxVciBits_Type.__name__=_C
_AtmfAtmLayerMaxVciBits_Object=MibTableColumn
atmfAtmLayerMaxVciBits=_AtmfAtmLayerMaxVciBits_Object((1,3,6,1,4,1,353,2,2,1,1,7),_AtmfAtmLayerMaxVciBits_Type())
atmfAtmLayerMaxVciBits.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerMaxVciBits.setStatus(_A)
class _AtmfAtmLayerUniType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('public',1),('private',2)))
_AtmfAtmLayerUniType_Type.__name__=_C
_AtmfAtmLayerUniType_Object=MibTableColumn
atmfAtmLayerUniType=_AtmfAtmLayerUniType_Object((1,3,6,1,4,1,353,2,2,1,1,8),_AtmfAtmLayerUniType_Type())
atmfAtmLayerUniType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerUniType.setStatus(_A)
class _AtmfAtmLayerUniVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('version2point0',1),('version3point0',2),('version3point1',3),(_S,4),(_H,5)))
_AtmfAtmLayerUniVersion_Type.__name__=_C
_AtmfAtmLayerUniVersion_Object=MibTableColumn
atmfAtmLayerUniVersion=_AtmfAtmLayerUniVersion_Object((1,3,6,1,4,1,353,2,2,1,1,9),_AtmfAtmLayerUniVersion_Type())
atmfAtmLayerUniVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerUniVersion.setStatus(_A)
class _AtmfAtmLayerDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('user',1),('node',2)))
_AtmfAtmLayerDeviceType_Type.__name__=_C
_AtmfAtmLayerDeviceType_Object=MibTableColumn
atmfAtmLayerDeviceType=_AtmfAtmLayerDeviceType_Object((1,3,6,1,4,1,353,2,2,1,1,10),_AtmfAtmLayerDeviceType_Type())
atmfAtmLayerDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerDeviceType.setStatus(_A)
class _AtmfAtmLayerIlmiVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_S,2)))
_AtmfAtmLayerIlmiVersion_Type.__name__=_C
_AtmfAtmLayerIlmiVersion_Object=MibTableColumn
atmfAtmLayerIlmiVersion=_AtmfAtmLayerIlmiVersion_Object((1,3,6,1,4,1,353,2,2,1,1,11),_AtmfAtmLayerIlmiVersion_Type())
atmfAtmLayerIlmiVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerIlmiVersion.setStatus(_A)
class _AtmfAtmLayerNniSigVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('iisp',2),('pnniVersion1point0',3)))
_AtmfAtmLayerNniSigVersion_Type.__name__=_C
_AtmfAtmLayerNniSigVersion_Object=MibTableColumn
atmfAtmLayerNniSigVersion=_AtmfAtmLayerNniSigVersion_Object((1,3,6,1,4,1,353,2,2,1,1,12),_AtmfAtmLayerNniSigVersion_Type())
atmfAtmLayerNniSigVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerNniSigVersion.setStatus(_A)
class _AtmfAtmLayerMaxSvpcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_AtmfAtmLayerMaxSvpcVpi_Type.__name__=_C
_AtmfAtmLayerMaxSvpcVpi_Object=MibTableColumn
atmfAtmLayerMaxSvpcVpi=_AtmfAtmLayerMaxSvpcVpi_Object((1,3,6,1,4,1,353,2,2,1,1,13),_AtmfAtmLayerMaxSvpcVpi_Type())
atmfAtmLayerMaxSvpcVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerMaxSvpcVpi.setStatus(_A)
class _AtmfAtmLayerMaxSvccVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_AtmfAtmLayerMaxSvccVpi_Type.__name__=_C
_AtmfAtmLayerMaxSvccVpi_Object=MibTableColumn
atmfAtmLayerMaxSvccVpi=_AtmfAtmLayerMaxSvccVpi_Object((1,3,6,1,4,1,353,2,2,1,1,14),_AtmfAtmLayerMaxSvccVpi_Type())
atmfAtmLayerMaxSvccVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerMaxSvccVpi.setStatus(_A)
class _AtmfAtmLayerMinSvccVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_AtmfAtmLayerMinSvccVci_Type.__name__=_C
_AtmfAtmLayerMinSvccVci_Object=MibTableColumn
atmfAtmLayerMinSvccVci=_AtmfAtmLayerMinSvccVci_Object((1,3,6,1,4,1,353,2,2,1,1,15),_AtmfAtmLayerMinSvccVci_Type())
atmfAtmLayerMinSvccVci.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmLayerMinSvccVci.setStatus(_A)
_AtmfAtmStatsGroup_ObjectIdentity=ObjectIdentity
atmfAtmStatsGroup=_AtmfAtmStatsGroup_ObjectIdentity((1,3,6,1,4,1,353,2,3))
_AtmfAtmStatsTable_Object=MibTable
atmfAtmStatsTable=_AtmfAtmStatsTable_Object((1,3,6,1,4,1,353,2,3,1))
if mibBuilder.loadTexts:atmfAtmStatsTable.setStatus(_E)
_AtmfAtmStatsEntry_Object=MibTableRow
atmfAtmStatsEntry=_AtmfAtmStatsEntry_Object((1,3,6,1,4,1,353,2,3,1,1))
atmfAtmStatsEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:atmfAtmStatsEntry.setStatus(_E)
class _AtmfAtmStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfAtmStatsIndex_Type.__name__=_C
_AtmfAtmStatsIndex_Object=MibTableColumn
atmfAtmStatsIndex=_AtmfAtmStatsIndex_Object((1,3,6,1,4,1,353,2,3,1,1,1),_AtmfAtmStatsIndex_Type())
atmfAtmStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmStatsIndex.setStatus(_E)
_AtmfAtmStatsReceivedCells_Type=Counter32
_AtmfAtmStatsReceivedCells_Object=MibTableColumn
atmfAtmStatsReceivedCells=_AtmfAtmStatsReceivedCells_Object((1,3,6,1,4,1,353,2,3,1,1,2),_AtmfAtmStatsReceivedCells_Type())
atmfAtmStatsReceivedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmStatsReceivedCells.setStatus(_E)
_AtmfAtmStatsDroppedReceivedCells_Type=Counter32
_AtmfAtmStatsDroppedReceivedCells_Object=MibTableColumn
atmfAtmStatsDroppedReceivedCells=_AtmfAtmStatsDroppedReceivedCells_Object((1,3,6,1,4,1,353,2,3,1,1,3),_AtmfAtmStatsDroppedReceivedCells_Type())
atmfAtmStatsDroppedReceivedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmStatsDroppedReceivedCells.setStatus(_E)
_AtmfAtmStatsTransmittedCells_Type=Counter32
_AtmfAtmStatsTransmittedCells_Object=MibTableColumn
atmfAtmStatsTransmittedCells=_AtmfAtmStatsTransmittedCells_Object((1,3,6,1,4,1,353,2,3,1,1,4),_AtmfAtmStatsTransmittedCells_Type())
atmfAtmStatsTransmittedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAtmStatsTransmittedCells.setStatus(_E)
_AtmfVpcGroup_ObjectIdentity=ObjectIdentity
atmfVpcGroup=_AtmfVpcGroup_ObjectIdentity((1,3,6,1,4,1,353,2,4))
_AtmfVpcTable_Object=MibTable
atmfVpcTable=_AtmfVpcTable_Object((1,3,6,1,4,1,353,2,4,1))
if mibBuilder.loadTexts:atmfVpcTable.setStatus(_A)
_AtmfVpcEntry_Object=MibTableRow
atmfVpcEntry=_AtmfVpcEntry_Object((1,3,6,1,4,1,353,2,4,1,1))
atmfVpcEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:atmfVpcEntry.setStatus(_A)
class _AtmfVpcPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcPortIndex_Type.__name__=_C
_AtmfVpcPortIndex_Object=MibTableColumn
atmfVpcPortIndex=_AtmfVpcPortIndex_Object((1,3,6,1,4,1,353,2,4,1,1,1),_AtmfVpcPortIndex_Type())
atmfVpcPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcPortIndex.setStatus(_A)
class _AtmfVpcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AtmfVpcVpi_Type.__name__=_C
_AtmfVpcVpi_Object=MibTableColumn
atmfVpcVpi=_AtmfVpcVpi_Object((1,3,6,1,4,1,353,2,4,1,1,2),_AtmfVpcVpi_Type())
atmfVpcVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcVpi.setStatus(_A)
class _AtmfVpcOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3),(_X,4),(_Y,5)))
_AtmfVpcOperStatus_Type.__name__=_C
_AtmfVpcOperStatus_Object=MibTableColumn
atmfVpcOperStatus=_AtmfVpcOperStatus_Object((1,3,6,1,4,1,353,2,4,1,1,3),_AtmfVpcOperStatus_Type())
atmfVpcOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcOperStatus.setStatus(_A)
_AtmfVpcTransmitTrafficDescriptorType_Type=ObjectIdentifier
_AtmfVpcTransmitTrafficDescriptorType_Object=MibTableColumn
atmfVpcTransmitTrafficDescriptorType=_AtmfVpcTransmitTrafficDescriptorType_Object((1,3,6,1,4,1,353,2,4,1,1,4),_AtmfVpcTransmitTrafficDescriptorType_Type())
atmfVpcTransmitTrafficDescriptorType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcTransmitTrafficDescriptorType.setStatus(_A)
class _AtmfVpcTransmitTrafficDescriptorParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcTransmitTrafficDescriptorParam1_Type.__name__=_C
_AtmfVpcTransmitTrafficDescriptorParam1_Object=MibTableColumn
atmfVpcTransmitTrafficDescriptorParam1=_AtmfVpcTransmitTrafficDescriptorParam1_Object((1,3,6,1,4,1,353,2,4,1,1,5),_AtmfVpcTransmitTrafficDescriptorParam1_Type())
atmfVpcTransmitTrafficDescriptorParam1.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcTransmitTrafficDescriptorParam1.setStatus(_A)
class _AtmfVpcTransmitTrafficDescriptorParam2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcTransmitTrafficDescriptorParam2_Type.__name__=_C
_AtmfVpcTransmitTrafficDescriptorParam2_Object=MibTableColumn
atmfVpcTransmitTrafficDescriptorParam2=_AtmfVpcTransmitTrafficDescriptorParam2_Object((1,3,6,1,4,1,353,2,4,1,1,6),_AtmfVpcTransmitTrafficDescriptorParam2_Type())
atmfVpcTransmitTrafficDescriptorParam2.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcTransmitTrafficDescriptorParam2.setStatus(_A)
class _AtmfVpcTransmitTrafficDescriptorParam3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcTransmitTrafficDescriptorParam3_Type.__name__=_C
_AtmfVpcTransmitTrafficDescriptorParam3_Object=MibTableColumn
atmfVpcTransmitTrafficDescriptorParam3=_AtmfVpcTransmitTrafficDescriptorParam3_Object((1,3,6,1,4,1,353,2,4,1,1,7),_AtmfVpcTransmitTrafficDescriptorParam3_Type())
atmfVpcTransmitTrafficDescriptorParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcTransmitTrafficDescriptorParam3.setStatus(_A)
class _AtmfVpcTransmitTrafficDescriptorParam4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcTransmitTrafficDescriptorParam4_Type.__name__=_C
_AtmfVpcTransmitTrafficDescriptorParam4_Object=MibTableColumn
atmfVpcTransmitTrafficDescriptorParam4=_AtmfVpcTransmitTrafficDescriptorParam4_Object((1,3,6,1,4,1,353,2,4,1,1,8),_AtmfVpcTransmitTrafficDescriptorParam4_Type())
atmfVpcTransmitTrafficDescriptorParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcTransmitTrafficDescriptorParam4.setStatus(_A)
class _AtmfVpcTransmitTrafficDescriptorParam5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcTransmitTrafficDescriptorParam5_Type.__name__=_C
_AtmfVpcTransmitTrafficDescriptorParam5_Object=MibTableColumn
atmfVpcTransmitTrafficDescriptorParam5=_AtmfVpcTransmitTrafficDescriptorParam5_Object((1,3,6,1,4,1,353,2,4,1,1,9),_AtmfVpcTransmitTrafficDescriptorParam5_Type())
atmfVpcTransmitTrafficDescriptorParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcTransmitTrafficDescriptorParam5.setStatus(_A)
_AtmfVpcReceiveTrafficDescriptorType_Type=ObjectIdentifier
_AtmfVpcReceiveTrafficDescriptorType_Object=MibTableColumn
atmfVpcReceiveTrafficDescriptorType=_AtmfVpcReceiveTrafficDescriptorType_Object((1,3,6,1,4,1,353,2,4,1,1,10),_AtmfVpcReceiveTrafficDescriptorType_Type())
atmfVpcReceiveTrafficDescriptorType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcReceiveTrafficDescriptorType.setStatus(_A)
class _AtmfVpcReceiveTrafficDescriptorParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcReceiveTrafficDescriptorParam1_Type.__name__=_C
_AtmfVpcReceiveTrafficDescriptorParam1_Object=MibTableColumn
atmfVpcReceiveTrafficDescriptorParam1=_AtmfVpcReceiveTrafficDescriptorParam1_Object((1,3,6,1,4,1,353,2,4,1,1,11),_AtmfVpcReceiveTrafficDescriptorParam1_Type())
atmfVpcReceiveTrafficDescriptorParam1.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcReceiveTrafficDescriptorParam1.setStatus(_A)
class _AtmfVpcReceiveTrafficDescriptorParam2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcReceiveTrafficDescriptorParam2_Type.__name__=_C
_AtmfVpcReceiveTrafficDescriptorParam2_Object=MibTableColumn
atmfVpcReceiveTrafficDescriptorParam2=_AtmfVpcReceiveTrafficDescriptorParam2_Object((1,3,6,1,4,1,353,2,4,1,1,12),_AtmfVpcReceiveTrafficDescriptorParam2_Type())
atmfVpcReceiveTrafficDescriptorParam2.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcReceiveTrafficDescriptorParam2.setStatus(_A)
class _AtmfVpcReceiveTrafficDescriptorParam3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcReceiveTrafficDescriptorParam3_Type.__name__=_C
_AtmfVpcReceiveTrafficDescriptorParam3_Object=MibTableColumn
atmfVpcReceiveTrafficDescriptorParam3=_AtmfVpcReceiveTrafficDescriptorParam3_Object((1,3,6,1,4,1,353,2,4,1,1,13),_AtmfVpcReceiveTrafficDescriptorParam3_Type())
atmfVpcReceiveTrafficDescriptorParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcReceiveTrafficDescriptorParam3.setStatus(_A)
class _AtmfVpcReceiveTrafficDescriptorParam4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcReceiveTrafficDescriptorParam4_Type.__name__=_C
_AtmfVpcReceiveTrafficDescriptorParam4_Object=MibTableColumn
atmfVpcReceiveTrafficDescriptorParam4=_AtmfVpcReceiveTrafficDescriptorParam4_Object((1,3,6,1,4,1,353,2,4,1,1,14),_AtmfVpcReceiveTrafficDescriptorParam4_Type())
atmfVpcReceiveTrafficDescriptorParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcReceiveTrafficDescriptorParam4.setStatus(_A)
class _AtmfVpcReceiveTrafficDescriptorParam5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcReceiveTrafficDescriptorParam5_Type.__name__=_C
_AtmfVpcReceiveTrafficDescriptorParam5_Object=MibTableColumn
atmfVpcReceiveTrafficDescriptorParam5=_AtmfVpcReceiveTrafficDescriptorParam5_Object((1,3,6,1,4,1,353,2,4,1,1,15),_AtmfVpcReceiveTrafficDescriptorParam5_Type())
atmfVpcReceiveTrafficDescriptorParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcReceiveTrafficDescriptorParam5.setStatus(_A)
class _AtmfVpcQoSCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_Z,2),(_a,3),(_b,4)))
_AtmfVpcQoSCategory_Type.__name__=_C
_AtmfVpcQoSCategory_Object=MibTableColumn
atmfVpcQoSCategory=_AtmfVpcQoSCategory_Object((1,3,6,1,4,1,353,2,4,1,1,16),_AtmfVpcQoSCategory_Type())
atmfVpcQoSCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcQoSCategory.setStatus(_J)
class _AtmfVpcTransmitQoSClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmfVpcTransmitQoSClass_Type.__name__=_C
_AtmfVpcTransmitQoSClass_Object=MibTableColumn
atmfVpcTransmitQoSClass=_AtmfVpcTransmitQoSClass_Object((1,3,6,1,4,1,353,2,4,1,1,17),_AtmfVpcTransmitQoSClass_Type())
atmfVpcTransmitQoSClass.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcTransmitQoSClass.setStatus(_E)
class _AtmfVpcReceiveQoSClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmfVpcReceiveQoSClass_Type.__name__=_C
_AtmfVpcReceiveQoSClass_Object=MibTableColumn
atmfVpcReceiveQoSClass=_AtmfVpcReceiveQoSClass_Object((1,3,6,1,4,1,353,2,4,1,1,18),_AtmfVpcReceiveQoSClass_Type())
atmfVpcReceiveQoSClass.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcReceiveQoSClass.setStatus(_E)
_AtmfVpcBestEffortIndicator_Type=TruthValue
_AtmfVpcBestEffortIndicator_Object=MibTableColumn
atmfVpcBestEffortIndicator=_AtmfVpcBestEffortIndicator_Object((1,3,6,1,4,1,353,2,4,1,1,19),_AtmfVpcBestEffortIndicator_Type())
atmfVpcBestEffortIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcBestEffortIndicator.setStatus(_A)
_AtmfVpcServiceCategory_Type=AtmServiceCategory
_AtmfVpcServiceCategory_Object=MibTableColumn
atmfVpcServiceCategory=_AtmfVpcServiceCategory_Object((1,3,6,1,4,1,353,2,4,1,1,20),_AtmfVpcServiceCategory_Type())
atmfVpcServiceCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcServiceCategory.setStatus(_A)
_AtmfVccGroup_ObjectIdentity=ObjectIdentity
atmfVccGroup=_AtmfVccGroup_ObjectIdentity((1,3,6,1,4,1,353,2,5))
_AtmfVccTable_Object=MibTable
atmfVccTable=_AtmfVccTable_Object((1,3,6,1,4,1,353,2,5,1))
if mibBuilder.loadTexts:atmfVccTable.setStatus(_A)
_AtmfVccEntry_Object=MibTableRow
atmfVccEntry=_AtmfVccEntry_Object((1,3,6,1,4,1,353,2,5,1,1))
atmfVccEntry.setIndexNames((0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:atmfVccEntry.setStatus(_A)
class _AtmfVccPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccPortIndex_Type.__name__=_C
_AtmfVccPortIndex_Object=MibTableColumn
atmfVccPortIndex=_AtmfVccPortIndex_Object((1,3,6,1,4,1,353,2,5,1,1,1),_AtmfVccPortIndex_Type())
atmfVccPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccPortIndex.setStatus(_A)
class _AtmfVccVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AtmfVccVpi_Type.__name__=_C
_AtmfVccVpi_Object=MibTableColumn
atmfVccVpi=_AtmfVccVpi_Object((1,3,6,1,4,1,353,2,5,1,1,2),_AtmfVccVpi_Type())
atmfVccVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccVpi.setStatus(_A)
class _AtmfVccVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmfVccVci_Type.__name__=_C
_AtmfVccVci_Object=MibTableColumn
atmfVccVci=_AtmfVccVci_Object((1,3,6,1,4,1,353,2,5,1,1,3),_AtmfVccVci_Type())
atmfVccVci.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccVci.setStatus(_A)
class _AtmfVccOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3),(_X,4),(_Y,5)))
_AtmfVccOperStatus_Type.__name__=_C
_AtmfVccOperStatus_Object=MibTableColumn
atmfVccOperStatus=_AtmfVccOperStatus_Object((1,3,6,1,4,1,353,2,5,1,1,4),_AtmfVccOperStatus_Type())
atmfVccOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccOperStatus.setStatus(_A)
_AtmfVccTransmitTrafficDescriptorType_Type=ObjectIdentifier
_AtmfVccTransmitTrafficDescriptorType_Object=MibTableColumn
atmfVccTransmitTrafficDescriptorType=_AtmfVccTransmitTrafficDescriptorType_Object((1,3,6,1,4,1,353,2,5,1,1,5),_AtmfVccTransmitTrafficDescriptorType_Type())
atmfVccTransmitTrafficDescriptorType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccTransmitTrafficDescriptorType.setStatus(_A)
class _AtmfVccTransmitTrafficDescriptorParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccTransmitTrafficDescriptorParam1_Type.__name__=_C
_AtmfVccTransmitTrafficDescriptorParam1_Object=MibTableColumn
atmfVccTransmitTrafficDescriptorParam1=_AtmfVccTransmitTrafficDescriptorParam1_Object((1,3,6,1,4,1,353,2,5,1,1,6),_AtmfVccTransmitTrafficDescriptorParam1_Type())
atmfVccTransmitTrafficDescriptorParam1.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccTransmitTrafficDescriptorParam1.setStatus(_A)
class _AtmfVccTransmitTrafficDescriptorParam2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccTransmitTrafficDescriptorParam2_Type.__name__=_C
_AtmfVccTransmitTrafficDescriptorParam2_Object=MibTableColumn
atmfVccTransmitTrafficDescriptorParam2=_AtmfVccTransmitTrafficDescriptorParam2_Object((1,3,6,1,4,1,353,2,5,1,1,7),_AtmfVccTransmitTrafficDescriptorParam2_Type())
atmfVccTransmitTrafficDescriptorParam2.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccTransmitTrafficDescriptorParam2.setStatus(_A)
class _AtmfVccTransmitTrafficDescriptorParam3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccTransmitTrafficDescriptorParam3_Type.__name__=_C
_AtmfVccTransmitTrafficDescriptorParam3_Object=MibTableColumn
atmfVccTransmitTrafficDescriptorParam3=_AtmfVccTransmitTrafficDescriptorParam3_Object((1,3,6,1,4,1,353,2,5,1,1,8),_AtmfVccTransmitTrafficDescriptorParam3_Type())
atmfVccTransmitTrafficDescriptorParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccTransmitTrafficDescriptorParam3.setStatus(_A)
class _AtmfVccTransmitTrafficDescriptorParam4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccTransmitTrafficDescriptorParam4_Type.__name__=_C
_AtmfVccTransmitTrafficDescriptorParam4_Object=MibTableColumn
atmfVccTransmitTrafficDescriptorParam4=_AtmfVccTransmitTrafficDescriptorParam4_Object((1,3,6,1,4,1,353,2,5,1,1,9),_AtmfVccTransmitTrafficDescriptorParam4_Type())
atmfVccTransmitTrafficDescriptorParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccTransmitTrafficDescriptorParam4.setStatus(_A)
class _AtmfVccTransmitTrafficDescriptorParam5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccTransmitTrafficDescriptorParam5_Type.__name__=_C
_AtmfVccTransmitTrafficDescriptorParam5_Object=MibTableColumn
atmfVccTransmitTrafficDescriptorParam5=_AtmfVccTransmitTrafficDescriptorParam5_Object((1,3,6,1,4,1,353,2,5,1,1,10),_AtmfVccTransmitTrafficDescriptorParam5_Type())
atmfVccTransmitTrafficDescriptorParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccTransmitTrafficDescriptorParam5.setStatus(_A)
_AtmfVccReceiveTrafficDescriptorType_Type=ObjectIdentifier
_AtmfVccReceiveTrafficDescriptorType_Object=MibTableColumn
atmfVccReceiveTrafficDescriptorType=_AtmfVccReceiveTrafficDescriptorType_Object((1,3,6,1,4,1,353,2,5,1,1,11),_AtmfVccReceiveTrafficDescriptorType_Type())
atmfVccReceiveTrafficDescriptorType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccReceiveTrafficDescriptorType.setStatus(_A)
class _AtmfVccReceiveTrafficDescriptorParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccReceiveTrafficDescriptorParam1_Type.__name__=_C
_AtmfVccReceiveTrafficDescriptorParam1_Object=MibTableColumn
atmfVccReceiveTrafficDescriptorParam1=_AtmfVccReceiveTrafficDescriptorParam1_Object((1,3,6,1,4,1,353,2,5,1,1,12),_AtmfVccReceiveTrafficDescriptorParam1_Type())
atmfVccReceiveTrafficDescriptorParam1.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccReceiveTrafficDescriptorParam1.setStatus(_A)
class _AtmfVccReceiveTrafficDescriptorParam2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccReceiveTrafficDescriptorParam2_Type.__name__=_C
_AtmfVccReceiveTrafficDescriptorParam2_Object=MibTableColumn
atmfVccReceiveTrafficDescriptorParam2=_AtmfVccReceiveTrafficDescriptorParam2_Object((1,3,6,1,4,1,353,2,5,1,1,13),_AtmfVccReceiveTrafficDescriptorParam2_Type())
atmfVccReceiveTrafficDescriptorParam2.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccReceiveTrafficDescriptorParam2.setStatus(_A)
class _AtmfVccReceiveTrafficDescriptorParam3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccReceiveTrafficDescriptorParam3_Type.__name__=_C
_AtmfVccReceiveTrafficDescriptorParam3_Object=MibTableColumn
atmfVccReceiveTrafficDescriptorParam3=_AtmfVccReceiveTrafficDescriptorParam3_Object((1,3,6,1,4,1,353,2,5,1,1,14),_AtmfVccReceiveTrafficDescriptorParam3_Type())
atmfVccReceiveTrafficDescriptorParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccReceiveTrafficDescriptorParam3.setStatus(_A)
class _AtmfVccReceiveTrafficDescriptorParam4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccReceiveTrafficDescriptorParam4_Type.__name__=_C
_AtmfVccReceiveTrafficDescriptorParam4_Object=MibTableColumn
atmfVccReceiveTrafficDescriptorParam4=_AtmfVccReceiveTrafficDescriptorParam4_Object((1,3,6,1,4,1,353,2,5,1,1,15),_AtmfVccReceiveTrafficDescriptorParam4_Type())
atmfVccReceiveTrafficDescriptorParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccReceiveTrafficDescriptorParam4.setStatus(_A)
class _AtmfVccReceiveTrafficDescriptorParam5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccReceiveTrafficDescriptorParam5_Type.__name__=_C
_AtmfVccReceiveTrafficDescriptorParam5_Object=MibTableColumn
atmfVccReceiveTrafficDescriptorParam5=_AtmfVccReceiveTrafficDescriptorParam5_Object((1,3,6,1,4,1,353,2,5,1,1,16),_AtmfVccReceiveTrafficDescriptorParam5_Type())
atmfVccReceiveTrafficDescriptorParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccReceiveTrafficDescriptorParam5.setStatus(_A)
class _AtmfVccQoSCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_Z,2),(_a,3),(_b,4)))
_AtmfVccQoSCategory_Type.__name__=_C
_AtmfVccQoSCategory_Object=MibTableColumn
atmfVccQoSCategory=_AtmfVccQoSCategory_Object((1,3,6,1,4,1,353,2,5,1,1,17),_AtmfVccQoSCategory_Type())
atmfVccQoSCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccQoSCategory.setStatus(_J)
class _AtmfVccTransmitQoSClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmfVccTransmitQoSClass_Type.__name__=_C
_AtmfVccTransmitQoSClass_Object=MibTableColumn
atmfVccTransmitQoSClass=_AtmfVccTransmitQoSClass_Object((1,3,6,1,4,1,353,2,5,1,1,18),_AtmfVccTransmitQoSClass_Type())
atmfVccTransmitQoSClass.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccTransmitQoSClass.setStatus(_E)
class _AtmfVccReceiveQoSClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmfVccReceiveQoSClass_Type.__name__=_C
_AtmfVccReceiveQoSClass_Object=MibTableColumn
atmfVccReceiveQoSClass=_AtmfVccReceiveQoSClass_Object((1,3,6,1,4,1,353,2,5,1,1,19),_AtmfVccReceiveQoSClass_Type())
atmfVccReceiveQoSClass.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccReceiveQoSClass.setStatus(_E)
_AtmfVccBestEffortIndicator_Type=TruthValue
_AtmfVccBestEffortIndicator_Object=MibTableColumn
atmfVccBestEffortIndicator=_AtmfVccBestEffortIndicator_Object((1,3,6,1,4,1,353,2,5,1,1,20),_AtmfVccBestEffortIndicator_Type())
atmfVccBestEffortIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccBestEffortIndicator.setStatus(_A)
_AtmfVccTransmitFrameDiscard_Type=TruthValue
_AtmfVccTransmitFrameDiscard_Object=MibTableColumn
atmfVccTransmitFrameDiscard=_AtmfVccTransmitFrameDiscard_Object((1,3,6,1,4,1,353,2,5,1,1,21),_AtmfVccTransmitFrameDiscard_Type())
atmfVccTransmitFrameDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccTransmitFrameDiscard.setStatus(_A)
_AtmfVccReceiveFrameDiscard_Type=TruthValue
_AtmfVccReceiveFrameDiscard_Object=MibTableColumn
atmfVccReceiveFrameDiscard=_AtmfVccReceiveFrameDiscard_Object((1,3,6,1,4,1,353,2,5,1,1,22),_AtmfVccReceiveFrameDiscard_Type())
atmfVccReceiveFrameDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccReceiveFrameDiscard.setStatus(_A)
_AtmfVccServiceCategory_Type=AtmServiceCategory
_AtmfVccServiceCategory_Object=MibTableColumn
atmfVccServiceCategory=_AtmfVccServiceCategory_Object((1,3,6,1,4,1,353,2,5,1,1,23),_AtmfVccServiceCategory_Type())
atmfVccServiceCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccServiceCategory.setStatus(_A)
_AtmfAddressGroup_ObjectIdentity=ObjectIdentity
atmfAddressGroup=_AtmfAddressGroup_ObjectIdentity((1,3,6,1,4,1,353,2,6))
_AtmfAddressTable_Object=MibTable
atmfAddressTable=_AtmfAddressTable_Object((1,3,6,1,4,1,353,2,6,1))
if mibBuilder.loadTexts:atmfAddressTable.setStatus(_A)
_AtmfAddressEntry_Object=MibTableRow
atmfAddressEntry=_AtmfAddressEntry_Object((1,3,6,1,4,1,353,2,6,1,1))
atmfAddressEntry.setIndexNames((0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:atmfAddressEntry.setStatus(_A)
class _AtmfAddressPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfAddressPort_Type.__name__=_C
_AtmfAddressPort_Object=MibTableColumn
atmfAddressPort=_AtmfAddressPort_Object((1,3,6,1,4,1,353,2,6,1,1,1),_AtmfAddressPort_Type())
atmfAddressPort.setMaxAccess(_F)
if mibBuilder.loadTexts:atmfAddressPort.setStatus(_A)
_AtmfAddressAtmAddress_Type=AtmAddress
_AtmfAddressAtmAddress_Object=MibTableColumn
atmfAddressAtmAddress=_AtmfAddressAtmAddress_Object((1,3,6,1,4,1,353,2,6,1,1,2),_AtmfAddressAtmAddress_Type())
atmfAddressAtmAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:atmfAddressAtmAddress.setStatus(_A)
class _AtmfAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_AtmfAddressStatus_Type.__name__=_C
_AtmfAddressStatus_Object=MibTableColumn
atmfAddressStatus=_AtmfAddressStatus_Object((1,3,6,1,4,1,353,2,6,1,1,3),_AtmfAddressStatus_Type())
atmfAddressStatus.setMaxAccess(_e)
if mibBuilder.loadTexts:atmfAddressStatus.setStatus(_A)
class _AtmfAddressOrgScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('localNetwork',1),('localNetworkPlusOne',2),('localNetworkPlusTwo',3),('siteMinusOne',4),('intraSite',5),('sitePlusOne',6),('organizationMinusOne',7),('intraOrganization',8),('organizationPlusOne',9),('communityMinusOne',10),('intraCommunity',11),('communityPlusOne',12),('regional',13),('interRegional',14),('global',15)))
_AtmfAddressOrgScope_Type.__name__=_C
_AtmfAddressOrgScope_Object=MibTableColumn
atmfAddressOrgScope=_AtmfAddressOrgScope_Object((1,3,6,1,4,1,353,2,6,1,1,4),_AtmfAddressOrgScope_Type())
atmfAddressOrgScope.setMaxAccess(_e)
if mibBuilder.loadTexts:atmfAddressOrgScope.setStatus(_A)
_AtmfNetPrefixGroup_ObjectIdentity=ObjectIdentity
atmfNetPrefixGroup=_AtmfNetPrefixGroup_ObjectIdentity((1,3,6,1,4,1,353,2,7))
_AtmfSrvcRegistryGroup_ObjectIdentity=ObjectIdentity
atmfSrvcRegistryGroup=_AtmfSrvcRegistryGroup_ObjectIdentity((1,3,6,1,4,1,353,2,8))
_AtmfSrvcRegTable_Object=MibTable
atmfSrvcRegTable=_AtmfSrvcRegTable_Object((1,3,6,1,4,1,353,2,8,1))
if mibBuilder.loadTexts:atmfSrvcRegTable.setStatus(_A)
_AtmfSrvcRegEntry_Object=MibTableRow
atmfSrvcRegEntry=_AtmfSrvcRegEntry_Object((1,3,6,1,4,1,353,2,8,1,1))
atmfSrvcRegEntry.setIndexNames((0,_D,_f),(0,_D,_g),(0,_D,_h))
if mibBuilder.loadTexts:atmfSrvcRegEntry.setStatus(_A)
class _AtmfSrvcRegPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfSrvcRegPort_Type.__name__=_C
_AtmfSrvcRegPort_Object=MibTableColumn
atmfSrvcRegPort=_AtmfSrvcRegPort_Object((1,3,6,1,4,1,353,2,8,1,1,1),_AtmfSrvcRegPort_Type())
atmfSrvcRegPort.setMaxAccess(_F)
if mibBuilder.loadTexts:atmfSrvcRegPort.setStatus(_A)
_AtmfSrvcRegServiceID_Type=ObjectIdentifier
_AtmfSrvcRegServiceID_Object=MibTableColumn
atmfSrvcRegServiceID=_AtmfSrvcRegServiceID_Object((1,3,6,1,4,1,353,2,8,1,1,2),_AtmfSrvcRegServiceID_Type())
atmfSrvcRegServiceID.setMaxAccess(_F)
if mibBuilder.loadTexts:atmfSrvcRegServiceID.setStatus(_A)
_AtmfSrvcRegATMAddress_Type=AtmAddress
_AtmfSrvcRegATMAddress_Object=MibTableColumn
atmfSrvcRegATMAddress=_AtmfSrvcRegATMAddress_Object((1,3,6,1,4,1,353,2,8,1,1,3),_AtmfSrvcRegATMAddress_Type())
atmfSrvcRegATMAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfSrvcRegATMAddress.setStatus(_A)
class _AtmfSrvcRegAddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AtmfSrvcRegAddressIndex_Type.__name__=_C
_AtmfSrvcRegAddressIndex_Object=MibTableColumn
atmfSrvcRegAddressIndex=_AtmfSrvcRegAddressIndex_Object((1,3,6,1,4,1,353,2,8,1,1,4),_AtmfSrvcRegAddressIndex_Type())
atmfSrvcRegAddressIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:atmfSrvcRegAddressIndex.setStatus(_A)
class _AtmfSrvcRegParm1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AtmfSrvcRegParm1_Type.__name__=_I
_AtmfSrvcRegParm1_Object=MibTableColumn
atmfSrvcRegParm1=_AtmfSrvcRegParm1_Object((1,3,6,1,4,1,353,2,8,1,1,5),_AtmfSrvcRegParm1_Type())
atmfSrvcRegParm1.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfSrvcRegParm1.setStatus(_A)
_AtmfVpcAbrGroup_ObjectIdentity=ObjectIdentity
atmfVpcAbrGroup=_AtmfVpcAbrGroup_ObjectIdentity((1,3,6,1,4,1,353,2,9))
_AtmfVpcAbrTable_Object=MibTable
atmfVpcAbrTable=_AtmfVpcAbrTable_Object((1,3,6,1,4,1,353,2,9,1))
if mibBuilder.loadTexts:atmfVpcAbrTable.setStatus(_A)
_AtmfVpcAbrEntry_Object=MibTableRow
atmfVpcAbrEntry=_AtmfVpcAbrEntry_Object((1,3,6,1,4,1,353,2,9,1,1))
atmfVpcAbrEntry.setIndexNames((0,_D,_i),(0,_D,_j))
if mibBuilder.loadTexts:atmfVpcAbrEntry.setStatus(_A)
class _AtmfVpcAbrPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcAbrPortIndex_Type.__name__=_C
_AtmfVpcAbrPortIndex_Object=MibTableColumn
atmfVpcAbrPortIndex=_AtmfVpcAbrPortIndex_Object((1,3,6,1,4,1,353,2,9,1,1,1),_AtmfVpcAbrPortIndex_Type())
atmfVpcAbrPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcAbrPortIndex.setStatus(_A)
class _AtmfVpcAbrVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AtmfVpcAbrVpi_Type.__name__=_C
_AtmfVpcAbrVpi_Object=MibTableColumn
atmfVpcAbrVpi=_AtmfVpcAbrVpi_Object((1,3,6,1,4,1,353,2,9,1,1,2),_AtmfVpcAbrVpi_Type())
atmfVpcAbrVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcAbrVpi.setStatus(_A)
class _AtmfVpcAbrTransmitIcr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AtmfVpcAbrTransmitIcr_Type.__name__=_C
_AtmfVpcAbrTransmitIcr_Object=MibTableColumn
atmfVpcAbrTransmitIcr=_AtmfVpcAbrTransmitIcr_Object((1,3,6,1,4,1,353,2,9,1,1,3),_AtmfVpcAbrTransmitIcr_Type())
atmfVpcAbrTransmitIcr.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcAbrTransmitIcr.setStatus(_A)
class _AtmfVpcAbrTransmitNrm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('nrm2',1),('nrm4',2),('nrm8',3),('nrm16',4),('nrm32',5),('nrm64',6),(_k,7),(_l,8)))
_AtmfVpcAbrTransmitNrm_Type.__name__=_C
_AtmfVpcAbrTransmitNrm_Object=MibTableColumn
atmfVpcAbrTransmitNrm=_AtmfVpcAbrTransmitNrm_Object((1,3,6,1,4,1,353,2,9,1,1,4),_AtmfVpcAbrTransmitNrm_Type())
atmfVpcAbrTransmitNrm.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcAbrTransmitNrm.setStatus(_A)
class _AtmfVpcAbrTransmitTrm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_m,1),(_n,2),(_o,3),(_p,4),(_q,5),('trm25',6),('trm50',7),(_r,8)))
_AtmfVpcAbrTransmitTrm_Type.__name__=_C
_AtmfVpcAbrTransmitTrm_Object=MibTableColumn
atmfVpcAbrTransmitTrm=_AtmfVpcAbrTransmitTrm_Object((1,3,6,1,4,1,353,2,9,1,1,5),_AtmfVpcAbrTransmitTrm_Type())
atmfVpcAbrTransmitTrm.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcAbrTransmitTrm.setStatus(_A)
class _AtmfVpcAbrTransmitCdf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('cdf0',1),(_s,2),(_t,3),(_u,4),(_v,5),(_w,6),(_x,7),(_y,8)))
_AtmfVpcAbrTransmitCdf_Type.__name__=_C
_AtmfVpcAbrTransmitCdf_Object=MibTableColumn
atmfVpcAbrTransmitCdf=_AtmfVpcAbrTransmitCdf_Object((1,3,6,1,4,1,353,2,9,1,1,6),_AtmfVpcAbrTransmitCdf_Type())
atmfVpcAbrTransmitCdf.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcAbrTransmitCdf.setStatus(_A)
class _AtmfVpcAbrTransmitRif_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_z,1),(_A0,2),(_A1,3),(_A2,4),(_A3,5),(_A4,6),(_A5,7),(_A6,8),(_A7,9),(_A8,10),(_A9,11),(_AA,12),(_AB,13),(_AC,14),(_AD,15),('rifOne',16)))
_AtmfVpcAbrTransmitRif_Type.__name__=_C
_AtmfVpcAbrTransmitRif_Object=MibTableColumn
atmfVpcAbrTransmitRif=_AtmfVpcAbrTransmitRif_Object((1,3,6,1,4,1,353,2,9,1,1,7),_AtmfVpcAbrTransmitRif_Type())
atmfVpcAbrTransmitRif.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcAbrTransmitRif.setStatus(_A)
class _AtmfVpcAbrTransmitRdf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_AE,1),(_AF,2),(_AG,3),(_AH,4),(_AI,5),(_AJ,6),(_AK,7),(_AL,8),(_AM,9),(_AN,10),(_AO,11),(_AP,12),(_AQ,13),(_AR,14),(_AS,15),('rdfOne',16)))
_AtmfVpcAbrTransmitRdf_Type.__name__=_C
_AtmfVpcAbrTransmitRdf_Object=MibTableColumn
atmfVpcAbrTransmitRdf=_AtmfVpcAbrTransmitRdf_Object((1,3,6,1,4,1,353,2,9,1,1,8),_AtmfVpcAbrTransmitRdf_Type())
atmfVpcAbrTransmitRdf.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcAbrTransmitRdf.setStatus(_A)
class _AtmfVpcAbrTransmitAdtf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_AtmfVpcAbrTransmitAdtf_Type.__name__=_C
_AtmfVpcAbrTransmitAdtf_Object=MibTableColumn
atmfVpcAbrTransmitAdtf=_AtmfVpcAbrTransmitAdtf_Object((1,3,6,1,4,1,353,2,9,1,1,9),_AtmfVpcAbrTransmitAdtf_Type())
atmfVpcAbrTransmitAdtf.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcAbrTransmitAdtf.setStatus(_A)
class _AtmfVpcAbrTransmitCrm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388608))
_AtmfVpcAbrTransmitCrm_Type.__name__=_C
_AtmfVpcAbrTransmitCrm_Object=MibTableColumn
atmfVpcAbrTransmitCrm=_AtmfVpcAbrTransmitCrm_Object((1,3,6,1,4,1,353,2,9,1,1,10),_AtmfVpcAbrTransmitCrm_Type())
atmfVpcAbrTransmitCrm.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVpcAbrTransmitCrm.setStatus(_A)
_AtmfVccAbrGroup_ObjectIdentity=ObjectIdentity
atmfVccAbrGroup=_AtmfVccAbrGroup_ObjectIdentity((1,3,6,1,4,1,353,2,10))
_AtmfVccAbrTable_Object=MibTable
atmfVccAbrTable=_AtmfVccAbrTable_Object((1,3,6,1,4,1,353,2,10,1))
if mibBuilder.loadTexts:atmfVccAbrTable.setStatus(_A)
_AtmfVccAbrEntry_Object=MibTableRow
atmfVccAbrEntry=_AtmfVccAbrEntry_Object((1,3,6,1,4,1,353,2,10,1,1))
atmfVccAbrEntry.setIndexNames((0,_D,_AT),(0,_D,_AU),(0,_D,_AV))
if mibBuilder.loadTexts:atmfVccAbrEntry.setStatus(_A)
class _AtmfVccAbrPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccAbrPortIndex_Type.__name__=_C
_AtmfVccAbrPortIndex_Object=MibTableColumn
atmfVccAbrPortIndex=_AtmfVccAbrPortIndex_Object((1,3,6,1,4,1,353,2,10,1,1,1),_AtmfVccAbrPortIndex_Type())
atmfVccAbrPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccAbrPortIndex.setStatus(_A)
class _AtmfVccAbrVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AtmfVccAbrVpi_Type.__name__=_C
_AtmfVccAbrVpi_Object=MibTableColumn
atmfVccAbrVpi=_AtmfVccAbrVpi_Object((1,3,6,1,4,1,353,2,10,1,1,2),_AtmfVccAbrVpi_Type())
atmfVccAbrVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccAbrVpi.setStatus(_A)
class _AtmfVccAbrVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmfVccAbrVci_Type.__name__=_C
_AtmfVccAbrVci_Object=MibTableColumn
atmfVccAbrVci=_AtmfVccAbrVci_Object((1,3,6,1,4,1,353,2,10,1,1,3),_AtmfVccAbrVci_Type())
atmfVccAbrVci.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccAbrVci.setStatus(_A)
class _AtmfVccAbrTransmitIcr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AtmfVccAbrTransmitIcr_Type.__name__=_C
_AtmfVccAbrTransmitIcr_Object=MibTableColumn
atmfVccAbrTransmitIcr=_AtmfVccAbrTransmitIcr_Object((1,3,6,1,4,1,353,2,10,1,1,4),_AtmfVccAbrTransmitIcr_Type())
atmfVccAbrTransmitIcr.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccAbrTransmitIcr.setStatus(_A)
class _AtmfVccAbrTransmitNrm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('nrm2',1),('nrm4',2),('nrm8',3),('nrm16',4),('nrm32',5),('nrm64',6),(_k,7),(_l,8)))
_AtmfVccAbrTransmitNrm_Type.__name__=_C
_AtmfVccAbrTransmitNrm_Object=MibTableColumn
atmfVccAbrTransmitNrm=_AtmfVccAbrTransmitNrm_Object((1,3,6,1,4,1,353,2,10,1,1,5),_AtmfVccAbrTransmitNrm_Type())
atmfVccAbrTransmitNrm.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccAbrTransmitNrm.setStatus(_A)
class _AtmfVccAbrTransmitTrm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_m,1),(_n,2),(_o,3),(_p,4),(_q,5),('trm25',6),('trm50',7),(_r,8)))
_AtmfVccAbrTransmitTrm_Type.__name__=_C
_AtmfVccAbrTransmitTrm_Object=MibTableColumn
atmfVccAbrTransmitTrm=_AtmfVccAbrTransmitTrm_Object((1,3,6,1,4,1,353,2,10,1,1,6),_AtmfVccAbrTransmitTrm_Type())
atmfVccAbrTransmitTrm.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccAbrTransmitTrm.setStatus(_A)
class _AtmfVccAbrTransmitCdf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('cdf0',1),(_s,2),(_t,3),(_u,4),(_v,5),(_w,6),(_x,7),(_y,8)))
_AtmfVccAbrTransmitCdf_Type.__name__=_C
_AtmfVccAbrTransmitCdf_Object=MibTableColumn
atmfVccAbrTransmitCdf=_AtmfVccAbrTransmitCdf_Object((1,3,6,1,4,1,353,2,10,1,1,7),_AtmfVccAbrTransmitCdf_Type())
atmfVccAbrTransmitCdf.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccAbrTransmitCdf.setStatus(_A)
class _AtmfVccAbrTransmitRif_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_z,1),(_A0,2),(_A1,3),(_A2,4),(_A3,5),(_A4,6),(_A5,7),(_A6,8),(_A7,9),(_A8,10),(_A9,11),(_AA,12),(_AB,13),(_AC,14),(_AD,15),('rifOne',16)))
_AtmfVccAbrTransmitRif_Type.__name__=_C
_AtmfVccAbrTransmitRif_Object=MibTableColumn
atmfVccAbrTransmitRif=_AtmfVccAbrTransmitRif_Object((1,3,6,1,4,1,353,2,10,1,1,8),_AtmfVccAbrTransmitRif_Type())
atmfVccAbrTransmitRif.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccAbrTransmitRif.setStatus(_A)
class _AtmfVccAbrTransmitRdf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_AE,1),(_AF,2),(_AG,3),(_AH,4),(_AI,5),(_AJ,6),(_AK,7),(_AL,8),(_AM,9),(_AN,10),(_AO,11),(_AP,12),(_AQ,13),(_AR,14),(_AS,15),('rdfOne',16)))
_AtmfVccAbrTransmitRdf_Type.__name__=_C
_AtmfVccAbrTransmitRdf_Object=MibTableColumn
atmfVccAbrTransmitRdf=_AtmfVccAbrTransmitRdf_Object((1,3,6,1,4,1,353,2,10,1,1,9),_AtmfVccAbrTransmitRdf_Type())
atmfVccAbrTransmitRdf.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccAbrTransmitRdf.setStatus(_A)
class _AtmfVccAbrTransmitAdtf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_AtmfVccAbrTransmitAdtf_Type.__name__=_C
_AtmfVccAbrTransmitAdtf_Object=MibTableColumn
atmfVccAbrTransmitAdtf=_AtmfVccAbrTransmitAdtf_Object((1,3,6,1,4,1,353,2,10,1,1,10),_AtmfVccAbrTransmitAdtf_Type())
atmfVccAbrTransmitAdtf.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccAbrTransmitAdtf.setStatus(_A)
class _AtmfVccAbrTransmitCrm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388608))
_AtmfVccAbrTransmitCrm_Type.__name__=_C
_AtmfVccAbrTransmitCrm_Object=MibTableColumn
atmfVccAbrTransmitCrm=_AtmfVccAbrTransmitCrm_Object((1,3,6,1,4,1,353,2,10,1,1,11),_AtmfVccAbrTransmitCrm_Type())
atmfVccAbrTransmitCrm.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfVccAbrTransmitCrm.setStatus(_A)
_AtmfAddressRegistrationAdminGroup_ObjectIdentity=ObjectIdentity
atmfAddressRegistrationAdminGroup=_AtmfAddressRegistrationAdminGroup_ObjectIdentity((1,3,6,1,4,1,353,2,11))
_AtmfAddressRegistrationAdminTable_Object=MibTable
atmfAddressRegistrationAdminTable=_AtmfAddressRegistrationAdminTable_Object((1,3,6,1,4,1,353,2,11,1))
if mibBuilder.loadTexts:atmfAddressRegistrationAdminTable.setStatus(_A)
_AtmfAddressRegistrationAdminEntry_Object=MibTableRow
atmfAddressRegistrationAdminEntry=_AtmfAddressRegistrationAdminEntry_Object((1,3,6,1,4,1,353,2,11,1,1))
atmfAddressRegistrationAdminEntry.setIndexNames((0,_D,_AW))
if mibBuilder.loadTexts:atmfAddressRegistrationAdminEntry.setStatus(_A)
class _AtmfAddressRegistrationAdminIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfAddressRegistrationAdminIndex_Type.__name__=_C
_AtmfAddressRegistrationAdminIndex_Object=MibTableColumn
atmfAddressRegistrationAdminIndex=_AtmfAddressRegistrationAdminIndex_Object((1,3,6,1,4,1,353,2,11,1,1,1),_AtmfAddressRegistrationAdminIndex_Type())
atmfAddressRegistrationAdminIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAddressRegistrationAdminIndex.setStatus(_A)
class _AtmfAddressRegistrationAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('supported',1),(_H,2)))
_AtmfAddressRegistrationAdminStatus_Type.__name__=_C
_AtmfAddressRegistrationAdminStatus_Object=MibTableColumn
atmfAddressRegistrationAdminStatus=_AtmfAddressRegistrationAdminStatus_Object((1,3,6,1,4,1,353,2,11,1,1,2),_AtmfAddressRegistrationAdminStatus_Type())
atmfAddressRegistrationAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atmfAddressRegistrationAdminStatus.setStatus(_A)
atmfVpcChange=NotificationType((1,3,6,1,4,1,353,0,1))
atmfVpcChange.setObjects(*((_D,_K),(_D,_L),(_D,_AX)))
if mibBuilder.loadTexts:atmfVpcChange.setStatus('')
atmfVccChange=NotificationType((1,3,6,1,4,1,353,0,2))
atmfVccChange.setObjects(*((_D,_M),(_D,_O),(_D,_N),(_D,_AY)))
if mibBuilder.loadTexts:atmfVccChange.setStatus('')
mibBuilder.exportSymbols(_D,**{'AtmAddress':AtmAddress,'TruthValue':TruthValue,'ClnpAddress':ClnpAddress,'AtmServiceCategory':AtmServiceCategory,'atmForum':atmForum,'atmfVpcChange':atmfVpcChange,'atmfVccChange':atmfVccChange,'atmForumAdmin':atmForumAdmin,'atmfTransmissionTypes':atmfTransmissionTypes,'atmfUnknownType':atmfUnknownType,'atmfSonetSTS3c':atmfSonetSTS3c,'atmfDs3':atmfDs3,'atmf4B5B':atmf4B5B,'atmf8B10B':atmf8B10B,'atmfSonetSTS12c':atmfSonetSTS12c,'atmfE3':atmfE3,'atmfT1':atmfT1,'atmfE1':atmfE1,'atmfMediaTypes':atmfMediaTypes,'atmfMediaUnknownType':atmfMediaUnknownType,'atmfMediaCoaxCable':atmfMediaCoaxCable,'atmfMediaSingleMode':atmfMediaSingleMode,'atmfMediaMultiMode':atmfMediaMultiMode,'atmfMediaStp':atmfMediaStp,'atmfMediaUtp':atmfMediaUtp,'atmfTrafficDescrTypes':atmfTrafficDescrTypes,'atmfNoDescriptor':atmfNoDescriptor,'atmfPeakRate':atmfPeakRate,'atmfNoClpNoScr':atmfNoClpNoScr,'atmfClpNoTaggingNoScr':atmfClpNoTaggingNoScr,'atmfClpTaggingNoScr':atmfClpTaggingNoScr,'atmfNoClpScr':atmfNoClpScr,'atmfClpNoTaggingScr':atmfClpNoTaggingScr,'atmfClpTaggingScr':atmfClpTaggingScr,'atmfClpNoTaggingMcr':atmfClpNoTaggingMcr,'atmfSrvcRegTypes':atmfSrvcRegTypes,'atmfSrvcRegLecs':atmfSrvcRegLecs,'atmfSrvcRegAns':atmfSrvcRegAns,'atmForumUni':atmForumUni,'atmfPhysicalGroup':atmfPhysicalGroup,'atmfPortTable':atmfPortTable,'atmfPortEntry':atmfPortEntry,_Q:atmfPortIndex,'atmfPortAddress':atmfPortAddress,'atmfPortTransmissionType':atmfPortTransmissionType,'atmfPortMediaType':atmfPortMediaType,'atmfPortOperStatus':atmfPortOperStatus,'atmfPortSpecific':atmfPortSpecific,'atmfPortMyIfName':atmfPortMyIfName,'atmfPortMyIfIdentifier':atmfPortMyIfIdentifier,'atmfMyIpNmAddress':atmfMyIpNmAddress,'atmfMyOsiNmNsapAddress':atmfMyOsiNmNsapAddress,'atmfMySystemIdentifier':atmfMySystemIdentifier,'atmfAtmLayerGroup':atmfAtmLayerGroup,'atmfAtmLayerTable':atmfAtmLayerTable,'atmfAtmLayerEntry':atmfAtmLayerEntry,_R:atmfAtmLayerIndex,'atmfAtmLayerMaxVPCs':atmfAtmLayerMaxVPCs,'atmfAtmLayerMaxVCCs':atmfAtmLayerMaxVCCs,'atmfAtmLayerConfiguredVPCs':atmfAtmLayerConfiguredVPCs,'atmfAtmLayerConfiguredVCCs':atmfAtmLayerConfiguredVCCs,'atmfAtmLayerMaxVpiBits':atmfAtmLayerMaxVpiBits,'atmfAtmLayerMaxVciBits':atmfAtmLayerMaxVciBits,'atmfAtmLayerUniType':atmfAtmLayerUniType,'atmfAtmLayerUniVersion':atmfAtmLayerUniVersion,'atmfAtmLayerDeviceType':atmfAtmLayerDeviceType,'atmfAtmLayerIlmiVersion':atmfAtmLayerIlmiVersion,'atmfAtmLayerNniSigVersion':atmfAtmLayerNniSigVersion,'atmfAtmLayerMaxSvpcVpi':atmfAtmLayerMaxSvpcVpi,'atmfAtmLayerMaxSvccVpi':atmfAtmLayerMaxSvccVpi,'atmfAtmLayerMinSvccVci':atmfAtmLayerMinSvccVci,'atmfAtmStatsGroup':atmfAtmStatsGroup,'atmfAtmStatsTable':atmfAtmStatsTable,'atmfAtmStatsEntry':atmfAtmStatsEntry,_T:atmfAtmStatsIndex,'atmfAtmStatsReceivedCells':atmfAtmStatsReceivedCells,'atmfAtmStatsDroppedReceivedCells':atmfAtmStatsDroppedReceivedCells,'atmfAtmStatsTransmittedCells':atmfAtmStatsTransmittedCells,'atmfVpcGroup':atmfVpcGroup,'atmfVpcTable':atmfVpcTable,'atmfVpcEntry':atmfVpcEntry,_K:atmfVpcPortIndex,_L:atmfVpcVpi,_AX:atmfVpcOperStatus,'atmfVpcTransmitTrafficDescriptorType':atmfVpcTransmitTrafficDescriptorType,'atmfVpcTransmitTrafficDescriptorParam1':atmfVpcTransmitTrafficDescriptorParam1,'atmfVpcTransmitTrafficDescriptorParam2':atmfVpcTransmitTrafficDescriptorParam2,'atmfVpcTransmitTrafficDescriptorParam3':atmfVpcTransmitTrafficDescriptorParam3,'atmfVpcTransmitTrafficDescriptorParam4':atmfVpcTransmitTrafficDescriptorParam4,'atmfVpcTransmitTrafficDescriptorParam5':atmfVpcTransmitTrafficDescriptorParam5,'atmfVpcReceiveTrafficDescriptorType':atmfVpcReceiveTrafficDescriptorType,'atmfVpcReceiveTrafficDescriptorParam1':atmfVpcReceiveTrafficDescriptorParam1,'atmfVpcReceiveTrafficDescriptorParam2':atmfVpcReceiveTrafficDescriptorParam2,'atmfVpcReceiveTrafficDescriptorParam3':atmfVpcReceiveTrafficDescriptorParam3,'atmfVpcReceiveTrafficDescriptorParam4':atmfVpcReceiveTrafficDescriptorParam4,'atmfVpcReceiveTrafficDescriptorParam5':atmfVpcReceiveTrafficDescriptorParam5,'atmfVpcQoSCategory':atmfVpcQoSCategory,'atmfVpcTransmitQoSClass':atmfVpcTransmitQoSClass,'atmfVpcReceiveQoSClass':atmfVpcReceiveQoSClass,'atmfVpcBestEffortIndicator':atmfVpcBestEffortIndicator,'atmfVpcServiceCategory':atmfVpcServiceCategory,'atmfVccGroup':atmfVccGroup,'atmfVccTable':atmfVccTable,'atmfVccEntry':atmfVccEntry,_M:atmfVccPortIndex,_N:atmfVccVpi,_O:atmfVccVci,_AY:atmfVccOperStatus,'atmfVccTransmitTrafficDescriptorType':atmfVccTransmitTrafficDescriptorType,'atmfVccTransmitTrafficDescriptorParam1':atmfVccTransmitTrafficDescriptorParam1,'atmfVccTransmitTrafficDescriptorParam2':atmfVccTransmitTrafficDescriptorParam2,'atmfVccTransmitTrafficDescriptorParam3':atmfVccTransmitTrafficDescriptorParam3,'atmfVccTransmitTrafficDescriptorParam4':atmfVccTransmitTrafficDescriptorParam4,'atmfVccTransmitTrafficDescriptorParam5':atmfVccTransmitTrafficDescriptorParam5,'atmfVccReceiveTrafficDescriptorType':atmfVccReceiveTrafficDescriptorType,'atmfVccReceiveTrafficDescriptorParam1':atmfVccReceiveTrafficDescriptorParam1,'atmfVccReceiveTrafficDescriptorParam2':atmfVccReceiveTrafficDescriptorParam2,'atmfVccReceiveTrafficDescriptorParam3':atmfVccReceiveTrafficDescriptorParam3,'atmfVccReceiveTrafficDescriptorParam4':atmfVccReceiveTrafficDescriptorParam4,'atmfVccReceiveTrafficDescriptorParam5':atmfVccReceiveTrafficDescriptorParam5,'atmfVccQoSCategory':atmfVccQoSCategory,'atmfVccTransmitQoSClass':atmfVccTransmitQoSClass,'atmfVccReceiveQoSClass':atmfVccReceiveQoSClass,'atmfVccBestEffortIndicator':atmfVccBestEffortIndicator,'atmfVccTransmitFrameDiscard':atmfVccTransmitFrameDiscard,'atmfVccReceiveFrameDiscard':atmfVccReceiveFrameDiscard,'atmfVccServiceCategory':atmfVccServiceCategory,'atmfAddressGroup':atmfAddressGroup,'atmfAddressTable':atmfAddressTable,'atmfAddressEntry':atmfAddressEntry,_c:atmfAddressPort,_d:atmfAddressAtmAddress,'atmfAddressStatus':atmfAddressStatus,'atmfAddressOrgScope':atmfAddressOrgScope,'atmfNetPrefixGroup':atmfNetPrefixGroup,'atmfSrvcRegistryGroup':atmfSrvcRegistryGroup,'atmfSrvcRegTable':atmfSrvcRegTable,'atmfSrvcRegEntry':atmfSrvcRegEntry,_f:atmfSrvcRegPort,_g:atmfSrvcRegServiceID,'atmfSrvcRegATMAddress':atmfSrvcRegATMAddress,_h:atmfSrvcRegAddressIndex,'atmfSrvcRegParm1':atmfSrvcRegParm1,'atmfVpcAbrGroup':atmfVpcAbrGroup,'atmfVpcAbrTable':atmfVpcAbrTable,'atmfVpcAbrEntry':atmfVpcAbrEntry,_i:atmfVpcAbrPortIndex,_j:atmfVpcAbrVpi,'atmfVpcAbrTransmitIcr':atmfVpcAbrTransmitIcr,'atmfVpcAbrTransmitNrm':atmfVpcAbrTransmitNrm,'atmfVpcAbrTransmitTrm':atmfVpcAbrTransmitTrm,'atmfVpcAbrTransmitCdf':atmfVpcAbrTransmitCdf,'atmfVpcAbrTransmitRif':atmfVpcAbrTransmitRif,'atmfVpcAbrTransmitRdf':atmfVpcAbrTransmitRdf,'atmfVpcAbrTransmitAdtf':atmfVpcAbrTransmitAdtf,'atmfVpcAbrTransmitCrm':atmfVpcAbrTransmitCrm,'atmfVccAbrGroup':atmfVccAbrGroup,'atmfVccAbrTable':atmfVccAbrTable,'atmfVccAbrEntry':atmfVccAbrEntry,_AT:atmfVccAbrPortIndex,_AU:atmfVccAbrVpi,_AV:atmfVccAbrVci,'atmfVccAbrTransmitIcr':atmfVccAbrTransmitIcr,'atmfVccAbrTransmitNrm':atmfVccAbrTransmitNrm,'atmfVccAbrTransmitTrm':atmfVccAbrTransmitTrm,'atmfVccAbrTransmitCdf':atmfVccAbrTransmitCdf,'atmfVccAbrTransmitRif':atmfVccAbrTransmitRif,'atmfVccAbrTransmitRdf':atmfVccAbrTransmitRdf,'atmfVccAbrTransmitAdtf':atmfVccAbrTransmitAdtf,'atmfVccAbrTransmitCrm':atmfVccAbrTransmitCrm,'atmfAddressRegistrationAdminGroup':atmfAddressRegistrationAdminGroup,'atmfAddressRegistrationAdminTable':atmfAddressRegistrationAdminTable,'atmfAddressRegistrationAdminEntry':atmfAddressRegistrationAdminEntry,_AW:atmfAddressRegistrationAdminIndex,'atmfAddressRegistrationAdminStatus':atmfAddressRegistrationAdminStatus})