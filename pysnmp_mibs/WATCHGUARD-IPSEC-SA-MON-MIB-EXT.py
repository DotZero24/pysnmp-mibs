_T='wgIpsecSaIpcompOutCpi'
_S='wgIpsecSaIpcompOutAddress'
_R='wgIpsecSaAhOutSpi'
_Q='wgIpsecSaAhOutAddress'
_P='wgIpsecSaEspOutSpi'
_O='wgIpsecSaEspOutAddress'
_N='wgIpsecSaIpcompInCpi'
_M='wgIpsecSaIpcompInAddress'
_L='wgIpsecSaAhInSpi'
_K='wgIpsecSaAhInAddress'
_J='wgIpsecSaEspInSpi'
_I='wgIpsecSaEspInAddress'
_H='bytes'
_G='kilobytes'
_F='seconds'
_E='WATCHGUARD-IPSEC-SA-MON-MIB-EXT'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
IpsecDoiAhTransform,IpsecDoiAuthAlgorithm,IpsecDoiEncapsulationMode,IpsecDoiEspTransform,IpsecDoiIdentType,IpsecDoiIpcompTransform,IpsecDoiSecProtocolId=mibBuilder.importSymbols('IPSEC-ISAKMP-IKE-DOI-TC','IpsecDoiAhTransform','IpsecDoiAuthAlgorithm','IpsecDoiEncapsulationMode','IpsecDoiEspTransform','IpsecDoiIdentType','IpsecDoiIpcompTransform','IpsecDoiSecProtocolId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
watchguard,=mibBuilder.importSymbols('WATCHGUARD-SMI','watchguard')
wgIpsecSaMonModule=ModuleIdentity((1,3,6,1,4,1,3097,3))
if mibBuilder.loadTexts:wgIpsecSaMonModule.setRevisions(('2007-01-25 12:00',))
class IpsecSaCreatorIdent(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('static',1),('ike',2),('other',3)))
class IpsecIpv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:2x:2x:2x:2x:2x:1d.1d.1d.1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_WgIpsecSaMonitorMIB_ObjectIdentity=ObjectIdentity
wgIpsecSaMonitorMIB=_WgIpsecSaMonitorMIB_ObjectIdentity((1,3,6,1,4,1,3097,3,1))
if mibBuilder.loadTexts:wgIpsecSaMonitorMIB.setStatus(_A)
_WgSaTables_ObjectIdentity=ObjectIdentity
wgSaTables=_WgSaTables_ObjectIdentity((1,3,6,1,4,1,3097,3,1,1))
if mibBuilder.loadTexts:wgSaTables.setStatus(_A)
_WgIpsecSaEspInTable_Object=MibTable
wgIpsecSaEspInTable=_WgIpsecSaEspInTable_Object((1,3,6,1,4,1,3097,3,1,1,1))
if mibBuilder.loadTexts:wgIpsecSaEspInTable.setStatus(_A)
_WgIpsecSaEspInEntry_Object=MibTableRow
wgIpsecSaEspInEntry=_WgIpsecSaEspInEntry_Object((1,3,6,1,4,1,3097,3,1,1,1,1))
wgIpsecSaEspInEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:wgIpsecSaEspInEntry.setStatus(_A)
_WgIpsecSaEspInAddress_Type=IpAddress
_WgIpsecSaEspInAddress_Object=MibTableColumn
wgIpsecSaEspInAddress=_WgIpsecSaEspInAddress_Object((1,3,6,1,4,1,3097,3,1,1,1,1,1),_WgIpsecSaEspInAddress_Type())
wgIpsecSaEspInAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInAddress.setStatus(_A)
_WgIpsecSaEspInSpi_Type=Unsigned32
_WgIpsecSaEspInSpi_Object=MibTableColumn
wgIpsecSaEspInSpi=_WgIpsecSaEspInSpi_Object((1,3,6,1,4,1,3097,3,1,1,1,1,2),_WgIpsecSaEspInSpi_Type())
wgIpsecSaEspInSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInSpi.setStatus(_A)
class _WgIpsecSaEspInDestId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_WgIpsecSaEspInDestId_Type.__name__=_D
_WgIpsecSaEspInDestId_Object=MibTableColumn
wgIpsecSaEspInDestId=_WgIpsecSaEspInDestId_Object((1,3,6,1,4,1,3097,3,1,1,1,1,3),_WgIpsecSaEspInDestId_Type())
wgIpsecSaEspInDestId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInDestId.setStatus(_A)
_WgIpsecSaEspInDestIdType_Type=IpsecDoiIdentType
_WgIpsecSaEspInDestIdType_Object=MibTableColumn
wgIpsecSaEspInDestIdType=_WgIpsecSaEspInDestIdType_Object((1,3,6,1,4,1,3097,3,1,1,1,1,4),_WgIpsecSaEspInDestIdType_Type())
wgIpsecSaEspInDestIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInDestIdType.setStatus(_A)
class _WgIpsecSaEspInSourceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_WgIpsecSaEspInSourceId_Type.__name__=_D
_WgIpsecSaEspInSourceId_Object=MibTableColumn
wgIpsecSaEspInSourceId=_WgIpsecSaEspInSourceId_Object((1,3,6,1,4,1,3097,3,1,1,1,1,5),_WgIpsecSaEspInSourceId_Type())
wgIpsecSaEspInSourceId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInSourceId.setStatus(_A)
_WgIpsecSaEspInSourceIdType_Type=IpsecDoiIdentType
_WgIpsecSaEspInSourceIdType_Object=MibTableColumn
wgIpsecSaEspInSourceIdType=_WgIpsecSaEspInSourceIdType_Object((1,3,6,1,4,1,3097,3,1,1,1,1,6),_WgIpsecSaEspInSourceIdType_Type())
wgIpsecSaEspInSourceIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInSourceIdType.setStatus(_A)
class _WgIpsecSaEspInProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WgIpsecSaEspInProtocol_Type.__name__=_C
_WgIpsecSaEspInProtocol_Object=MibTableColumn
wgIpsecSaEspInProtocol=_WgIpsecSaEspInProtocol_Object((1,3,6,1,4,1,3097,3,1,1,1,1,7),_WgIpsecSaEspInProtocol_Type())
wgIpsecSaEspInProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInProtocol.setStatus(_A)
class _WgIpsecSaEspInDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecSaEspInDestPort_Type.__name__=_C
_WgIpsecSaEspInDestPort_Object=MibTableColumn
wgIpsecSaEspInDestPort=_WgIpsecSaEspInDestPort_Object((1,3,6,1,4,1,3097,3,1,1,1,1,8),_WgIpsecSaEspInDestPort_Type())
wgIpsecSaEspInDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInDestPort.setStatus(_A)
class _WgIpsecSaEspInSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecSaEspInSourcePort_Type.__name__=_C
_WgIpsecSaEspInSourcePort_Object=MibTableColumn
wgIpsecSaEspInSourcePort=_WgIpsecSaEspInSourcePort_Object((1,3,6,1,4,1,3097,3,1,1,1,1,9),_WgIpsecSaEspInSourcePort_Type())
wgIpsecSaEspInSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInSourcePort.setStatus(_A)
_WgIpsecSaEspInCreator_Type=IpsecSaCreatorIdent
_WgIpsecSaEspInCreator_Object=MibTableColumn
wgIpsecSaEspInCreator=_WgIpsecSaEspInCreator_Object((1,3,6,1,4,1,3097,3,1,1,1,1,10),_WgIpsecSaEspInCreator_Type())
wgIpsecSaEspInCreator.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInCreator.setStatus(_A)
_WgIpsecSaEspInEncapsulation_Type=IpsecDoiEncapsulationMode
_WgIpsecSaEspInEncapsulation_Object=MibTableColumn
wgIpsecSaEspInEncapsulation=_WgIpsecSaEspInEncapsulation_Object((1,3,6,1,4,1,3097,3,1,1,1,1,11),_WgIpsecSaEspInEncapsulation_Type())
wgIpsecSaEspInEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInEncapsulation.setStatus(_A)
_WgIpsecSaEspInEncAlg_Type=IpsecDoiEspTransform
_WgIpsecSaEspInEncAlg_Object=MibTableColumn
wgIpsecSaEspInEncAlg=_WgIpsecSaEspInEncAlg_Object((1,3,6,1,4,1,3097,3,1,1,1,1,12),_WgIpsecSaEspInEncAlg_Type())
wgIpsecSaEspInEncAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInEncAlg.setStatus(_A)
class _WgIpsecSaEspInEncKeyLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65531))
_WgIpsecSaEspInEncKeyLength_Type.__name__=_C
_WgIpsecSaEspInEncKeyLength_Object=MibTableColumn
wgIpsecSaEspInEncKeyLength=_WgIpsecSaEspInEncKeyLength_Object((1,3,6,1,4,1,3097,3,1,1,1,1,13),_WgIpsecSaEspInEncKeyLength_Type())
wgIpsecSaEspInEncKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInEncKeyLength.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaEspInEncKeyLength.setUnits('bits')
_WgIpsecSaEspInAuthAlg_Type=IpsecDoiAuthAlgorithm
_WgIpsecSaEspInAuthAlg_Object=MibTableColumn
wgIpsecSaEspInAuthAlg=_WgIpsecSaEspInAuthAlg_Object((1,3,6,1,4,1,3097,3,1,1,1,1,14),_WgIpsecSaEspInAuthAlg_Type())
wgIpsecSaEspInAuthAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInAuthAlg.setStatus(_A)
_WgIpsecSaEspInLimitSeconds_Type=Integer32
_WgIpsecSaEspInLimitSeconds_Object=MibTableColumn
wgIpsecSaEspInLimitSeconds=_WgIpsecSaEspInLimitSeconds_Object((1,3,6,1,4,1,3097,3,1,1,1,1,15),_WgIpsecSaEspInLimitSeconds_Type())
wgIpsecSaEspInLimitSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInLimitSeconds.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaEspInLimitSeconds.setUnits(_F)
_WgIpsecSaEspInLimitKbytes_Type=Integer32
_WgIpsecSaEspInLimitKbytes_Object=MibTableColumn
wgIpsecSaEspInLimitKbytes=_WgIpsecSaEspInLimitKbytes_Object((1,3,6,1,4,1,3097,3,1,1,1,1,16),_WgIpsecSaEspInLimitKbytes_Type())
wgIpsecSaEspInLimitKbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInLimitKbytes.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaEspInLimitKbytes.setUnits(_G)
_WgIpsecSaEspInAccSeconds_Type=Counter32
_WgIpsecSaEspInAccSeconds_Object=MibTableColumn
wgIpsecSaEspInAccSeconds=_WgIpsecSaEspInAccSeconds_Object((1,3,6,1,4,1,3097,3,1,1,1,1,17),_WgIpsecSaEspInAccSeconds_Type())
wgIpsecSaEspInAccSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInAccSeconds.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaEspInAccSeconds.setUnits(_F)
_WgIpsecSaEspInAccKbytes_Type=Counter64
_WgIpsecSaEspInAccKbytes_Object=MibTableColumn
wgIpsecSaEspInAccKbytes=_WgIpsecSaEspInAccKbytes_Object((1,3,6,1,4,1,3097,3,1,1,1,1,18),_WgIpsecSaEspInAccKbytes_Type())
wgIpsecSaEspInAccKbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInAccKbytes.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaEspInAccKbytes.setUnits(_G)
_WgIpsecSaEspInUserOctets_Type=Counter32
_WgIpsecSaEspInUserOctets_Object=MibTableColumn
wgIpsecSaEspInUserOctets=_WgIpsecSaEspInUserOctets_Object((1,3,6,1,4,1,3097,3,1,1,1,1,19),_WgIpsecSaEspInUserOctets_Type())
wgIpsecSaEspInUserOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInUserOctets.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaEspInUserOctets.setUnits(_H)
_WgIpsecSaEspInPackets_Type=Counter64
_WgIpsecSaEspInPackets_Object=MibTableColumn
wgIpsecSaEspInPackets=_WgIpsecSaEspInPackets_Object((1,3,6,1,4,1,3097,3,1,1,1,1,20),_WgIpsecSaEspInPackets_Type())
wgIpsecSaEspInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInPackets.setStatus(_A)
_WgIpsecSaEspInDecryptErrors_Type=Counter32
_WgIpsecSaEspInDecryptErrors_Object=MibTableColumn
wgIpsecSaEspInDecryptErrors=_WgIpsecSaEspInDecryptErrors_Object((1,3,6,1,4,1,3097,3,1,1,1,1,21),_WgIpsecSaEspInDecryptErrors_Type())
wgIpsecSaEspInDecryptErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInDecryptErrors.setStatus(_A)
_WgIpsecSaEspInAuthErrors_Type=Counter32
_WgIpsecSaEspInAuthErrors_Object=MibTableColumn
wgIpsecSaEspInAuthErrors=_WgIpsecSaEspInAuthErrors_Object((1,3,6,1,4,1,3097,3,1,1,1,1,22),_WgIpsecSaEspInAuthErrors_Type())
wgIpsecSaEspInAuthErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInAuthErrors.setStatus(_A)
_WgIpsecSaEspInReplayErrors_Type=Counter32
_WgIpsecSaEspInReplayErrors_Object=MibTableColumn
wgIpsecSaEspInReplayErrors=_WgIpsecSaEspInReplayErrors_Object((1,3,6,1,4,1,3097,3,1,1,1,1,23),_WgIpsecSaEspInReplayErrors_Type())
wgIpsecSaEspInReplayErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInReplayErrors.setStatus(_A)
_WgIpsecSaEspInPolicyErrors_Type=Counter32
_WgIpsecSaEspInPolicyErrors_Object=MibTableColumn
wgIpsecSaEspInPolicyErrors=_WgIpsecSaEspInPolicyErrors_Object((1,3,6,1,4,1,3097,3,1,1,1,1,24),_WgIpsecSaEspInPolicyErrors_Type())
wgIpsecSaEspInPolicyErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInPolicyErrors.setStatus(_A)
_WgIpsecSaEspInPadErrors_Type=Counter32
_WgIpsecSaEspInPadErrors_Object=MibTableColumn
wgIpsecSaEspInPadErrors=_WgIpsecSaEspInPadErrors_Object((1,3,6,1,4,1,3097,3,1,1,1,1,25),_WgIpsecSaEspInPadErrors_Type())
wgIpsecSaEspInPadErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInPadErrors.setStatus(_A)
_WgIpsecSaEspInOtherReceiveErrors_Type=Counter32
_WgIpsecSaEspInOtherReceiveErrors_Object=MibTableColumn
wgIpsecSaEspInOtherReceiveErrors=_WgIpsecSaEspInOtherReceiveErrors_Object((1,3,6,1,4,1,3097,3,1,1,1,1,26),_WgIpsecSaEspInOtherReceiveErrors_Type())
wgIpsecSaEspInOtherReceiveErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspInOtherReceiveErrors.setStatus(_A)
_WgIpsecSaAhInTable_Object=MibTable
wgIpsecSaAhInTable=_WgIpsecSaAhInTable_Object((1,3,6,1,4,1,3097,3,1,1,2))
if mibBuilder.loadTexts:wgIpsecSaAhInTable.setStatus(_A)
_WgIpsecSaAhInEntry_Object=MibTableRow
wgIpsecSaAhInEntry=_WgIpsecSaAhInEntry_Object((1,3,6,1,4,1,3097,3,1,1,2,1))
wgIpsecSaAhInEntry.setIndexNames((0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:wgIpsecSaAhInEntry.setStatus(_A)
_WgIpsecSaAhInAddress_Type=IpAddress
_WgIpsecSaAhInAddress_Object=MibTableColumn
wgIpsecSaAhInAddress=_WgIpsecSaAhInAddress_Object((1,3,6,1,4,1,3097,3,1,1,2,1,1),_WgIpsecSaAhInAddress_Type())
wgIpsecSaAhInAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInAddress.setStatus(_A)
_WgIpsecSaAhInSpi_Type=Integer32
_WgIpsecSaAhInSpi_Object=MibTableColumn
wgIpsecSaAhInSpi=_WgIpsecSaAhInSpi_Object((1,3,6,1,4,1,3097,3,1,1,2,1,2),_WgIpsecSaAhInSpi_Type())
wgIpsecSaAhInSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInSpi.setStatus(_A)
class _WgIpsecSaAhInDestId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_WgIpsecSaAhInDestId_Type.__name__=_D
_WgIpsecSaAhInDestId_Object=MibTableColumn
wgIpsecSaAhInDestId=_WgIpsecSaAhInDestId_Object((1,3,6,1,4,1,3097,3,1,1,2,1,3),_WgIpsecSaAhInDestId_Type())
wgIpsecSaAhInDestId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInDestId.setStatus(_A)
_WgIpsecSaAhInDestIdType_Type=IpsecDoiIdentType
_WgIpsecSaAhInDestIdType_Object=MibTableColumn
wgIpsecSaAhInDestIdType=_WgIpsecSaAhInDestIdType_Object((1,3,6,1,4,1,3097,3,1,1,2,1,4),_WgIpsecSaAhInDestIdType_Type())
wgIpsecSaAhInDestIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInDestIdType.setStatus(_A)
class _WgIpsecSaAhInSourceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_WgIpsecSaAhInSourceId_Type.__name__=_D
_WgIpsecSaAhInSourceId_Object=MibTableColumn
wgIpsecSaAhInSourceId=_WgIpsecSaAhInSourceId_Object((1,3,6,1,4,1,3097,3,1,1,2,1,5),_WgIpsecSaAhInSourceId_Type())
wgIpsecSaAhInSourceId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInSourceId.setStatus(_A)
_WgIpsecSaAhInSourceIdType_Type=IpsecDoiIdentType
_WgIpsecSaAhInSourceIdType_Object=MibTableColumn
wgIpsecSaAhInSourceIdType=_WgIpsecSaAhInSourceIdType_Object((1,3,6,1,4,1,3097,3,1,1,2,1,6),_WgIpsecSaAhInSourceIdType_Type())
wgIpsecSaAhInSourceIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInSourceIdType.setStatus(_A)
class _WgIpsecSaAhInProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WgIpsecSaAhInProtocol_Type.__name__=_C
_WgIpsecSaAhInProtocol_Object=MibTableColumn
wgIpsecSaAhInProtocol=_WgIpsecSaAhInProtocol_Object((1,3,6,1,4,1,3097,3,1,1,2,1,7),_WgIpsecSaAhInProtocol_Type())
wgIpsecSaAhInProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInProtocol.setStatus(_A)
class _WgIpsecSaAhInDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecSaAhInDestPort_Type.__name__=_C
_WgIpsecSaAhInDestPort_Object=MibTableColumn
wgIpsecSaAhInDestPort=_WgIpsecSaAhInDestPort_Object((1,3,6,1,4,1,3097,3,1,1,2,1,8),_WgIpsecSaAhInDestPort_Type())
wgIpsecSaAhInDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInDestPort.setStatus(_A)
class _WgIpsecSaAhInSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecSaAhInSourcePort_Type.__name__=_C
_WgIpsecSaAhInSourcePort_Object=MibTableColumn
wgIpsecSaAhInSourcePort=_WgIpsecSaAhInSourcePort_Object((1,3,6,1,4,1,3097,3,1,1,2,1,9),_WgIpsecSaAhInSourcePort_Type())
wgIpsecSaAhInSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInSourcePort.setStatus(_A)
_WgIpsecSaAhInCreator_Type=IpsecSaCreatorIdent
_WgIpsecSaAhInCreator_Object=MibTableColumn
wgIpsecSaAhInCreator=_WgIpsecSaAhInCreator_Object((1,3,6,1,4,1,3097,3,1,1,2,1,10),_WgIpsecSaAhInCreator_Type())
wgIpsecSaAhInCreator.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInCreator.setStatus(_A)
_WgIpsecSaAhInEncapsulation_Type=IpsecDoiEncapsulationMode
_WgIpsecSaAhInEncapsulation_Object=MibTableColumn
wgIpsecSaAhInEncapsulation=_WgIpsecSaAhInEncapsulation_Object((1,3,6,1,4,1,3097,3,1,1,2,1,11),_WgIpsecSaAhInEncapsulation_Type())
wgIpsecSaAhInEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInEncapsulation.setStatus(_A)
_WgIpsecSaAhInAuthAlg_Type=IpsecDoiAhTransform
_WgIpsecSaAhInAuthAlg_Object=MibTableColumn
wgIpsecSaAhInAuthAlg=_WgIpsecSaAhInAuthAlg_Object((1,3,6,1,4,1,3097,3,1,1,2,1,12),_WgIpsecSaAhInAuthAlg_Type())
wgIpsecSaAhInAuthAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInAuthAlg.setStatus(_A)
_WgIpsecSaAhInLimitSeconds_Type=Integer32
_WgIpsecSaAhInLimitSeconds_Object=MibTableColumn
wgIpsecSaAhInLimitSeconds=_WgIpsecSaAhInLimitSeconds_Object((1,3,6,1,4,1,3097,3,1,1,2,1,13),_WgIpsecSaAhInLimitSeconds_Type())
wgIpsecSaAhInLimitSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInLimitSeconds.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaAhInLimitSeconds.setUnits(_F)
_WgIpsecSaAhInLimitKbytes_Type=Integer32
_WgIpsecSaAhInLimitKbytes_Object=MibTableColumn
wgIpsecSaAhInLimitKbytes=_WgIpsecSaAhInLimitKbytes_Object((1,3,6,1,4,1,3097,3,1,1,2,1,14),_WgIpsecSaAhInLimitKbytes_Type())
wgIpsecSaAhInLimitKbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInLimitKbytes.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaAhInLimitKbytes.setUnits(_G)
_WgIpsecSaAhInAccSeconds_Type=Counter32
_WgIpsecSaAhInAccSeconds_Object=MibTableColumn
wgIpsecSaAhInAccSeconds=_WgIpsecSaAhInAccSeconds_Object((1,3,6,1,4,1,3097,3,1,1,2,1,15),_WgIpsecSaAhInAccSeconds_Type())
wgIpsecSaAhInAccSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInAccSeconds.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaAhInAccSeconds.setUnits(_F)
_WgIpsecSaAhInAccKbytes_Type=Counter64
_WgIpsecSaAhInAccKbytes_Object=MibTableColumn
wgIpsecSaAhInAccKbytes=_WgIpsecSaAhInAccKbytes_Object((1,3,6,1,4,1,3097,3,1,1,2,1,16),_WgIpsecSaAhInAccKbytes_Type())
wgIpsecSaAhInAccKbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInAccKbytes.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaAhInAccKbytes.setUnits(_G)
_WgIpsecSaAhInUserOctets_Type=Counter32
_WgIpsecSaAhInUserOctets_Object=MibTableColumn
wgIpsecSaAhInUserOctets=_WgIpsecSaAhInUserOctets_Object((1,3,6,1,4,1,3097,3,1,1,2,1,17),_WgIpsecSaAhInUserOctets_Type())
wgIpsecSaAhInUserOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInUserOctets.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaAhInUserOctets.setUnits(_H)
_WgIpsecSaAhInPackets_Type=Counter64
_WgIpsecSaAhInPackets_Object=MibTableColumn
wgIpsecSaAhInPackets=_WgIpsecSaAhInPackets_Object((1,3,6,1,4,1,3097,3,1,1,2,1,18),_WgIpsecSaAhInPackets_Type())
wgIpsecSaAhInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInPackets.setStatus(_A)
_WgIpsecSaAhInAuthErrors_Type=Counter32
_WgIpsecSaAhInAuthErrors_Object=MibTableColumn
wgIpsecSaAhInAuthErrors=_WgIpsecSaAhInAuthErrors_Object((1,3,6,1,4,1,3097,3,1,1,2,1,19),_WgIpsecSaAhInAuthErrors_Type())
wgIpsecSaAhInAuthErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInAuthErrors.setStatus(_A)
_WgIpsecSaAhInReplayErrors_Type=Counter32
_WgIpsecSaAhInReplayErrors_Object=MibTableColumn
wgIpsecSaAhInReplayErrors=_WgIpsecSaAhInReplayErrors_Object((1,3,6,1,4,1,3097,3,1,1,2,1,20),_WgIpsecSaAhInReplayErrors_Type())
wgIpsecSaAhInReplayErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInReplayErrors.setStatus(_A)
_WgIpsecSaAhInPolicyErrors_Type=Counter32
_WgIpsecSaAhInPolicyErrors_Object=MibTableColumn
wgIpsecSaAhInPolicyErrors=_WgIpsecSaAhInPolicyErrors_Object((1,3,6,1,4,1,3097,3,1,1,2,1,21),_WgIpsecSaAhInPolicyErrors_Type())
wgIpsecSaAhInPolicyErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInPolicyErrors.setStatus(_A)
_WgIpsecSaAhInOtherReceiveErrors_Type=Counter32
_WgIpsecSaAhInOtherReceiveErrors_Object=MibTableColumn
wgIpsecSaAhInOtherReceiveErrors=_WgIpsecSaAhInOtherReceiveErrors_Object((1,3,6,1,4,1,3097,3,1,1,2,1,22),_WgIpsecSaAhInOtherReceiveErrors_Type())
wgIpsecSaAhInOtherReceiveErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhInOtherReceiveErrors.setStatus(_A)
_WgIpsecSaIpcompInTable_Object=MibTable
wgIpsecSaIpcompInTable=_WgIpsecSaIpcompInTable_Object((1,3,6,1,4,1,3097,3,1,1,3))
if mibBuilder.loadTexts:wgIpsecSaIpcompInTable.setStatus(_A)
_WgIpsecSaIpcompInEntry_Object=MibTableRow
wgIpsecSaIpcompInEntry=_WgIpsecSaIpcompInEntry_Object((1,3,6,1,4,1,3097,3,1,1,3,1))
wgIpsecSaIpcompInEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:wgIpsecSaIpcompInEntry.setStatus(_A)
_WgIpsecSaIpcompInAddress_Type=IpAddress
_WgIpsecSaIpcompInAddress_Object=MibTableColumn
wgIpsecSaIpcompInAddress=_WgIpsecSaIpcompInAddress_Object((1,3,6,1,4,1,3097,3,1,1,3,1,1),_WgIpsecSaIpcompInAddress_Type())
wgIpsecSaIpcompInAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInAddress.setStatus(_A)
_WgIpsecSaIpcompInCpi_Type=IpsecDoiIpcompTransform
_WgIpsecSaIpcompInCpi_Object=MibTableColumn
wgIpsecSaIpcompInCpi=_WgIpsecSaIpcompInCpi_Object((1,3,6,1,4,1,3097,3,1,1,3,1,2),_WgIpsecSaIpcompInCpi_Type())
wgIpsecSaIpcompInCpi.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInCpi.setStatus(_A)
class _WgIpsecSaIpcompInDestId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_WgIpsecSaIpcompInDestId_Type.__name__=_D
_WgIpsecSaIpcompInDestId_Object=MibTableColumn
wgIpsecSaIpcompInDestId=_WgIpsecSaIpcompInDestId_Object((1,3,6,1,4,1,3097,3,1,1,3,1,3),_WgIpsecSaIpcompInDestId_Type())
wgIpsecSaIpcompInDestId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInDestId.setStatus(_A)
_WgIpsecSaIpcompInDestIdType_Type=IpsecDoiIdentType
_WgIpsecSaIpcompInDestIdType_Object=MibTableColumn
wgIpsecSaIpcompInDestIdType=_WgIpsecSaIpcompInDestIdType_Object((1,3,6,1,4,1,3097,3,1,1,3,1,4),_WgIpsecSaIpcompInDestIdType_Type())
wgIpsecSaIpcompInDestIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInDestIdType.setStatus(_A)
class _WgIpsecSaIpcompInSourceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_WgIpsecSaIpcompInSourceId_Type.__name__=_D
_WgIpsecSaIpcompInSourceId_Object=MibTableColumn
wgIpsecSaIpcompInSourceId=_WgIpsecSaIpcompInSourceId_Object((1,3,6,1,4,1,3097,3,1,1,3,1,5),_WgIpsecSaIpcompInSourceId_Type())
wgIpsecSaIpcompInSourceId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInSourceId.setStatus(_A)
_WgIpsecSaIpcompInSourceIdType_Type=IpsecDoiIdentType
_WgIpsecSaIpcompInSourceIdType_Object=MibTableColumn
wgIpsecSaIpcompInSourceIdType=_WgIpsecSaIpcompInSourceIdType_Object((1,3,6,1,4,1,3097,3,1,1,3,1,6),_WgIpsecSaIpcompInSourceIdType_Type())
wgIpsecSaIpcompInSourceIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInSourceIdType.setStatus(_A)
class _WgIpsecSaIpcompInProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WgIpsecSaIpcompInProtocol_Type.__name__=_C
_WgIpsecSaIpcompInProtocol_Object=MibTableColumn
wgIpsecSaIpcompInProtocol=_WgIpsecSaIpcompInProtocol_Object((1,3,6,1,4,1,3097,3,1,1,3,1,7),_WgIpsecSaIpcompInProtocol_Type())
wgIpsecSaIpcompInProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInProtocol.setStatus(_A)
class _WgIpsecSaIpcompInDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecSaIpcompInDestPort_Type.__name__=_C
_WgIpsecSaIpcompInDestPort_Object=MibTableColumn
wgIpsecSaIpcompInDestPort=_WgIpsecSaIpcompInDestPort_Object((1,3,6,1,4,1,3097,3,1,1,3,1,8),_WgIpsecSaIpcompInDestPort_Type())
wgIpsecSaIpcompInDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInDestPort.setStatus(_A)
class _WgIpsecSaIpcompInSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecSaIpcompInSourcePort_Type.__name__=_C
_WgIpsecSaIpcompInSourcePort_Object=MibTableColumn
wgIpsecSaIpcompInSourcePort=_WgIpsecSaIpcompInSourcePort_Object((1,3,6,1,4,1,3097,3,1,1,3,1,9),_WgIpsecSaIpcompInSourcePort_Type())
wgIpsecSaIpcompInSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInSourcePort.setStatus(_A)
_WgIpsecSaIpcompInCreator_Type=IpsecSaCreatorIdent
_WgIpsecSaIpcompInCreator_Object=MibTableColumn
wgIpsecSaIpcompInCreator=_WgIpsecSaIpcompInCreator_Object((1,3,6,1,4,1,3097,3,1,1,3,1,10),_WgIpsecSaIpcompInCreator_Type())
wgIpsecSaIpcompInCreator.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInCreator.setStatus(_A)
_WgIpsecSaIpcompInEncapsulation_Type=IpsecDoiEncapsulationMode
_WgIpsecSaIpcompInEncapsulation_Object=MibTableColumn
wgIpsecSaIpcompInEncapsulation=_WgIpsecSaIpcompInEncapsulation_Object((1,3,6,1,4,1,3097,3,1,1,3,1,11),_WgIpsecSaIpcompInEncapsulation_Type())
wgIpsecSaIpcompInEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInEncapsulation.setStatus(_A)
_WgIpsecSaIpcompInDecompAlg_Type=IpsecDoiIpcompTransform
_WgIpsecSaIpcompInDecompAlg_Object=MibTableColumn
wgIpsecSaIpcompInDecompAlg=_WgIpsecSaIpcompInDecompAlg_Object((1,3,6,1,4,1,3097,3,1,1,3,1,12),_WgIpsecSaIpcompInDecompAlg_Type())
wgIpsecSaIpcompInDecompAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInDecompAlg.setStatus(_A)
_WgIpsecSaIpcompInSeconds_Type=Counter32
_WgIpsecSaIpcompInSeconds_Object=MibTableColumn
wgIpsecSaIpcompInSeconds=_WgIpsecSaIpcompInSeconds_Object((1,3,6,1,4,1,3097,3,1,1,3,1,13),_WgIpsecSaIpcompInSeconds_Type())
wgIpsecSaIpcompInSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInSeconds.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaIpcompInSeconds.setUnits(_F)
_WgIpsecSaIpcompInUserOctets_Type=Counter32
_WgIpsecSaIpcompInUserOctets_Object=MibTableColumn
wgIpsecSaIpcompInUserOctets=_WgIpsecSaIpcompInUserOctets_Object((1,3,6,1,4,1,3097,3,1,1,3,1,14),_WgIpsecSaIpcompInUserOctets_Type())
wgIpsecSaIpcompInUserOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInUserOctets.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaIpcompInUserOctets.setUnits(_H)
_WgIpsecSaIpcompInPackets_Type=Counter32
_WgIpsecSaIpcompInPackets_Object=MibTableColumn
wgIpsecSaIpcompInPackets=_WgIpsecSaIpcompInPackets_Object((1,3,6,1,4,1,3097,3,1,1,3,1,15),_WgIpsecSaIpcompInPackets_Type())
wgIpsecSaIpcompInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInPackets.setStatus(_A)
_WgIpsecSaIpcompInDecompErrors_Type=Counter32
_WgIpsecSaIpcompInDecompErrors_Object=MibTableColumn
wgIpsecSaIpcompInDecompErrors=_WgIpsecSaIpcompInDecompErrors_Object((1,3,6,1,4,1,3097,3,1,1,3,1,16),_WgIpsecSaIpcompInDecompErrors_Type())
wgIpsecSaIpcompInDecompErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInDecompErrors.setStatus(_A)
_WgIpsecSaIpcompInOtherReceiveErrors_Type=Counter32
_WgIpsecSaIpcompInOtherReceiveErrors_Object=MibTableColumn
wgIpsecSaIpcompInOtherReceiveErrors=_WgIpsecSaIpcompInOtherReceiveErrors_Object((1,3,6,1,4,1,3097,3,1,1,3,1,17),_WgIpsecSaIpcompInOtherReceiveErrors_Type())
wgIpsecSaIpcompInOtherReceiveErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompInOtherReceiveErrors.setStatus(_A)
_WgIpsecSaEspOutTable_Object=MibTable
wgIpsecSaEspOutTable=_WgIpsecSaEspOutTable_Object((1,3,6,1,4,1,3097,3,1,1,4))
if mibBuilder.loadTexts:wgIpsecSaEspOutTable.setStatus(_A)
_WgIpsecSaEspOutEntry_Object=MibTableRow
wgIpsecSaEspOutEntry=_WgIpsecSaEspOutEntry_Object((1,3,6,1,4,1,3097,3,1,1,4,1))
wgIpsecSaEspOutEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:wgIpsecSaEspOutEntry.setStatus(_A)
_WgIpsecSaEspOutAddress_Type=IpAddress
_WgIpsecSaEspOutAddress_Object=MibTableColumn
wgIpsecSaEspOutAddress=_WgIpsecSaEspOutAddress_Object((1,3,6,1,4,1,3097,3,1,1,4,1,1),_WgIpsecSaEspOutAddress_Type())
wgIpsecSaEspOutAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutAddress.setStatus(_A)
_WgIpsecSaEspOutSpi_Type=Unsigned32
_WgIpsecSaEspOutSpi_Object=MibTableColumn
wgIpsecSaEspOutSpi=_WgIpsecSaEspOutSpi_Object((1,3,6,1,4,1,3097,3,1,1,4,1,2),_WgIpsecSaEspOutSpi_Type())
wgIpsecSaEspOutSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutSpi.setStatus(_A)
class _WgIpsecSaEspOutSourceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,255))
_WgIpsecSaEspOutSourceId_Type.__name__=_D
_WgIpsecSaEspOutSourceId_Object=MibTableColumn
wgIpsecSaEspOutSourceId=_WgIpsecSaEspOutSourceId_Object((1,3,6,1,4,1,3097,3,1,1,4,1,3),_WgIpsecSaEspOutSourceId_Type())
wgIpsecSaEspOutSourceId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutSourceId.setStatus(_A)
_WgIpsecSaEspOutSourceIdType_Type=IpsecDoiIdentType
_WgIpsecSaEspOutSourceIdType_Object=MibTableColumn
wgIpsecSaEspOutSourceIdType=_WgIpsecSaEspOutSourceIdType_Object((1,3,6,1,4,1,3097,3,1,1,4,1,4),_WgIpsecSaEspOutSourceIdType_Type())
wgIpsecSaEspOutSourceIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutSourceIdType.setStatus(_A)
class _WgIpsecSaEspOutDestId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,255))
_WgIpsecSaEspOutDestId_Type.__name__=_D
_WgIpsecSaEspOutDestId_Object=MibTableColumn
wgIpsecSaEspOutDestId=_WgIpsecSaEspOutDestId_Object((1,3,6,1,4,1,3097,3,1,1,4,1,5),_WgIpsecSaEspOutDestId_Type())
wgIpsecSaEspOutDestId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutDestId.setStatus(_A)
_WgIpsecSaEspOutDestIdType_Type=IpsecDoiIdentType
_WgIpsecSaEspOutDestIdType_Object=MibTableColumn
wgIpsecSaEspOutDestIdType=_WgIpsecSaEspOutDestIdType_Object((1,3,6,1,4,1,3097,3,1,1,4,1,6),_WgIpsecSaEspOutDestIdType_Type())
wgIpsecSaEspOutDestIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutDestIdType.setStatus(_A)
class _WgIpsecSaEspOutProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WgIpsecSaEspOutProtocol_Type.__name__=_C
_WgIpsecSaEspOutProtocol_Object=MibTableColumn
wgIpsecSaEspOutProtocol=_WgIpsecSaEspOutProtocol_Object((1,3,6,1,4,1,3097,3,1,1,4,1,7),_WgIpsecSaEspOutProtocol_Type())
wgIpsecSaEspOutProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutProtocol.setStatus(_A)
class _WgIpsecSaEspOutSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecSaEspOutSourcePort_Type.__name__=_C
_WgIpsecSaEspOutSourcePort_Object=MibTableColumn
wgIpsecSaEspOutSourcePort=_WgIpsecSaEspOutSourcePort_Object((1,3,6,1,4,1,3097,3,1,1,4,1,8),_WgIpsecSaEspOutSourcePort_Type())
wgIpsecSaEspOutSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutSourcePort.setStatus(_A)
class _WgIpsecSaEspOutDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecSaEspOutDestPort_Type.__name__=_C
_WgIpsecSaEspOutDestPort_Object=MibTableColumn
wgIpsecSaEspOutDestPort=_WgIpsecSaEspOutDestPort_Object((1,3,6,1,4,1,3097,3,1,1,4,1,9),_WgIpsecSaEspOutDestPort_Type())
wgIpsecSaEspOutDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutDestPort.setStatus(_A)
_WgIpsecSaEspOutCreator_Type=IpsecSaCreatorIdent
_WgIpsecSaEspOutCreator_Object=MibTableColumn
wgIpsecSaEspOutCreator=_WgIpsecSaEspOutCreator_Object((1,3,6,1,4,1,3097,3,1,1,4,1,10),_WgIpsecSaEspOutCreator_Type())
wgIpsecSaEspOutCreator.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutCreator.setStatus(_A)
_WgIpsecSaEspOutEncapsulation_Type=IpsecDoiEncapsulationMode
_WgIpsecSaEspOutEncapsulation_Object=MibTableColumn
wgIpsecSaEspOutEncapsulation=_WgIpsecSaEspOutEncapsulation_Object((1,3,6,1,4,1,3097,3,1,1,4,1,11),_WgIpsecSaEspOutEncapsulation_Type())
wgIpsecSaEspOutEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutEncapsulation.setStatus(_A)
_WgIpsecSaEspOutEncAlg_Type=IpsecDoiEspTransform
_WgIpsecSaEspOutEncAlg_Object=MibTableColumn
wgIpsecSaEspOutEncAlg=_WgIpsecSaEspOutEncAlg_Object((1,3,6,1,4,1,3097,3,1,1,4,1,12),_WgIpsecSaEspOutEncAlg_Type())
wgIpsecSaEspOutEncAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutEncAlg.setStatus(_A)
class _WgIpsecSaEspOutEncKeyLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65531))
_WgIpsecSaEspOutEncKeyLength_Type.__name__=_C
_WgIpsecSaEspOutEncKeyLength_Object=MibTableColumn
wgIpsecSaEspOutEncKeyLength=_WgIpsecSaEspOutEncKeyLength_Object((1,3,6,1,4,1,3097,3,1,1,4,1,13),_WgIpsecSaEspOutEncKeyLength_Type())
wgIpsecSaEspOutEncKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutEncKeyLength.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaEspOutEncKeyLength.setUnits('bits')
_WgIpsecSaEspOutAuthAlg_Type=IpsecDoiAuthAlgorithm
_WgIpsecSaEspOutAuthAlg_Object=MibTableColumn
wgIpsecSaEspOutAuthAlg=_WgIpsecSaEspOutAuthAlg_Object((1,3,6,1,4,1,3097,3,1,1,4,1,14),_WgIpsecSaEspOutAuthAlg_Type())
wgIpsecSaEspOutAuthAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutAuthAlg.setStatus(_A)
_WgIpsecSaEspOutLimitSeconds_Type=Integer32
_WgIpsecSaEspOutLimitSeconds_Object=MibTableColumn
wgIpsecSaEspOutLimitSeconds=_WgIpsecSaEspOutLimitSeconds_Object((1,3,6,1,4,1,3097,3,1,1,4,1,15),_WgIpsecSaEspOutLimitSeconds_Type())
wgIpsecSaEspOutLimitSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutLimitSeconds.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaEspOutLimitSeconds.setUnits(_F)
_WgIpsecSaEspOutLimitKbytes_Type=Integer32
_WgIpsecSaEspOutLimitKbytes_Object=MibTableColumn
wgIpsecSaEspOutLimitKbytes=_WgIpsecSaEspOutLimitKbytes_Object((1,3,6,1,4,1,3097,3,1,1,4,1,16),_WgIpsecSaEspOutLimitKbytes_Type())
wgIpsecSaEspOutLimitKbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutLimitKbytes.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaEspOutLimitKbytes.setUnits(_G)
_WgIpsecSaEspOutAccSeconds_Type=Counter32
_WgIpsecSaEspOutAccSeconds_Object=MibTableColumn
wgIpsecSaEspOutAccSeconds=_WgIpsecSaEspOutAccSeconds_Object((1,3,6,1,4,1,3097,3,1,1,4,1,17),_WgIpsecSaEspOutAccSeconds_Type())
wgIpsecSaEspOutAccSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutAccSeconds.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaEspOutAccSeconds.setUnits(_F)
_WgIpsecSaEspOutAccKbytes_Type=Counter64
_WgIpsecSaEspOutAccKbytes_Object=MibTableColumn
wgIpsecSaEspOutAccKbytes=_WgIpsecSaEspOutAccKbytes_Object((1,3,6,1,4,1,3097,3,1,1,4,1,18),_WgIpsecSaEspOutAccKbytes_Type())
wgIpsecSaEspOutAccKbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutAccKbytes.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaEspOutAccKbytes.setUnits(_G)
_WgIpsecSaEspOutUserOctets_Type=Counter64
_WgIpsecSaEspOutUserOctets_Object=MibTableColumn
wgIpsecSaEspOutUserOctets=_WgIpsecSaEspOutUserOctets_Object((1,3,6,1,4,1,3097,3,1,1,4,1,19),_WgIpsecSaEspOutUserOctets_Type())
wgIpsecSaEspOutUserOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutUserOctets.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaEspOutUserOctets.setUnits(_H)
_WgIpsecSaEspOutPackets_Type=Counter64
_WgIpsecSaEspOutPackets_Object=MibTableColumn
wgIpsecSaEspOutPackets=_WgIpsecSaEspOutPackets_Object((1,3,6,1,4,1,3097,3,1,1,4,1,20),_WgIpsecSaEspOutPackets_Type())
wgIpsecSaEspOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutPackets.setStatus(_A)
_WgIpsecSaEspOutSendErrors_Type=Counter32
_WgIpsecSaEspOutSendErrors_Object=MibTableColumn
wgIpsecSaEspOutSendErrors=_WgIpsecSaEspOutSendErrors_Object((1,3,6,1,4,1,3097,3,1,1,4,1,21),_WgIpsecSaEspOutSendErrors_Type())
wgIpsecSaEspOutSendErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaEspOutSendErrors.setStatus(_A)
_WgIpsecSaAhOutTable_Object=MibTable
wgIpsecSaAhOutTable=_WgIpsecSaAhOutTable_Object((1,3,6,1,4,1,3097,3,1,1,5))
if mibBuilder.loadTexts:wgIpsecSaAhOutTable.setStatus(_A)
_WgIpsecSaAhOutEntry_Object=MibTableRow
wgIpsecSaAhOutEntry=_WgIpsecSaAhOutEntry_Object((1,3,6,1,4,1,3097,3,1,1,5,1))
wgIpsecSaAhOutEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:wgIpsecSaAhOutEntry.setStatus(_A)
_WgIpsecSaAhOutAddress_Type=IpAddress
_WgIpsecSaAhOutAddress_Object=MibTableColumn
wgIpsecSaAhOutAddress=_WgIpsecSaAhOutAddress_Object((1,3,6,1,4,1,3097,3,1,1,5,1,1),_WgIpsecSaAhOutAddress_Type())
wgIpsecSaAhOutAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutAddress.setStatus(_A)
_WgIpsecSaAhOutSpi_Type=Integer32
_WgIpsecSaAhOutSpi_Object=MibTableColumn
wgIpsecSaAhOutSpi=_WgIpsecSaAhOutSpi_Object((1,3,6,1,4,1,3097,3,1,1,5,1,2),_WgIpsecSaAhOutSpi_Type())
wgIpsecSaAhOutSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutSpi.setStatus(_A)
class _WgIpsecSaAhOutSourceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,255))
_WgIpsecSaAhOutSourceId_Type.__name__=_D
_WgIpsecSaAhOutSourceId_Object=MibTableColumn
wgIpsecSaAhOutSourceId=_WgIpsecSaAhOutSourceId_Object((1,3,6,1,4,1,3097,3,1,1,5,1,3),_WgIpsecSaAhOutSourceId_Type())
wgIpsecSaAhOutSourceId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutSourceId.setStatus(_A)
_WgIpsecSaAhOutSourceIdType_Type=IpsecDoiIdentType
_WgIpsecSaAhOutSourceIdType_Object=MibTableColumn
wgIpsecSaAhOutSourceIdType=_WgIpsecSaAhOutSourceIdType_Object((1,3,6,1,4,1,3097,3,1,1,5,1,4),_WgIpsecSaAhOutSourceIdType_Type())
wgIpsecSaAhOutSourceIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutSourceIdType.setStatus(_A)
class _WgIpsecSaAhOutDestId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,255))
_WgIpsecSaAhOutDestId_Type.__name__=_D
_WgIpsecSaAhOutDestId_Object=MibTableColumn
wgIpsecSaAhOutDestId=_WgIpsecSaAhOutDestId_Object((1,3,6,1,4,1,3097,3,1,1,5,1,5),_WgIpsecSaAhOutDestId_Type())
wgIpsecSaAhOutDestId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutDestId.setStatus(_A)
_WgIpsecSaAhOutDestIdType_Type=IpsecDoiIdentType
_WgIpsecSaAhOutDestIdType_Object=MibTableColumn
wgIpsecSaAhOutDestIdType=_WgIpsecSaAhOutDestIdType_Object((1,3,6,1,4,1,3097,3,1,1,5,1,6),_WgIpsecSaAhOutDestIdType_Type())
wgIpsecSaAhOutDestIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutDestIdType.setStatus(_A)
class _WgIpsecSaAhOutProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WgIpsecSaAhOutProtocol_Type.__name__=_C
_WgIpsecSaAhOutProtocol_Object=MibTableColumn
wgIpsecSaAhOutProtocol=_WgIpsecSaAhOutProtocol_Object((1,3,6,1,4,1,3097,3,1,1,5,1,7),_WgIpsecSaAhOutProtocol_Type())
wgIpsecSaAhOutProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutProtocol.setStatus(_A)
class _WgIpsecSaAhOutSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecSaAhOutSourcePort_Type.__name__=_C
_WgIpsecSaAhOutSourcePort_Object=MibTableColumn
wgIpsecSaAhOutSourcePort=_WgIpsecSaAhOutSourcePort_Object((1,3,6,1,4,1,3097,3,1,1,5,1,8),_WgIpsecSaAhOutSourcePort_Type())
wgIpsecSaAhOutSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutSourcePort.setStatus(_A)
class _WgIpsecSaAhOutDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecSaAhOutDestPort_Type.__name__=_C
_WgIpsecSaAhOutDestPort_Object=MibTableColumn
wgIpsecSaAhOutDestPort=_WgIpsecSaAhOutDestPort_Object((1,3,6,1,4,1,3097,3,1,1,5,1,9),_WgIpsecSaAhOutDestPort_Type())
wgIpsecSaAhOutDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutDestPort.setStatus(_A)
_WgIpsecSaAhOutCreator_Type=IpsecSaCreatorIdent
_WgIpsecSaAhOutCreator_Object=MibTableColumn
wgIpsecSaAhOutCreator=_WgIpsecSaAhOutCreator_Object((1,3,6,1,4,1,3097,3,1,1,5,1,10),_WgIpsecSaAhOutCreator_Type())
wgIpsecSaAhOutCreator.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutCreator.setStatus(_A)
_WgIpsecSaAhOutEncapsulation_Type=IpsecDoiEncapsulationMode
_WgIpsecSaAhOutEncapsulation_Object=MibTableColumn
wgIpsecSaAhOutEncapsulation=_WgIpsecSaAhOutEncapsulation_Object((1,3,6,1,4,1,3097,3,1,1,5,1,11),_WgIpsecSaAhOutEncapsulation_Type())
wgIpsecSaAhOutEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutEncapsulation.setStatus(_A)
_WgIpsecSaAhOutAuthAlg_Type=IpsecDoiAhTransform
_WgIpsecSaAhOutAuthAlg_Object=MibTableColumn
wgIpsecSaAhOutAuthAlg=_WgIpsecSaAhOutAuthAlg_Object((1,3,6,1,4,1,3097,3,1,1,5,1,12),_WgIpsecSaAhOutAuthAlg_Type())
wgIpsecSaAhOutAuthAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutAuthAlg.setStatus(_A)
_WgIpsecSaAhOutLimitSeconds_Type=Integer32
_WgIpsecSaAhOutLimitSeconds_Object=MibTableColumn
wgIpsecSaAhOutLimitSeconds=_WgIpsecSaAhOutLimitSeconds_Object((1,3,6,1,4,1,3097,3,1,1,5,1,13),_WgIpsecSaAhOutLimitSeconds_Type())
wgIpsecSaAhOutLimitSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutLimitSeconds.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaAhOutLimitSeconds.setUnits(_F)
_WgIpsecSaAhOutLimitKbytes_Type=Integer32
_WgIpsecSaAhOutLimitKbytes_Object=MibTableColumn
wgIpsecSaAhOutLimitKbytes=_WgIpsecSaAhOutLimitKbytes_Object((1,3,6,1,4,1,3097,3,1,1,5,1,14),_WgIpsecSaAhOutLimitKbytes_Type())
wgIpsecSaAhOutLimitKbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutLimitKbytes.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaAhOutLimitKbytes.setUnits(_G)
_WgIpsecSaAhOutAccSeconds_Type=Counter32
_WgIpsecSaAhOutAccSeconds_Object=MibTableColumn
wgIpsecSaAhOutAccSeconds=_WgIpsecSaAhOutAccSeconds_Object((1,3,6,1,4,1,3097,3,1,1,5,1,15),_WgIpsecSaAhOutAccSeconds_Type())
wgIpsecSaAhOutAccSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutAccSeconds.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaAhOutAccSeconds.setUnits(_F)
_WgIpsecSaAhOutAccKbytes_Type=Counter64
_WgIpsecSaAhOutAccKbytes_Object=MibTableColumn
wgIpsecSaAhOutAccKbytes=_WgIpsecSaAhOutAccKbytes_Object((1,3,6,1,4,1,3097,3,1,1,5,1,16),_WgIpsecSaAhOutAccKbytes_Type())
wgIpsecSaAhOutAccKbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutAccKbytes.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaAhOutAccKbytes.setUnits(_G)
_WgIpsecSaAhOutUserOctets_Type=Counter64
_WgIpsecSaAhOutUserOctets_Object=MibTableColumn
wgIpsecSaAhOutUserOctets=_WgIpsecSaAhOutUserOctets_Object((1,3,6,1,4,1,3097,3,1,1,5,1,17),_WgIpsecSaAhOutUserOctets_Type())
wgIpsecSaAhOutUserOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutUserOctets.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaAhOutUserOctets.setUnits(_H)
_WgIpsecSaAhOutPackets_Type=Counter64
_WgIpsecSaAhOutPackets_Object=MibTableColumn
wgIpsecSaAhOutPackets=_WgIpsecSaAhOutPackets_Object((1,3,6,1,4,1,3097,3,1,1,5,1,18),_WgIpsecSaAhOutPackets_Type())
wgIpsecSaAhOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutPackets.setStatus(_A)
_WgIpsecSaAhOutSendErrors_Type=Counter32
_WgIpsecSaAhOutSendErrors_Object=MibTableColumn
wgIpsecSaAhOutSendErrors=_WgIpsecSaAhOutSendErrors_Object((1,3,6,1,4,1,3097,3,1,1,5,1,19),_WgIpsecSaAhOutSendErrors_Type())
wgIpsecSaAhOutSendErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaAhOutSendErrors.setStatus(_A)
_WgIpsecSaIpcompOutTable_Object=MibTable
wgIpsecSaIpcompOutTable=_WgIpsecSaIpcompOutTable_Object((1,3,6,1,4,1,3097,3,1,1,6))
if mibBuilder.loadTexts:wgIpsecSaIpcompOutTable.setStatus(_A)
_WgIpsecSaIpcompOutEntry_Object=MibTableRow
wgIpsecSaIpcompOutEntry=_WgIpsecSaIpcompOutEntry_Object((1,3,6,1,4,1,3097,3,1,1,6,1))
wgIpsecSaIpcompOutEntry.setIndexNames((0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:wgIpsecSaIpcompOutEntry.setStatus(_A)
_WgIpsecSaIpcompOutAddress_Type=IpAddress
_WgIpsecSaIpcompOutAddress_Object=MibTableColumn
wgIpsecSaIpcompOutAddress=_WgIpsecSaIpcompOutAddress_Object((1,3,6,1,4,1,3097,3,1,1,6,1,1),_WgIpsecSaIpcompOutAddress_Type())
wgIpsecSaIpcompOutAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutAddress.setStatus(_A)
_WgIpsecSaIpcompOutCpi_Type=IpsecDoiIpcompTransform
_WgIpsecSaIpcompOutCpi_Object=MibTableColumn
wgIpsecSaIpcompOutCpi=_WgIpsecSaIpcompOutCpi_Object((1,3,6,1,4,1,3097,3,1,1,6,1,2),_WgIpsecSaIpcompOutCpi_Type())
wgIpsecSaIpcompOutCpi.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutCpi.setStatus(_A)
class _WgIpsecSaIpcompOutSourceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,255))
_WgIpsecSaIpcompOutSourceId_Type.__name__=_D
_WgIpsecSaIpcompOutSourceId_Object=MibTableColumn
wgIpsecSaIpcompOutSourceId=_WgIpsecSaIpcompOutSourceId_Object((1,3,6,1,4,1,3097,3,1,1,6,1,3),_WgIpsecSaIpcompOutSourceId_Type())
wgIpsecSaIpcompOutSourceId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutSourceId.setStatus(_A)
_WgIpsecSaIpcompOutSourceIdType_Type=IpsecDoiIdentType
_WgIpsecSaIpcompOutSourceIdType_Object=MibTableColumn
wgIpsecSaIpcompOutSourceIdType=_WgIpsecSaIpcompOutSourceIdType_Object((1,3,6,1,4,1,3097,3,1,1,6,1,4),_WgIpsecSaIpcompOutSourceIdType_Type())
wgIpsecSaIpcompOutSourceIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutSourceIdType.setStatus(_A)
class _WgIpsecSaIpcompOutDestId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,255))
_WgIpsecSaIpcompOutDestId_Type.__name__=_D
_WgIpsecSaIpcompOutDestId_Object=MibTableColumn
wgIpsecSaIpcompOutDestId=_WgIpsecSaIpcompOutDestId_Object((1,3,6,1,4,1,3097,3,1,1,6,1,5),_WgIpsecSaIpcompOutDestId_Type())
wgIpsecSaIpcompOutDestId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutDestId.setStatus(_A)
_WgIpsecSaIpcompOutDestIdType_Type=IpsecDoiIdentType
_WgIpsecSaIpcompOutDestIdType_Object=MibTableColumn
wgIpsecSaIpcompOutDestIdType=_WgIpsecSaIpcompOutDestIdType_Object((1,3,6,1,4,1,3097,3,1,1,6,1,6),_WgIpsecSaIpcompOutDestIdType_Type())
wgIpsecSaIpcompOutDestIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutDestIdType.setStatus(_A)
class _WgIpsecSaIpcompOutProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WgIpsecSaIpcompOutProtocol_Type.__name__=_C
_WgIpsecSaIpcompOutProtocol_Object=MibTableColumn
wgIpsecSaIpcompOutProtocol=_WgIpsecSaIpcompOutProtocol_Object((1,3,6,1,4,1,3097,3,1,1,6,1,7),_WgIpsecSaIpcompOutProtocol_Type())
wgIpsecSaIpcompOutProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutProtocol.setStatus(_A)
class _WgIpsecSaIpcompOutSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecSaIpcompOutSourcePort_Type.__name__=_C
_WgIpsecSaIpcompOutSourcePort_Object=MibTableColumn
wgIpsecSaIpcompOutSourcePort=_WgIpsecSaIpcompOutSourcePort_Object((1,3,6,1,4,1,3097,3,1,1,6,1,8),_WgIpsecSaIpcompOutSourcePort_Type())
wgIpsecSaIpcompOutSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutSourcePort.setStatus(_A)
class _WgIpsecSaIpcompOutDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecSaIpcompOutDestPort_Type.__name__=_C
_WgIpsecSaIpcompOutDestPort_Object=MibTableColumn
wgIpsecSaIpcompOutDestPort=_WgIpsecSaIpcompOutDestPort_Object((1,3,6,1,4,1,3097,3,1,1,6,1,9),_WgIpsecSaIpcompOutDestPort_Type())
wgIpsecSaIpcompOutDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutDestPort.setStatus(_A)
_WgIpsecSaIpcompOutCreator_Type=IpsecSaCreatorIdent
_WgIpsecSaIpcompOutCreator_Object=MibTableColumn
wgIpsecSaIpcompOutCreator=_WgIpsecSaIpcompOutCreator_Object((1,3,6,1,4,1,3097,3,1,1,6,1,10),_WgIpsecSaIpcompOutCreator_Type())
wgIpsecSaIpcompOutCreator.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutCreator.setStatus(_A)
_WgIpsecSaIpcompOutEncapsulation_Type=IpsecDoiEncapsulationMode
_WgIpsecSaIpcompOutEncapsulation_Object=MibTableColumn
wgIpsecSaIpcompOutEncapsulation=_WgIpsecSaIpcompOutEncapsulation_Object((1,3,6,1,4,1,3097,3,1,1,6,1,11),_WgIpsecSaIpcompOutEncapsulation_Type())
wgIpsecSaIpcompOutEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutEncapsulation.setStatus(_A)
_WgIpsecSaIpcompOutCompAlg_Type=IpsecDoiIpcompTransform
_WgIpsecSaIpcompOutCompAlg_Object=MibTableColumn
wgIpsecSaIpcompOutCompAlg=_WgIpsecSaIpcompOutCompAlg_Object((1,3,6,1,4,1,3097,3,1,1,6,1,12),_WgIpsecSaIpcompOutCompAlg_Type())
wgIpsecSaIpcompOutCompAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutCompAlg.setStatus(_A)
_WgIpsecSaIpcompOutSeconds_Type=Counter32
_WgIpsecSaIpcompOutSeconds_Object=MibTableColumn
wgIpsecSaIpcompOutSeconds=_WgIpsecSaIpcompOutSeconds_Object((1,3,6,1,4,1,3097,3,1,1,6,1,13),_WgIpsecSaIpcompOutSeconds_Type())
wgIpsecSaIpcompOutSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutSeconds.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutSeconds.setUnits(_F)
_WgIpsecSaIpcompOutUserOctets_Type=Counter32
_WgIpsecSaIpcompOutUserOctets_Object=MibTableColumn
wgIpsecSaIpcompOutUserOctets=_WgIpsecSaIpcompOutUserOctets_Object((1,3,6,1,4,1,3097,3,1,1,6,1,14),_WgIpsecSaIpcompOutUserOctets_Type())
wgIpsecSaIpcompOutUserOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutUserOctets.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutUserOctets.setUnits(_H)
_WgIpsecSaIpcompOutPackets_Type=Counter32
_WgIpsecSaIpcompOutPackets_Object=MibTableColumn
wgIpsecSaIpcompOutPackets=_WgIpsecSaIpcompOutPackets_Object((1,3,6,1,4,1,3097,3,1,1,6,1,15),_WgIpsecSaIpcompOutPackets_Type())
wgIpsecSaIpcompOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSaIpcompOutPackets.setStatus(_A)
_WgSaStatistics_ObjectIdentity=ObjectIdentity
wgSaStatistics=_WgSaStatistics_ObjectIdentity((1,3,6,1,4,1,3097,3,1,2))
if mibBuilder.loadTexts:wgSaStatistics.setStatus(_A)
_WgIpsecEspCurrentInboundSAs_Type=Gauge32
_WgIpsecEspCurrentInboundSAs_Object=MibScalar
wgIpsecEspCurrentInboundSAs=_WgIpsecEspCurrentInboundSAs_Object((1,3,6,1,4,1,3097,3,1,2,1),_WgIpsecEspCurrentInboundSAs_Type())
wgIpsecEspCurrentInboundSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecEspCurrentInboundSAs.setStatus(_A)
_WgIpsecEspTotalInboundSAs_Type=Counter32
_WgIpsecEspTotalInboundSAs_Object=MibScalar
wgIpsecEspTotalInboundSAs=_WgIpsecEspTotalInboundSAs_Object((1,3,6,1,4,1,3097,3,1,2,2),_WgIpsecEspTotalInboundSAs_Type())
wgIpsecEspTotalInboundSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecEspTotalInboundSAs.setStatus(_A)
_WgIpsecEspCurrentOutboundSAs_Type=Gauge32
_WgIpsecEspCurrentOutboundSAs_Object=MibScalar
wgIpsecEspCurrentOutboundSAs=_WgIpsecEspCurrentOutboundSAs_Object((1,3,6,1,4,1,3097,3,1,2,3),_WgIpsecEspCurrentOutboundSAs_Type())
wgIpsecEspCurrentOutboundSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecEspCurrentOutboundSAs.setStatus(_A)
_WgIpsecEspTotalOutboundSAs_Type=Counter32
_WgIpsecEspTotalOutboundSAs_Object=MibScalar
wgIpsecEspTotalOutboundSAs=_WgIpsecEspTotalOutboundSAs_Object((1,3,6,1,4,1,3097,3,1,2,4),_WgIpsecEspTotalOutboundSAs_Type())
wgIpsecEspTotalOutboundSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecEspTotalOutboundSAs.setStatus(_A)
_WgIpsecAhCurrentInboundSAs_Type=Gauge32
_WgIpsecAhCurrentInboundSAs_Object=MibScalar
wgIpsecAhCurrentInboundSAs=_WgIpsecAhCurrentInboundSAs_Object((1,3,6,1,4,1,3097,3,1,2,5),_WgIpsecAhCurrentInboundSAs_Type())
wgIpsecAhCurrentInboundSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecAhCurrentInboundSAs.setStatus(_A)
_WgIpsecAhTotalInboundSAs_Type=Counter32
_WgIpsecAhTotalInboundSAs_Object=MibScalar
wgIpsecAhTotalInboundSAs=_WgIpsecAhTotalInboundSAs_Object((1,3,6,1,4,1,3097,3,1,2,6),_WgIpsecAhTotalInboundSAs_Type())
wgIpsecAhTotalInboundSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecAhTotalInboundSAs.setStatus(_A)
_WgIpsecAhCurrentOutboundSAs_Type=Gauge32
_WgIpsecAhCurrentOutboundSAs_Object=MibScalar
wgIpsecAhCurrentOutboundSAs=_WgIpsecAhCurrentOutboundSAs_Object((1,3,6,1,4,1,3097,3,1,2,7),_WgIpsecAhCurrentOutboundSAs_Type())
wgIpsecAhCurrentOutboundSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecAhCurrentOutboundSAs.setStatus(_A)
_WgIpsecAhTotalOutboundSAs_Type=Counter32
_WgIpsecAhTotalOutboundSAs_Object=MibScalar
wgIpsecAhTotalOutboundSAs=_WgIpsecAhTotalOutboundSAs_Object((1,3,6,1,4,1,3097,3,1,2,8),_WgIpsecAhTotalOutboundSAs_Type())
wgIpsecAhTotalOutboundSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecAhTotalOutboundSAs.setStatus(_A)
_WgIpsecIpcompCurrentInboundSAs_Type=Gauge32
_WgIpsecIpcompCurrentInboundSAs_Object=MibScalar
wgIpsecIpcompCurrentInboundSAs=_WgIpsecIpcompCurrentInboundSAs_Object((1,3,6,1,4,1,3097,3,1,2,9),_WgIpsecIpcompCurrentInboundSAs_Type())
wgIpsecIpcompCurrentInboundSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecIpcompCurrentInboundSAs.setStatus(_A)
_WgIpsecIpcompTotalInboundSAs_Type=Counter32
_WgIpsecIpcompTotalInboundSAs_Object=MibScalar
wgIpsecIpcompTotalInboundSAs=_WgIpsecIpcompTotalInboundSAs_Object((1,3,6,1,4,1,3097,3,1,2,10),_WgIpsecIpcompTotalInboundSAs_Type())
wgIpsecIpcompTotalInboundSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecIpcompTotalInboundSAs.setStatus(_A)
_WgIpsecIpcompCurrentOutboundSAs_Type=Gauge32
_WgIpsecIpcompCurrentOutboundSAs_Object=MibScalar
wgIpsecIpcompCurrentOutboundSAs=_WgIpsecIpcompCurrentOutboundSAs_Object((1,3,6,1,4,1,3097,3,1,2,11),_WgIpsecIpcompCurrentOutboundSAs_Type())
wgIpsecIpcompCurrentOutboundSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecIpcompCurrentOutboundSAs.setStatus(_A)
_WgIpsecIpcompTotalOutboundSAs_Type=Counter32
_WgIpsecIpcompTotalOutboundSAs_Object=MibScalar
wgIpsecIpcompTotalOutboundSAs=_WgIpsecIpcompTotalOutboundSAs_Object((1,3,6,1,4,1,3097,3,1,2,12),_WgIpsecIpcompTotalOutboundSAs_Type())
wgIpsecIpcompTotalOutboundSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecIpcompTotalOutboundSAs.setStatus(_A)
_WgSaErrors_ObjectIdentity=ObjectIdentity
wgSaErrors=_WgSaErrors_ObjectIdentity((1,3,6,1,4,1,3097,3,1,3))
if mibBuilder.loadTexts:wgSaErrors.setStatus(_A)
_WgIpsecDecryptionErrors_Type=Counter32
_WgIpsecDecryptionErrors_Object=MibScalar
wgIpsecDecryptionErrors=_WgIpsecDecryptionErrors_Object((1,3,6,1,4,1,3097,3,1,3,1),_WgIpsecDecryptionErrors_Type())
wgIpsecDecryptionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecDecryptionErrors.setStatus(_A)
_WgIpsecAuthenticationErrors_Type=Counter32
_WgIpsecAuthenticationErrors_Object=MibScalar
wgIpsecAuthenticationErrors=_WgIpsecAuthenticationErrors_Object((1,3,6,1,4,1,3097,3,1,3,2),_WgIpsecAuthenticationErrors_Type())
wgIpsecAuthenticationErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecAuthenticationErrors.setStatus(_A)
_WgIpsecReplayErrors_Type=Counter32
_WgIpsecReplayErrors_Object=MibScalar
wgIpsecReplayErrors=_WgIpsecReplayErrors_Object((1,3,6,1,4,1,3097,3,1,3,3),_WgIpsecReplayErrors_Type())
wgIpsecReplayErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecReplayErrors.setStatus(_A)
_WgIpsecPolicyErrors_Type=Counter32
_WgIpsecPolicyErrors_Object=MibScalar
wgIpsecPolicyErrors=_WgIpsecPolicyErrors_Object((1,3,6,1,4,1,3097,3,1,3,4),_WgIpsecPolicyErrors_Type())
wgIpsecPolicyErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecPolicyErrors.setStatus(_A)
_WgIpsecOtherReceiveErrors_Type=Counter32
_WgIpsecOtherReceiveErrors_Object=MibScalar
wgIpsecOtherReceiveErrors=_WgIpsecOtherReceiveErrors_Object((1,3,6,1,4,1,3097,3,1,3,5),_WgIpsecOtherReceiveErrors_Type())
wgIpsecOtherReceiveErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecOtherReceiveErrors.setStatus(_A)
_WgIpsecSendErrors_Type=Counter32
_WgIpsecSendErrors_Object=MibScalar
wgIpsecSendErrors=_WgIpsecSendErrors_Object((1,3,6,1,4,1,3097,3,1,3,6),_WgIpsecSendErrors_Type())
wgIpsecSendErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecSendErrors.setStatus(_A)
_WgIpsecUnknownSpiErrors_Type=Counter32
_WgIpsecUnknownSpiErrors_Object=MibScalar
wgIpsecUnknownSpiErrors=_WgIpsecUnknownSpiErrors_Object((1,3,6,1,4,1,3097,3,1,3,7),_WgIpsecUnknownSpiErrors_Type())
wgIpsecUnknownSpiErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecUnknownSpiErrors.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'IpsecSaCreatorIdent':IpsecSaCreatorIdent,'IpsecIpv6Address':IpsecIpv6Address,'wgIpsecSaMonModule':wgIpsecSaMonModule,'wgIpsecSaMonitorMIB':wgIpsecSaMonitorMIB,'wgSaTables':wgSaTables,'wgIpsecSaEspInTable':wgIpsecSaEspInTable,'wgIpsecSaEspInEntry':wgIpsecSaEspInEntry,_I:wgIpsecSaEspInAddress,_J:wgIpsecSaEspInSpi,'wgIpsecSaEspInDestId':wgIpsecSaEspInDestId,'wgIpsecSaEspInDestIdType':wgIpsecSaEspInDestIdType,'wgIpsecSaEspInSourceId':wgIpsecSaEspInSourceId,'wgIpsecSaEspInSourceIdType':wgIpsecSaEspInSourceIdType,'wgIpsecSaEspInProtocol':wgIpsecSaEspInProtocol,'wgIpsecSaEspInDestPort':wgIpsecSaEspInDestPort,'wgIpsecSaEspInSourcePort':wgIpsecSaEspInSourcePort,'wgIpsecSaEspInCreator':wgIpsecSaEspInCreator,'wgIpsecSaEspInEncapsulation':wgIpsecSaEspInEncapsulation,'wgIpsecSaEspInEncAlg':wgIpsecSaEspInEncAlg,'wgIpsecSaEspInEncKeyLength':wgIpsecSaEspInEncKeyLength,'wgIpsecSaEspInAuthAlg':wgIpsecSaEspInAuthAlg,'wgIpsecSaEspInLimitSeconds':wgIpsecSaEspInLimitSeconds,'wgIpsecSaEspInLimitKbytes':wgIpsecSaEspInLimitKbytes,'wgIpsecSaEspInAccSeconds':wgIpsecSaEspInAccSeconds,'wgIpsecSaEspInAccKbytes':wgIpsecSaEspInAccKbytes,'wgIpsecSaEspInUserOctets':wgIpsecSaEspInUserOctets,'wgIpsecSaEspInPackets':wgIpsecSaEspInPackets,'wgIpsecSaEspInDecryptErrors':wgIpsecSaEspInDecryptErrors,'wgIpsecSaEspInAuthErrors':wgIpsecSaEspInAuthErrors,'wgIpsecSaEspInReplayErrors':wgIpsecSaEspInReplayErrors,'wgIpsecSaEspInPolicyErrors':wgIpsecSaEspInPolicyErrors,'wgIpsecSaEspInPadErrors':wgIpsecSaEspInPadErrors,'wgIpsecSaEspInOtherReceiveErrors':wgIpsecSaEspInOtherReceiveErrors,'wgIpsecSaAhInTable':wgIpsecSaAhInTable,'wgIpsecSaAhInEntry':wgIpsecSaAhInEntry,_K:wgIpsecSaAhInAddress,_L:wgIpsecSaAhInSpi,'wgIpsecSaAhInDestId':wgIpsecSaAhInDestId,'wgIpsecSaAhInDestIdType':wgIpsecSaAhInDestIdType,'wgIpsecSaAhInSourceId':wgIpsecSaAhInSourceId,'wgIpsecSaAhInSourceIdType':wgIpsecSaAhInSourceIdType,'wgIpsecSaAhInProtocol':wgIpsecSaAhInProtocol,'wgIpsecSaAhInDestPort':wgIpsecSaAhInDestPort,'wgIpsecSaAhInSourcePort':wgIpsecSaAhInSourcePort,'wgIpsecSaAhInCreator':wgIpsecSaAhInCreator,'wgIpsecSaAhInEncapsulation':wgIpsecSaAhInEncapsulation,'wgIpsecSaAhInAuthAlg':wgIpsecSaAhInAuthAlg,'wgIpsecSaAhInLimitSeconds':wgIpsecSaAhInLimitSeconds,'wgIpsecSaAhInLimitKbytes':wgIpsecSaAhInLimitKbytes,'wgIpsecSaAhInAccSeconds':wgIpsecSaAhInAccSeconds,'wgIpsecSaAhInAccKbytes':wgIpsecSaAhInAccKbytes,'wgIpsecSaAhInUserOctets':wgIpsecSaAhInUserOctets,'wgIpsecSaAhInPackets':wgIpsecSaAhInPackets,'wgIpsecSaAhInAuthErrors':wgIpsecSaAhInAuthErrors,'wgIpsecSaAhInReplayErrors':wgIpsecSaAhInReplayErrors,'wgIpsecSaAhInPolicyErrors':wgIpsecSaAhInPolicyErrors,'wgIpsecSaAhInOtherReceiveErrors':wgIpsecSaAhInOtherReceiveErrors,'wgIpsecSaIpcompInTable':wgIpsecSaIpcompInTable,'wgIpsecSaIpcompInEntry':wgIpsecSaIpcompInEntry,_M:wgIpsecSaIpcompInAddress,_N:wgIpsecSaIpcompInCpi,'wgIpsecSaIpcompInDestId':wgIpsecSaIpcompInDestId,'wgIpsecSaIpcompInDestIdType':wgIpsecSaIpcompInDestIdType,'wgIpsecSaIpcompInSourceId':wgIpsecSaIpcompInSourceId,'wgIpsecSaIpcompInSourceIdType':wgIpsecSaIpcompInSourceIdType,'wgIpsecSaIpcompInProtocol':wgIpsecSaIpcompInProtocol,'wgIpsecSaIpcompInDestPort':wgIpsecSaIpcompInDestPort,'wgIpsecSaIpcompInSourcePort':wgIpsecSaIpcompInSourcePort,'wgIpsecSaIpcompInCreator':wgIpsecSaIpcompInCreator,'wgIpsecSaIpcompInEncapsulation':wgIpsecSaIpcompInEncapsulation,'wgIpsecSaIpcompInDecompAlg':wgIpsecSaIpcompInDecompAlg,'wgIpsecSaIpcompInSeconds':wgIpsecSaIpcompInSeconds,'wgIpsecSaIpcompInUserOctets':wgIpsecSaIpcompInUserOctets,'wgIpsecSaIpcompInPackets':wgIpsecSaIpcompInPackets,'wgIpsecSaIpcompInDecompErrors':wgIpsecSaIpcompInDecompErrors,'wgIpsecSaIpcompInOtherReceiveErrors':wgIpsecSaIpcompInOtherReceiveErrors,'wgIpsecSaEspOutTable':wgIpsecSaEspOutTable,'wgIpsecSaEspOutEntry':wgIpsecSaEspOutEntry,_O:wgIpsecSaEspOutAddress,_P:wgIpsecSaEspOutSpi,'wgIpsecSaEspOutSourceId':wgIpsecSaEspOutSourceId,'wgIpsecSaEspOutSourceIdType':wgIpsecSaEspOutSourceIdType,'wgIpsecSaEspOutDestId':wgIpsecSaEspOutDestId,'wgIpsecSaEspOutDestIdType':wgIpsecSaEspOutDestIdType,'wgIpsecSaEspOutProtocol':wgIpsecSaEspOutProtocol,'wgIpsecSaEspOutSourcePort':wgIpsecSaEspOutSourcePort,'wgIpsecSaEspOutDestPort':wgIpsecSaEspOutDestPort,'wgIpsecSaEspOutCreator':wgIpsecSaEspOutCreator,'wgIpsecSaEspOutEncapsulation':wgIpsecSaEspOutEncapsulation,'wgIpsecSaEspOutEncAlg':wgIpsecSaEspOutEncAlg,'wgIpsecSaEspOutEncKeyLength':wgIpsecSaEspOutEncKeyLength,'wgIpsecSaEspOutAuthAlg':wgIpsecSaEspOutAuthAlg,'wgIpsecSaEspOutLimitSeconds':wgIpsecSaEspOutLimitSeconds,'wgIpsecSaEspOutLimitKbytes':wgIpsecSaEspOutLimitKbytes,'wgIpsecSaEspOutAccSeconds':wgIpsecSaEspOutAccSeconds,'wgIpsecSaEspOutAccKbytes':wgIpsecSaEspOutAccKbytes,'wgIpsecSaEspOutUserOctets':wgIpsecSaEspOutUserOctets,'wgIpsecSaEspOutPackets':wgIpsecSaEspOutPackets,'wgIpsecSaEspOutSendErrors':wgIpsecSaEspOutSendErrors,'wgIpsecSaAhOutTable':wgIpsecSaAhOutTable,'wgIpsecSaAhOutEntry':wgIpsecSaAhOutEntry,_Q:wgIpsecSaAhOutAddress,_R:wgIpsecSaAhOutSpi,'wgIpsecSaAhOutSourceId':wgIpsecSaAhOutSourceId,'wgIpsecSaAhOutSourceIdType':wgIpsecSaAhOutSourceIdType,'wgIpsecSaAhOutDestId':wgIpsecSaAhOutDestId,'wgIpsecSaAhOutDestIdType':wgIpsecSaAhOutDestIdType,'wgIpsecSaAhOutProtocol':wgIpsecSaAhOutProtocol,'wgIpsecSaAhOutSourcePort':wgIpsecSaAhOutSourcePort,'wgIpsecSaAhOutDestPort':wgIpsecSaAhOutDestPort,'wgIpsecSaAhOutCreator':wgIpsecSaAhOutCreator,'wgIpsecSaAhOutEncapsulation':wgIpsecSaAhOutEncapsulation,'wgIpsecSaAhOutAuthAlg':wgIpsecSaAhOutAuthAlg,'wgIpsecSaAhOutLimitSeconds':wgIpsecSaAhOutLimitSeconds,'wgIpsecSaAhOutLimitKbytes':wgIpsecSaAhOutLimitKbytes,'wgIpsecSaAhOutAccSeconds':wgIpsecSaAhOutAccSeconds,'wgIpsecSaAhOutAccKbytes':wgIpsecSaAhOutAccKbytes,'wgIpsecSaAhOutUserOctets':wgIpsecSaAhOutUserOctets,'wgIpsecSaAhOutPackets':wgIpsecSaAhOutPackets,'wgIpsecSaAhOutSendErrors':wgIpsecSaAhOutSendErrors,'wgIpsecSaIpcompOutTable':wgIpsecSaIpcompOutTable,'wgIpsecSaIpcompOutEntry':wgIpsecSaIpcompOutEntry,_S:wgIpsecSaIpcompOutAddress,_T:wgIpsecSaIpcompOutCpi,'wgIpsecSaIpcompOutSourceId':wgIpsecSaIpcompOutSourceId,'wgIpsecSaIpcompOutSourceIdType':wgIpsecSaIpcompOutSourceIdType,'wgIpsecSaIpcompOutDestId':wgIpsecSaIpcompOutDestId,'wgIpsecSaIpcompOutDestIdType':wgIpsecSaIpcompOutDestIdType,'wgIpsecSaIpcompOutProtocol':wgIpsecSaIpcompOutProtocol,'wgIpsecSaIpcompOutSourcePort':wgIpsecSaIpcompOutSourcePort,'wgIpsecSaIpcompOutDestPort':wgIpsecSaIpcompOutDestPort,'wgIpsecSaIpcompOutCreator':wgIpsecSaIpcompOutCreator,'wgIpsecSaIpcompOutEncapsulation':wgIpsecSaIpcompOutEncapsulation,'wgIpsecSaIpcompOutCompAlg':wgIpsecSaIpcompOutCompAlg,'wgIpsecSaIpcompOutSeconds':wgIpsecSaIpcompOutSeconds,'wgIpsecSaIpcompOutUserOctets':wgIpsecSaIpcompOutUserOctets,'wgIpsecSaIpcompOutPackets':wgIpsecSaIpcompOutPackets,'wgSaStatistics':wgSaStatistics,'wgIpsecEspCurrentInboundSAs':wgIpsecEspCurrentInboundSAs,'wgIpsecEspTotalInboundSAs':wgIpsecEspTotalInboundSAs,'wgIpsecEspCurrentOutboundSAs':wgIpsecEspCurrentOutboundSAs,'wgIpsecEspTotalOutboundSAs':wgIpsecEspTotalOutboundSAs,'wgIpsecAhCurrentInboundSAs':wgIpsecAhCurrentInboundSAs,'wgIpsecAhTotalInboundSAs':wgIpsecAhTotalInboundSAs,'wgIpsecAhCurrentOutboundSAs':wgIpsecAhCurrentOutboundSAs,'wgIpsecAhTotalOutboundSAs':wgIpsecAhTotalOutboundSAs,'wgIpsecIpcompCurrentInboundSAs':wgIpsecIpcompCurrentInboundSAs,'wgIpsecIpcompTotalInboundSAs':wgIpsecIpcompTotalInboundSAs,'wgIpsecIpcompCurrentOutboundSAs':wgIpsecIpcompCurrentOutboundSAs,'wgIpsecIpcompTotalOutboundSAs':wgIpsecIpcompTotalOutboundSAs,'wgSaErrors':wgSaErrors,'wgIpsecDecryptionErrors':wgIpsecDecryptionErrors,'wgIpsecAuthenticationErrors':wgIpsecAuthenticationErrors,'wgIpsecReplayErrors':wgIpsecReplayErrors,'wgIpsecPolicyErrors':wgIpsecPolicyErrors,'wgIpsecOtherReceiveErrors':wgIpsecOtherReceiveErrors,'wgIpsecSendErrors':wgIpsecSendErrors,'wgIpsecUnknownSpiErrors':wgIpsecUnknownSpiErrors})