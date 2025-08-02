_AN='atmfVccAbrVci'
_AM='atmfVccAbrVpi'
_AL='atmfVccAbrPortIndex'
_AK='rdfOneOver2'
_AJ='rdfOneOver4'
_AI='rdfOneOver8'
_AH='rdfOneOver16'
_AG='rdfOneOver32'
_AF='rdfOneOver64'
_AE='rdfOneOver128'
_AD='rdfOneOver256'
_AC='rdfOneOver512'
_AB='rdfOneOver1024'
_AA='rdfOneOver2048'
_A9='rdfOneOver4096'
_A8='rdfOneOver8192'
_A7='rdfOneOver16384'
_A6='rdfOneOver32768'
_A5='rifOneOver2'
_A4='rifOneOver4'
_A3='rifOneOver8'
_A2='rifOneOver16'
_A1='rifOneOver32'
_A0='rifOneOver64'
_z='rifOneOver128'
_y='rifOneOver256'
_x='rifOneOver512'
_w='rifOneOver1024'
_v='rifOneOver2048'
_u='rifOneOver4096'
_t='rifOneOver8192'
_s='rifOneOver16384'
_r='rifOneOver32768'
_q='cdfOne'
_p='cdfOneOver2'
_o='cdfOneOver4'
_n='cdfOneOver8'
_m='cdfOneOver16'
_l='cdfOneOver32'
_k='cdfOneOver64'
_j='trm100'
_i='trm12point5'
_h='trm6point25'
_g='trm3point125'
_f='trm1point5625'
_e='trm0point78125'
_d='nrm256'
_c='nrm128'
_b='atmfVpcAbrVpi'
_a='atmfVpcAbrPortIndex'
_Z='atmfVccVci'
_Y='atmfVccVpi'
_X='atmfVccPortIndex'
_W='unspecified'
_V='statistical'
_U='deterministic'
_T='localDown'
_S='localUpEnd2endUnknown'
_R='end2endDown'
_Q='end2endUp'
_P='unknown'
_O='atmfVpcVpi'
_N='atmfVpcPortIndex'
_M='atmfAtmStatsIndex'
_L='version4point0'
_K='atmfAtmLayerIndex'
_J='atmfPortIndex'
_I='OctetString'
_H='unsupported'
_G='other'
_F='obsolete'
_E='deprecated'
_D='ATM-FORUM-MIB'
_C='Integer32'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmServiceCategory,ClnpAddress,TruthValue,atmfAtmLayerGroup,atmfAtmStatsGroup,atmfPhysicalGroup,atmfVccAbrGroup,atmfVccGroup,atmfVpcAbrGroup,atmfVpcGroup=mibBuilder.importSymbols('ATM-FORUM-TC-MIB','AtmServiceCategory','ClnpAddress','TruthValue','atmfAtmLayerGroup','atmfAtmStatsGroup','atmfPhysicalGroup','atmfVccAbrGroup','atmfVccGroup','atmfVpcAbrGroup','atmfVpcGroup')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class AtmAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AtmfPortTable_Object=MibTable
atmfPortTable=_AtmfPortTable_Object((1,3,6,1,4,1,353,2,1,1))
if mibBuilder.loadTexts:atmfPortTable.setStatus(_B)
_AtmfPortEntry_Object=MibTableRow
atmfPortEntry=_AtmfPortEntry_Object((1,3,6,1,4,1,353,2,1,1,1))
atmfPortEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:atmfPortEntry.setStatus(_B)
class _AtmfPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfPortIndex_Type.__name__=_C
_AtmfPortIndex_Object=MibTableColumn
atmfPortIndex=_AtmfPortIndex_Object((1,3,6,1,4,1,353,2,1,1,1,1),_AtmfPortIndex_Type())
atmfPortIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfPortIndex.setStatus(_B)
_AtmfPortAddress_Type=AtmAddress
_AtmfPortAddress_Object=MibTableColumn
atmfPortAddress=_AtmfPortAddress_Object((1,3,6,1,4,1,353,2,1,1,1,2),_AtmfPortAddress_Type())
atmfPortAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfPortAddress.setStatus(_F)
_AtmfPortTransmissionType_Type=ObjectIdentifier
_AtmfPortTransmissionType_Object=MibTableColumn
atmfPortTransmissionType=_AtmfPortTransmissionType_Object((1,3,6,1,4,1,353,2,1,1,1,3),_AtmfPortTransmissionType_Type())
atmfPortTransmissionType.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfPortTransmissionType.setStatus(_E)
_AtmfPortMediaType_Type=ObjectIdentifier
_AtmfPortMediaType_Object=MibTableColumn
atmfPortMediaType=_AtmfPortMediaType_Object((1,3,6,1,4,1,353,2,1,1,1,4),_AtmfPortMediaType_Type())
atmfPortMediaType.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfPortMediaType.setStatus(_E)
class _AtmfPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('inService',2),('outOfService',3),('loopBack',4)))
_AtmfPortOperStatus_Type.__name__=_C
_AtmfPortOperStatus_Object=MibTableColumn
atmfPortOperStatus=_AtmfPortOperStatus_Object((1,3,6,1,4,1,353,2,1,1,1,5),_AtmfPortOperStatus_Type())
atmfPortOperStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfPortOperStatus.setStatus(_E)
_AtmfPortSpecific_Type=ObjectIdentifier
_AtmfPortSpecific_Object=MibTableColumn
atmfPortSpecific=_AtmfPortSpecific_Object((1,3,6,1,4,1,353,2,1,1,1,6),_AtmfPortSpecific_Type())
atmfPortSpecific.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfPortSpecific.setStatus(_E)
_AtmfPortMyIfName_Type=DisplayString
_AtmfPortMyIfName_Object=MibTableColumn
atmfPortMyIfName=_AtmfPortMyIfName_Object((1,3,6,1,4,1,353,2,1,1,1,7),_AtmfPortMyIfName_Type())
atmfPortMyIfName.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfPortMyIfName.setStatus(_B)
class _AtmfPortMyIfIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfPortMyIfIdentifier_Type.__name__=_C
_AtmfPortMyIfIdentifier_Object=MibTableColumn
atmfPortMyIfIdentifier=_AtmfPortMyIfIdentifier_Object((1,3,6,1,4,1,353,2,1,1,1,8),_AtmfPortMyIfIdentifier_Type())
atmfPortMyIfIdentifier.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfPortMyIfIdentifier.setStatus(_B)
_AtmfMyIpNmAddress_Type=IpAddress
_AtmfMyIpNmAddress_Object=MibScalar
atmfMyIpNmAddress=_AtmfMyIpNmAddress_Object((1,3,6,1,4,1,353,2,1,2),_AtmfMyIpNmAddress_Type())
atmfMyIpNmAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfMyIpNmAddress.setStatus(_B)
_AtmfMyOsiNmNsapAddress_Type=ClnpAddress
_AtmfMyOsiNmNsapAddress_Object=MibScalar
atmfMyOsiNmNsapAddress=_AtmfMyOsiNmNsapAddress_Object((1,3,6,1,4,1,353,2,1,3),_AtmfMyOsiNmNsapAddress_Type())
atmfMyOsiNmNsapAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfMyOsiNmNsapAddress.setStatus(_B)
class _AtmfMySystemIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AtmfMySystemIdentifier_Type.__name__=_I
_AtmfMySystemIdentifier_Object=MibScalar
atmfMySystemIdentifier=_AtmfMySystemIdentifier_Object((1,3,6,1,4,1,353,2,1,4),_AtmfMySystemIdentifier_Type())
atmfMySystemIdentifier.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfMySystemIdentifier.setStatus(_B)
_AtmfAtmLayerTable_Object=MibTable
atmfAtmLayerTable=_AtmfAtmLayerTable_Object((1,3,6,1,4,1,353,2,2,1))
if mibBuilder.loadTexts:atmfAtmLayerTable.setStatus(_B)
_AtmfAtmLayerEntry_Object=MibTableRow
atmfAtmLayerEntry=_AtmfAtmLayerEntry_Object((1,3,6,1,4,1,353,2,2,1,1))
atmfAtmLayerEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:atmfAtmLayerEntry.setStatus(_B)
class _AtmfAtmLayerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfAtmLayerIndex_Type.__name__=_C
_AtmfAtmLayerIndex_Object=MibTableColumn
atmfAtmLayerIndex=_AtmfAtmLayerIndex_Object((1,3,6,1,4,1,353,2,2,1,1,1),_AtmfAtmLayerIndex_Type())
atmfAtmLayerIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerIndex.setStatus(_B)
class _AtmfAtmLayerMaxVPCs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_AtmfAtmLayerMaxVPCs_Type.__name__=_C
_AtmfAtmLayerMaxVPCs_Object=MibTableColumn
atmfAtmLayerMaxVPCs=_AtmfAtmLayerMaxVPCs_Object((1,3,6,1,4,1,353,2,2,1,1,2),_AtmfAtmLayerMaxVPCs_Type())
atmfAtmLayerMaxVPCs.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerMaxVPCs.setStatus(_B)
class _AtmfAtmLayerMaxVCCs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,268435456))
_AtmfAtmLayerMaxVCCs_Type.__name__=_C
_AtmfAtmLayerMaxVCCs_Object=MibTableColumn
atmfAtmLayerMaxVCCs=_AtmfAtmLayerMaxVCCs_Object((1,3,6,1,4,1,353,2,2,1,1,3),_AtmfAtmLayerMaxVCCs_Type())
atmfAtmLayerMaxVCCs.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerMaxVCCs.setStatus(_B)
class _AtmfAtmLayerConfiguredVPCs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_AtmfAtmLayerConfiguredVPCs_Type.__name__=_C
_AtmfAtmLayerConfiguredVPCs_Object=MibTableColumn
atmfAtmLayerConfiguredVPCs=_AtmfAtmLayerConfiguredVPCs_Object((1,3,6,1,4,1,353,2,2,1,1,4),_AtmfAtmLayerConfiguredVPCs_Type())
atmfAtmLayerConfiguredVPCs.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerConfiguredVPCs.setStatus(_B)
class _AtmfAtmLayerConfiguredVCCs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,268435456))
_AtmfAtmLayerConfiguredVCCs_Type.__name__=_C
_AtmfAtmLayerConfiguredVCCs_Object=MibTableColumn
atmfAtmLayerConfiguredVCCs=_AtmfAtmLayerConfiguredVCCs_Object((1,3,6,1,4,1,353,2,2,1,1,5),_AtmfAtmLayerConfiguredVCCs_Type())
atmfAtmLayerConfiguredVCCs.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerConfiguredVCCs.setStatus(_B)
class _AtmfAtmLayerMaxVpiBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_AtmfAtmLayerMaxVpiBits_Type.__name__=_C
_AtmfAtmLayerMaxVpiBits_Object=MibTableColumn
atmfAtmLayerMaxVpiBits=_AtmfAtmLayerMaxVpiBits_Object((1,3,6,1,4,1,353,2,2,1,1,6),_AtmfAtmLayerMaxVpiBits_Type())
atmfAtmLayerMaxVpiBits.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerMaxVpiBits.setStatus(_B)
class _AtmfAtmLayerMaxVciBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AtmfAtmLayerMaxVciBits_Type.__name__=_C
_AtmfAtmLayerMaxVciBits_Object=MibTableColumn
atmfAtmLayerMaxVciBits=_AtmfAtmLayerMaxVciBits_Object((1,3,6,1,4,1,353,2,2,1,1,7),_AtmfAtmLayerMaxVciBits_Type())
atmfAtmLayerMaxVciBits.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerMaxVciBits.setStatus(_B)
class _AtmfAtmLayerUniType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('public',1),('private',2)))
_AtmfAtmLayerUniType_Type.__name__=_C
_AtmfAtmLayerUniType_Object=MibTableColumn
atmfAtmLayerUniType=_AtmfAtmLayerUniType_Object((1,3,6,1,4,1,353,2,2,1,1,8),_AtmfAtmLayerUniType_Type())
atmfAtmLayerUniType.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerUniType.setStatus(_B)
class _AtmfAtmLayerUniVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('version2point0',1),('version3point0',2),('version3point1',3),(_L,4),(_H,5)))
_AtmfAtmLayerUniVersion_Type.__name__=_C
_AtmfAtmLayerUniVersion_Object=MibTableColumn
atmfAtmLayerUniVersion=_AtmfAtmLayerUniVersion_Object((1,3,6,1,4,1,353,2,2,1,1,9),_AtmfAtmLayerUniVersion_Type())
atmfAtmLayerUniVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerUniVersion.setStatus(_B)
class _AtmfAtmLayerDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('user',1),('node',2)))
_AtmfAtmLayerDeviceType_Type.__name__=_C
_AtmfAtmLayerDeviceType_Object=MibTableColumn
atmfAtmLayerDeviceType=_AtmfAtmLayerDeviceType_Object((1,3,6,1,4,1,353,2,2,1,1,10),_AtmfAtmLayerDeviceType_Type())
atmfAtmLayerDeviceType.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerDeviceType.setStatus(_B)
class _AtmfAtmLayerIlmiVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_L,2)))
_AtmfAtmLayerIlmiVersion_Type.__name__=_C
_AtmfAtmLayerIlmiVersion_Object=MibTableColumn
atmfAtmLayerIlmiVersion=_AtmfAtmLayerIlmiVersion_Object((1,3,6,1,4,1,353,2,2,1,1,11),_AtmfAtmLayerIlmiVersion_Type())
atmfAtmLayerIlmiVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerIlmiVersion.setStatus(_B)
class _AtmfAtmLayerNniSigVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('iisp',2),('pnniVersion1point0',3)))
_AtmfAtmLayerNniSigVersion_Type.__name__=_C
_AtmfAtmLayerNniSigVersion_Object=MibTableColumn
atmfAtmLayerNniSigVersion=_AtmfAtmLayerNniSigVersion_Object((1,3,6,1,4,1,353,2,2,1,1,12),_AtmfAtmLayerNniSigVersion_Type())
atmfAtmLayerNniSigVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerNniSigVersion.setStatus(_B)
class _AtmfAtmLayerMaxSvpcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_AtmfAtmLayerMaxSvpcVpi_Type.__name__=_C
_AtmfAtmLayerMaxSvpcVpi_Object=MibTableColumn
atmfAtmLayerMaxSvpcVpi=_AtmfAtmLayerMaxSvpcVpi_Object((1,3,6,1,4,1,353,2,2,1,1,13),_AtmfAtmLayerMaxSvpcVpi_Type())
atmfAtmLayerMaxSvpcVpi.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerMaxSvpcVpi.setStatus(_B)
class _AtmfAtmLayerMaxSvccVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_AtmfAtmLayerMaxSvccVpi_Type.__name__=_C
_AtmfAtmLayerMaxSvccVpi_Object=MibTableColumn
atmfAtmLayerMaxSvccVpi=_AtmfAtmLayerMaxSvccVpi_Object((1,3,6,1,4,1,353,2,2,1,1,14),_AtmfAtmLayerMaxSvccVpi_Type())
atmfAtmLayerMaxSvccVpi.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerMaxSvccVpi.setStatus(_B)
class _AtmfAtmLayerMinSvccVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_AtmfAtmLayerMinSvccVci_Type.__name__=_C
_AtmfAtmLayerMinSvccVci_Object=MibTableColumn
atmfAtmLayerMinSvccVci=_AtmfAtmLayerMinSvccVci_Object((1,3,6,1,4,1,353,2,2,1,1,15),_AtmfAtmLayerMinSvccVci_Type())
atmfAtmLayerMinSvccVci.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmLayerMinSvccVci.setStatus(_B)
_AtmfAtmStatsTable_Object=MibTable
atmfAtmStatsTable=_AtmfAtmStatsTable_Object((1,3,6,1,4,1,353,2,3,1))
if mibBuilder.loadTexts:atmfAtmStatsTable.setStatus(_E)
_AtmfAtmStatsEntry_Object=MibTableRow
atmfAtmStatsEntry=_AtmfAtmStatsEntry_Object((1,3,6,1,4,1,353,2,3,1,1))
atmfAtmStatsEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:atmfAtmStatsEntry.setStatus(_E)
class _AtmfAtmStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfAtmStatsIndex_Type.__name__=_C
_AtmfAtmStatsIndex_Object=MibTableColumn
atmfAtmStatsIndex=_AtmfAtmStatsIndex_Object((1,3,6,1,4,1,353,2,3,1,1,1),_AtmfAtmStatsIndex_Type())
atmfAtmStatsIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmStatsIndex.setStatus(_E)
_AtmfAtmStatsReceivedCells_Type=Counter32
_AtmfAtmStatsReceivedCells_Object=MibTableColumn
atmfAtmStatsReceivedCells=_AtmfAtmStatsReceivedCells_Object((1,3,6,1,4,1,353,2,3,1,1,2),_AtmfAtmStatsReceivedCells_Type())
atmfAtmStatsReceivedCells.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmStatsReceivedCells.setStatus(_E)
_AtmfAtmStatsDroppedReceivedCells_Type=Counter32
_AtmfAtmStatsDroppedReceivedCells_Object=MibTableColumn
atmfAtmStatsDroppedReceivedCells=_AtmfAtmStatsDroppedReceivedCells_Object((1,3,6,1,4,1,353,2,3,1,1,3),_AtmfAtmStatsDroppedReceivedCells_Type())
atmfAtmStatsDroppedReceivedCells.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmStatsDroppedReceivedCells.setStatus(_E)
_AtmfAtmStatsTransmittedCells_Type=Counter32
_AtmfAtmStatsTransmittedCells_Object=MibTableColumn
atmfAtmStatsTransmittedCells=_AtmfAtmStatsTransmittedCells_Object((1,3,6,1,4,1,353,2,3,1,1,4),_AtmfAtmStatsTransmittedCells_Type())
atmfAtmStatsTransmittedCells.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfAtmStatsTransmittedCells.setStatus(_E)
_AtmfVpcTable_Object=MibTable
atmfVpcTable=_AtmfVpcTable_Object((1,3,6,1,4,1,353,2,4,1))
if mibBuilder.loadTexts:atmfVpcTable.setStatus(_B)
_AtmfVpcEntry_Object=MibTableRow
atmfVpcEntry=_AtmfVpcEntry_Object((1,3,6,1,4,1,353,2,4,1,1))
atmfVpcEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:atmfVpcEntry.setStatus(_B)
class _AtmfVpcPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcPortIndex_Type.__name__=_C
_AtmfVpcPortIndex_Object=MibTableColumn
atmfVpcPortIndex=_AtmfVpcPortIndex_Object((1,3,6,1,4,1,353,2,4,1,1,1),_AtmfVpcPortIndex_Type())
atmfVpcPortIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcPortIndex.setStatus(_B)
class _AtmfVpcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AtmfVpcVpi_Type.__name__=_C
_AtmfVpcVpi_Object=MibTableColumn
atmfVpcVpi=_AtmfVpcVpi_Object((1,3,6,1,4,1,353,2,4,1,1,2),_AtmfVpcVpi_Type())
atmfVpcVpi.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcVpi.setStatus(_B)
class _AtmfVpcOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5)))
_AtmfVpcOperStatus_Type.__name__=_C
_AtmfVpcOperStatus_Object=MibTableColumn
atmfVpcOperStatus=_AtmfVpcOperStatus_Object((1,3,6,1,4,1,353,2,4,1,1,3),_AtmfVpcOperStatus_Type())
atmfVpcOperStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcOperStatus.setStatus(_B)
_AtmfVpcTransmitTrafficDescriptorType_Type=ObjectIdentifier
_AtmfVpcTransmitTrafficDescriptorType_Object=MibTableColumn
atmfVpcTransmitTrafficDescriptorType=_AtmfVpcTransmitTrafficDescriptorType_Object((1,3,6,1,4,1,353,2,4,1,1,4),_AtmfVpcTransmitTrafficDescriptorType_Type())
atmfVpcTransmitTrafficDescriptorType.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcTransmitTrafficDescriptorType.setStatus(_B)
class _AtmfVpcTransmitTrafficDescriptorParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcTransmitTrafficDescriptorParam1_Type.__name__=_C
_AtmfVpcTransmitTrafficDescriptorParam1_Object=MibTableColumn
atmfVpcTransmitTrafficDescriptorParam1=_AtmfVpcTransmitTrafficDescriptorParam1_Object((1,3,6,1,4,1,353,2,4,1,1,5),_AtmfVpcTransmitTrafficDescriptorParam1_Type())
atmfVpcTransmitTrafficDescriptorParam1.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcTransmitTrafficDescriptorParam1.setStatus(_B)
class _AtmfVpcTransmitTrafficDescriptorParam2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcTransmitTrafficDescriptorParam2_Type.__name__=_C
_AtmfVpcTransmitTrafficDescriptorParam2_Object=MibTableColumn
atmfVpcTransmitTrafficDescriptorParam2=_AtmfVpcTransmitTrafficDescriptorParam2_Object((1,3,6,1,4,1,353,2,4,1,1,6),_AtmfVpcTransmitTrafficDescriptorParam2_Type())
atmfVpcTransmitTrafficDescriptorParam2.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcTransmitTrafficDescriptorParam2.setStatus(_B)
class _AtmfVpcTransmitTrafficDescriptorParam3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcTransmitTrafficDescriptorParam3_Type.__name__=_C
_AtmfVpcTransmitTrafficDescriptorParam3_Object=MibTableColumn
atmfVpcTransmitTrafficDescriptorParam3=_AtmfVpcTransmitTrafficDescriptorParam3_Object((1,3,6,1,4,1,353,2,4,1,1,7),_AtmfVpcTransmitTrafficDescriptorParam3_Type())
atmfVpcTransmitTrafficDescriptorParam3.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcTransmitTrafficDescriptorParam3.setStatus(_B)
class _AtmfVpcTransmitTrafficDescriptorParam4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcTransmitTrafficDescriptorParam4_Type.__name__=_C
_AtmfVpcTransmitTrafficDescriptorParam4_Object=MibTableColumn
atmfVpcTransmitTrafficDescriptorParam4=_AtmfVpcTransmitTrafficDescriptorParam4_Object((1,3,6,1,4,1,353,2,4,1,1,8),_AtmfVpcTransmitTrafficDescriptorParam4_Type())
atmfVpcTransmitTrafficDescriptorParam4.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcTransmitTrafficDescriptorParam4.setStatus(_B)
class _AtmfVpcTransmitTrafficDescriptorParam5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcTransmitTrafficDescriptorParam5_Type.__name__=_C
_AtmfVpcTransmitTrafficDescriptorParam5_Object=MibTableColumn
atmfVpcTransmitTrafficDescriptorParam5=_AtmfVpcTransmitTrafficDescriptorParam5_Object((1,3,6,1,4,1,353,2,4,1,1,9),_AtmfVpcTransmitTrafficDescriptorParam5_Type())
atmfVpcTransmitTrafficDescriptorParam5.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcTransmitTrafficDescriptorParam5.setStatus(_B)
_AtmfVpcReceiveTrafficDescriptorType_Type=ObjectIdentifier
_AtmfVpcReceiveTrafficDescriptorType_Object=MibTableColumn
atmfVpcReceiveTrafficDescriptorType=_AtmfVpcReceiveTrafficDescriptorType_Object((1,3,6,1,4,1,353,2,4,1,1,10),_AtmfVpcReceiveTrafficDescriptorType_Type())
atmfVpcReceiveTrafficDescriptorType.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcReceiveTrafficDescriptorType.setStatus(_B)
class _AtmfVpcReceiveTrafficDescriptorParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcReceiveTrafficDescriptorParam1_Type.__name__=_C
_AtmfVpcReceiveTrafficDescriptorParam1_Object=MibTableColumn
atmfVpcReceiveTrafficDescriptorParam1=_AtmfVpcReceiveTrafficDescriptorParam1_Object((1,3,6,1,4,1,353,2,4,1,1,11),_AtmfVpcReceiveTrafficDescriptorParam1_Type())
atmfVpcReceiveTrafficDescriptorParam1.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcReceiveTrafficDescriptorParam1.setStatus(_B)
class _AtmfVpcReceiveTrafficDescriptorParam2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcReceiveTrafficDescriptorParam2_Type.__name__=_C
_AtmfVpcReceiveTrafficDescriptorParam2_Object=MibTableColumn
atmfVpcReceiveTrafficDescriptorParam2=_AtmfVpcReceiveTrafficDescriptorParam2_Object((1,3,6,1,4,1,353,2,4,1,1,12),_AtmfVpcReceiveTrafficDescriptorParam2_Type())
atmfVpcReceiveTrafficDescriptorParam2.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcReceiveTrafficDescriptorParam2.setStatus(_B)
class _AtmfVpcReceiveTrafficDescriptorParam3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcReceiveTrafficDescriptorParam3_Type.__name__=_C
_AtmfVpcReceiveTrafficDescriptorParam3_Object=MibTableColumn
atmfVpcReceiveTrafficDescriptorParam3=_AtmfVpcReceiveTrafficDescriptorParam3_Object((1,3,6,1,4,1,353,2,4,1,1,13),_AtmfVpcReceiveTrafficDescriptorParam3_Type())
atmfVpcReceiveTrafficDescriptorParam3.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcReceiveTrafficDescriptorParam3.setStatus(_B)
class _AtmfVpcReceiveTrafficDescriptorParam4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcReceiveTrafficDescriptorParam4_Type.__name__=_C
_AtmfVpcReceiveTrafficDescriptorParam4_Object=MibTableColumn
atmfVpcReceiveTrafficDescriptorParam4=_AtmfVpcReceiveTrafficDescriptorParam4_Object((1,3,6,1,4,1,353,2,4,1,1,14),_AtmfVpcReceiveTrafficDescriptorParam4_Type())
atmfVpcReceiveTrafficDescriptorParam4.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcReceiveTrafficDescriptorParam4.setStatus(_B)
class _AtmfVpcReceiveTrafficDescriptorParam5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcReceiveTrafficDescriptorParam5_Type.__name__=_C
_AtmfVpcReceiveTrafficDescriptorParam5_Object=MibTableColumn
atmfVpcReceiveTrafficDescriptorParam5=_AtmfVpcReceiveTrafficDescriptorParam5_Object((1,3,6,1,4,1,353,2,4,1,1,15),_AtmfVpcReceiveTrafficDescriptorParam5_Type())
atmfVpcReceiveTrafficDescriptorParam5.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcReceiveTrafficDescriptorParam5.setStatus(_B)
class _AtmfVpcQoSCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_U,2),(_V,3),(_W,4)))
_AtmfVpcQoSCategory_Type.__name__=_C
_AtmfVpcQoSCategory_Object=MibTableColumn
atmfVpcQoSCategory=_AtmfVpcQoSCategory_Object((1,3,6,1,4,1,353,2,4,1,1,16),_AtmfVpcQoSCategory_Type())
atmfVpcQoSCategory.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcQoSCategory.setStatus(_F)
class _AtmfVpcTransmitQoSClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmfVpcTransmitQoSClass_Type.__name__=_C
_AtmfVpcTransmitQoSClass_Object=MibTableColumn
atmfVpcTransmitQoSClass=_AtmfVpcTransmitQoSClass_Object((1,3,6,1,4,1,353,2,4,1,1,17),_AtmfVpcTransmitQoSClass_Type())
atmfVpcTransmitQoSClass.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcTransmitQoSClass.setStatus(_E)
class _AtmfVpcReceiveQoSClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmfVpcReceiveQoSClass_Type.__name__=_C
_AtmfVpcReceiveQoSClass_Object=MibTableColumn
atmfVpcReceiveQoSClass=_AtmfVpcReceiveQoSClass_Object((1,3,6,1,4,1,353,2,4,1,1,18),_AtmfVpcReceiveQoSClass_Type())
atmfVpcReceiveQoSClass.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcReceiveQoSClass.setStatus(_E)
_AtmfVpcBestEffortIndicator_Type=TruthValue
_AtmfVpcBestEffortIndicator_Object=MibTableColumn
atmfVpcBestEffortIndicator=_AtmfVpcBestEffortIndicator_Object((1,3,6,1,4,1,353,2,4,1,1,19),_AtmfVpcBestEffortIndicator_Type())
atmfVpcBestEffortIndicator.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcBestEffortIndicator.setStatus(_B)
_AtmfVpcServiceCategory_Type=AtmServiceCategory
_AtmfVpcServiceCategory_Object=MibTableColumn
atmfVpcServiceCategory=_AtmfVpcServiceCategory_Object((1,3,6,1,4,1,353,2,4,1,1,20),_AtmfVpcServiceCategory_Type())
atmfVpcServiceCategory.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcServiceCategory.setStatus(_B)
_AtmfVccTable_Object=MibTable
atmfVccTable=_AtmfVccTable_Object((1,3,6,1,4,1,353,2,5,1))
if mibBuilder.loadTexts:atmfVccTable.setStatus(_B)
_AtmfVccEntry_Object=MibTableRow
atmfVccEntry=_AtmfVccEntry_Object((1,3,6,1,4,1,353,2,5,1,1))
atmfVccEntry.setIndexNames((0,_D,_X),(0,_D,_Y),(0,_D,_Z))
if mibBuilder.loadTexts:atmfVccEntry.setStatus(_B)
class _AtmfVccPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccPortIndex_Type.__name__=_C
_AtmfVccPortIndex_Object=MibTableColumn
atmfVccPortIndex=_AtmfVccPortIndex_Object((1,3,6,1,4,1,353,2,5,1,1,1),_AtmfVccPortIndex_Type())
atmfVccPortIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccPortIndex.setStatus(_B)
class _AtmfVccVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AtmfVccVpi_Type.__name__=_C
_AtmfVccVpi_Object=MibTableColumn
atmfVccVpi=_AtmfVccVpi_Object((1,3,6,1,4,1,353,2,5,1,1,2),_AtmfVccVpi_Type())
atmfVccVpi.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccVpi.setStatus(_B)
class _AtmfVccVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmfVccVci_Type.__name__=_C
_AtmfVccVci_Object=MibTableColumn
atmfVccVci=_AtmfVccVci_Object((1,3,6,1,4,1,353,2,5,1,1,3),_AtmfVccVci_Type())
atmfVccVci.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccVci.setStatus(_B)
class _AtmfVccOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5)))
_AtmfVccOperStatus_Type.__name__=_C
_AtmfVccOperStatus_Object=MibTableColumn
atmfVccOperStatus=_AtmfVccOperStatus_Object((1,3,6,1,4,1,353,2,5,1,1,4),_AtmfVccOperStatus_Type())
atmfVccOperStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccOperStatus.setStatus(_B)
_AtmfVccTransmitTrafficDescriptorType_Type=ObjectIdentifier
_AtmfVccTransmitTrafficDescriptorType_Object=MibTableColumn
atmfVccTransmitTrafficDescriptorType=_AtmfVccTransmitTrafficDescriptorType_Object((1,3,6,1,4,1,353,2,5,1,1,5),_AtmfVccTransmitTrafficDescriptorType_Type())
atmfVccTransmitTrafficDescriptorType.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccTransmitTrafficDescriptorType.setStatus(_B)
class _AtmfVccTransmitTrafficDescriptorParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccTransmitTrafficDescriptorParam1_Type.__name__=_C
_AtmfVccTransmitTrafficDescriptorParam1_Object=MibTableColumn
atmfVccTransmitTrafficDescriptorParam1=_AtmfVccTransmitTrafficDescriptorParam1_Object((1,3,6,1,4,1,353,2,5,1,1,6),_AtmfVccTransmitTrafficDescriptorParam1_Type())
atmfVccTransmitTrafficDescriptorParam1.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccTransmitTrafficDescriptorParam1.setStatus(_B)
class _AtmfVccTransmitTrafficDescriptorParam2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccTransmitTrafficDescriptorParam2_Type.__name__=_C
_AtmfVccTransmitTrafficDescriptorParam2_Object=MibTableColumn
atmfVccTransmitTrafficDescriptorParam2=_AtmfVccTransmitTrafficDescriptorParam2_Object((1,3,6,1,4,1,353,2,5,1,1,7),_AtmfVccTransmitTrafficDescriptorParam2_Type())
atmfVccTransmitTrafficDescriptorParam2.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccTransmitTrafficDescriptorParam2.setStatus(_B)
class _AtmfVccTransmitTrafficDescriptorParam3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccTransmitTrafficDescriptorParam3_Type.__name__=_C
_AtmfVccTransmitTrafficDescriptorParam3_Object=MibTableColumn
atmfVccTransmitTrafficDescriptorParam3=_AtmfVccTransmitTrafficDescriptorParam3_Object((1,3,6,1,4,1,353,2,5,1,1,8),_AtmfVccTransmitTrafficDescriptorParam3_Type())
atmfVccTransmitTrafficDescriptorParam3.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccTransmitTrafficDescriptorParam3.setStatus(_B)
class _AtmfVccTransmitTrafficDescriptorParam4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccTransmitTrafficDescriptorParam4_Type.__name__=_C
_AtmfVccTransmitTrafficDescriptorParam4_Object=MibTableColumn
atmfVccTransmitTrafficDescriptorParam4=_AtmfVccTransmitTrafficDescriptorParam4_Object((1,3,6,1,4,1,353,2,5,1,1,9),_AtmfVccTransmitTrafficDescriptorParam4_Type())
atmfVccTransmitTrafficDescriptorParam4.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccTransmitTrafficDescriptorParam4.setStatus(_B)
class _AtmfVccTransmitTrafficDescriptorParam5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccTransmitTrafficDescriptorParam5_Type.__name__=_C
_AtmfVccTransmitTrafficDescriptorParam5_Object=MibTableColumn
atmfVccTransmitTrafficDescriptorParam5=_AtmfVccTransmitTrafficDescriptorParam5_Object((1,3,6,1,4,1,353,2,5,1,1,10),_AtmfVccTransmitTrafficDescriptorParam5_Type())
atmfVccTransmitTrafficDescriptorParam5.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccTransmitTrafficDescriptorParam5.setStatus(_B)
_AtmfVccReceiveTrafficDescriptorType_Type=ObjectIdentifier
_AtmfVccReceiveTrafficDescriptorType_Object=MibTableColumn
atmfVccReceiveTrafficDescriptorType=_AtmfVccReceiveTrafficDescriptorType_Object((1,3,6,1,4,1,353,2,5,1,1,11),_AtmfVccReceiveTrafficDescriptorType_Type())
atmfVccReceiveTrafficDescriptorType.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccReceiveTrafficDescriptorType.setStatus(_B)
class _AtmfVccReceiveTrafficDescriptorParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccReceiveTrafficDescriptorParam1_Type.__name__=_C
_AtmfVccReceiveTrafficDescriptorParam1_Object=MibTableColumn
atmfVccReceiveTrafficDescriptorParam1=_AtmfVccReceiveTrafficDescriptorParam1_Object((1,3,6,1,4,1,353,2,5,1,1,12),_AtmfVccReceiveTrafficDescriptorParam1_Type())
atmfVccReceiveTrafficDescriptorParam1.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccReceiveTrafficDescriptorParam1.setStatus(_B)
class _AtmfVccReceiveTrafficDescriptorParam2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccReceiveTrafficDescriptorParam2_Type.__name__=_C
_AtmfVccReceiveTrafficDescriptorParam2_Object=MibTableColumn
atmfVccReceiveTrafficDescriptorParam2=_AtmfVccReceiveTrafficDescriptorParam2_Object((1,3,6,1,4,1,353,2,5,1,1,13),_AtmfVccReceiveTrafficDescriptorParam2_Type())
atmfVccReceiveTrafficDescriptorParam2.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccReceiveTrafficDescriptorParam2.setStatus(_B)
class _AtmfVccReceiveTrafficDescriptorParam3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccReceiveTrafficDescriptorParam3_Type.__name__=_C
_AtmfVccReceiveTrafficDescriptorParam3_Object=MibTableColumn
atmfVccReceiveTrafficDescriptorParam3=_AtmfVccReceiveTrafficDescriptorParam3_Object((1,3,6,1,4,1,353,2,5,1,1,14),_AtmfVccReceiveTrafficDescriptorParam3_Type())
atmfVccReceiveTrafficDescriptorParam3.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccReceiveTrafficDescriptorParam3.setStatus(_B)
class _AtmfVccReceiveTrafficDescriptorParam4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccReceiveTrafficDescriptorParam4_Type.__name__=_C
_AtmfVccReceiveTrafficDescriptorParam4_Object=MibTableColumn
atmfVccReceiveTrafficDescriptorParam4=_AtmfVccReceiveTrafficDescriptorParam4_Object((1,3,6,1,4,1,353,2,5,1,1,15),_AtmfVccReceiveTrafficDescriptorParam4_Type())
atmfVccReceiveTrafficDescriptorParam4.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccReceiveTrafficDescriptorParam4.setStatus(_B)
class _AtmfVccReceiveTrafficDescriptorParam5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccReceiveTrafficDescriptorParam5_Type.__name__=_C
_AtmfVccReceiveTrafficDescriptorParam5_Object=MibTableColumn
atmfVccReceiveTrafficDescriptorParam5=_AtmfVccReceiveTrafficDescriptorParam5_Object((1,3,6,1,4,1,353,2,5,1,1,16),_AtmfVccReceiveTrafficDescriptorParam5_Type())
atmfVccReceiveTrafficDescriptorParam5.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccReceiveTrafficDescriptorParam5.setStatus(_B)
class _AtmfVccQoSCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_U,2),(_V,3),(_W,4)))
_AtmfVccQoSCategory_Type.__name__=_C
_AtmfVccQoSCategory_Object=MibTableColumn
atmfVccQoSCategory=_AtmfVccQoSCategory_Object((1,3,6,1,4,1,353,2,5,1,1,17),_AtmfVccQoSCategory_Type())
atmfVccQoSCategory.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccQoSCategory.setStatus(_F)
class _AtmfVccTransmitQoSClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmfVccTransmitQoSClass_Type.__name__=_C
_AtmfVccTransmitQoSClass_Object=MibTableColumn
atmfVccTransmitQoSClass=_AtmfVccTransmitQoSClass_Object((1,3,6,1,4,1,353,2,5,1,1,18),_AtmfVccTransmitQoSClass_Type())
atmfVccTransmitQoSClass.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccTransmitQoSClass.setStatus(_E)
class _AtmfVccReceiveQoSClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmfVccReceiveQoSClass_Type.__name__=_C
_AtmfVccReceiveQoSClass_Object=MibTableColumn
atmfVccReceiveQoSClass=_AtmfVccReceiveQoSClass_Object((1,3,6,1,4,1,353,2,5,1,1,19),_AtmfVccReceiveQoSClass_Type())
atmfVccReceiveQoSClass.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccReceiveQoSClass.setStatus(_E)
_AtmfVccBestEffortIndicator_Type=TruthValue
_AtmfVccBestEffortIndicator_Object=MibTableColumn
atmfVccBestEffortIndicator=_AtmfVccBestEffortIndicator_Object((1,3,6,1,4,1,353,2,5,1,1,20),_AtmfVccBestEffortIndicator_Type())
atmfVccBestEffortIndicator.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccBestEffortIndicator.setStatus(_B)
_AtmfVccTransmitFrameDiscard_Type=TruthValue
_AtmfVccTransmitFrameDiscard_Object=MibTableColumn
atmfVccTransmitFrameDiscard=_AtmfVccTransmitFrameDiscard_Object((1,3,6,1,4,1,353,2,5,1,1,21),_AtmfVccTransmitFrameDiscard_Type())
atmfVccTransmitFrameDiscard.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccTransmitFrameDiscard.setStatus(_B)
_AtmfVccReceiveFrameDiscard_Type=TruthValue
_AtmfVccReceiveFrameDiscard_Object=MibTableColumn
atmfVccReceiveFrameDiscard=_AtmfVccReceiveFrameDiscard_Object((1,3,6,1,4,1,353,2,5,1,1,22),_AtmfVccReceiveFrameDiscard_Type())
atmfVccReceiveFrameDiscard.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccReceiveFrameDiscard.setStatus(_B)
_AtmfVccServiceCategory_Type=AtmServiceCategory
_AtmfVccServiceCategory_Object=MibTableColumn
atmfVccServiceCategory=_AtmfVccServiceCategory_Object((1,3,6,1,4,1,353,2,5,1,1,23),_AtmfVccServiceCategory_Type())
atmfVccServiceCategory.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccServiceCategory.setStatus(_B)
_AtmfVpcAbrTable_Object=MibTable
atmfVpcAbrTable=_AtmfVpcAbrTable_Object((1,3,6,1,4,1,353,2,9,1))
if mibBuilder.loadTexts:atmfVpcAbrTable.setStatus(_B)
_AtmfVpcAbrEntry_Object=MibTableRow
atmfVpcAbrEntry=_AtmfVpcAbrEntry_Object((1,3,6,1,4,1,353,2,9,1,1))
atmfVpcAbrEntry.setIndexNames((0,_D,_a),(0,_D,_b))
if mibBuilder.loadTexts:atmfVpcAbrEntry.setStatus(_B)
class _AtmfVpcAbrPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVpcAbrPortIndex_Type.__name__=_C
_AtmfVpcAbrPortIndex_Object=MibTableColumn
atmfVpcAbrPortIndex=_AtmfVpcAbrPortIndex_Object((1,3,6,1,4,1,353,2,9,1,1,1),_AtmfVpcAbrPortIndex_Type())
atmfVpcAbrPortIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcAbrPortIndex.setStatus(_B)
class _AtmfVpcAbrVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AtmfVpcAbrVpi_Type.__name__=_C
_AtmfVpcAbrVpi_Object=MibTableColumn
atmfVpcAbrVpi=_AtmfVpcAbrVpi_Object((1,3,6,1,4,1,353,2,9,1,1,2),_AtmfVpcAbrVpi_Type())
atmfVpcAbrVpi.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcAbrVpi.setStatus(_B)
class _AtmfVpcAbrTransmitIcr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AtmfVpcAbrTransmitIcr_Type.__name__=_C
_AtmfVpcAbrTransmitIcr_Object=MibTableColumn
atmfVpcAbrTransmitIcr=_AtmfVpcAbrTransmitIcr_Object((1,3,6,1,4,1,353,2,9,1,1,3),_AtmfVpcAbrTransmitIcr_Type())
atmfVpcAbrTransmitIcr.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcAbrTransmitIcr.setStatus(_B)
class _AtmfVpcAbrTransmitNrm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('nrm2',1),('nrm4',2),('nrm8',3),('nrm16',4),('nrm32',5),('nrm64',6),(_c,7),(_d,8)))
_AtmfVpcAbrTransmitNrm_Type.__name__=_C
_AtmfVpcAbrTransmitNrm_Object=MibTableColumn
atmfVpcAbrTransmitNrm=_AtmfVpcAbrTransmitNrm_Object((1,3,6,1,4,1,353,2,9,1,1,4),_AtmfVpcAbrTransmitNrm_Type())
atmfVpcAbrTransmitNrm.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcAbrTransmitNrm.setStatus(_B)
class _AtmfVpcAbrTransmitTrm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3),(_h,4),(_i,5),('trm25',6),('trm50',7),(_j,8)))
_AtmfVpcAbrTransmitTrm_Type.__name__=_C
_AtmfVpcAbrTransmitTrm_Object=MibTableColumn
atmfVpcAbrTransmitTrm=_AtmfVpcAbrTransmitTrm_Object((1,3,6,1,4,1,353,2,9,1,1,5),_AtmfVpcAbrTransmitTrm_Type())
atmfVpcAbrTransmitTrm.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcAbrTransmitTrm.setStatus(_B)
class _AtmfVpcAbrTransmitCdf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('cdf0',1),(_k,2),(_l,3),(_m,4),(_n,5),(_o,6),(_p,7),(_q,8)))
_AtmfVpcAbrTransmitCdf_Type.__name__=_C
_AtmfVpcAbrTransmitCdf_Object=MibTableColumn
atmfVpcAbrTransmitCdf=_AtmfVpcAbrTransmitCdf_Object((1,3,6,1,4,1,353,2,9,1,1,6),_AtmfVpcAbrTransmitCdf_Type())
atmfVpcAbrTransmitCdf.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcAbrTransmitCdf.setStatus(_B)
class _AtmfVpcAbrTransmitRif_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_r,1),(_s,2),(_t,3),(_u,4),(_v,5),(_w,6),(_x,7),(_y,8),(_z,9),(_A0,10),(_A1,11),(_A2,12),(_A3,13),(_A4,14),(_A5,15),('rifOne',16)))
_AtmfVpcAbrTransmitRif_Type.__name__=_C
_AtmfVpcAbrTransmitRif_Object=MibTableColumn
atmfVpcAbrTransmitRif=_AtmfVpcAbrTransmitRif_Object((1,3,6,1,4,1,353,2,9,1,1,7),_AtmfVpcAbrTransmitRif_Type())
atmfVpcAbrTransmitRif.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcAbrTransmitRif.setStatus(_B)
class _AtmfVpcAbrTransmitRdf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_A6,1),(_A7,2),(_A8,3),(_A9,4),(_AA,5),(_AB,6),(_AC,7),(_AD,8),(_AE,9),(_AF,10),(_AG,11),(_AH,12),(_AI,13),(_AJ,14),(_AK,15),('rdfOne',16)))
_AtmfVpcAbrTransmitRdf_Type.__name__=_C
_AtmfVpcAbrTransmitRdf_Object=MibTableColumn
atmfVpcAbrTransmitRdf=_AtmfVpcAbrTransmitRdf_Object((1,3,6,1,4,1,353,2,9,1,1,8),_AtmfVpcAbrTransmitRdf_Type())
atmfVpcAbrTransmitRdf.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcAbrTransmitRdf.setStatus(_B)
class _AtmfVpcAbrTransmitAdtf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_AtmfVpcAbrTransmitAdtf_Type.__name__=_C
_AtmfVpcAbrTransmitAdtf_Object=MibTableColumn
atmfVpcAbrTransmitAdtf=_AtmfVpcAbrTransmitAdtf_Object((1,3,6,1,4,1,353,2,9,1,1,9),_AtmfVpcAbrTransmitAdtf_Type())
atmfVpcAbrTransmitAdtf.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcAbrTransmitAdtf.setStatus(_B)
class _AtmfVpcAbrTransmitCrm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388608))
_AtmfVpcAbrTransmitCrm_Type.__name__=_C
_AtmfVpcAbrTransmitCrm_Object=MibTableColumn
atmfVpcAbrTransmitCrm=_AtmfVpcAbrTransmitCrm_Object((1,3,6,1,4,1,353,2,9,1,1,10),_AtmfVpcAbrTransmitCrm_Type())
atmfVpcAbrTransmitCrm.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVpcAbrTransmitCrm.setStatus(_B)
_AtmfVccAbrTable_Object=MibTable
atmfVccAbrTable=_AtmfVccAbrTable_Object((1,3,6,1,4,1,353,2,10,1))
if mibBuilder.loadTexts:atmfVccAbrTable.setStatus(_B)
_AtmfVccAbrEntry_Object=MibTableRow
atmfVccAbrEntry=_AtmfVccAbrEntry_Object((1,3,6,1,4,1,353,2,10,1,1))
atmfVccAbrEntry.setIndexNames((0,_D,_AL),(0,_D,_AM),(0,_D,_AN))
if mibBuilder.loadTexts:atmfVccAbrEntry.setStatus(_B)
class _AtmfVccAbrPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmfVccAbrPortIndex_Type.__name__=_C
_AtmfVccAbrPortIndex_Object=MibTableColumn
atmfVccAbrPortIndex=_AtmfVccAbrPortIndex_Object((1,3,6,1,4,1,353,2,10,1,1,1),_AtmfVccAbrPortIndex_Type())
atmfVccAbrPortIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccAbrPortIndex.setStatus(_B)
class _AtmfVccAbrVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AtmfVccAbrVpi_Type.__name__=_C
_AtmfVccAbrVpi_Object=MibTableColumn
atmfVccAbrVpi=_AtmfVccAbrVpi_Object((1,3,6,1,4,1,353,2,10,1,1,2),_AtmfVccAbrVpi_Type())
atmfVccAbrVpi.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccAbrVpi.setStatus(_B)
class _AtmfVccAbrVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmfVccAbrVci_Type.__name__=_C
_AtmfVccAbrVci_Object=MibTableColumn
atmfVccAbrVci=_AtmfVccAbrVci_Object((1,3,6,1,4,1,353,2,10,1,1,3),_AtmfVccAbrVci_Type())
atmfVccAbrVci.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccAbrVci.setStatus(_B)
class _AtmfVccAbrTransmitIcr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AtmfVccAbrTransmitIcr_Type.__name__=_C
_AtmfVccAbrTransmitIcr_Object=MibTableColumn
atmfVccAbrTransmitIcr=_AtmfVccAbrTransmitIcr_Object((1,3,6,1,4,1,353,2,10,1,1,4),_AtmfVccAbrTransmitIcr_Type())
atmfVccAbrTransmitIcr.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccAbrTransmitIcr.setStatus(_B)
class _AtmfVccAbrTransmitNrm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('nrm2',1),('nrm4',2),('nrm8',3),('nrm16',4),('nrm32',5),('nrm64',6),(_c,7),(_d,8)))
_AtmfVccAbrTransmitNrm_Type.__name__=_C
_AtmfVccAbrTransmitNrm_Object=MibTableColumn
atmfVccAbrTransmitNrm=_AtmfVccAbrTransmitNrm_Object((1,3,6,1,4,1,353,2,10,1,1,5),_AtmfVccAbrTransmitNrm_Type())
atmfVccAbrTransmitNrm.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccAbrTransmitNrm.setStatus(_B)
class _AtmfVccAbrTransmitTrm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3),(_h,4),(_i,5),('trm25',6),('trm50',7),(_j,8)))
_AtmfVccAbrTransmitTrm_Type.__name__=_C
_AtmfVccAbrTransmitTrm_Object=MibTableColumn
atmfVccAbrTransmitTrm=_AtmfVccAbrTransmitTrm_Object((1,3,6,1,4,1,353,2,10,1,1,6),_AtmfVccAbrTransmitTrm_Type())
atmfVccAbrTransmitTrm.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccAbrTransmitTrm.setStatus(_B)
class _AtmfVccAbrTransmitCdf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('cdf0',1),(_k,2),(_l,3),(_m,4),(_n,5),(_o,6),(_p,7),(_q,8)))
_AtmfVccAbrTransmitCdf_Type.__name__=_C
_AtmfVccAbrTransmitCdf_Object=MibTableColumn
atmfVccAbrTransmitCdf=_AtmfVccAbrTransmitCdf_Object((1,3,6,1,4,1,353,2,10,1,1,7),_AtmfVccAbrTransmitCdf_Type())
atmfVccAbrTransmitCdf.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccAbrTransmitCdf.setStatus(_B)
class _AtmfVccAbrTransmitRif_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_r,1),(_s,2),(_t,3),(_u,4),(_v,5),(_w,6),(_x,7),(_y,8),(_z,9),(_A0,10),(_A1,11),(_A2,12),(_A3,13),(_A4,14),(_A5,15),('rifOne',16)))
_AtmfVccAbrTransmitRif_Type.__name__=_C
_AtmfVccAbrTransmitRif_Object=MibTableColumn
atmfVccAbrTransmitRif=_AtmfVccAbrTransmitRif_Object((1,3,6,1,4,1,353,2,10,1,1,8),_AtmfVccAbrTransmitRif_Type())
atmfVccAbrTransmitRif.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccAbrTransmitRif.setStatus(_B)
class _AtmfVccAbrTransmitRdf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_A6,1),(_A7,2),(_A8,3),(_A9,4),(_AA,5),(_AB,6),(_AC,7),(_AD,8),(_AE,9),(_AF,10),(_AG,11),(_AH,12),(_AI,13),(_AJ,14),(_AK,15),('rdfOne',16)))
_AtmfVccAbrTransmitRdf_Type.__name__=_C
_AtmfVccAbrTransmitRdf_Object=MibTableColumn
atmfVccAbrTransmitRdf=_AtmfVccAbrTransmitRdf_Object((1,3,6,1,4,1,353,2,10,1,1,9),_AtmfVccAbrTransmitRdf_Type())
atmfVccAbrTransmitRdf.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccAbrTransmitRdf.setStatus(_B)
class _AtmfVccAbrTransmitAdtf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_AtmfVccAbrTransmitAdtf_Type.__name__=_C
_AtmfVccAbrTransmitAdtf_Object=MibTableColumn
atmfVccAbrTransmitAdtf=_AtmfVccAbrTransmitAdtf_Object((1,3,6,1,4,1,353,2,10,1,1,10),_AtmfVccAbrTransmitAdtf_Type())
atmfVccAbrTransmitAdtf.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccAbrTransmitAdtf.setStatus(_B)
class _AtmfVccAbrTransmitCrm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388608))
_AtmfVccAbrTransmitCrm_Type.__name__=_C
_AtmfVccAbrTransmitCrm_Object=MibTableColumn
atmfVccAbrTransmitCrm=_AtmfVccAbrTransmitCrm_Object((1,3,6,1,4,1,353,2,10,1,1,11),_AtmfVccAbrTransmitCrm_Type())
atmfVccAbrTransmitCrm.setMaxAccess(_A)
if mibBuilder.loadTexts:atmfVccAbrTransmitCrm.setStatus(_B)
mibBuilder.exportSymbols(_D,**{'AtmAddress':AtmAddress,'atmfPortTable':atmfPortTable,'atmfPortEntry':atmfPortEntry,_J:atmfPortIndex,'atmfPortAddress':atmfPortAddress,'atmfPortTransmissionType':atmfPortTransmissionType,'atmfPortMediaType':atmfPortMediaType,'atmfPortOperStatus':atmfPortOperStatus,'atmfPortSpecific':atmfPortSpecific,'atmfPortMyIfName':atmfPortMyIfName,'atmfPortMyIfIdentifier':atmfPortMyIfIdentifier,'atmfMyIpNmAddress':atmfMyIpNmAddress,'atmfMyOsiNmNsapAddress':atmfMyOsiNmNsapAddress,'atmfMySystemIdentifier':atmfMySystemIdentifier,'atmfAtmLayerTable':atmfAtmLayerTable,'atmfAtmLayerEntry':atmfAtmLayerEntry,_K:atmfAtmLayerIndex,'atmfAtmLayerMaxVPCs':atmfAtmLayerMaxVPCs,'atmfAtmLayerMaxVCCs':atmfAtmLayerMaxVCCs,'atmfAtmLayerConfiguredVPCs':atmfAtmLayerConfiguredVPCs,'atmfAtmLayerConfiguredVCCs':atmfAtmLayerConfiguredVCCs,'atmfAtmLayerMaxVpiBits':atmfAtmLayerMaxVpiBits,'atmfAtmLayerMaxVciBits':atmfAtmLayerMaxVciBits,'atmfAtmLayerUniType':atmfAtmLayerUniType,'atmfAtmLayerUniVersion':atmfAtmLayerUniVersion,'atmfAtmLayerDeviceType':atmfAtmLayerDeviceType,'atmfAtmLayerIlmiVersion':atmfAtmLayerIlmiVersion,'atmfAtmLayerNniSigVersion':atmfAtmLayerNniSigVersion,'atmfAtmLayerMaxSvpcVpi':atmfAtmLayerMaxSvpcVpi,'atmfAtmLayerMaxSvccVpi':atmfAtmLayerMaxSvccVpi,'atmfAtmLayerMinSvccVci':atmfAtmLayerMinSvccVci,'atmfAtmStatsTable':atmfAtmStatsTable,'atmfAtmStatsEntry':atmfAtmStatsEntry,_M:atmfAtmStatsIndex,'atmfAtmStatsReceivedCells':atmfAtmStatsReceivedCells,'atmfAtmStatsDroppedReceivedCells':atmfAtmStatsDroppedReceivedCells,'atmfAtmStatsTransmittedCells':atmfAtmStatsTransmittedCells,'atmfVpcTable':atmfVpcTable,'atmfVpcEntry':atmfVpcEntry,_N:atmfVpcPortIndex,_O:atmfVpcVpi,'atmfVpcOperStatus':atmfVpcOperStatus,'atmfVpcTransmitTrafficDescriptorType':atmfVpcTransmitTrafficDescriptorType,'atmfVpcTransmitTrafficDescriptorParam1':atmfVpcTransmitTrafficDescriptorParam1,'atmfVpcTransmitTrafficDescriptorParam2':atmfVpcTransmitTrafficDescriptorParam2,'atmfVpcTransmitTrafficDescriptorParam3':atmfVpcTransmitTrafficDescriptorParam3,'atmfVpcTransmitTrafficDescriptorParam4':atmfVpcTransmitTrafficDescriptorParam4,'atmfVpcTransmitTrafficDescriptorParam5':atmfVpcTransmitTrafficDescriptorParam5,'atmfVpcReceiveTrafficDescriptorType':atmfVpcReceiveTrafficDescriptorType,'atmfVpcReceiveTrafficDescriptorParam1':atmfVpcReceiveTrafficDescriptorParam1,'atmfVpcReceiveTrafficDescriptorParam2':atmfVpcReceiveTrafficDescriptorParam2,'atmfVpcReceiveTrafficDescriptorParam3':atmfVpcReceiveTrafficDescriptorParam3,'atmfVpcReceiveTrafficDescriptorParam4':atmfVpcReceiveTrafficDescriptorParam4,'atmfVpcReceiveTrafficDescriptorParam5':atmfVpcReceiveTrafficDescriptorParam5,'atmfVpcQoSCategory':atmfVpcQoSCategory,'atmfVpcTransmitQoSClass':atmfVpcTransmitQoSClass,'atmfVpcReceiveQoSClass':atmfVpcReceiveQoSClass,'atmfVpcBestEffortIndicator':atmfVpcBestEffortIndicator,'atmfVpcServiceCategory':atmfVpcServiceCategory,'atmfVccTable':atmfVccTable,'atmfVccEntry':atmfVccEntry,_X:atmfVccPortIndex,_Y:atmfVccVpi,_Z:atmfVccVci,'atmfVccOperStatus':atmfVccOperStatus,'atmfVccTransmitTrafficDescriptorType':atmfVccTransmitTrafficDescriptorType,'atmfVccTransmitTrafficDescriptorParam1':atmfVccTransmitTrafficDescriptorParam1,'atmfVccTransmitTrafficDescriptorParam2':atmfVccTransmitTrafficDescriptorParam2,'atmfVccTransmitTrafficDescriptorParam3':atmfVccTransmitTrafficDescriptorParam3,'atmfVccTransmitTrafficDescriptorParam4':atmfVccTransmitTrafficDescriptorParam4,'atmfVccTransmitTrafficDescriptorParam5':atmfVccTransmitTrafficDescriptorParam5,'atmfVccReceiveTrafficDescriptorType':atmfVccReceiveTrafficDescriptorType,'atmfVccReceiveTrafficDescriptorParam1':atmfVccReceiveTrafficDescriptorParam1,'atmfVccReceiveTrafficDescriptorParam2':atmfVccReceiveTrafficDescriptorParam2,'atmfVccReceiveTrafficDescriptorParam3':atmfVccReceiveTrafficDescriptorParam3,'atmfVccReceiveTrafficDescriptorParam4':atmfVccReceiveTrafficDescriptorParam4,'atmfVccReceiveTrafficDescriptorParam5':atmfVccReceiveTrafficDescriptorParam5,'atmfVccQoSCategory':atmfVccQoSCategory,'atmfVccTransmitQoSClass':atmfVccTransmitQoSClass,'atmfVccReceiveQoSClass':atmfVccReceiveQoSClass,'atmfVccBestEffortIndicator':atmfVccBestEffortIndicator,'atmfVccTransmitFrameDiscard':atmfVccTransmitFrameDiscard,'atmfVccReceiveFrameDiscard':atmfVccReceiveFrameDiscard,'atmfVccServiceCategory':atmfVccServiceCategory,'atmfVpcAbrTable':atmfVpcAbrTable,'atmfVpcAbrEntry':atmfVpcAbrEntry,_a:atmfVpcAbrPortIndex,_b:atmfVpcAbrVpi,'atmfVpcAbrTransmitIcr':atmfVpcAbrTransmitIcr,'atmfVpcAbrTransmitNrm':atmfVpcAbrTransmitNrm,'atmfVpcAbrTransmitTrm':atmfVpcAbrTransmitTrm,'atmfVpcAbrTransmitCdf':atmfVpcAbrTransmitCdf,'atmfVpcAbrTransmitRif':atmfVpcAbrTransmitRif,'atmfVpcAbrTransmitRdf':atmfVpcAbrTransmitRdf,'atmfVpcAbrTransmitAdtf':atmfVpcAbrTransmitAdtf,'atmfVpcAbrTransmitCrm':atmfVpcAbrTransmitCrm,'atmfVccAbrTable':atmfVccAbrTable,'atmfVccAbrEntry':atmfVccAbrEntry,_AL:atmfVccAbrPortIndex,_AM:atmfVccAbrVpi,_AN:atmfVccAbrVci,'atmfVccAbrTransmitIcr':atmfVccAbrTransmitIcr,'atmfVccAbrTransmitNrm':atmfVccAbrTransmitNrm,'atmfVccAbrTransmitTrm':atmfVccAbrTransmitTrm,'atmfVccAbrTransmitCdf':atmfVccAbrTransmitCdf,'atmfVccAbrTransmitRif':atmfVccAbrTransmitRif,'atmfVccAbrTransmitRdf':atmfVccAbrTransmitRdf,'atmfVccAbrTransmitAdtf':atmfVccAbrTransmitAdtf,'atmfVccAbrTransmitCrm':atmfVccAbrTransmitCrm})