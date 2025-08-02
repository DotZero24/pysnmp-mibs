_A8='ciscoCasaFaNotifGroup'
_A7='ciscoCasaFaADGroup'
_A6='ciscoCasaFaDispatchGroup'
_A5='ciscoCasaFaWildcardAffGroup'
_A4='ciscoCasaFaWildcardAffDeleted'
_A3='ciscoCasaFaWildcardAffCreated'
_A2='ccfaAdvertisedDispatchAddress'
_A1='ccfaDispatchFlows'
_A0='ccfaDispatchHCPacketsOut'
_z='ccfaDispatchPacketsOut'
_y='ccfaDispatchHCPacketsIn'
_x='ccfaDispatchPacketsIn'
_w='ccfaDispatchHCBytesOut'
_v='ccfaDispatchBytesOut'
_u='ccfaDispatchHCBytesIn'
_t='ccfaDispatchBytesIn'
_s='ccfaWildcardAffDispatchAddr'
_r='ccfaWildcardAffDispatch'
_q='ccfaWildAffInterestTickelSpec'
_p='ccfaWildAffInterestPacketSpec'
_o='ccfaWildcardAffInterestPort'
_n='ccfaWildcardAffInterestAddr'
_m='ccfaWildcardAffAdvertiseDestAddr'
_l='ccfaWildcardAffInterestTimeouts'
_k='ccfaWildcardAffInsertTime'
_j='ccfaWildcardAffHCPackets'
_i='ccfaWildcardAffPackets'
_h='ccfaWildcardAffHCBytes'
_g='ccfaWildcardAffBytes'
_f='ccfaWildcardAffDrops'
_e='ccfaWildcardAffDenies'
_d='ccfaWildAffCacheHiWtrMarkReset'
_c='ccfaWildcardAffHiWtrMark'
_b='ccfaWildcardAffNotifEnabled'
_a='ccfaWildcardAffNumOf'
_Z='ccfaWildcardAffTotalPackets'
_Y='ccfaWildcardAffHCTotalBytes'
_X='ccfaWildcardAffTotalBytes'
_W='ccfaAdvertisedAddress'
_V='ccfaDispatchAddress'
_U='ccfaWildcardAffIndex'
_T='read-write'
_S='TruthValue'
_R='ccfaWildcardAffFlows'
_Q='not-accessible'
_P='ccfaWildcardAffSvcManagerPort'
_O='ccfaWildcardAffSvcManagerAddr'
_N='ccfaWildcardAffDestinationMask'
_M='ccfaWildcardAffSourceMask'
_L='ccfaWildcardAffFragment'
_K='ccfaWildcardAffProtocol'
_J='ccfaWildcardAffDestinationPort'
_I='ccfaWildcardAffSourcePort'
_H='ccfaWildcardAffDestinationAddr'
_G='ccfaWildcardAffSourceAddr'
_F='affinities'
_E='packets'
_D='bytes'
_C='read-only'
_B='current'
_A='CISCO-CASA-FA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoIpProtocol,CiscoPort=mibBuilder.importSymbols('CISCO-TC','CiscoIpProtocol','CiscoPort')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeStamp',_S)
ciscoCasaFaMIB=ModuleIdentity((1,3,6,1,4,1,9,9,115))
if mibBuilder.loadTexts:ciscoCasaFaMIB.setRevisions(('2002-09-18 00:00',))
class CasaWildcardAffIndex(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
class CasaInterestPacketSpecification(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CiscoCasaFaMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCasaFaMIBObjects=_CiscoCasaFaMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,115,1))
_CcfaGlobal_ObjectIdentity=ObjectIdentity
ccfaGlobal=_CcfaGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,115,1,1))
_CcfaStats_ObjectIdentity=ObjectIdentity
ccfaStats=_CcfaStats_ObjectIdentity((1,3,6,1,4,1,9,9,115,1,2))
_CcfaWildcardAff_ObjectIdentity=ObjectIdentity
ccfaWildcardAff=_CcfaWildcardAff_ObjectIdentity((1,3,6,1,4,1,9,9,115,1,3))
_CcfaWildcardAffTotalBytes_Type=Counter32
_CcfaWildcardAffTotalBytes_Object=MibScalar
ccfaWildcardAffTotalBytes=_CcfaWildcardAffTotalBytes_Object((1,3,6,1,4,1,9,9,115,1,3,1),_CcfaWildcardAffTotalBytes_Type())
ccfaWildcardAffTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffTotalBytes.setStatus(_B)
if mibBuilder.loadTexts:ccfaWildcardAffTotalBytes.setUnits(_D)
_CcfaWildcardAffHCTotalBytes_Type=Counter64
_CcfaWildcardAffHCTotalBytes_Object=MibScalar
ccfaWildcardAffHCTotalBytes=_CcfaWildcardAffHCTotalBytes_Object((1,3,6,1,4,1,9,9,115,1,3,2),_CcfaWildcardAffHCTotalBytes_Type())
ccfaWildcardAffHCTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffHCTotalBytes.setStatus(_B)
if mibBuilder.loadTexts:ccfaWildcardAffHCTotalBytes.setUnits(_D)
_CcfaWildcardAffTotalPackets_Type=Counter32
_CcfaWildcardAffTotalPackets_Object=MibScalar
ccfaWildcardAffTotalPackets=_CcfaWildcardAffTotalPackets_Object((1,3,6,1,4,1,9,9,115,1,3,3),_CcfaWildcardAffTotalPackets_Type())
ccfaWildcardAffTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffTotalPackets.setStatus(_B)
if mibBuilder.loadTexts:ccfaWildcardAffTotalPackets.setUnits(_E)
_CcfaWildcardAffNumOf_Type=Gauge32
_CcfaWildcardAffNumOf_Object=MibScalar
ccfaWildcardAffNumOf=_CcfaWildcardAffNumOf_Object((1,3,6,1,4,1,9,9,115,1,3,4),_CcfaWildcardAffNumOf_Type())
ccfaWildcardAffNumOf.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffNumOf.setStatus(_B)
if mibBuilder.loadTexts:ccfaWildcardAffNumOf.setUnits(_F)
class _CcfaWildcardAffNotifEnabled_Type(TruthValue):defaultValue=2
_CcfaWildcardAffNotifEnabled_Type.__name__=_S
_CcfaWildcardAffNotifEnabled_Object=MibScalar
ccfaWildcardAffNotifEnabled=_CcfaWildcardAffNotifEnabled_Object((1,3,6,1,4,1,9,9,115,1,3,5),_CcfaWildcardAffNotifEnabled_Type())
ccfaWildcardAffNotifEnabled.setMaxAccess(_T)
if mibBuilder.loadTexts:ccfaWildcardAffNotifEnabled.setStatus(_B)
_CcfaWildcardAffTable_Object=MibTable
ccfaWildcardAffTable=_CcfaWildcardAffTable_Object((1,3,6,1,4,1,9,9,115,1,3,6))
if mibBuilder.loadTexts:ccfaWildcardAffTable.setStatus(_B)
_CcfaWildcardAffEntry_Object=MibTableRow
ccfaWildcardAffEntry=_CcfaWildcardAffEntry_Object((1,3,6,1,4,1,9,9,115,1,3,6,1))
ccfaWildcardAffEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:ccfaWildcardAffEntry.setStatus(_B)
_CcfaWildcardAffIndex_Type=CasaWildcardAffIndex
_CcfaWildcardAffIndex_Object=MibTableColumn
ccfaWildcardAffIndex=_CcfaWildcardAffIndex_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,1),_CcfaWildcardAffIndex_Type())
ccfaWildcardAffIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:ccfaWildcardAffIndex.setStatus(_B)
_CcfaWildcardAffSourceAddr_Type=IpAddress
_CcfaWildcardAffSourceAddr_Object=MibTableColumn
ccfaWildcardAffSourceAddr=_CcfaWildcardAffSourceAddr_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,2),_CcfaWildcardAffSourceAddr_Type())
ccfaWildcardAffSourceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffSourceAddr.setStatus(_B)
_CcfaWildcardAffDestinationAddr_Type=IpAddress
_CcfaWildcardAffDestinationAddr_Object=MibTableColumn
ccfaWildcardAffDestinationAddr=_CcfaWildcardAffDestinationAddr_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,3),_CcfaWildcardAffDestinationAddr_Type())
ccfaWildcardAffDestinationAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffDestinationAddr.setStatus(_B)
_CcfaWildcardAffSourcePort_Type=CiscoPort
_CcfaWildcardAffSourcePort_Object=MibTableColumn
ccfaWildcardAffSourcePort=_CcfaWildcardAffSourcePort_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,4),_CcfaWildcardAffSourcePort_Type())
ccfaWildcardAffSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffSourcePort.setStatus(_B)
_CcfaWildcardAffDestinationPort_Type=CiscoPort
_CcfaWildcardAffDestinationPort_Object=MibTableColumn
ccfaWildcardAffDestinationPort=_CcfaWildcardAffDestinationPort_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,5),_CcfaWildcardAffDestinationPort_Type())
ccfaWildcardAffDestinationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffDestinationPort.setStatus(_B)
_CcfaWildcardAffProtocol_Type=CiscoIpProtocol
_CcfaWildcardAffProtocol_Object=MibTableColumn
ccfaWildcardAffProtocol=_CcfaWildcardAffProtocol_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,6),_CcfaWildcardAffProtocol_Type())
ccfaWildcardAffProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffProtocol.setStatus(_B)
_CcfaWildcardAffFragment_Type=TruthValue
_CcfaWildcardAffFragment_Object=MibTableColumn
ccfaWildcardAffFragment=_CcfaWildcardAffFragment_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,7),_CcfaWildcardAffFragment_Type())
ccfaWildcardAffFragment.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffFragment.setStatus(_B)
_CcfaWildcardAffSourceMask_Type=IpAddress
_CcfaWildcardAffSourceMask_Object=MibTableColumn
ccfaWildcardAffSourceMask=_CcfaWildcardAffSourceMask_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,8),_CcfaWildcardAffSourceMask_Type())
ccfaWildcardAffSourceMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffSourceMask.setStatus(_B)
_CcfaWildcardAffDestinationMask_Type=IpAddress
_CcfaWildcardAffDestinationMask_Object=MibTableColumn
ccfaWildcardAffDestinationMask=_CcfaWildcardAffDestinationMask_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,9),_CcfaWildcardAffDestinationMask_Type())
ccfaWildcardAffDestinationMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffDestinationMask.setStatus(_B)
_CcfaWildcardAffSvcManagerAddr_Type=IpAddress
_CcfaWildcardAffSvcManagerAddr_Object=MibTableColumn
ccfaWildcardAffSvcManagerAddr=_CcfaWildcardAffSvcManagerAddr_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,10),_CcfaWildcardAffSvcManagerAddr_Type())
ccfaWildcardAffSvcManagerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffSvcManagerAddr.setStatus(_B)
_CcfaWildcardAffSvcManagerPort_Type=CiscoPort
_CcfaWildcardAffSvcManagerPort_Object=MibTableColumn
ccfaWildcardAffSvcManagerPort=_CcfaWildcardAffSvcManagerPort_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,11),_CcfaWildcardAffSvcManagerPort_Type())
ccfaWildcardAffSvcManagerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffSvcManagerPort.setStatus(_B)
_CcfaWildcardAffBytes_Type=Counter32
_CcfaWildcardAffBytes_Object=MibTableColumn
ccfaWildcardAffBytes=_CcfaWildcardAffBytes_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,12),_CcfaWildcardAffBytes_Type())
ccfaWildcardAffBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffBytes.setStatus(_B)
if mibBuilder.loadTexts:ccfaWildcardAffBytes.setUnits(_D)
_CcfaWildcardAffHCBytes_Type=Counter64
_CcfaWildcardAffHCBytes_Object=MibTableColumn
ccfaWildcardAffHCBytes=_CcfaWildcardAffHCBytes_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,13),_CcfaWildcardAffHCBytes_Type())
ccfaWildcardAffHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffHCBytes.setStatus(_B)
if mibBuilder.loadTexts:ccfaWildcardAffHCBytes.setUnits(_D)
_CcfaWildcardAffPackets_Type=Counter32
_CcfaWildcardAffPackets_Object=MibTableColumn
ccfaWildcardAffPackets=_CcfaWildcardAffPackets_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,14),_CcfaWildcardAffPackets_Type())
ccfaWildcardAffPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffPackets.setStatus(_B)
if mibBuilder.loadTexts:ccfaWildcardAffPackets.setUnits(_E)
_CcfaWildcardAffHCPackets_Type=Counter64
_CcfaWildcardAffHCPackets_Object=MibTableColumn
ccfaWildcardAffHCPackets=_CcfaWildcardAffHCPackets_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,15),_CcfaWildcardAffHCPackets_Type())
ccfaWildcardAffHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffHCPackets.setStatus(_B)
if mibBuilder.loadTexts:ccfaWildcardAffHCPackets.setUnits(_E)
_CcfaWildcardAffFlows_Type=Gauge32
_CcfaWildcardAffFlows_Object=MibTableColumn
ccfaWildcardAffFlows=_CcfaWildcardAffFlows_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,16),_CcfaWildcardAffFlows_Type())
ccfaWildcardAffFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffFlows.setStatus(_B)
if mibBuilder.loadTexts:ccfaWildcardAffFlows.setUnits(_F)
_CcfaWildcardAffInsertTime_Type=DateAndTime
_CcfaWildcardAffInsertTime_Object=MibTableColumn
ccfaWildcardAffInsertTime=_CcfaWildcardAffInsertTime_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,17),_CcfaWildcardAffInsertTime_Type())
ccfaWildcardAffInsertTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffInsertTime.setStatus(_B)
_CcfaWildcardAffInterestTimeouts_Type=Counter32
_CcfaWildcardAffInterestTimeouts_Object=MibTableColumn
ccfaWildcardAffInterestTimeouts=_CcfaWildcardAffInterestTimeouts_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,18),_CcfaWildcardAffInterestTimeouts_Type())
ccfaWildcardAffInterestTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffInterestTimeouts.setStatus(_B)
_CcfaWildcardAffAdvertiseDestAddr_Type=TruthValue
_CcfaWildcardAffAdvertiseDestAddr_Object=MibTableColumn
ccfaWildcardAffAdvertiseDestAddr=_CcfaWildcardAffAdvertiseDestAddr_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,19),_CcfaWildcardAffAdvertiseDestAddr_Type())
ccfaWildcardAffAdvertiseDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffAdvertiseDestAddr.setStatus(_B)
_CcfaWildcardAffInterestAddr_Type=IpAddress
_CcfaWildcardAffInterestAddr_Object=MibTableColumn
ccfaWildcardAffInterestAddr=_CcfaWildcardAffInterestAddr_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,20),_CcfaWildcardAffInterestAddr_Type())
ccfaWildcardAffInterestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffInterestAddr.setStatus(_B)
_CcfaWildcardAffInterestPort_Type=CiscoPort
_CcfaWildcardAffInterestPort_Object=MibTableColumn
ccfaWildcardAffInterestPort=_CcfaWildcardAffInterestPort_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,21),_CcfaWildcardAffInterestPort_Type())
ccfaWildcardAffInterestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffInterestPort.setStatus(_B)
_CcfaWildAffInterestPacketSpec_Type=CasaInterestPacketSpecification
_CcfaWildAffInterestPacketSpec_Object=MibTableColumn
ccfaWildAffInterestPacketSpec=_CcfaWildAffInterestPacketSpec_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,22),_CcfaWildAffInterestPacketSpec_Type())
ccfaWildAffInterestPacketSpec.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildAffInterestPacketSpec.setStatus(_B)
_CcfaWildAffInterestTickelSpec_Type=CasaInterestPacketSpecification
_CcfaWildAffInterestTickelSpec_Object=MibTableColumn
ccfaWildAffInterestTickelSpec=_CcfaWildAffInterestTickelSpec_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,23),_CcfaWildAffInterestTickelSpec_Type())
ccfaWildAffInterestTickelSpec.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildAffInterestTickelSpec.setStatus(_B)
_CcfaWildcardAffDispatch_Type=TruthValue
_CcfaWildcardAffDispatch_Object=MibTableColumn
ccfaWildcardAffDispatch=_CcfaWildcardAffDispatch_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,24),_CcfaWildcardAffDispatch_Type())
ccfaWildcardAffDispatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffDispatch.setStatus(_B)
_CcfaWildcardAffDispatchAddr_Type=IpAddress
_CcfaWildcardAffDispatchAddr_Object=MibTableColumn
ccfaWildcardAffDispatchAddr=_CcfaWildcardAffDispatchAddr_Object((1,3,6,1,4,1,9,9,115,1,3,6,1,25),_CcfaWildcardAffDispatchAddr_Type())
ccfaWildcardAffDispatchAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffDispatchAddr.setStatus(_B)
_CcfaWildcardAffHiWtrMark_Type=Unsigned32
_CcfaWildcardAffHiWtrMark_Object=MibScalar
ccfaWildcardAffHiWtrMark=_CcfaWildcardAffHiWtrMark_Object((1,3,6,1,4,1,9,9,115,1,3,7),_CcfaWildcardAffHiWtrMark_Type())
ccfaWildcardAffHiWtrMark.setMaxAccess(_T)
if mibBuilder.loadTexts:ccfaWildcardAffHiWtrMark.setStatus(_B)
if mibBuilder.loadTexts:ccfaWildcardAffHiWtrMark.setUnits(_F)
_CcfaWildAffCacheHiWtrMarkReset_Type=TimeStamp
_CcfaWildAffCacheHiWtrMarkReset_Object=MibScalar
ccfaWildAffCacheHiWtrMarkReset=_CcfaWildAffCacheHiWtrMarkReset_Object((1,3,6,1,4,1,9,9,115,1,3,8),_CcfaWildAffCacheHiWtrMarkReset_Type())
ccfaWildAffCacheHiWtrMarkReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildAffCacheHiWtrMarkReset.setStatus(_B)
_CcfaWildcardAffDenies_Type=Counter32
_CcfaWildcardAffDenies_Object=MibScalar
ccfaWildcardAffDenies=_CcfaWildcardAffDenies_Object((1,3,6,1,4,1,9,9,115,1,3,9),_CcfaWildcardAffDenies_Type())
ccfaWildcardAffDenies.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffDenies.setStatus(_B)
if mibBuilder.loadTexts:ccfaWildcardAffDenies.setUnits(_F)
_CcfaWildcardAffDrops_Type=Counter32
_CcfaWildcardAffDrops_Object=MibScalar
ccfaWildcardAffDrops=_CcfaWildcardAffDrops_Object((1,3,6,1,4,1,9,9,115,1,3,10),_CcfaWildcardAffDrops_Type())
ccfaWildcardAffDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaWildcardAffDrops.setStatus(_B)
if mibBuilder.loadTexts:ccfaWildcardAffDrops.setUnits(_F)
_CcfaDispatchStats_ObjectIdentity=ObjectIdentity
ccfaDispatchStats=_CcfaDispatchStats_ObjectIdentity((1,3,6,1,4,1,9,9,115,1,4))
_CcfaDispatchStatsTable_Object=MibTable
ccfaDispatchStatsTable=_CcfaDispatchStatsTable_Object((1,3,6,1,4,1,9,9,115,1,4,1))
if mibBuilder.loadTexts:ccfaDispatchStatsTable.setStatus(_B)
_CcfaDispatchStatsEntry_Object=MibTableRow
ccfaDispatchStatsEntry=_CcfaDispatchStatsEntry_Object((1,3,6,1,4,1,9,9,115,1,4,1,1))
ccfaDispatchStatsEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:ccfaDispatchStatsEntry.setStatus(_B)
_CcfaDispatchAddress_Type=IpAddress
_CcfaDispatchAddress_Object=MibTableColumn
ccfaDispatchAddress=_CcfaDispatchAddress_Object((1,3,6,1,4,1,9,9,115,1,4,1,1,1),_CcfaDispatchAddress_Type())
ccfaDispatchAddress.setMaxAccess(_Q)
if mibBuilder.loadTexts:ccfaDispatchAddress.setStatus(_B)
_CcfaDispatchBytesIn_Type=Counter32
_CcfaDispatchBytesIn_Object=MibTableColumn
ccfaDispatchBytesIn=_CcfaDispatchBytesIn_Object((1,3,6,1,4,1,9,9,115,1,4,1,1,2),_CcfaDispatchBytesIn_Type())
ccfaDispatchBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaDispatchBytesIn.setStatus(_B)
if mibBuilder.loadTexts:ccfaDispatchBytesIn.setUnits(_D)
_CcfaDispatchHCBytesIn_Type=Counter64
_CcfaDispatchHCBytesIn_Object=MibTableColumn
ccfaDispatchHCBytesIn=_CcfaDispatchHCBytesIn_Object((1,3,6,1,4,1,9,9,115,1,4,1,1,3),_CcfaDispatchHCBytesIn_Type())
ccfaDispatchHCBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaDispatchHCBytesIn.setStatus(_B)
if mibBuilder.loadTexts:ccfaDispatchHCBytesIn.setUnits(_D)
_CcfaDispatchBytesOut_Type=Counter32
_CcfaDispatchBytesOut_Object=MibTableColumn
ccfaDispatchBytesOut=_CcfaDispatchBytesOut_Object((1,3,6,1,4,1,9,9,115,1,4,1,1,4),_CcfaDispatchBytesOut_Type())
ccfaDispatchBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaDispatchBytesOut.setStatus(_B)
if mibBuilder.loadTexts:ccfaDispatchBytesOut.setUnits(_D)
_CcfaDispatchHCBytesOut_Type=Counter64
_CcfaDispatchHCBytesOut_Object=MibTableColumn
ccfaDispatchHCBytesOut=_CcfaDispatchHCBytesOut_Object((1,3,6,1,4,1,9,9,115,1,4,1,1,5),_CcfaDispatchHCBytesOut_Type())
ccfaDispatchHCBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaDispatchHCBytesOut.setStatus(_B)
if mibBuilder.loadTexts:ccfaDispatchHCBytesOut.setUnits(_D)
_CcfaDispatchPacketsIn_Type=Counter32
_CcfaDispatchPacketsIn_Object=MibTableColumn
ccfaDispatchPacketsIn=_CcfaDispatchPacketsIn_Object((1,3,6,1,4,1,9,9,115,1,4,1,1,6),_CcfaDispatchPacketsIn_Type())
ccfaDispatchPacketsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaDispatchPacketsIn.setStatus(_B)
if mibBuilder.loadTexts:ccfaDispatchPacketsIn.setUnits(_E)
_CcfaDispatchHCPacketsIn_Type=Counter64
_CcfaDispatchHCPacketsIn_Object=MibTableColumn
ccfaDispatchHCPacketsIn=_CcfaDispatchHCPacketsIn_Object((1,3,6,1,4,1,9,9,115,1,4,1,1,7),_CcfaDispatchHCPacketsIn_Type())
ccfaDispatchHCPacketsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaDispatchHCPacketsIn.setStatus(_B)
if mibBuilder.loadTexts:ccfaDispatchHCPacketsIn.setUnits(_E)
_CcfaDispatchPacketsOut_Type=Counter32
_CcfaDispatchPacketsOut_Object=MibTableColumn
ccfaDispatchPacketsOut=_CcfaDispatchPacketsOut_Object((1,3,6,1,4,1,9,9,115,1,4,1,1,8),_CcfaDispatchPacketsOut_Type())
ccfaDispatchPacketsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaDispatchPacketsOut.setStatus(_B)
if mibBuilder.loadTexts:ccfaDispatchPacketsOut.setUnits(_E)
_CcfaDispatchHCPacketsOut_Type=Counter64
_CcfaDispatchHCPacketsOut_Object=MibTableColumn
ccfaDispatchHCPacketsOut=_CcfaDispatchHCPacketsOut_Object((1,3,6,1,4,1,9,9,115,1,4,1,1,9),_CcfaDispatchHCPacketsOut_Type())
ccfaDispatchHCPacketsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaDispatchHCPacketsOut.setStatus(_B)
if mibBuilder.loadTexts:ccfaDispatchHCPacketsOut.setUnits(_E)
_CcfaDispatchFlows_Type=Gauge32
_CcfaDispatchFlows_Object=MibTableColumn
ccfaDispatchFlows=_CcfaDispatchFlows_Object((1,3,6,1,4,1,9,9,115,1,4,1,1,10),_CcfaDispatchFlows_Type())
ccfaDispatchFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaDispatchFlows.setStatus(_B)
if mibBuilder.loadTexts:ccfaDispatchFlows.setUnits(_F)
_CcfaAdvertisedDispatchTable_Object=MibTable
ccfaAdvertisedDispatchTable=_CcfaAdvertisedDispatchTable_Object((1,3,6,1,4,1,9,9,115,1,4,2))
if mibBuilder.loadTexts:ccfaAdvertisedDispatchTable.setStatus(_B)
_CcfaAdvertisedDispatchEntry_Object=MibTableRow
ccfaAdvertisedDispatchEntry=_CcfaAdvertisedDispatchEntry_Object((1,3,6,1,4,1,9,9,115,1,4,2,1))
ccfaAdvertisedDispatchEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:ccfaAdvertisedDispatchEntry.setStatus(_B)
_CcfaAdvertisedAddress_Type=IpAddress
_CcfaAdvertisedAddress_Object=MibTableColumn
ccfaAdvertisedAddress=_CcfaAdvertisedAddress_Object((1,3,6,1,4,1,9,9,115,1,4,2,1,1),_CcfaAdvertisedAddress_Type())
ccfaAdvertisedAddress.setMaxAccess(_Q)
if mibBuilder.loadTexts:ccfaAdvertisedAddress.setStatus(_B)
_CcfaAdvertisedDispatchAddress_Type=IpAddress
_CcfaAdvertisedDispatchAddress_Object=MibTableColumn
ccfaAdvertisedDispatchAddress=_CcfaAdvertisedDispatchAddress_Object((1,3,6,1,4,1,9,9,115,1,4,2,1,2),_CcfaAdvertisedDispatchAddress_Type())
ccfaAdvertisedDispatchAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccfaAdvertisedDispatchAddress.setStatus(_B)
_CiscoCasaFaMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoCasaFaMIBNotificationPrefix=_CiscoCasaFaMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,115,2))
_CiscoCasaFaMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoCasaFaMIBNotifications=_CiscoCasaFaMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,115,2,0))
_CiscoCasaFaMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCasaFaMIBConformance=_CiscoCasaFaMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,115,3))
_CiscoCasaFaMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCasaFaMIBCompliances=_CiscoCasaFaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,115,3,1))
_CiscoCasaFaMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCasaFaMIBGroups=_CiscoCasaFaMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,115,3,2))
ciscoCasaFaWildcardAffGroup=ObjectGroup((1,3,6,1,4,1,9,9,115,3,2,3))
ciscoCasaFaWildcardAffGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_R),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:ciscoCasaFaWildcardAffGroup.setStatus(_B)
ciscoCasaFaDispatchGroup=ObjectGroup((1,3,6,1,4,1,9,9,115,3,2,5))
ciscoCasaFaDispatchGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:ciscoCasaFaDispatchGroup.setStatus(_B)
ciscoCasaFaADGroup=ObjectGroup((1,3,6,1,4,1,9,9,115,3,2,6))
ciscoCasaFaADGroup.setObjects((_A,_A2))
if mibBuilder.loadTexts:ciscoCasaFaADGroup.setStatus(_B)
ciscoCasaFaWildcardAffCreated=NotificationType((1,3,6,1,4,1,9,9,115,2,1))
ciscoCasaFaWildcardAffCreated.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoCasaFaWildcardAffCreated.setStatus(_B)
ciscoCasaFaWildcardAffDeleted=NotificationType((1,3,6,1,4,1,9,9,115,2,2))
ciscoCasaFaWildcardAffDeleted.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_R)))
if mibBuilder.loadTexts:ciscoCasaFaWildcardAffDeleted.setStatus(_B)
ciscoCasaFaNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,115,3,2,7))
ciscoCasaFaNotifGroup.setObjects(*((_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:ciscoCasaFaNotifGroup.setStatus(_B)
ciscoCasaFaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,115,3,1,1))
ciscoCasaFaMIBCompliance.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:ciscoCasaFaMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CasaWildcardAffIndex':CasaWildcardAffIndex,'CasaInterestPacketSpecification':CasaInterestPacketSpecification,'ciscoCasaFaMIB':ciscoCasaFaMIB,'ciscoCasaFaMIBObjects':ciscoCasaFaMIBObjects,'ccfaGlobal':ccfaGlobal,'ccfaStats':ccfaStats,'ccfaWildcardAff':ccfaWildcardAff,_X:ccfaWildcardAffTotalBytes,_Y:ccfaWildcardAffHCTotalBytes,_Z:ccfaWildcardAffTotalPackets,_a:ccfaWildcardAffNumOf,_b:ccfaWildcardAffNotifEnabled,'ccfaWildcardAffTable':ccfaWildcardAffTable,'ccfaWildcardAffEntry':ccfaWildcardAffEntry,_U:ccfaWildcardAffIndex,_G:ccfaWildcardAffSourceAddr,_H:ccfaWildcardAffDestinationAddr,_I:ccfaWildcardAffSourcePort,_J:ccfaWildcardAffDestinationPort,_K:ccfaWildcardAffProtocol,_L:ccfaWildcardAffFragment,_M:ccfaWildcardAffSourceMask,_N:ccfaWildcardAffDestinationMask,_O:ccfaWildcardAffSvcManagerAddr,_P:ccfaWildcardAffSvcManagerPort,_g:ccfaWildcardAffBytes,_h:ccfaWildcardAffHCBytes,_i:ccfaWildcardAffPackets,_j:ccfaWildcardAffHCPackets,_R:ccfaWildcardAffFlows,_k:ccfaWildcardAffInsertTime,_l:ccfaWildcardAffInterestTimeouts,_m:ccfaWildcardAffAdvertiseDestAddr,_n:ccfaWildcardAffInterestAddr,_o:ccfaWildcardAffInterestPort,_p:ccfaWildAffInterestPacketSpec,_q:ccfaWildAffInterestTickelSpec,_r:ccfaWildcardAffDispatch,_s:ccfaWildcardAffDispatchAddr,_c:ccfaWildcardAffHiWtrMark,_d:ccfaWildAffCacheHiWtrMarkReset,_e:ccfaWildcardAffDenies,_f:ccfaWildcardAffDrops,'ccfaDispatchStats':ccfaDispatchStats,'ccfaDispatchStatsTable':ccfaDispatchStatsTable,'ccfaDispatchStatsEntry':ccfaDispatchStatsEntry,_V:ccfaDispatchAddress,_t:ccfaDispatchBytesIn,_u:ccfaDispatchHCBytesIn,_v:ccfaDispatchBytesOut,_w:ccfaDispatchHCBytesOut,_x:ccfaDispatchPacketsIn,_y:ccfaDispatchHCPacketsIn,_z:ccfaDispatchPacketsOut,_A0:ccfaDispatchHCPacketsOut,_A1:ccfaDispatchFlows,'ccfaAdvertisedDispatchTable':ccfaAdvertisedDispatchTable,'ccfaAdvertisedDispatchEntry':ccfaAdvertisedDispatchEntry,_W:ccfaAdvertisedAddress,_A2:ccfaAdvertisedDispatchAddress,'ciscoCasaFaMIBNotificationPrefix':ciscoCasaFaMIBNotificationPrefix,'ciscoCasaFaMIBNotifications':ciscoCasaFaMIBNotifications,_A3:ciscoCasaFaWildcardAffCreated,_A4:ciscoCasaFaWildcardAffDeleted,'ciscoCasaFaMIBConformance':ciscoCasaFaMIBConformance,'ciscoCasaFaMIBCompliances':ciscoCasaFaMIBCompliances,'ciscoCasaFaMIBCompliance':ciscoCasaFaMIBCompliance,'ciscoCasaFaMIBGroups':ciscoCasaFaMIBGroups,_A5:ciscoCasaFaWildcardAffGroup,_A6:ciscoCasaFaDispatchGroup,_A7:ciscoCasaFaADGroup,_A8:ciscoCasaFaNotifGroup})