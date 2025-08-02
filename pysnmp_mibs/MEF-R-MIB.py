_p='pmFlowCmdIndex'
_o='serviceIdRowPointer'
_n='overwriteEtherType'
_m='overwriteVlan'
_l='overwritePbit'
_k='remove'
_j='preserve'
_i='overwrite'
_h='flowIdx2'
_g='flowIdx1'
_f='uniRunningIndex'
_e='l2cpStatMacAddress'
_d='l2cpStatProtocol'
_c='l2cpStatPortIndex'
_b='portAuthentication'
_a='efmOam'
_Z='cPProfileRunningIndex'
_Y='cPProfileIndex'
_X='envelopeBwProfileCosIndex'
_W='bwProfileIndex'
_V='bwProfileID'
_U='untagged'
_T='ifIndex'
_S='IF-MIB'
_R='serviceIdName'
_Q='bytes'
_P='envelopeBwProfileIndex'
_O='Octets'
_N='none'
_M='kbps'
_L='read-write'
_K='TruthValue'
_J='SnmpAdminString'
_I='read-only'
_H='Unsigned32'
_G='Gauge32'
_F='Bits'
_E='not-accessible'
_D='MEF-R-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_S,'InterfaceIndexOrZero',_T)
radExperimental,=mibBuilder.importSymbols('RAD-SMI-MIB','radExperimental')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64',_G,_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp',_K)
mefMIBR=ModuleIdentity((1,3,6,1,4,1,164,20,8))
class TCVlanId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
class TCBurstSizeV2(TextualConvention,Unsigned32):status=_A;displayHint='d'
class TCV2DefaultUserPriority(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
class TCEthFrameHandling(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_U,1),('noChange',2),('changeVlan',3),('addVlan',4),('removeVlan',5),('rangeVlan',6)))
class TCSLAPrioritySource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('defUserPrio',1),('ieee802dot1p',2),('tos',3),('diffServ',4),('ieee802dot1q',5),('copy',6),('userMarkingTable',7),('spVlanId',8),('spVlanIdAndPBit',9)))
class TCEvcId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
class TCVTIdV2(TextualConvention,Unsigned32):status=_A;displayHint='d'
_MefObjects_ObjectIdentity=ObjectIdentity
mefObjects=_MefObjects_ObjectIdentity((1,3,6,1,4,1,164,20,8,1))
_MefrScalarObjects_ObjectIdentity=ObjectIdentity
mefrScalarObjects=_MefrScalarObjects_ObjectIdentity((1,3,6,1,4,1,164,20,8,1,1))
class _MefrBwRoundUp_Type(TruthValue):defaultValue=2
_MefrBwRoundUp_Type.__name__=_K
_MefrBwRoundUp_Object=MibScalar
mefrBwRoundUp=_MefrBwRoundUp_Object((1,3,6,1,4,1,164,20,8,1,1,1),_MefrBwRoundUp_Type())
mefrBwRoundUp.setMaxAccess(_L)
if mibBuilder.loadTexts:mefrBwRoundUp.setStatus(_A)
class _MefrEnvelopeRanks_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,4),ValueRangeConstraint(8,8))
_MefrEnvelopeRanks_Type.__name__=_H
_MefrEnvelopeRanks_Object=MibScalar
mefrEnvelopeRanks=_MefrEnvelopeRanks_Object((1,3,6,1,4,1,164,20,8,1,1,2),_MefrEnvelopeRanks_Type())
mefrEnvelopeRanks.setMaxAccess(_L)
if mibBuilder.loadTexts:mefrEnvelopeRanks.setStatus(_A)
class _HsQBlockMapping_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*(('slot1',1),('slot4',4)))
_HsQBlockMapping_Type.__name__=_C
_HsQBlockMapping_Object=MibScalar
hsQBlockMapping=_HsQBlockMapping_Object((1,3,6,1,4,1,164,20,8,1,1,3),_HsQBlockMapping_Type())
hsQBlockMapping.setMaxAccess(_L)
if mibBuilder.loadTexts:hsQBlockMapping.setStatus(_A)
_BwProfileObjects_ObjectIdentity=ObjectIdentity
bwProfileObjects=_BwProfileObjects_ObjectIdentity((1,3,6,1,4,1,164,20,8,1,3))
_BwProfileTable_Object=MibTable
bwProfileTable=_BwProfileTable_Object((1,3,6,1,4,1,164,20,8,1,3,1))
if mibBuilder.loadTexts:bwProfileTable.setStatus(_A)
_BwProfileEntry_Object=MibTableRow
bwProfileEntry=_BwProfileEntry_Object((1,3,6,1,4,1,164,20,8,1,3,1,1))
bwProfileEntry.setIndexNames((0,_D,_V),(0,_D,_W))
if mibBuilder.loadTexts:bwProfileEntry.setStatus(_A)
_BwProfileID_Type=TCVTIdV2
_BwProfileID_Object=MibTableColumn
bwProfileID=_BwProfileID_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,1),_BwProfileID_Type())
bwProfileID.setMaxAccess(_E)
if mibBuilder.loadTexts:bwProfileID.setStatus(_A)
_BwProfileIndex_Type=Unsigned32
_BwProfileIndex_Object=MibTableColumn
bwProfileIndex=_BwProfileIndex_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,2),_BwProfileIndex_Type())
bwProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bwProfileIndex.setStatus(_A)
_BwProfileRowStatus_Type=RowStatus
_BwProfileRowStatus_Object=MibTableColumn
bwProfileRowStatus=_BwProfileRowStatus_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,3),_BwProfileRowStatus_Type())
bwProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bwProfileRowStatus.setStatus(_A)
_BwProfileCIR_Type=Unsigned32
_BwProfileCIR_Object=MibTableColumn
bwProfileCIR=_BwProfileCIR_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,4),_BwProfileCIR_Type())
bwProfileCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:bwProfileCIR.setStatus(_A)
if mibBuilder.loadTexts:bwProfileCIR.setUnits('Kbps')
_BwProfileCBS_Type=TCBurstSizeV2
_BwProfileCBS_Object=MibTableColumn
bwProfileCBS=_BwProfileCBS_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,5),_BwProfileCBS_Type())
bwProfileCBS.setMaxAccess(_B)
if mibBuilder.loadTexts:bwProfileCBS.setStatus(_A)
if mibBuilder.loadTexts:bwProfileCBS.setUnits(_O)
_BwProfileEIR_Type=Unsigned32
_BwProfileEIR_Object=MibTableColumn
bwProfileEIR=_BwProfileEIR_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,8),_BwProfileEIR_Type())
bwProfileEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:bwProfileEIR.setStatus(_A)
if mibBuilder.loadTexts:bwProfileEIR.setUnits('Kbps')
_BwProfileEBS_Type=TCBurstSizeV2
_BwProfileEBS_Object=MibTableColumn
bwProfileEBS=_BwProfileEBS_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,9),_BwProfileEBS_Type())
bwProfileEBS.setMaxAccess(_B)
if mibBuilder.loadTexts:bwProfileEBS.setStatus(_A)
if mibBuilder.loadTexts:bwProfileEBS.setUnits(_O)
class _BwProfileColorAware_Type(TruthValue):defaultValue=2
_BwProfileColorAware_Type.__name__=_K
_BwProfileColorAware_Object=MibTableColumn
bwProfileColorAware=_BwProfileColorAware_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,12),_BwProfileColorAware_Type())
bwProfileColorAware.setMaxAccess(_B)
if mibBuilder.loadTexts:bwProfileColorAware.setStatus(_A)
class _BwProfileColorAwareAdmissionOption_Type(TruthValue):defaultValue=2
_BwProfileColorAwareAdmissionOption_Type.__name__=_K
_BwProfileColorAwareAdmissionOption_Object=MibTableColumn
bwProfileColorAwareAdmissionOption=_BwProfileColorAwareAdmissionOption_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,13),_BwProfileColorAwareAdmissionOption_Type())
bwProfileColorAwareAdmissionOption.setMaxAccess(_B)
if mibBuilder.loadTexts:bwProfileColorAwareAdmissionOption.setStatus(_A)
_BwProfileName_Type=SnmpAdminString
_BwProfileName_Object=MibTableColumn
bwProfileName=_BwProfileName_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,14),_BwProfileName_Type())
bwProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:bwProfileName.setStatus(_A)
class _BwProfileGranularity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*(('r64kbps',2),('r1Mbps',3),('r10Mbps',4),('r100Mbps',5)))
_BwProfileGranularity_Type.__name__=_C
_BwProfileGranularity_Object=MibTableColumn
bwProfileGranularity=_BwProfileGranularity_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,15),_BwProfileGranularity_Type())
bwProfileGranularity.setMaxAccess(_B)
if mibBuilder.loadTexts:bwProfileGranularity.setStatus(_A)
class _BwProfilePolicedTraffic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*(('all',2),('broadcast',3),('multicast',4),('unknownUnicast',5),('broadcastAndMulticast',6),('broadcastAndMulticastAndUnknownUnicast',7)))
_BwProfilePolicedTraffic_Type.__name__=_C
_BwProfilePolicedTraffic_Object=MibTableColumn
bwProfilePolicedTraffic=_BwProfilePolicedTraffic_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,16),_BwProfilePolicedTraffic_Type())
bwProfilePolicedTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:bwProfilePolicedTraffic.setStatus(_A)
_BwProfileCompensation_Type=Unsigned32
_BwProfileCompensation_Object=MibTableColumn
bwProfileCompensation=_BwProfileCompensation_Object((1,3,6,1,4,1,164,20,8,1,3,1,1,17),_BwProfileCompensation_Type())
bwProfileCompensation.setMaxAccess(_B)
if mibBuilder.loadTexts:bwProfileCompensation.setStatus(_A)
if mibBuilder.loadTexts:bwProfileCompensation.setUnits(_O)
_EnvelopeBwProfileTable_Object=MibTable
envelopeBwProfileTable=_EnvelopeBwProfileTable_Object((1,3,6,1,4,1,164,20,8,1,3,2))
if mibBuilder.loadTexts:envelopeBwProfileTable.setStatus(_A)
_EnvelopeBwProfileEntry_Object=MibTableRow
envelopeBwProfileEntry=_EnvelopeBwProfileEntry_Object((1,3,6,1,4,1,164,20,8,1,3,2,1))
envelopeBwProfileEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:envelopeBwProfileEntry.setStatus(_A)
_EnvelopeBwProfileIndex_Type=Unsigned32
_EnvelopeBwProfileIndex_Object=MibTableColumn
envelopeBwProfileIndex=_EnvelopeBwProfileIndex_Object((1,3,6,1,4,1,164,20,8,1,3,2,1,1),_EnvelopeBwProfileIndex_Type())
envelopeBwProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:envelopeBwProfileIndex.setStatus(_A)
class _EnvelopeBwProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_EnvelopeBwProfileName_Type.__name__=_J
_EnvelopeBwProfileName_Object=MibTableColumn
envelopeBwProfileName=_EnvelopeBwProfileName_Object((1,3,6,1,4,1,164,20,8,1,3,2,1,2),_EnvelopeBwProfileName_Type())
envelopeBwProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileName.setStatus(_A)
_EnvelopeBwProfileRowStatus_Type=RowStatus
_EnvelopeBwProfileRowStatus_Object=MibTableColumn
envelopeBwProfileRowStatus=_EnvelopeBwProfileRowStatus_Object((1,3,6,1,4,1,164,20,8,1,3,2,1,3),_EnvelopeBwProfileRowStatus_Type())
envelopeBwProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileRowStatus.setStatus(_A)
class _EnvelopeBwProfileCouplingFlagPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('sharingExcessBw',2),('uncoupledBwSharing',3)))
_EnvelopeBwProfileCouplingFlagPolicy_Type.__name__=_C
_EnvelopeBwProfileCouplingFlagPolicy_Object=MibTableColumn
envelopeBwProfileCouplingFlagPolicy=_EnvelopeBwProfileCouplingFlagPolicy_Object((1,3,6,1,4,1,164,20,8,1,3,2,1,4),_EnvelopeBwProfileCouplingFlagPolicy_Type())
envelopeBwProfileCouplingFlagPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileCouplingFlagPolicy.setStatus(_A)
class _EnvelopeBwProfileCouplingFlag0_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_EnvelopeBwProfileCouplingFlag0_Type.__name__=_H
_EnvelopeBwProfileCouplingFlag0_Object=MibTableColumn
envelopeBwProfileCouplingFlag0=_EnvelopeBwProfileCouplingFlag0_Object((1,3,6,1,4,1,164,20,8,1,3,2,1,5),_EnvelopeBwProfileCouplingFlag0_Type())
envelopeBwProfileCouplingFlag0.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileCouplingFlag0.setStatus(_A)
class _EnvelopeBwProfileColorMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('colorAware',1),('colorBlind',2)))
_EnvelopeBwProfileColorMode_Type.__name__=_C
_EnvelopeBwProfileColorMode_Object=MibTableColumn
envelopeBwProfileColorMode=_EnvelopeBwProfileColorMode_Object((1,3,6,1,4,1,164,20,8,1,3,2,1,6),_EnvelopeBwProfileColorMode_Type())
envelopeBwProfileColorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileColorMode.setStatus(_A)
class _EnvelopeBwProfileCompensation_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_EnvelopeBwProfileCompensation_Type.__name__=_H
_EnvelopeBwProfileCompensation_Object=MibTableColumn
envelopeBwProfileCompensation=_EnvelopeBwProfileCompensation_Object((1,3,6,1,4,1,164,20,8,1,3,2,1,7),_EnvelopeBwProfileCompensation_Type())
envelopeBwProfileCompensation.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileCompensation.setStatus(_A)
if mibBuilder.loadTexts:envelopeBwProfileCompensation.setUnits(_Q)
_EnvelopeBwProfileCosTable_Object=MibTable
envelopeBwProfileCosTable=_EnvelopeBwProfileCosTable_Object((1,3,6,1,4,1,164,20,8,1,3,3))
if mibBuilder.loadTexts:envelopeBwProfileCosTable.setStatus(_A)
_EnvelopeBwProfileCosEntry_Object=MibTableRow
envelopeBwProfileCosEntry=_EnvelopeBwProfileCosEntry_Object((1,3,6,1,4,1,164,20,8,1,3,3,1))
envelopeBwProfileCosEntry.setIndexNames((0,_D,_P),(0,_D,_X))
if mibBuilder.loadTexts:envelopeBwProfileCosEntry.setStatus(_A)
class _EnvelopeBwProfileCosIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_EnvelopeBwProfileCosIndex_Type.__name__=_H
_EnvelopeBwProfileCosIndex_Object=MibTableColumn
envelopeBwProfileCosIndex=_EnvelopeBwProfileCosIndex_Object((1,3,6,1,4,1,164,20,8,1,3,3,1,1),_EnvelopeBwProfileCosIndex_Type())
envelopeBwProfileCosIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:envelopeBwProfileCosIndex.setStatus(_A)
_EnvelopeBwProfileCosRowStatus_Type=RowStatus
_EnvelopeBwProfileCosRowStatus_Object=MibTableColumn
envelopeBwProfileCosRowStatus=_EnvelopeBwProfileCosRowStatus_Object((1,3,6,1,4,1,164,20,8,1,3,3,1,2),_EnvelopeBwProfileCosRowStatus_Type())
envelopeBwProfileCosRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileCosRowStatus.setStatus(_A)
class _EnvelopeBwProfileCosCir_Type(Gauge32):defaultValue=0
_EnvelopeBwProfileCosCir_Type.__name__=_G
_EnvelopeBwProfileCosCir_Object=MibTableColumn
envelopeBwProfileCosCir=_EnvelopeBwProfileCosCir_Object((1,3,6,1,4,1,164,20,8,1,3,3,1,3),_EnvelopeBwProfileCosCir_Type())
envelopeBwProfileCosCir.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileCosCir.setStatus(_A)
if mibBuilder.loadTexts:envelopeBwProfileCosCir.setUnits(_M)
class _EnvelopeBwProfileCosCirMax_Type(Gauge32):defaultValue=10000000
_EnvelopeBwProfileCosCirMax_Type.__name__=_G
_EnvelopeBwProfileCosCirMax_Object=MibTableColumn
envelopeBwProfileCosCirMax=_EnvelopeBwProfileCosCirMax_Object((1,3,6,1,4,1,164,20,8,1,3,3,1,4),_EnvelopeBwProfileCosCirMax_Type())
envelopeBwProfileCosCirMax.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileCosCirMax.setStatus(_A)
if mibBuilder.loadTexts:envelopeBwProfileCosCirMax.setUnits(_M)
class _EnvelopeBwProfileCosCbs_Type(Gauge32):defaultValue=0
_EnvelopeBwProfileCosCbs_Type.__name__=_G
_EnvelopeBwProfileCosCbs_Object=MibTableColumn
envelopeBwProfileCosCbs=_EnvelopeBwProfileCosCbs_Object((1,3,6,1,4,1,164,20,8,1,3,3,1,5),_EnvelopeBwProfileCosCbs_Type())
envelopeBwProfileCosCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileCosCbs.setStatus(_A)
if mibBuilder.loadTexts:envelopeBwProfileCosCbs.setUnits(_Q)
class _EnvelopeBwProfileCosEir_Type(Gauge32):defaultValue=0
_EnvelopeBwProfileCosEir_Type.__name__=_G
_EnvelopeBwProfileCosEir_Object=MibTableColumn
envelopeBwProfileCosEir=_EnvelopeBwProfileCosEir_Object((1,3,6,1,4,1,164,20,8,1,3,3,1,6),_EnvelopeBwProfileCosEir_Type())
envelopeBwProfileCosEir.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileCosEir.setStatus(_A)
if mibBuilder.loadTexts:envelopeBwProfileCosEir.setUnits(_M)
class _EnvelopeBwProfileCosEirMax_Type(Gauge32):defaultValue=10000000
_EnvelopeBwProfileCosEirMax_Type.__name__=_G
_EnvelopeBwProfileCosEirMax_Object=MibTableColumn
envelopeBwProfileCosEirMax=_EnvelopeBwProfileCosEirMax_Object((1,3,6,1,4,1,164,20,8,1,3,3,1,7),_EnvelopeBwProfileCosEirMax_Type())
envelopeBwProfileCosEirMax.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileCosEirMax.setStatus(_A)
if mibBuilder.loadTexts:envelopeBwProfileCosEirMax.setUnits(_M)
class _EnvelopeBwProfileCosEbs_Type(Gauge32):defaultValue=0
_EnvelopeBwProfileCosEbs_Type.__name__=_G
_EnvelopeBwProfileCosEbs_Object=MibTableColumn
envelopeBwProfileCosEbs=_EnvelopeBwProfileCosEbs_Object((1,3,6,1,4,1,164,20,8,1,3,3,1,8),_EnvelopeBwProfileCosEbs_Type())
envelopeBwProfileCosEbs.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileCosEbs.setStatus(_A)
if mibBuilder.loadTexts:envelopeBwProfileCosEbs.setUnits(_Q)
class _EnvelopeBwProfileCoSCouplingFlag_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_EnvelopeBwProfileCoSCouplingFlag_Type.__name__=_H
_EnvelopeBwProfileCoSCouplingFlag_Object=MibTableColumn
envelopeBwProfileCoSCouplingFlag=_EnvelopeBwProfileCoSCouplingFlag_Object((1,3,6,1,4,1,164,20,8,1,3,3,1,9),_EnvelopeBwProfileCoSCouplingFlag_Type())
envelopeBwProfileCoSCouplingFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:envelopeBwProfileCoSCouplingFlag.setStatus(_A)
_CPObjects_ObjectIdentity=ObjectIdentity
cPObjects=_CPObjects_ObjectIdentity((1,3,6,1,4,1,164,20,8,1,4))
_CPProfileTable_Object=MibTable
cPProfileTable=_CPProfileTable_Object((1,3,6,1,4,1,164,20,8,1,4,1))
if mibBuilder.loadTexts:cPProfileTable.setStatus(_A)
_CPProfileEntry_Object=MibTableRow
cPProfileEntry=_CPProfileEntry_Object((1,3,6,1,4,1,164,20,8,1,4,1,1))
cPProfileEntry.setIndexNames((0,_D,_Y),(0,_D,_Z))
if mibBuilder.loadTexts:cPProfileEntry.setStatus(_A)
class _CPProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CPProfileIndex_Type.__name__=_C
_CPProfileIndex_Object=MibTableColumn
cPProfileIndex=_CPProfileIndex_Object((1,3,6,1,4,1,164,20,8,1,4,1,1,1),_CPProfileIndex_Type())
cPProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cPProfileIndex.setStatus(_A)
class _CPProfileRunningIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CPProfileRunningIndex_Type.__name__=_C
_CPProfileRunningIndex_Object=MibTableColumn
cPProfileRunningIndex=_CPProfileRunningIndex_Object((1,3,6,1,4,1,164,20,8,1,4,1,1,2),_CPProfileRunningIndex_Type())
cPProfileRunningIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cPProfileRunningIndex.setStatus(_A)
_CPProfileRowStatus_Type=RowStatus
_CPProfileRowStatus_Object=MibTableColumn
cPProfileRowStatus=_CPProfileRowStatus_Object((1,3,6,1,4,1,164,20,8,1,4,1,1,3),_CPProfileRowStatus_Type())
cPProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cPProfileRowStatus.setStatus(_A)
_CPProfileMacAddress_Type=MacAddress
_CPProfileMacAddress_Object=MibTableColumn
cPProfileMacAddress=_CPProfileMacAddress_Object((1,3,6,1,4,1,164,20,8,1,4,1,1,4),_CPProfileMacAddress_Type())
cPProfileMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cPProfileMacAddress.setStatus(_A)
class _CPProfileMacProcessing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ignore',1),('discard',2),('peer',3),('tunnel',4),('macChangeTunnel',5)))
_CPProfileMacProcessing_Type.__name__=_C
_CPProfileMacProcessing_Object=MibTableColumn
cPProfileMacProcessing=_CPProfileMacProcessing_Object((1,3,6,1,4,1,164,20,8,1,4,1,1,5),_CPProfileMacProcessing_Type())
cPProfileMacProcessing.setMaxAccess(_B)
if mibBuilder.loadTexts:cPProfileMacProcessing.setStatus(_A)
_CPProfileName_Type=SnmpAdminString
_CPProfileName_Object=MibTableColumn
cPProfileName=_CPProfileName_Object((1,3,6,1,4,1,164,20,8,1,4,1,1,6),_CPProfileName_Type())
cPProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cPProfileName.setStatus(_A)
class _CPProfileProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,14,15,16)));namedValues=NamedValues(*((_N,1),(_a,2),(_b,3),('lacp',4),('garp',5),('stp',6),('cdp',7),('vtp',8),('lldp',9),('pvstp',10),('pagp',11),('udld',14),('dtp',15),('loopback',16)))
_CPProfileProtocol_Type.__name__=_C
_CPProfileProtocol_Object=MibTableColumn
cPProfileProtocol=_CPProfileProtocol_Object((1,3,6,1,4,1,164,20,8,1,4,1,1,7),_CPProfileProtocol_Type())
cPProfileProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cPProfileProtocol.setStatus(_A)
_L2cpStatTable_Object=MibTable
l2cpStatTable=_L2cpStatTable_Object((1,3,6,1,4,1,164,20,8,1,4,2))
if mibBuilder.loadTexts:l2cpStatTable.setStatus(_A)
_L2cpStatEntry_Object=MibTableRow
l2cpStatEntry=_L2cpStatEntry_Object((1,3,6,1,4,1,164,20,8,1,4,2,1))
l2cpStatEntry.setIndexNames((0,_D,_c),(0,_D,_d),(0,_D,_e))
if mibBuilder.loadTexts:l2cpStatEntry.setStatus(_A)
class _L2cpStatPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_L2cpStatPortIndex_Type.__name__=_C
_L2cpStatPortIndex_Object=MibTableColumn
l2cpStatPortIndex=_L2cpStatPortIndex_Object((1,3,6,1,4,1,164,20,8,1,4,2,1,1),_L2cpStatPortIndex_Type())
l2cpStatPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:l2cpStatPortIndex.setStatus(_A)
class _L2cpStatProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_N,1),('other',2),('all',3),(_a,4),(_b,5),('lacp',6),('garp',7),('stp',8),('cdp',9),('vtp',10),('lldp',11),('pvstp',12),('pagp',13),('udld',14),('dtp',15)))
_L2cpStatProtocol_Type.__name__=_C
_L2cpStatProtocol_Object=MibTableColumn
l2cpStatProtocol=_L2cpStatProtocol_Object((1,3,6,1,4,1,164,20,8,1,4,2,1,2),_L2cpStatProtocol_Type())
l2cpStatProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:l2cpStatProtocol.setStatus(_A)
_L2cpStatMacAddress_Type=MacAddress
_L2cpStatMacAddress_Object=MibTableColumn
l2cpStatMacAddress=_L2cpStatMacAddress_Object((1,3,6,1,4,1,164,20,8,1,4,2,1,3),_L2cpStatMacAddress_Type())
l2cpStatMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:l2cpStatMacAddress.setStatus(_A)
_L2cpStatEncapsulatedFrames_Type=Counter32
_L2cpStatEncapsulatedFrames_Object=MibTableColumn
l2cpStatEncapsulatedFrames=_L2cpStatEncapsulatedFrames_Object((1,3,6,1,4,1,164,20,8,1,4,2,1,4),_L2cpStatEncapsulatedFrames_Type())
l2cpStatEncapsulatedFrames.setMaxAccess(_I)
if mibBuilder.loadTexts:l2cpStatEncapsulatedFrames.setStatus(_A)
_L2cpStatDecapsulatedFrames_Type=Counter32
_L2cpStatDecapsulatedFrames_Object=MibTableColumn
l2cpStatDecapsulatedFrames=_L2cpStatDecapsulatedFrames_Object((1,3,6,1,4,1,164,20,8,1,4,2,1,5),_L2cpStatDecapsulatedFrames_Type())
l2cpStatDecapsulatedFrames.setMaxAccess(_I)
if mibBuilder.loadTexts:l2cpStatDecapsulatedFrames.setStatus(_A)
_UniObjects_ObjectIdentity=ObjectIdentity
uniObjects=_UniObjects_ObjectIdentity((1,3,6,1,4,1,164,20,8,1,5))
_UniTable_Object=MibTable
uniTable=_UniTable_Object((1,3,6,1,4,1,164,20,8,1,5,1))
if mibBuilder.loadTexts:uniTable.setStatus(_A)
_UniEntry_Object=MibTableRow
uniEntry=_UniEntry_Object((1,3,6,1,4,1,164,20,8,1,5,1,1))
uniEntry.setIndexNames((0,_S,_T),(0,_D,_f))
if mibBuilder.loadTexts:uniEntry.setStatus(_A)
_UniRunningIndex_Type=Unsigned32
_UniRunningIndex_Object=MibTableColumn
uniRunningIndex=_UniRunningIndex_Object((1,3,6,1,4,1,164,20,8,1,5,1,1,1),_UniRunningIndex_Type())
uniRunningIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:uniRunningIndex.setStatus(_A)
_UniRowStatus_Type=RowStatus
_UniRowStatus_Object=MibTableColumn
uniRowStatus=_UniRowStatus_Object((1,3,6,1,4,1,164,20,8,1,5,1,1,2),_UniRowStatus_Type())
uniRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:uniRowStatus.setStatus(_A)
_UniLayer2CPProcessingProfile_Type=Integer32
_UniLayer2CPProcessingProfile_Object=MibTableColumn
uniLayer2CPProcessingProfile=_UniLayer2CPProcessingProfile_Object((1,3,6,1,4,1,164,20,8,1,5,1,1,12),_UniLayer2CPProcessingProfile_Type())
uniLayer2CPProcessingProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:uniLayer2CPProcessingProfile.setStatus(_A)
_UniPerUniBWprofile_Type=TCVTIdV2
_UniPerUniBWprofile_Object=MibTableColumn
uniPerUniBWprofile=_UniPerUniBWprofile_Object((1,3,6,1,4,1,164,20,8,1,5,1,1,13),_UniPerUniBWprofile_Type())
uniPerUniBWprofile.setMaxAccess(_B)
if mibBuilder.loadTexts:uniPerUniBWprofile.setStatus(_A)
_UniSpTagProtocolIdentifier_Type=Integer32
_UniSpTagProtocolIdentifier_Object=MibTableColumn
uniSpTagProtocolIdentifier=_UniSpTagProtocolIdentifier_Object((1,3,6,1,4,1,164,20,8,1,5,1,1,22),_UniSpTagProtocolIdentifier_Type())
uniSpTagProtocolIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:uniSpTagProtocolIdentifier.setStatus(_A)
class _UniPacketColoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('deiColoring',2),('priorityLsbColoring',3)))
_UniPacketColoring_Type.__name__=_C
_UniPacketColoring_Object=MibTableColumn
uniPacketColoring=_UniPacketColoring_Object((1,3,6,1,4,1,164,20,8,1,5,1,1,23),_UniPacketColoring_Type())
uniPacketColoring.setMaxAccess(_B)
if mibBuilder.loadTexts:uniPacketColoring.setStatus(_A)
class _UniPerUniEgressAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('addSpTag',2)))
_UniPerUniEgressAction_Type.__name__=_C
_UniPerUniEgressAction_Object=MibTableColumn
uniPerUniEgressAction=_UniPerUniEgressAction_Object((1,3,6,1,4,1,164,20,8,1,5,1,1,27),_UniPerUniEgressAction_Type())
uniPerUniEgressAction.setMaxAccess(_B)
if mibBuilder.loadTexts:uniPerUniEgressAction.setStatus(_A)
_UniQueueGroupName_Type=SnmpAdminString
_UniQueueGroupName_Object=MibTableColumn
uniQueueGroupName=_UniQueueGroupName_Object((1,3,6,1,4,1,164,20,8,1,5,1,1,33),_UniQueueGroupName_Type())
uniQueueGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:uniQueueGroupName.setStatus(_A)
class _UniClassifierKey_Type(Bits):namedValues=NamedValues(*(('vlan',0),('innerVlan',1),('pBit',2),('ipPrecedence',3),('ipDscp',4),('srcIpAddr',5),('destIpAddr',6),('legacy',7),('dscp',8),('macSrcAddr',9),('macDestAddr',10),('etherType',11),('myMac',12),(_U,13)))
_UniClassifierKey_Type.__name__=_F
_UniClassifierKey_Object=MibTableColumn
uniClassifierKey=_UniClassifierKey_Object((1,3,6,1,4,1,164,20,8,1,5,1,1,36),_UniClassifierKey_Type())
uniClassifierKey.setMaxAccess(_B)
if mibBuilder.loadTexts:uniClassifierKey.setStatus(_A)
_EvcObjects_ObjectIdentity=ObjectIdentity
evcObjects=_EvcObjects_ObjectIdentity((1,3,6,1,4,1,164,20,8,1,6))
_FlowTable_Object=MibTable
flowTable=_FlowTable_Object((1,3,6,1,4,1,164,20,8,1,6,3))
if mibBuilder.loadTexts:flowTable.setStatus(_A)
_FlowEntry_Object=MibTableRow
flowEntry=_FlowEntry_Object((1,3,6,1,4,1,164,20,8,1,6,3,1))
flowEntry.setIndexNames((0,_D,_g),(0,_D,_h))
if mibBuilder.loadTexts:flowEntry.setStatus(_A)
_FlowIdx1_Type=Unsigned32
_FlowIdx1_Object=MibTableColumn
flowIdx1=_FlowIdx1_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,1),_FlowIdx1_Type())
flowIdx1.setMaxAccess(_E)
if mibBuilder.loadTexts:flowIdx1.setStatus(_A)
_FlowIdx2_Type=Unsigned32
_FlowIdx2_Object=MibTableColumn
flowIdx2=_FlowIdx2_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,2),_FlowIdx2_Type())
flowIdx2.setMaxAccess(_E)
if mibBuilder.loadTexts:flowIdx2.setStatus(_A)
_FlowName_Type=SnmpAdminString
_FlowName_Object=MibTableColumn
flowName=_FlowName_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,3),_FlowName_Type())
flowName.setMaxAccess(_B)
if mibBuilder.loadTexts:flowName.setStatus(_A)
_FlowRowStatus_Type=RowStatus
_FlowRowStatus_Object=MibTableColumn
flowRowStatus=_FlowRowStatus_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,4),_FlowRowStatus_Type())
flowRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:flowRowStatus.setStatus(_A)
_FlowBWprofile_Type=TCVTIdV2
_FlowBWprofile_Object=MibTableColumn
flowBWprofile=_FlowBWprofile_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,5),_FlowBWprofile_Type())
flowBWprofile.setMaxAccess(_B)
if mibBuilder.loadTexts:flowBWprofile.setStatus(_A)
_FlowFixedCos_Type=Unsigned32
_FlowFixedCos_Object=MibTableColumn
flowFixedCos=_FlowFixedCos_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,6),_FlowFixedCos_Type())
flowFixedCos.setMaxAccess(_B)
if mibBuilder.loadTexts:flowFixedCos.setStatus(_A)
_FlowCOSProfile_Type=Unsigned32
_FlowCOSProfile_Object=MibTableColumn
flowCOSProfile=_FlowCOSProfile_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,7),_FlowCOSProfile_Type())
flowCOSProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:flowCOSProfile.setStatus(_A)
_FlowQBlock_Type=ObjectIdentifier
_FlowQBlock_Object=MibTableColumn
flowQBlock=_FlowQBlock_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,8),_FlowQBlock_Type())
flowQBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:flowQBlock.setStatus(_A)
_FlowMappingProfile_Type=Unsigned32
_FlowMappingProfile_Object=MibTableColumn
flowMappingProfile=_FlowMappingProfile_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,9),_FlowMappingProfile_Type())
flowMappingProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMappingProfile.setStatus(_A)
_FlowFixedMarking_Type=Unsigned32
_FlowFixedMarking_Object=MibTableColumn
flowFixedMarking=_FlowFixedMarking_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,10),_FlowFixedMarking_Type())
flowFixedMarking.setMaxAccess(_B)
if mibBuilder.loadTexts:flowFixedMarking.setStatus(_A)
_FlowMarkingProfile_Type=Unsigned32
_FlowMarkingProfile_Object=MibTableColumn
flowMarkingProfile=_FlowMarkingProfile_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,11),_FlowMarkingProfile_Type())
flowMarkingProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMarkingProfile.setStatus(_A)
class _FlowOuterVlanTagging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('add',1),(_i,2),(_j,3),(_k,4)))
_FlowOuterVlanTagging_Type.__name__=_C
_FlowOuterVlanTagging_Object=MibTableColumn
flowOuterVlanTagging=_FlowOuterVlanTagging_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,12),_FlowOuterVlanTagging_Type())
flowOuterVlanTagging.setMaxAccess(_B)
if mibBuilder.loadTexts:flowOuterVlanTagging.setStatus(_A)
_FlowOuterVlan_Type=Unsigned32
_FlowOuterVlan_Object=MibTableColumn
flowOuterVlan=_FlowOuterVlan_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,13),_FlowOuterVlan_Type())
flowOuterVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:flowOuterVlan.setStatus(_A)
class _FlowInnerVlanTagging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('add',1),(_i,2),(_j,3),(_k,4)))
_FlowInnerVlanTagging_Type.__name__=_C
_FlowInnerVlanTagging_Object=MibTableColumn
flowInnerVlanTagging=_FlowInnerVlanTagging_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,14),_FlowInnerVlanTagging_Type())
flowInnerVlanTagging.setMaxAccess(_B)
if mibBuilder.loadTexts:flowInnerVlanTagging.setStatus(_A)
_FlowInnerVlan_Type=Unsigned32
_FlowInnerVlan_Object=MibTableColumn
flowInnerVlan=_FlowInnerVlan_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,15),_FlowInnerVlan_Type())
flowInnerVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:flowInnerVlan.setStatus(_A)
_FlowEgressPort_Type=Unsigned32
_FlowEgressPort_Object=MibTableColumn
flowEgressPort=_FlowEgressPort_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,16),_FlowEgressPort_Type())
flowEgressPort.setMaxAccess(_B)
if mibBuilder.loadTexts:flowEgressPort.setStatus(_A)
_FlowIngressPort_Type=Unsigned32
_FlowIngressPort_Object=MibTableColumn
flowIngressPort=_FlowIngressPort_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,17),_FlowIngressPort_Type())
flowIngressPort.setMaxAccess(_B)
if mibBuilder.loadTexts:flowIngressPort.setStatus(_A)
_FlowInnerFixedMarking_Type=Unsigned32
_FlowInnerFixedMarking_Object=MibTableColumn
flowInnerFixedMarking=_FlowInnerFixedMarking_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,18),_FlowInnerFixedMarking_Type())
flowInnerFixedMarking.setMaxAccess(_B)
if mibBuilder.loadTexts:flowInnerFixedMarking.setStatus(_A)
_FlowInnerMarkingProfile_Type=Unsigned32
_FlowInnerMarkingProfile_Object=MibTableColumn
flowInnerMarkingProfile=_FlowInnerMarkingProfile_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,19),_FlowInnerMarkingProfile_Type())
flowInnerMarkingProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:flowInnerMarkingProfile.setStatus(_A)
class _FlowDropAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('disable',2),('enable',3)))
_FlowDropAction_Type.__name__=_C
_FlowDropAction_Object=MibTableColumn
flowDropAction=_FlowDropAction_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,20),_FlowDropAction_Type())
flowDropAction.setMaxAccess(_B)
if mibBuilder.loadTexts:flowDropAction.setStatus(_A)
_FlowPriority_Type=Unsigned32
_FlowPriority_Object=MibTableColumn
flowPriority=_FlowPriority_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,21),_FlowPriority_Type())
flowPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:flowPriority.setStatus(_A)
_FlowMarkOuterFixedMarking_Type=Unsigned32
_FlowMarkOuterFixedMarking_Object=MibTableColumn
flowMarkOuterFixedMarking=_FlowMarkOuterFixedMarking_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,22),_FlowMarkOuterFixedMarking_Type())
flowMarkOuterFixedMarking.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMarkOuterFixedMarking.setStatus(_A)
_FlowMarkOuterMarkingProfile_Type=Unsigned32
_FlowMarkOuterMarkingProfile_Object=MibTableColumn
flowMarkOuterMarkingProfile=_FlowMarkOuterMarkingProfile_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,23),_FlowMarkOuterMarkingProfile_Type())
flowMarkOuterMarkingProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMarkOuterMarkingProfile.setStatus(_A)
_FlowMarkInnerFixedMarking_Type=Unsigned32
_FlowMarkInnerFixedMarking_Object=MibTableColumn
flowMarkInnerFixedMarking=_FlowMarkInnerFixedMarking_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,24),_FlowMarkInnerFixedMarking_Type())
flowMarkInnerFixedMarking.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMarkInnerFixedMarking.setStatus(_A)
_FlowMarkInnerMarkingProfile_Type=Unsigned32
_FlowMarkInnerMarkingProfile_Object=MibTableColumn
flowMarkInnerMarkingProfile=_FlowMarkInnerMarkingProfile_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,25),_FlowMarkInnerMarkingProfile_Type())
flowMarkInnerMarkingProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMarkInnerMarkingProfile.setStatus(_A)
class _FlowMarkOuterVlanTagging_Type(Bits):namedValues=NamedValues(*((_l,0),(_m,1),(_n,2)))
_FlowMarkOuterVlanTagging_Type.__name__=_F
_FlowMarkOuterVlanTagging_Object=MibTableColumn
flowMarkOuterVlanTagging=_FlowMarkOuterVlanTagging_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,26),_FlowMarkOuterVlanTagging_Type())
flowMarkOuterVlanTagging.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMarkOuterVlanTagging.setStatus(_A)
_FlowMarkOuterVlan_Type=Unsigned32
_FlowMarkOuterVlan_Object=MibTableColumn
flowMarkOuterVlan=_FlowMarkOuterVlan_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,27),_FlowMarkOuterVlan_Type())
flowMarkOuterVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMarkOuterVlan.setStatus(_A)
class _FlowMarkInnerVlanTagging_Type(Bits):namedValues=NamedValues(*((_l,0),(_m,1),(_n,2)))
_FlowMarkInnerVlanTagging_Type.__name__=_F
_FlowMarkInnerVlanTagging_Object=MibTableColumn
flowMarkInnerVlanTagging=_FlowMarkInnerVlanTagging_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,28),_FlowMarkInnerVlanTagging_Type())
flowMarkInnerVlanTagging.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMarkInnerVlanTagging.setStatus(_A)
_FlowMarkInnerVlan_Type=Unsigned32
_FlowMarkInnerVlan_Object=MibTableColumn
flowMarkInnerVlan=_FlowMarkInnerVlan_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,29),_FlowMarkInnerVlan_Type())
flowMarkInnerVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMarkInnerVlan.setStatus(_A)
_FlowPolicerAggregate_Type=Unsigned32
_FlowPolicerAggregate_Object=MibTableColumn
flowPolicerAggregate=_FlowPolicerAggregate_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,30),_FlowPolicerAggregate_Type())
flowPolicerAggregate.setMaxAccess(_B)
if mibBuilder.loadTexts:flowPolicerAggregate.setStatus(_A)
class _FlowMarkMacTagging_Type(Bits):namedValues=NamedValues(*(('swapMacSrcAndDst',0),('overwriteSrcMac',1),('overwriteDstMac',2)))
_FlowMarkMacTagging_Type.__name__=_F
_FlowMarkMacTagging_Object=MibTableColumn
flowMarkMacTagging=_FlowMarkMacTagging_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,32),_FlowMarkMacTagging_Type())
flowMarkMacTagging.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMarkMacTagging.setStatus(_A)
class _FlowMarkIpTagging_Type(Bits):namedValues=NamedValues(*(('swapIpSrcAndDst',0),('overwriteSrcIp',1),('overwriteDstIp',2)))
_FlowMarkIpTagging_Type.__name__=_F
_FlowMarkIpTagging_Object=MibTableColumn
flowMarkIpTagging=_FlowMarkIpTagging_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,33),_FlowMarkIpTagging_Type())
flowMarkIpTagging.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMarkIpTagging.setStatus(_A)
_FlowLayer2CPProcessingProfile_Type=Unsigned32
_FlowLayer2CPProcessingProfile_Object=MibTableColumn
flowLayer2CPProcessingProfile=_FlowLayer2CPProcessingProfile_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,38),_FlowLayer2CPProcessingProfile_Type())
flowLayer2CPProcessingProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:flowLayer2CPProcessingProfile.setStatus(_A)
class _FlowIngressColorMapping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('green',1),('yellow',2),('colorProfile',255)))
_FlowIngressColorMapping_Type.__name__=_C
_FlowIngressColorMapping_Object=MibTableColumn
flowIngressColorMapping=_FlowIngressColorMapping_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,39),_FlowIngressColorMapping_Type())
flowIngressColorMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:flowIngressColorMapping.setStatus(_A)
_FlowIngressColorProfile_Type=Unsigned32
_FlowIngressColorProfile_Object=MibTableColumn
flowIngressColorProfile=_FlowIngressColorProfile_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,40),_FlowIngressColorProfile_Type())
flowIngressColorProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:flowIngressColorProfile.setStatus(_A)
_FlowCosMapping_Type=Unsigned32
_FlowCosMapping_Object=MibTableColumn
flowCosMapping=_FlowCosMapping_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,41),_FlowCosMapping_Type())
flowCosMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:flowCosMapping.setStatus(_A)
_FlowCosMappingProfile_Type=Unsigned32
_FlowCosMappingProfile_Object=MibTableColumn
flowCosMappingProfile=_FlowCosMappingProfile_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,42),_FlowCosMappingProfile_Type())
flowCosMappingProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:flowCosMappingProfile.setStatus(_A)
class _FlowStatus_Type(Bits):namedValues=NamedValues(*(('operStat',0),('adminStatDown',1),('ingressOperStatNotUp',2),('egressOperStatNotUp',3),('test',4),('lackOfResources',5),('cfmOamFailure',6),('y1564Test',7),('rfc2544Test',8),('mef46Loop',9)))
_FlowStatus_Type.__name__=_F
_FlowStatus_Object=MibTableColumn
flowStatus=_FlowStatus_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,47),_FlowStatus_Type())
flowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:flowStatus.setStatus(_A)
class _FlowServiceIdName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FlowServiceIdName_Type.__name__=_J
_FlowServiceIdName_Object=MibTableColumn
flowServiceIdName=_FlowServiceIdName_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,49),_FlowServiceIdName_Type())
flowServiceIdName.setMaxAccess(_B)
if mibBuilder.loadTexts:flowServiceIdName.setStatus(_A)
class _FlowPolicerType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),('regular',2),('aggregate',3),('envelope',4),('regularAccountingOnly',5)))
_FlowPolicerType_Type.__name__=_C
_FlowPolicerType_Object=MibTableColumn
flowPolicerType=_FlowPolicerType_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,51),_FlowPolicerType_Type())
flowPolicerType.setMaxAccess(_B)
if mibBuilder.loadTexts:flowPolicerType.setStatus(_A)
class _FlowMultiCosCounters_Type(Bits):defaultBinValue='1';namedValues=NamedValues(*(('cos0',0),('cos1',1),('cos2',2),('cos3',3),('cos4',4),('cos5',5),('cos6',6),('cos7',7)))
_FlowMultiCosCounters_Type.__name__=_F
_FlowMultiCosCounters_Object=MibTableColumn
flowMultiCosCounters=_FlowMultiCosCounters_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,52),_FlowMultiCosCounters_Type())
flowMultiCosCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:flowMultiCosCounters.setStatus(_A)
class _FlowClassifierType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('flowClassifier',1),('portClassifier',2)))
_FlowClassifierType_Type.__name__=_C
_FlowClassifierType_Object=MibTableColumn
flowClassifierType=_FlowClassifierType_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,53),_FlowClassifierType_Type())
flowClassifierType.setMaxAccess(_B)
if mibBuilder.loadTexts:flowClassifierType.setStatus(_A)
_FlowIngressPortClassifier_Type=InterfaceIndexOrZero
_FlowIngressPortClassifier_Object=MibTableColumn
flowIngressPortClassifier=_FlowIngressPortClassifier_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,54),_FlowIngressPortClassifier_Type())
flowIngressPortClassifier.setMaxAccess(_I)
if mibBuilder.loadTexts:flowIngressPortClassifier.setStatus(_A)
class _FlowDscpMarkingProfile_Type(Unsigned32):defaultValue=0
_FlowDscpMarkingProfile_Type.__name__=_H
_FlowDscpMarkingProfile_Object=MibTableColumn
flowDscpMarkingProfile=_FlowDscpMarkingProfile_Object((1,3,6,1,4,1,164,20,8,1,6,3,1,55),_FlowDscpMarkingProfile_Type())
flowDscpMarkingProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:flowDscpMarkingProfile.setStatus(_A)
_FlowMapping_ObjectIdentity=ObjectIdentity
flowMapping=_FlowMapping_ObjectIdentity((1,3,6,1,4,1,164,20,8,1,6,4))
_ServiceIdTable_Object=MibTable
serviceIdTable=_ServiceIdTable_Object((1,3,6,1,4,1,164,20,8,1,6,4,2))
if mibBuilder.loadTexts:serviceIdTable.setStatus(_A)
_ServiceIdEntry_Object=MibTableRow
serviceIdEntry=_ServiceIdEntry_Object((1,3,6,1,4,1,164,20,8,1,6,4,2,1))
serviceIdEntry.setIndexNames((0,_D,_R),(1,_D,_o))
if mibBuilder.loadTexts:serviceIdEntry.setStatus(_A)
class _ServiceIdName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ServiceIdName_Type.__name__=_J
_ServiceIdName_Object=MibTableColumn
serviceIdName=_ServiceIdName_Object((1,3,6,1,4,1,164,20,8,1,6,4,2,1,1),_ServiceIdName_Type())
serviceIdName.setMaxAccess(_E)
if mibBuilder.loadTexts:serviceIdName.setStatus(_A)
_ServiceIdRowPointer_Type=RowPointer
_ServiceIdRowPointer_Object=MibTableColumn
serviceIdRowPointer=_ServiceIdRowPointer_Object((1,3,6,1,4,1,164,20,8,1,6,4,2,1,2),_ServiceIdRowPointer_Type())
serviceIdRowPointer.setMaxAccess(_E)
if mibBuilder.loadTexts:serviceIdRowPointer.setStatus(_A)
class _ServiceIdEntityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('flow',1),('erpVlan',2),('ma',3)))
_ServiceIdEntityType_Type.__name__=_C
_ServiceIdEntityType_Object=MibTableColumn
serviceIdEntityType=_ServiceIdEntityType_Object((1,3,6,1,4,1,164,20,8,1,6,4,2,1,3),_ServiceIdEntityType_Type())
serviceIdEntityType.setMaxAccess(_I)
if mibBuilder.loadTexts:serviceIdEntityType.setStatus(_A)
_ServiceIdRowStatus_Type=RowStatus
_ServiceIdRowStatus_Object=MibTableColumn
serviceIdRowStatus=_ServiceIdRowStatus_Object((1,3,6,1,4,1,164,20,8,1,6,4,2,1,5),_ServiceIdRowStatus_Type())
serviceIdRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:serviceIdRowStatus.setStatus(_A)
_ServiceIdCmdTable_Object=MibTable
serviceIdCmdTable=_ServiceIdCmdTable_Object((1,3,6,1,4,1,164,20,8,1,6,4,3))
if mibBuilder.loadTexts:serviceIdCmdTable.setStatus(_A)
_ServiceIdCmdEntry_Object=MibTableRow
serviceIdCmdEntry=_ServiceIdCmdEntry_Object((1,3,6,1,4,1,164,20,8,1,6,4,3,1))
serviceIdCmdEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:serviceIdCmdEntry.setStatus(_A)
_ServiceIdCmdRowStatus_Type=RowStatus
_ServiceIdCmdRowStatus_Object=MibTableColumn
serviceIdCmdRowStatus=_ServiceIdCmdRowStatus_Object((1,3,6,1,4,1,164,20,8,1,6,4,3,1,1),_ServiceIdCmdRowStatus_Type())
serviceIdCmdRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:serviceIdCmdRowStatus.setStatus(_A)
_ServiceIdCmdVlan_Type=Unsigned32
_ServiceIdCmdVlan_Object=MibTableColumn
serviceIdCmdVlan=_ServiceIdCmdVlan_Object((1,3,6,1,4,1,164,20,8,1,6,4,3,1,2),_ServiceIdCmdVlan_Type())
serviceIdCmdVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:serviceIdCmdVlan.setStatus(_A)
_ServiceIdCmdInnerVlan_Type=Unsigned32
_ServiceIdCmdInnerVlan_Object=MibTableColumn
serviceIdCmdInnerVlan=_ServiceIdCmdInnerVlan_Object((1,3,6,1,4,1,164,20,8,1,6,4,3,1,3),_ServiceIdCmdInnerVlan_Type())
serviceIdCmdInnerVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:serviceIdCmdInnerVlan.setStatus(_A)
_ServiceIdCmdPortIdx_Type=Unsigned32
_ServiceIdCmdPortIdx_Object=MibTableColumn
serviceIdCmdPortIdx=_ServiceIdCmdPortIdx_Object((1,3,6,1,4,1,164,20,8,1,6,4,3,1,4),_ServiceIdCmdPortIdx_Type())
serviceIdCmdPortIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:serviceIdCmdPortIdx.setStatus(_A)
_PmFlowCmdTable_Object=MibTable
pmFlowCmdTable=_PmFlowCmdTable_Object((1,3,6,1,4,1,164,20,8,1,6,6))
if mibBuilder.loadTexts:pmFlowCmdTable.setStatus(_A)
_PmFlowCmdEntry_Object=MibTableRow
pmFlowCmdEntry=_PmFlowCmdEntry_Object((1,3,6,1,4,1,164,20,8,1,6,6,1))
pmFlowCmdEntry.setIndexNames((0,_D,_p))
if mibBuilder.loadTexts:pmFlowCmdEntry.setStatus(_A)
_PmFlowCmdIndex_Type=Unsigned32
_PmFlowCmdIndex_Object=MibTableColumn
pmFlowCmdIndex=_PmFlowCmdIndex_Object((1,3,6,1,4,1,164,20,8,1,6,6,1,1),_PmFlowCmdIndex_Type())
pmFlowCmdIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pmFlowCmdIndex.setStatus(_A)
class _PmFlowCmdWithOAMTraffic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('yes',2),('no',3)))
_PmFlowCmdWithOAMTraffic_Type.__name__=_C
_PmFlowCmdWithOAMTraffic_Object=MibTableColumn
pmFlowCmdWithOAMTraffic=_PmFlowCmdWithOAMTraffic_Object((1,3,6,1,4,1,164,20,8,1,6,6,1,2),_PmFlowCmdWithOAMTraffic_Type())
pmFlowCmdWithOAMTraffic.setMaxAccess(_L)
if mibBuilder.loadTexts:pmFlowCmdWithOAMTraffic.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'TCVlanId':TCVlanId,'TCBurstSizeV2':TCBurstSizeV2,'TCV2DefaultUserPriority':TCV2DefaultUserPriority,'TCEthFrameHandling':TCEthFrameHandling,'TCSLAPrioritySource':TCSLAPrioritySource,'TCEvcId':TCEvcId,'TCVTIdV2':TCVTIdV2,'mefMIBR':mefMIBR,'mefObjects':mefObjects,'mefrScalarObjects':mefrScalarObjects,'mefrBwRoundUp':mefrBwRoundUp,'mefrEnvelopeRanks':mefrEnvelopeRanks,'hsQBlockMapping':hsQBlockMapping,'bwProfileObjects':bwProfileObjects,'bwProfileTable':bwProfileTable,'bwProfileEntry':bwProfileEntry,_V:bwProfileID,_W:bwProfileIndex,'bwProfileRowStatus':bwProfileRowStatus,'bwProfileCIR':bwProfileCIR,'bwProfileCBS':bwProfileCBS,'bwProfileEIR':bwProfileEIR,'bwProfileEBS':bwProfileEBS,'bwProfileColorAware':bwProfileColorAware,'bwProfileColorAwareAdmissionOption':bwProfileColorAwareAdmissionOption,'bwProfileName':bwProfileName,'bwProfileGranularity':bwProfileGranularity,'bwProfilePolicedTraffic':bwProfilePolicedTraffic,'bwProfileCompensation':bwProfileCompensation,'envelopeBwProfileTable':envelopeBwProfileTable,'envelopeBwProfileEntry':envelopeBwProfileEntry,_P:envelopeBwProfileIndex,'envelopeBwProfileName':envelopeBwProfileName,'envelopeBwProfileRowStatus':envelopeBwProfileRowStatus,'envelopeBwProfileCouplingFlagPolicy':envelopeBwProfileCouplingFlagPolicy,'envelopeBwProfileCouplingFlag0':envelopeBwProfileCouplingFlag0,'envelopeBwProfileColorMode':envelopeBwProfileColorMode,'envelopeBwProfileCompensation':envelopeBwProfileCompensation,'envelopeBwProfileCosTable':envelopeBwProfileCosTable,'envelopeBwProfileCosEntry':envelopeBwProfileCosEntry,_X:envelopeBwProfileCosIndex,'envelopeBwProfileCosRowStatus':envelopeBwProfileCosRowStatus,'envelopeBwProfileCosCir':envelopeBwProfileCosCir,'envelopeBwProfileCosCirMax':envelopeBwProfileCosCirMax,'envelopeBwProfileCosCbs':envelopeBwProfileCosCbs,'envelopeBwProfileCosEir':envelopeBwProfileCosEir,'envelopeBwProfileCosEirMax':envelopeBwProfileCosEirMax,'envelopeBwProfileCosEbs':envelopeBwProfileCosEbs,'envelopeBwProfileCoSCouplingFlag':envelopeBwProfileCoSCouplingFlag,'cPObjects':cPObjects,'cPProfileTable':cPProfileTable,'cPProfileEntry':cPProfileEntry,_Y:cPProfileIndex,_Z:cPProfileRunningIndex,'cPProfileRowStatus':cPProfileRowStatus,'cPProfileMacAddress':cPProfileMacAddress,'cPProfileMacProcessing':cPProfileMacProcessing,'cPProfileName':cPProfileName,'cPProfileProtocol':cPProfileProtocol,'l2cpStatTable':l2cpStatTable,'l2cpStatEntry':l2cpStatEntry,_c:l2cpStatPortIndex,_d:l2cpStatProtocol,_e:l2cpStatMacAddress,'l2cpStatEncapsulatedFrames':l2cpStatEncapsulatedFrames,'l2cpStatDecapsulatedFrames':l2cpStatDecapsulatedFrames,'uniObjects':uniObjects,'uniTable':uniTable,'uniEntry':uniEntry,_f:uniRunningIndex,'uniRowStatus':uniRowStatus,'uniLayer2CPProcessingProfile':uniLayer2CPProcessingProfile,'uniPerUniBWprofile':uniPerUniBWprofile,'uniSpTagProtocolIdentifier':uniSpTagProtocolIdentifier,'uniPacketColoring':uniPacketColoring,'uniPerUniEgressAction':uniPerUniEgressAction,'uniQueueGroupName':uniQueueGroupName,'uniClassifierKey':uniClassifierKey,'evcObjects':evcObjects,'flowTable':flowTable,'flowEntry':flowEntry,_g:flowIdx1,_h:flowIdx2,'flowName':flowName,'flowRowStatus':flowRowStatus,'flowBWprofile':flowBWprofile,'flowFixedCos':flowFixedCos,'flowCOSProfile':flowCOSProfile,'flowQBlock':flowQBlock,'flowMappingProfile':flowMappingProfile,'flowFixedMarking':flowFixedMarking,'flowMarkingProfile':flowMarkingProfile,'flowOuterVlanTagging':flowOuterVlanTagging,'flowOuterVlan':flowOuterVlan,'flowInnerVlanTagging':flowInnerVlanTagging,'flowInnerVlan':flowInnerVlan,'flowEgressPort':flowEgressPort,'flowIngressPort':flowIngressPort,'flowInnerFixedMarking':flowInnerFixedMarking,'flowInnerMarkingProfile':flowInnerMarkingProfile,'flowDropAction':flowDropAction,'flowPriority':flowPriority,'flowMarkOuterFixedMarking':flowMarkOuterFixedMarking,'flowMarkOuterMarkingProfile':flowMarkOuterMarkingProfile,'flowMarkInnerFixedMarking':flowMarkInnerFixedMarking,'flowMarkInnerMarkingProfile':flowMarkInnerMarkingProfile,'flowMarkOuterVlanTagging':flowMarkOuterVlanTagging,'flowMarkOuterVlan':flowMarkOuterVlan,'flowMarkInnerVlanTagging':flowMarkInnerVlanTagging,'flowMarkInnerVlan':flowMarkInnerVlan,'flowPolicerAggregate':flowPolicerAggregate,'flowMarkMacTagging':flowMarkMacTagging,'flowMarkIpTagging':flowMarkIpTagging,'flowLayer2CPProcessingProfile':flowLayer2CPProcessingProfile,'flowIngressColorMapping':flowIngressColorMapping,'flowIngressColorProfile':flowIngressColorProfile,'flowCosMapping':flowCosMapping,'flowCosMappingProfile':flowCosMappingProfile,'flowStatus':flowStatus,'flowServiceIdName':flowServiceIdName,'flowPolicerType':flowPolicerType,'flowMultiCosCounters':flowMultiCosCounters,'flowClassifierType':flowClassifierType,'flowIngressPortClassifier':flowIngressPortClassifier,'flowDscpMarkingProfile':flowDscpMarkingProfile,'flowMapping':flowMapping,'serviceIdTable':serviceIdTable,'serviceIdEntry':serviceIdEntry,_R:serviceIdName,_o:serviceIdRowPointer,'serviceIdEntityType':serviceIdEntityType,'serviceIdRowStatus':serviceIdRowStatus,'serviceIdCmdTable':serviceIdCmdTable,'serviceIdCmdEntry':serviceIdCmdEntry,'serviceIdCmdRowStatus':serviceIdCmdRowStatus,'serviceIdCmdVlan':serviceIdCmdVlan,'serviceIdCmdInnerVlan':serviceIdCmdInnerVlan,'serviceIdCmdPortIdx':serviceIdCmdPortIdx,'pmFlowCmdTable':pmFlowCmdTable,'pmFlowCmdEntry':pmFlowCmdEntry,_p:pmFlowCmdIndex,'pmFlowCmdWithOAMTraffic':pmFlowCmdWithOAMTraffic})