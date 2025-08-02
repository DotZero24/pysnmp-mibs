_A6='adGenEthernetDslamFlowRev2NameLookupName'
_A5='adGenEthernetDslamFlowRev2Index'
_A4='adGenEthernetDslamFlowShaperLookupAlias'
_A3='adGenEthernetDslamFlowProfileLookupAlias'
_A2='adGenSubscriberAccessStaticIpAddress'
_A1='adGenEthernetDslamFlowShaperPrioritySet'
_A0='adGenEthernetDslamFlowShaperInterfaceLogicalIndex'
_z='adGenEthernetDslamFlowNameLookupName'
_y='adGenEthernetDslamFlowProfileIndex'
_x='active'
_w='inProgress'
_v='notActivated'
_u='forking'
_t='snooping'
_s='forward'
_r='ethernet'
_q='autoDetect'
_p='pppoaVcMux'
_o='bidirectional'
_n='downstream'
_m='upstream'
_l='adGenEthernetInterfaceLogicalIndex'
_k='adGenEthernetDslamFlowIndex'
_j='TruthValue'
_i='ifIndex'
_h='IF-MIB'
_g='adGenMiniDslam3gMacAddress'
_f='ADTRAN-TAMINIDSLAM3G-MIB'
_e='adGenPortInfoIndex'
_d='ADTRAN-GENPORT-MIB'
_c='sameAsDhcpv4'
_b='authenticate'
_a='proxy'
_Z='sysName'
_Y='SNMPv2-MIB'
_X='adTAeSCUTrapAlarmLevel'
_W='ADTRAN-TAeSCUEXT1-MIB'
_V='adTrapInformSeqNum'
_U='ADTRAN-GENTRAPINFORM-MIB'
_T='snoop'
_S='mapped'
_R='marked'
_Q='inherit'
_P='true'
_O='false'
_N='block'
_M='not-accessible'
_L='transparent'
_K='ADTRAN-ETHERNET-DSLAM-FLOW-MIB'
_J='adGenSlotInfoIndex'
_I='ADTRAN-GENSLOT-MIB'
_H='DisplayString'
_G='disabled'
_F='enabled'
_E='notApplicable'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortInfoIndex,=mibBuilder.importSymbols(_d,_e)
adGenSlotInfoIndex,=mibBuilder.importSymbols(_I,_J)
adTrapInformSeqNum,=mibBuilder.importSymbols(_U,_V)
adGenEthernetDslamFlow,adGenEthernetDslamFlowID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenEthernetDslamFlow','adGenEthernetDslamFlowID')
GenSystemInterfaceType,=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-TC-MIB','GenSystemInterfaceType')
adGenMiniDslam3gMacAddress,=mibBuilder.importSymbols(_f,_g)
adTAeSCUTrapAlarmLevel,=mibBuilder.importSymbols(_W,_X)
ifIndex,=mibBuilder.importSymbols(_h,_i)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_Y,_Z)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention',_j)
adGenEthernetDslamFlowMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,2,2))
if mibBuilder.loadTexts:adGenEthernetDslamFlowMIB.setRevisions(('2021-03-03 00:00','2016-01-21 00:00','2014-09-12 00:00','2014-05-13 00:00','2013-11-08 00:00','2013-09-12 00:00','2013-02-19 00:00','2013-01-03 00:00','2012-11-06 00:00','2012-09-13 00:00','2012-07-30 00:00','2012-07-17 00:00','2012-06-27 11:50','2012-04-20 11:50','2012-04-09 11:50','2011-12-21 00:00','2011-11-28 00:00','2011-09-19 00:00','2011-08-22 00:00','2011-08-03 00:00','2011-06-01 00:00','2011-03-24 00:00','2007-09-11 00:00'))
_AdGenEthernetInterfaceTable_Object=MibTable
adGenEthernetInterfaceTable=_AdGenEthernetInterfaceTable_Object((1,3,6,1,4,1,664,5,70,2,1))
if mibBuilder.loadTexts:adGenEthernetInterfaceTable.setStatus(_A)
_AdGenEthernetInterfaceEntry_Object=MibTableRow
adGenEthernetInterfaceEntry=_AdGenEthernetInterfaceEntry_Object((1,3,6,1,4,1,664,5,70,2,1,1))
adGenEthernetInterfaceEntry.setIndexNames((0,_h,_i),(0,_K,_l))
if mibBuilder.loadTexts:adGenEthernetInterfaceEntry.setStatus(_A)
_AdGenEthernetInterfaceLogicalIndex_Type=Integer32
_AdGenEthernetInterfaceLogicalIndex_Object=MibTableColumn
adGenEthernetInterfaceLogicalIndex=_AdGenEthernetInterfaceLogicalIndex_Object((1,3,6,1,4,1,664,5,70,2,1,1,1),_AdGenEthernetInterfaceLogicalIndex_Type())
adGenEthernetInterfaceLogicalIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenEthernetInterfaceLogicalIndex.setStatus(_A)
_AdGenEthernetInterfaceMaxMACAddresses_Type=Integer32
_AdGenEthernetInterfaceMaxMACAddresses_Object=MibTableColumn
adGenEthernetInterfaceMaxMACAddresses=_AdGenEthernetInterfaceMaxMACAddresses_Object((1,3,6,1,4,1,664,5,70,2,1,1,2),_AdGenEthernetInterfaceMaxMACAddresses_Type())
adGenEthernetInterfaceMaxMACAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetInterfaceMaxMACAddresses.setStatus(_A)
_AdGenEthernetInterfaceFlowList_Type=DisplayString
_AdGenEthernetInterfaceFlowList_Object=MibTableColumn
adGenEthernetInterfaceFlowList=_AdGenEthernetInterfaceFlowList_Object((1,3,6,1,4,1,664,5,70,2,1,1,3),_AdGenEthernetInterfaceFlowList_Type())
adGenEthernetInterfaceFlowList.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetInterfaceFlowList.setStatus(_A)
class _AdGenEthernetInterfaceSourceAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AdGenEthernetInterfaceSourceAuthentication_Type.__name__=_C
_AdGenEthernetInterfaceSourceAuthentication_Object=MibTableColumn
adGenEthernetInterfaceSourceAuthentication=_AdGenEthernetInterfaceSourceAuthentication_Object((1,3,6,1,4,1,664,5,70,2,1,1,4),_AdGenEthernetInterfaceSourceAuthentication_Type())
adGenEthernetInterfaceSourceAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetInterfaceSourceAuthentication.setStatus(_A)
_AdGenEthernetInterfaceType_Type=GenSystemInterfaceType
_AdGenEthernetInterfaceType_Object=MibTableColumn
adGenEthernetInterfaceType=_AdGenEthernetInterfaceType_Object((1,3,6,1,4,1,664,5,70,2,1,1,5),_AdGenEthernetInterfaceType_Type())
adGenEthernetInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetInterfaceType.setStatus(_A)
_AdGenEthernetInterfaceTypeSpecific_Type=OctetString
_AdGenEthernetInterfaceTypeSpecific_Object=MibTableColumn
adGenEthernetInterfaceTypeSpecific=_AdGenEthernetInterfaceTypeSpecific_Object((1,3,6,1,4,1,664,5,70,2,1,1,6),_AdGenEthernetInterfaceTypeSpecific_Type())
adGenEthernetInterfaceTypeSpecific.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetInterfaceTypeSpecific.setStatus(_A)
_AdGenEthernetDslamFlowTable_Object=MibTable
adGenEthernetDslamFlowTable=_AdGenEthernetDslamFlowTable_Object((1,3,6,1,4,1,664,5,70,2,2))
if mibBuilder.loadTexts:adGenEthernetDslamFlowTable.setStatus(_A)
_AdGenEthernetDslamFlowEntry_Object=MibTableRow
adGenEthernetDslamFlowEntry=_AdGenEthernetDslamFlowEntry_Object((1,3,6,1,4,1,664,5,70,2,2,1))
adGenEthernetDslamFlowEntry.setIndexNames((0,_I,_J),(0,_K,_k))
if mibBuilder.loadTexts:adGenEthernetDslamFlowEntry.setStatus(_A)
_AdGenEthernetDslamFlowIndex_Type=Integer32
_AdGenEthernetDslamFlowIndex_Object=MibTableColumn
adGenEthernetDslamFlowIndex=_AdGenEthernetDslamFlowIndex_Object((1,3,6,1,4,1,664,5,70,2,2,1,1),_AdGenEthernetDslamFlowIndex_Type())
adGenEthernetDslamFlowIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenEthernetDslamFlowIndex.setStatus(_A)
class _AdGenEthernetDslamFlowName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenEthernetDslamFlowName_Type.__name__=_H
_AdGenEthernetDslamFlowName_Object=MibTableColumn
adGenEthernetDslamFlowName=_AdGenEthernetDslamFlowName_Object((1,3,6,1,4,1,664,5,70,2,2,1,2),_AdGenEthernetDslamFlowName_Type())
adGenEthernetDslamFlowName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowName.setStatus(_A)
class _AdGenEthernetDslamFlowTrafficDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_m,1),(_n,2),(_o,3)))
_AdGenEthernetDslamFlowTrafficDirection_Type.__name__=_C
_AdGenEthernetDslamFlowTrafficDirection_Object=MibTableColumn
adGenEthernetDslamFlowTrafficDirection=_AdGenEthernetDslamFlowTrafficDirection_Object((1,3,6,1,4,1,664,5,70,2,2,1,3),_AdGenEthernetDslamFlowTrafficDirection_Type())
adGenEthernetDslamFlowTrafficDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowTrafficDirection.setStatus(_A)
class _AdGenEthernetDslamFlowNetworkSTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_AdGenEthernetDslamFlowNetworkSTag_Type.__name__=_C
_AdGenEthernetDslamFlowNetworkSTag_Object=MibTableColumn
adGenEthernetDslamFlowNetworkSTag=_AdGenEthernetDslamFlowNetworkSTag_Object((1,3,6,1,4,1,664,5,70,2,2,1,4),_AdGenEthernetDslamFlowNetworkSTag_Type())
adGenEthernetDslamFlowNetworkSTag.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowNetworkSTag.setStatus(_A)
class _AdGenEthernetDslamFlowNetworkCTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4096))
_AdGenEthernetDslamFlowNetworkCTag_Type.__name__=_C
_AdGenEthernetDslamFlowNetworkCTag_Object=MibTableColumn
adGenEthernetDslamFlowNetworkCTag=_AdGenEthernetDslamFlowNetworkCTag_Object((1,3,6,1,4,1,664,5,70,2,2,1,5),_AdGenEthernetDslamFlowNetworkCTag_Type())
adGenEthernetDslamFlowNetworkCTag.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowNetworkCTag.setStatus(_A)
class _AdGenEthernetDslamFlowCEVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4098))
_AdGenEthernetDslamFlowCEVlan_Type.__name__=_C
_AdGenEthernetDslamFlowCEVlan_Object=MibTableColumn
adGenEthernetDslamFlowCEVlan=_AdGenEthernetDslamFlowCEVlan_Object((1,3,6,1,4,1,664,5,70,2,2,1,6),_AdGenEthernetDslamFlowCEVlan_Type())
adGenEthernetDslamFlowCEVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowCEVlan.setStatus(_A)
_AdGenEthernetDslamFlowDownstreamForwardingMode_Type=Integer32
_AdGenEthernetDslamFlowDownstreamForwardingMode_Object=MibTableColumn
adGenEthernetDslamFlowDownstreamForwardingMode=_AdGenEthernetDslamFlowDownstreamForwardingMode_Object((1,3,6,1,4,1,664,5,70,2,2,1,7),_AdGenEthernetDslamFlowDownstreamForwardingMode_Type())
adGenEthernetDslamFlowDownstreamForwardingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDownstreamForwardingMode.setStatus(_A)
class _AdGenEthernetDslamFlowDownstreamPbitMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_AdGenEthernetDslamFlowDownstreamPbitMethod_Type.__name__=_C
_AdGenEthernetDslamFlowDownstreamPbitMethod_Object=MibTableColumn
adGenEthernetDslamFlowDownstreamPbitMethod=_AdGenEthernetDslamFlowDownstreamPbitMethod_Object((1,3,6,1,4,1,664,5,70,2,2,1,8),_AdGenEthernetDslamFlowDownstreamPbitMethod_Type())
adGenEthernetDslamFlowDownstreamPbitMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDownstreamPbitMethod.setStatus(_A)
class _AdGenEthernetDslamFlowDownstreamPbitMarking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenEthernetDslamFlowDownstreamPbitMarking_Type.__name__=_C
_AdGenEthernetDslamFlowDownstreamPbitMarking_Object=MibTableColumn
adGenEthernetDslamFlowDownstreamPbitMarking=_AdGenEthernetDslamFlowDownstreamPbitMarking_Object((1,3,6,1,4,1,664,5,70,2,2,1,9),_AdGenEthernetDslamFlowDownstreamPbitMarking_Type())
adGenEthernetDslamFlowDownstreamPbitMarking.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDownstreamPbitMarking.setStatus(_A)
_AdGenEthernetDslamFlowDownstreamPbitMapping_Type=Integer32
_AdGenEthernetDslamFlowDownstreamPbitMapping_Object=MibTableColumn
adGenEthernetDslamFlowDownstreamPbitMapping=_AdGenEthernetDslamFlowDownstreamPbitMapping_Object((1,3,6,1,4,1,664,5,70,2,2,1,10),_AdGenEthernetDslamFlowDownstreamPbitMapping_Type())
adGenEthernetDslamFlowDownstreamPbitMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDownstreamPbitMapping.setStatus(_A)
class _AdGenEthernetDslamFlowNetworkIngressPbit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenEthernetDslamFlowNetworkIngressPbit_Type.__name__=_C
_AdGenEthernetDslamFlowNetworkIngressPbit_Object=MibTableColumn
adGenEthernetDslamFlowNetworkIngressPbit=_AdGenEthernetDslamFlowNetworkIngressPbit_Object((1,3,6,1,4,1,664,5,70,2,2,1,11),_AdGenEthernetDslamFlowNetworkIngressPbit_Type())
adGenEthernetDslamFlowNetworkIngressPbit.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowNetworkIngressPbit.setStatus(_A)
_AdGenEthernetDslamFlowNetworkIngressEtherType_Type=Integer32
_AdGenEthernetDslamFlowNetworkIngressEtherType_Object=MibTableColumn
adGenEthernetDslamFlowNetworkIngressEtherType=_AdGenEthernetDslamFlowNetworkIngressEtherType_Object((1,3,6,1,4,1,664,5,70,2,2,1,12),_AdGenEthernetDslamFlowNetworkIngressEtherType_Type())
adGenEthernetDslamFlowNetworkIngressEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowNetworkIngressEtherType.setStatus(_A)
class _AdGenEthernetDslamFlowNetworkIngressDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_AdGenEthernetDslamFlowNetworkIngressDSCP_Type.__name__=_C
_AdGenEthernetDslamFlowNetworkIngressDSCP_Object=MibTableColumn
adGenEthernetDslamFlowNetworkIngressDSCP=_AdGenEthernetDslamFlowNetworkIngressDSCP_Object((1,3,6,1,4,1,664,5,70,2,2,1,13),_AdGenEthernetDslamFlowNetworkIngressDSCP_Type())
adGenEthernetDslamFlowNetworkIngressDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowNetworkIngressDSCP.setStatus(_A)
_AdGenEthernetDslamFlowNetworkIngressIPProtocolID_Type=Integer32
_AdGenEthernetDslamFlowNetworkIngressIPProtocolID_Object=MibTableColumn
adGenEthernetDslamFlowNetworkIngressIPProtocolID=_AdGenEthernetDslamFlowNetworkIngressIPProtocolID_Object((1,3,6,1,4,1,664,5,70,2,2,1,14),_AdGenEthernetDslamFlowNetworkIngressIPProtocolID_Type())
adGenEthernetDslamFlowNetworkIngressIPProtocolID.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowNetworkIngressIPProtocolID.setStatus(_A)
_AdGenEthernetDslamFlowUpstreamForwardingMode_Type=Integer32
_AdGenEthernetDslamFlowUpstreamForwardingMode_Object=MibTableColumn
adGenEthernetDslamFlowUpstreamForwardingMode=_AdGenEthernetDslamFlowUpstreamForwardingMode_Object((1,3,6,1,4,1,664,5,70,2,2,1,15),_AdGenEthernetDslamFlowUpstreamForwardingMode_Type())
adGenEthernetDslamFlowUpstreamForwardingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowUpstreamForwardingMode.setStatus(_A)
class _AdGenEthernetDslamFlowUpstreamSTagPbitMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_AdGenEthernetDslamFlowUpstreamSTagPbitMethod_Type.__name__=_C
_AdGenEthernetDslamFlowUpstreamSTagPbitMethod_Object=MibTableColumn
adGenEthernetDslamFlowUpstreamSTagPbitMethod=_AdGenEthernetDslamFlowUpstreamSTagPbitMethod_Object((1,3,6,1,4,1,664,5,70,2,2,1,16),_AdGenEthernetDslamFlowUpstreamSTagPbitMethod_Type())
adGenEthernetDslamFlowUpstreamSTagPbitMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowUpstreamSTagPbitMethod.setStatus(_A)
class _AdGenEthernetDslamFlowUpstreamSTagPbitMarking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenEthernetDslamFlowUpstreamSTagPbitMarking_Type.__name__=_C
_AdGenEthernetDslamFlowUpstreamSTagPbitMarking_Object=MibTableColumn
adGenEthernetDslamFlowUpstreamSTagPbitMarking=_AdGenEthernetDslamFlowUpstreamSTagPbitMarking_Object((1,3,6,1,4,1,664,5,70,2,2,1,17),_AdGenEthernetDslamFlowUpstreamSTagPbitMarking_Type())
adGenEthernetDslamFlowUpstreamSTagPbitMarking.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowUpstreamSTagPbitMarking.setStatus(_A)
_AdGenEthernetDslamFlowUpstreamSTagPbitMapping_Type=Integer32
_AdGenEthernetDslamFlowUpstreamSTagPbitMapping_Object=MibTableColumn
adGenEthernetDslamFlowUpstreamSTagPbitMapping=_AdGenEthernetDslamFlowUpstreamSTagPbitMapping_Object((1,3,6,1,4,1,664,5,70,2,2,1,18),_AdGenEthernetDslamFlowUpstreamSTagPbitMapping_Type())
adGenEthernetDslamFlowUpstreamSTagPbitMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowUpstreamSTagPbitMapping.setStatus(_A)
class _AdGenEthernetDslamFlowUpstreamCTagPbitMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_AdGenEthernetDslamFlowUpstreamCTagPbitMethod_Type.__name__=_C
_AdGenEthernetDslamFlowUpstreamCTagPbitMethod_Object=MibTableColumn
adGenEthernetDslamFlowUpstreamCTagPbitMethod=_AdGenEthernetDslamFlowUpstreamCTagPbitMethod_Object((1,3,6,1,4,1,664,5,70,2,2,1,19),_AdGenEthernetDslamFlowUpstreamCTagPbitMethod_Type())
adGenEthernetDslamFlowUpstreamCTagPbitMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowUpstreamCTagPbitMethod.setStatus(_A)
class _AdGenEthernetDslamFlowUpstreamCTagPbitMarking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenEthernetDslamFlowUpstreamCTagPbitMarking_Type.__name__=_C
_AdGenEthernetDslamFlowUpstreamCTagPbitMarking_Object=MibTableColumn
adGenEthernetDslamFlowUpstreamCTagPbitMarking=_AdGenEthernetDslamFlowUpstreamCTagPbitMarking_Object((1,3,6,1,4,1,664,5,70,2,2,1,20),_AdGenEthernetDslamFlowUpstreamCTagPbitMarking_Type())
adGenEthernetDslamFlowUpstreamCTagPbitMarking.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowUpstreamCTagPbitMarking.setStatus(_A)
_AdGenEthernetDslamFlowUpstreamCTagPbitMapping_Type=Integer32
_AdGenEthernetDslamFlowUpstreamCTagPbitMapping_Object=MibTableColumn
adGenEthernetDslamFlowUpstreamCTagPbitMapping=_AdGenEthernetDslamFlowUpstreamCTagPbitMapping_Object((1,3,6,1,4,1,664,5,70,2,2,1,21),_AdGenEthernetDslamFlowUpstreamCTagPbitMapping_Type())
adGenEthernetDslamFlowUpstreamCTagPbitMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowUpstreamCTagPbitMapping.setStatus(_A)
class _AdGenEthernetDslamFlowCustomerIngressPbit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenEthernetDslamFlowCustomerIngressPbit_Type.__name__=_C
_AdGenEthernetDslamFlowCustomerIngressPbit_Object=MibTableColumn
adGenEthernetDslamFlowCustomerIngressPbit=_AdGenEthernetDslamFlowCustomerIngressPbit_Object((1,3,6,1,4,1,664,5,70,2,2,1,22),_AdGenEthernetDslamFlowCustomerIngressPbit_Type())
adGenEthernetDslamFlowCustomerIngressPbit.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowCustomerIngressPbit.setStatus(_A)
_AdGenEthernetDslamFlowCustomerIngressEtherType_Type=Integer32
_AdGenEthernetDslamFlowCustomerIngressEtherType_Object=MibTableColumn
adGenEthernetDslamFlowCustomerIngressEtherType=_AdGenEthernetDslamFlowCustomerIngressEtherType_Object((1,3,6,1,4,1,664,5,70,2,2,1,23),_AdGenEthernetDslamFlowCustomerIngressEtherType_Type())
adGenEthernetDslamFlowCustomerIngressEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowCustomerIngressEtherType.setStatus(_A)
class _AdGenEthernetDslamFlowCustomerIngressDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_AdGenEthernetDslamFlowCustomerIngressDSCP_Type.__name__=_C
_AdGenEthernetDslamFlowCustomerIngressDSCP_Object=MibTableColumn
adGenEthernetDslamFlowCustomerIngressDSCP=_AdGenEthernetDslamFlowCustomerIngressDSCP_Object((1,3,6,1,4,1,664,5,70,2,2,1,24),_AdGenEthernetDslamFlowCustomerIngressDSCP_Type())
adGenEthernetDslamFlowCustomerIngressDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowCustomerIngressDSCP.setStatus(_A)
_AdGenEthernetDslamFlowCustomerIngressIPProtocolID_Type=Integer32
_AdGenEthernetDslamFlowCustomerIngressIPProtocolID_Object=MibTableColumn
adGenEthernetDslamFlowCustomerIngressIPProtocolID=_AdGenEthernetDslamFlowCustomerIngressIPProtocolID_Object((1,3,6,1,4,1,664,5,70,2,2,1,25),_AdGenEthernetDslamFlowCustomerIngressIPProtocolID_Type())
adGenEthernetDslamFlowCustomerIngressIPProtocolID.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowCustomerIngressIPProtocolID.setStatus(_A)
class _AdGenEthernetDslamFlowCustomerIngressBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowCustomerIngressBroadcast_Type.__name__=_C
_AdGenEthernetDslamFlowCustomerIngressBroadcast_Object=MibTableColumn
adGenEthernetDslamFlowCustomerIngressBroadcast=_AdGenEthernetDslamFlowCustomerIngressBroadcast_Object((1,3,6,1,4,1,664,5,70,2,2,1,26),_AdGenEthernetDslamFlowCustomerIngressBroadcast_Type())
adGenEthernetDslamFlowCustomerIngressBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowCustomerIngressBroadcast.setStatus(_A)
class _AdGenEthernetDslamFlowCustomerIngressMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowCustomerIngressMulticast_Type.__name__=_C
_AdGenEthernetDslamFlowCustomerIngressMulticast_Object=MibTableColumn
adGenEthernetDslamFlowCustomerIngressMulticast=_AdGenEthernetDslamFlowCustomerIngressMulticast_Object((1,3,6,1,4,1,664,5,70,2,2,1,27),_AdGenEthernetDslamFlowCustomerIngressMulticast_Type())
adGenEthernetDslamFlowCustomerIngressMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowCustomerIngressMulticast.setStatus(_A)
class _AdGenEthernetDslamFlowCustomerIngressUnicast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowCustomerIngressUnicast_Type.__name__=_C
_AdGenEthernetDslamFlowCustomerIngressUnicast_Object=MibTableColumn
adGenEthernetDslamFlowCustomerIngressUnicast=_AdGenEthernetDslamFlowCustomerIngressUnicast_Object((1,3,6,1,4,1,664,5,70,2,2,1,28),_AdGenEthernetDslamFlowCustomerIngressUnicast_Type())
adGenEthernetDslamFlowCustomerIngressUnicast.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowCustomerIngressUnicast.setStatus(_A)
_AdGenEthernetDslamFlowCustomerIngressPolicer_Type=Integer32
_AdGenEthernetDslamFlowCustomerIngressPolicer_Object=MibTableColumn
adGenEthernetDslamFlowCustomerIngressPolicer=_AdGenEthernetDslamFlowCustomerIngressPolicer_Object((1,3,6,1,4,1,664,5,70,2,2,1,29),_AdGenEthernetDslamFlowCustomerIngressPolicer_Type())
adGenEthernetDslamFlowCustomerIngressPolicer.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowCustomerIngressPolicer.setStatus(_A)
class _AdGenEthernetDslamFlowEncapsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('ipoe',1),('pppoe',2),('pppoa',3),(_E,4),('atmoe',5),(_p,6),(_q,7),(_r,8)))
_AdGenEthernetDslamFlowEncapsMode_Type.__name__=_C
_AdGenEthernetDslamFlowEncapsMode_Object=MibTableColumn
adGenEthernetDslamFlowEncapsMode=_AdGenEthernetDslamFlowEncapsMode_Object((1,3,6,1,4,1,664,5,70,2,2,1,30),_AdGenEthernetDslamFlowEncapsMode_Type())
adGenEthernetDslamFlowEncapsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowEncapsMode.setStatus(_A)
class _AdGenEthernetDslamFlowManualAddrAging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_AdGenEthernetDslamFlowManualAddrAging_Type.__name__=_C
_AdGenEthernetDslamFlowManualAddrAging_Object=MibTableColumn
adGenEthernetDslamFlowManualAddrAging=_AdGenEthernetDslamFlowManualAddrAging_Object((1,3,6,1,4,1,664,5,70,2,2,1,31),_AdGenEthernetDslamFlowManualAddrAging_Type())
adGenEthernetDslamFlowManualAddrAging.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowManualAddrAging.setStatus(_A)
class _AdGenEthernetDslamFlowIntermedAgent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowIntermedAgent_Type.__name__=_C
_AdGenEthernetDslamFlowIntermedAgent_Object=MibTableColumn
adGenEthernetDslamFlowIntermedAgent=_AdGenEthernetDslamFlowIntermedAgent_Object((1,3,6,1,4,1,664,5,70,2,2,1,32),_AdGenEthernetDslamFlowIntermedAgent_Type())
adGenEthernetDslamFlowIntermedAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowIntermedAgent.setStatus(_A)
class _AdGenEthernetDslamFlowDhcpRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3),(_L,4),(_T,5)))
_AdGenEthernetDslamFlowDhcpRelay_Type.__name__=_C
_AdGenEthernetDslamFlowDhcpRelay_Object=MibTableColumn
adGenEthernetDslamFlowDhcpRelay=_AdGenEthernetDslamFlowDhcpRelay_Object((1,3,6,1,4,1,664,5,70,2,2,1,33),_AdGenEthernetDslamFlowDhcpRelay_Type())
adGenEthernetDslamFlowDhcpRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpRelay.setStatus(_A)
class _AdGenEthernetDslamFlowOption82Insert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowOption82Insert_Type.__name__=_C
_AdGenEthernetDslamFlowOption82Insert_Object=MibTableColumn
adGenEthernetDslamFlowOption82Insert=_AdGenEthernetDslamFlowOption82Insert_Object((1,3,6,1,4,1,664,5,70,2,2,1,34),_AdGenEthernetDslamFlowOption82Insert_Type())
adGenEthernetDslamFlowOption82Insert.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowOption82Insert.setStatus(_A)
class _AdGenEthernetDslamFlowLearnedIpAddrAgingMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lease',1),('fixed',2),(_E,3)))
_AdGenEthernetDslamFlowLearnedIpAddrAgingMethod_Type.__name__=_C
_AdGenEthernetDslamFlowLearnedIpAddrAgingMethod_Object=MibTableColumn
adGenEthernetDslamFlowLearnedIpAddrAgingMethod=_AdGenEthernetDslamFlowLearnedIpAddrAgingMethod_Object((1,3,6,1,4,1,664,5,70,2,2,1,35),_AdGenEthernetDslamFlowLearnedIpAddrAgingMethod_Type())
adGenEthernetDslamFlowLearnedIpAddrAgingMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowLearnedIpAddrAgingMethod.setStatus(_A)
class _AdGenEthernetDslamFlowIgmpProcessing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,1),(_s,2),(_t,3),(_a,4),(_E,5),(_L,6),(_u,7)))
_AdGenEthernetDslamFlowIgmpProcessing_Type.__name__=_C
_AdGenEthernetDslamFlowIgmpProcessing_Object=MibTableColumn
adGenEthernetDslamFlowIgmpProcessing=_AdGenEthernetDslamFlowIgmpProcessing_Object((1,3,6,1,4,1,664,5,70,2,2,1,36),_AdGenEthernetDslamFlowIgmpProcessing_Type())
adGenEthernetDslamFlowIgmpProcessing.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowIgmpProcessing.setStatus(_A)
class _AdGenEthernetDslamFlowIgmpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('v1',1),('v2',2),('v3',3),(_E,4)))
_AdGenEthernetDslamFlowIgmpVersion_Type.__name__=_C
_AdGenEthernetDslamFlowIgmpVersion_Object=MibTableColumn
adGenEthernetDslamFlowIgmpVersion=_AdGenEthernetDslamFlowIgmpVersion_Object((1,3,6,1,4,1,664,5,70,2,2,1,37),_AdGenEthernetDslamFlowIgmpVersion_Type())
adGenEthernetDslamFlowIgmpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowIgmpVersion.setStatus(_A)
class _AdGenEthernetDslamFlowLastMemberQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,65535))
_AdGenEthernetDslamFlowLastMemberQueryInterval_Type.__name__=_C
_AdGenEthernetDslamFlowLastMemberQueryInterval_Object=MibTableColumn
adGenEthernetDslamFlowLastMemberQueryInterval=_AdGenEthernetDslamFlowLastMemberQueryInterval_Object((1,3,6,1,4,1,664,5,70,2,2,1,38),_AdGenEthernetDslamFlowLastMemberQueryInterval_Type())
adGenEthernetDslamFlowLastMemberQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowLastMemberQueryInterval.setStatus(_A)
class _AdGenEthernetDslamFlowLastMemberQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenEthernetDslamFlowLastMemberQueryCount_Type.__name__=_C
_AdGenEthernetDslamFlowLastMemberQueryCount_Object=MibTableColumn
adGenEthernetDslamFlowLastMemberQueryCount=_AdGenEthernetDslamFlowLastMemberQueryCount_Object((1,3,6,1,4,1,664,5,70,2,2,1,39),_AdGenEthernetDslamFlowLastMemberQueryCount_Type())
adGenEthernetDslamFlowLastMemberQueryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowLastMemberQueryCount.setStatus(_A)
class _AdGenEthernetDslamFlowImmediateLeave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowImmediateLeave_Type.__name__=_C
_AdGenEthernetDslamFlowImmediateLeave_Object=MibTableColumn
adGenEthernetDslamFlowImmediateLeave=_AdGenEthernetDslamFlowImmediateLeave_Object((1,3,6,1,4,1,664,5,70,2,2,1,40),_AdGenEthernetDslamFlowImmediateLeave_Type())
adGenEthernetDslamFlowImmediateLeave.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowImmediateLeave.setStatus(_A)
_AdGenEthernetDslamFlowMaxAllowedMcastGroups_Type=Integer32
_AdGenEthernetDslamFlowMaxAllowedMcastGroups_Object=MibTableColumn
adGenEthernetDslamFlowMaxAllowedMcastGroups=_AdGenEthernetDslamFlowMaxAllowedMcastGroups_Object((1,3,6,1,4,1,664,5,70,2,2,1,41),_AdGenEthernetDslamFlowMaxAllowedMcastGroups_Type())
adGenEthernetDslamFlowMaxAllowedMcastGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowMaxAllowedMcastGroups.setStatus(_A)
class _AdGenEthernetDslamFlowDhcpPPPoERemoteId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowDhcpPPPoERemoteId_Type.__name__=_C
_AdGenEthernetDslamFlowDhcpPPPoERemoteId_Object=MibTableColumn
adGenEthernetDslamFlowDhcpPPPoERemoteId=_AdGenEthernetDslamFlowDhcpPPPoERemoteId_Object((1,3,6,1,4,1,664,5,70,2,2,1,42),_AdGenEthernetDslamFlowDhcpPPPoERemoteId_Type())
adGenEthernetDslamFlowDhcpPPPoERemoteId.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpPPPoERemoteId.setStatus(_A)
class _AdGenEthernetDslamFlowDhcpPPPoELoopCharacteristics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowDhcpPPPoELoopCharacteristics_Type.__name__=_C
_AdGenEthernetDslamFlowDhcpPPPoELoopCharacteristics_Object=MibTableColumn
adGenEthernetDslamFlowDhcpPPPoELoopCharacteristics=_AdGenEthernetDslamFlowDhcpPPPoELoopCharacteristics_Object((1,3,6,1,4,1,664,5,70,2,2,1,43),_AdGenEthernetDslamFlowDhcpPPPoELoopCharacteristics_Type())
adGenEthernetDslamFlowDhcpPPPoELoopCharacteristics.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpPPPoELoopCharacteristics.setStatus(_A)
class _AdGenEthernetDslamFlowDhcpPPPoECircuitIdFormat_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AdGenEthernetDslamFlowDhcpPPPoECircuitIdFormat_Type.__name__=_H
_AdGenEthernetDslamFlowDhcpPPPoECircuitIdFormat_Object=MibTableColumn
adGenEthernetDslamFlowDhcpPPPoECircuitIdFormat=_AdGenEthernetDslamFlowDhcpPPPoECircuitIdFormat_Object((1,3,6,1,4,1,664,5,70,2,2,1,44),_AdGenEthernetDslamFlowDhcpPPPoECircuitIdFormat_Type())
adGenEthernetDslamFlowDhcpPPPoECircuitIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpPPPoECircuitIdFormat.setStatus(_A)
_AdGenEthernetDslamFlowPPPoASessionTimeout_Type=Integer32
_AdGenEthernetDslamFlowPPPoASessionTimeout_Object=MibTableColumn
adGenEthernetDslamFlowPPPoASessionTimeout=_AdGenEthernetDslamFlowPPPoASessionTimeout_Object((1,3,6,1,4,1,664,5,70,2,2,1,45),_AdGenEthernetDslamFlowPPPoASessionTimeout_Type())
adGenEthernetDslamFlowPPPoASessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowPPPoASessionTimeout.setStatus(_A)
_AdGenEthernetDslamFlowInterfaceIfIndex_Type=Integer32
_AdGenEthernetDslamFlowInterfaceIfIndex_Object=MibTableColumn
adGenEthernetDslamFlowInterfaceIfIndex=_AdGenEthernetDslamFlowInterfaceIfIndex_Object((1,3,6,1,4,1,664,5,70,2,2,1,46),_AdGenEthernetDslamFlowInterfaceIfIndex_Type())
adGenEthernetDslamFlowInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowInterfaceIfIndex.setStatus(_A)
_AdGenEthernetDslamFlowInterfaceLogicalIndex_Type=Integer32
_AdGenEthernetDslamFlowInterfaceLogicalIndex_Object=MibTableColumn
adGenEthernetDslamFlowInterfaceLogicalIndex=_AdGenEthernetDslamFlowInterfaceLogicalIndex_Object((1,3,6,1,4,1,664,5,70,2,2,1,47),_AdGenEthernetDslamFlowInterfaceLogicalIndex_Type())
adGenEthernetDslamFlowInterfaceLogicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowInterfaceLogicalIndex.setStatus(_A)
_AdGenEthernetDslamFlowLastErrorString_Type=DisplayString
_AdGenEthernetDslamFlowLastErrorString_Object=MibTableColumn
adGenEthernetDslamFlowLastErrorString=_AdGenEthernetDslamFlowLastErrorString_Object((1,3,6,1,4,1,664,5,70,2,2,1,48),_AdGenEthernetDslamFlowLastErrorString_Type())
adGenEthernetDslamFlowLastErrorString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowLastErrorString.setStatus(_A)
_AdGenEthernetDslamFlowRowStatus_Type=RowStatus
_AdGenEthernetDslamFlowRowStatus_Object=MibTableColumn
adGenEthernetDslamFlowRowStatus=_AdGenEthernetDslamFlowRowStatus_Object((1,3,6,1,4,1,664,5,70,2,2,1,49),_AdGenEthernetDslamFlowRowStatus_Type())
adGenEthernetDslamFlowRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRowStatus.setStatus(_A)
_AdGenEthernetDslamFlowNetworkIngressPolicer_Type=Integer32
_AdGenEthernetDslamFlowNetworkIngressPolicer_Object=MibTableColumn
adGenEthernetDslamFlowNetworkIngressPolicer=_AdGenEthernetDslamFlowNetworkIngressPolicer_Object((1,3,6,1,4,1,664,5,70,2,2,1,50),_AdGenEthernetDslamFlowNetworkIngressPolicer_Type())
adGenEthernetDslamFlowNetworkIngressPolicer.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowNetworkIngressPolicer.setStatus(_A)
class _AdGenEthernetDslamFlowUpstreamDiscard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_AdGenEthernetDslamFlowUpstreamDiscard_Type.__name__=_C
_AdGenEthernetDslamFlowUpstreamDiscard_Object=MibTableColumn
adGenEthernetDslamFlowUpstreamDiscard=_AdGenEthernetDslamFlowUpstreamDiscard_Object((1,3,6,1,4,1,664,5,70,2,2,1,51),_AdGenEthernetDslamFlowUpstreamDiscard_Type())
adGenEthernetDslamFlowUpstreamDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowUpstreamDiscard.setStatus(_A)
_AdGenEthernetDslamFlowMaxAllowedMulticastBandwidth_Type=Integer32
_AdGenEthernetDslamFlowMaxAllowedMulticastBandwidth_Object=MibTableColumn
adGenEthernetDslamFlowMaxAllowedMulticastBandwidth=_AdGenEthernetDslamFlowMaxAllowedMulticastBandwidth_Object((1,3,6,1,4,1,664,5,70,2,2,1,53),_AdGenEthernetDslamFlowMaxAllowedMulticastBandwidth_Type())
adGenEthernetDslamFlowMaxAllowedMulticastBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowMaxAllowedMulticastBandwidth.setStatus(_A)
class _AdGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_AdGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable_Type.__name__=_C
_AdGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable_Object=MibTableColumn
adGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable=_AdGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable_Object((1,3,6,1,4,1,664,5,70,2,2,1,54),_AdGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable_Type())
adGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable.setStatus(_A)
class _AdGenEthernetDslamFlowProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenEthernetDslamFlowProfileName_Type.__name__=_H
_AdGenEthernetDslamFlowProfileName_Object=MibTableColumn
adGenEthernetDslamFlowProfileName=_AdGenEthernetDslamFlowProfileName_Object((1,3,6,1,4,1,664,5,70,2,2,1,55),_AdGenEthernetDslamFlowProfileName_Type())
adGenEthernetDslamFlowProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileName.setStatus(_A)
class _AdGenEthernetDslamFlowMaxAllowedMcastGroupsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_AdGenEthernetDslamFlowMaxAllowedMcastGroupsEnable_Type.__name__=_C
_AdGenEthernetDslamFlowMaxAllowedMcastGroupsEnable_Object=MibTableColumn
adGenEthernetDslamFlowMaxAllowedMcastGroupsEnable=_AdGenEthernetDslamFlowMaxAllowedMcastGroupsEnable_Object((1,3,6,1,4,1,664,5,70,2,2,1,56),_AdGenEthernetDslamFlowMaxAllowedMcastGroupsEnable_Type())
adGenEthernetDslamFlowMaxAllowedMcastGroupsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowMaxAllowedMcastGroupsEnable.setStatus(_A)
_AdGenEthernetDslamFlowNetworkIngressDSCPList_Type=DisplayString
_AdGenEthernetDslamFlowNetworkIngressDSCPList_Object=MibTableColumn
adGenEthernetDslamFlowNetworkIngressDSCPList=_AdGenEthernetDslamFlowNetworkIngressDSCPList_Object((1,3,6,1,4,1,664,5,70,2,2,1,57),_AdGenEthernetDslamFlowNetworkIngressDSCPList_Type())
adGenEthernetDslamFlowNetworkIngressDSCPList.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowNetworkIngressDSCPList.setStatus(_A)
_AdGenEthernetDslamFlowCustomerIngressDSCPList_Type=DisplayString
_AdGenEthernetDslamFlowCustomerIngressDSCPList_Object=MibTableColumn
adGenEthernetDslamFlowCustomerIngressDSCPList=_AdGenEthernetDslamFlowCustomerIngressDSCPList_Object((1,3,6,1,4,1,664,5,70,2,2,1,58),_AdGenEthernetDslamFlowCustomerIngressDSCPList_Type())
adGenEthernetDslamFlowCustomerIngressDSCPList.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowCustomerIngressDSCPList.setStatus(_A)
_AdGenEthernetDslamFlowIgmpRouterIP_Type=IpAddress
_AdGenEthernetDslamFlowIgmpRouterIP_Object=MibTableColumn
adGenEthernetDslamFlowIgmpRouterIP=_AdGenEthernetDslamFlowIgmpRouterIP_Object((1,3,6,1,4,1,664,5,70,2,2,1,59),_AdGenEthernetDslamFlowIgmpRouterIP_Type())
adGenEthernetDslamFlowIgmpRouterIP.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowIgmpRouterIP.setStatus(_A)
class _AdGenEthernetDslamFlowActivationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_v,1),(_w,2),(_x,3),('error',4)))
_AdGenEthernetDslamFlowActivationStatus_Type.__name__=_C
_AdGenEthernetDslamFlowActivationStatus_Object=MibTableColumn
adGenEthernetDslamFlowActivationStatus=_AdGenEthernetDslamFlowActivationStatus_Object((1,3,6,1,4,1,664,5,70,2,2,1,60),_AdGenEthernetDslamFlowActivationStatus_Type())
adGenEthernetDslamFlowActivationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowActivationStatus.setStatus(_A)
class _AdGenEthernetDslamFlowARPProcessing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_a,2),(_L,3)))
_AdGenEthernetDslamFlowARPProcessing_Type.__name__=_C
_AdGenEthernetDslamFlowARPProcessing_Object=MibTableColumn
adGenEthernetDslamFlowARPProcessing=_AdGenEthernetDslamFlowARPProcessing_Object((1,3,6,1,4,1,664,5,70,2,2,1,61),_AdGenEthernetDslamFlowARPProcessing_Type())
adGenEthernetDslamFlowARPProcessing.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowARPProcessing.setStatus(_A)
class _AdGenEthernetDslamFlowPPPoEProcessing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3),(_L,4)))
_AdGenEthernetDslamFlowPPPoEProcessing_Type.__name__=_C
_AdGenEthernetDslamFlowPPPoEProcessing_Object=MibTableColumn
adGenEthernetDslamFlowPPPoEProcessing=_AdGenEthernetDslamFlowPPPoEProcessing_Object((1,3,6,1,4,1,664,5,70,2,2,1,62),_AdGenEthernetDslamFlowPPPoEProcessing_Type())
adGenEthernetDslamFlowPPPoEProcessing.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowPPPoEProcessing.setStatus(_A)
_AdGenEthernetDslamFlowSubscriberIpRowCreateError_Type=DisplayString
_AdGenEthernetDslamFlowSubscriberIpRowCreateError_Object=MibTableColumn
adGenEthernetDslamFlowSubscriberIpRowCreateError=_AdGenEthernetDslamFlowSubscriberIpRowCreateError_Object((1,3,6,1,4,1,664,5,70,2,2,1,63),_AdGenEthernetDslamFlowSubscriberIpRowCreateError_Type())
adGenEthernetDslamFlowSubscriberIpRowCreateError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowSubscriberIpRowCreateError.setStatus(_A)
_AdGenEthernetDslamFlowDhcpPPPoEVendorNumber_Type=Integer32
_AdGenEthernetDslamFlowDhcpPPPoEVendorNumber_Object=MibTableColumn
adGenEthernetDslamFlowDhcpPPPoEVendorNumber=_AdGenEthernetDslamFlowDhcpPPPoEVendorNumber_Object((1,3,6,1,4,1,664,5,70,2,2,1,64),_AdGenEthernetDslamFlowDhcpPPPoEVendorNumber_Type())
adGenEthernetDslamFlowDhcpPPPoEVendorNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpPPPoEVendorNumber.setStatus(_A)
class _AdGenEthernetDslamFlowDhcpPPPoEVendorIdFormat_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AdGenEthernetDslamFlowDhcpPPPoEVendorIdFormat_Type.__name__=_H
_AdGenEthernetDslamFlowDhcpPPPoEVendorIdFormat_Object=MibTableColumn
adGenEthernetDslamFlowDhcpPPPoEVendorIdFormat=_AdGenEthernetDslamFlowDhcpPPPoEVendorIdFormat_Object((1,3,6,1,4,1,664,5,70,2,2,1,65),_AdGenEthernetDslamFlowDhcpPPPoEVendorIdFormat_Type())
adGenEthernetDslamFlowDhcpPPPoEVendorIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpPPPoEVendorIdFormat.setStatus(_A)
class _AdGenEthernetDslamFlowEvcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_AdGenEthernetDslamFlowEvcName_Type.__name__=_H
_AdGenEthernetDslamFlowEvcName_Object=MibTableColumn
adGenEthernetDslamFlowEvcName=_AdGenEthernetDslamFlowEvcName_Object((1,3,6,1,4,1,664,5,70,2,2,1,66),_AdGenEthernetDslamFlowEvcName_Type())
adGenEthernetDslamFlowEvcName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowEvcName.setStatus(_A)
class _AdGenEthernetDslamFlowEvcRoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_AdGenEthernetDslamFlowEvcRoot_Type.__name__=_C
_AdGenEthernetDslamFlowEvcRoot_Object=MibTableColumn
adGenEthernetDslamFlowEvcRoot=_AdGenEthernetDslamFlowEvcRoot_Object((1,3,6,1,4,1,664,5,70,2,2,1,67),_AdGenEthernetDslamFlowEvcRoot_Type())
adGenEthernetDslamFlowEvcRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowEvcRoot.setStatus(_A)
class _AdGenEthernetDslamFlowDhcpv6Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_b,1),(_N,2),(_L,3),(_T,4),(_c,5)))
_AdGenEthernetDslamFlowDhcpv6Mode_Type.__name__=_C
_AdGenEthernetDslamFlowDhcpv6Mode_Object=MibTableColumn
adGenEthernetDslamFlowDhcpv6Mode=_AdGenEthernetDslamFlowDhcpv6Mode_Object((1,3,6,1,4,1,664,5,70,2,2,1,68),_AdGenEthernetDslamFlowDhcpv6Mode_Type())
adGenEthernetDslamFlowDhcpv6Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpv6Mode.setStatus(_A)
class _AdGenEthernetDslamFlowDhcpv6RelayAgent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_c,3)))
_AdGenEthernetDslamFlowDhcpv6RelayAgent_Type.__name__=_C
_AdGenEthernetDslamFlowDhcpv6RelayAgent_Object=MibTableColumn
adGenEthernetDslamFlowDhcpv6RelayAgent=_AdGenEthernetDslamFlowDhcpv6RelayAgent_Object((1,3,6,1,4,1,664,5,70,2,2,1,69),_AdGenEthernetDslamFlowDhcpv6RelayAgent_Type())
adGenEthernetDslamFlowDhcpv6RelayAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpv6RelayAgent.setStatus(_A)
class _AdGenEthernetDslamFlowDhcpv6RelayAgentTrusted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AdGenEthernetDslamFlowDhcpv6RelayAgentTrusted_Type.__name__=_C
_AdGenEthernetDslamFlowDhcpv6RelayAgentTrusted_Object=MibTableColumn
adGenEthernetDslamFlowDhcpv6RelayAgentTrusted=_AdGenEthernetDslamFlowDhcpv6RelayAgentTrusted_Object((1,3,6,1,4,1,664,5,70,2,2,1,70),_AdGenEthernetDslamFlowDhcpv6RelayAgentTrusted_Type())
adGenEthernetDslamFlowDhcpv6RelayAgentTrusted.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpv6RelayAgentTrusted.setStatus(_A)
class _AdGenEthernetDslamFlowDhcpPPPoERemoteIdFormat_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AdGenEthernetDslamFlowDhcpPPPoERemoteIdFormat_Type.__name__=_H
_AdGenEthernetDslamFlowDhcpPPPoERemoteIdFormat_Object=MibTableColumn
adGenEthernetDslamFlowDhcpPPPoERemoteIdFormat=_AdGenEthernetDslamFlowDhcpPPPoERemoteIdFormat_Object((1,3,6,1,4,1,664,5,70,2,2,1,71),_AdGenEthernetDslamFlowDhcpPPPoERemoteIdFormat_Type())
adGenEthernetDslamFlowDhcpPPPoERemoteIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpPPPoERemoteIdFormat.setStatus(_A)
class _AdGenEthernetDslamFlowDownstreamQosMapProfile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenEthernetDslamFlowDownstreamQosMapProfile_Type.__name__=_H
_AdGenEthernetDslamFlowDownstreamQosMapProfile_Object=MibTableColumn
adGenEthernetDslamFlowDownstreamQosMapProfile=_AdGenEthernetDslamFlowDownstreamQosMapProfile_Object((1,3,6,1,4,1,664,5,70,2,2,1,72),_AdGenEthernetDslamFlowDownstreamQosMapProfile_Type())
adGenEthernetDslamFlowDownstreamQosMapProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDownstreamQosMapProfile.setStatus(_A)
class _AdGenEthernetDslamFlowUpstreamChannel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_AdGenEthernetDslamFlowUpstreamChannel_Type.__name__=_C
_AdGenEthernetDslamFlowUpstreamChannel_Object=MibTableColumn
adGenEthernetDslamFlowUpstreamChannel=_AdGenEthernetDslamFlowUpstreamChannel_Object((1,3,6,1,4,1,664,5,70,2,2,1,73),_AdGenEthernetDslamFlowUpstreamChannel_Type())
adGenEthernetDslamFlowUpstreamChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowUpstreamChannel.setStatus(_A)
class _AdGenEthernetDslamFlowDhcpv6CurrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),(_N,2),(_L,3),(_T,4)))
_AdGenEthernetDslamFlowDhcpv6CurrMode_Type.__name__=_C
_AdGenEthernetDslamFlowDhcpv6CurrMode_Object=MibTableColumn
adGenEthernetDslamFlowDhcpv6CurrMode=_AdGenEthernetDslamFlowDhcpv6CurrMode_Object((1,3,6,1,4,1,664,5,70,2,2,1,74),_AdGenEthernetDslamFlowDhcpv6CurrMode_Type())
adGenEthernetDslamFlowDhcpv6CurrMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpv6CurrMode.setStatus(_A)
class _AdGenEthernetDslamFlowDhcpPPPoEVendorIdInsert_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AdGenEthernetDslamFlowDhcpPPPoEVendorIdInsert_Type.__name__=_C
_AdGenEthernetDslamFlowDhcpPPPoEVendorIdInsert_Object=MibTableColumn
adGenEthernetDslamFlowDhcpPPPoEVendorIdInsert=_AdGenEthernetDslamFlowDhcpPPPoEVendorIdInsert_Object((1,3,6,1,4,1,664,5,70,2,2,1,75),_AdGenEthernetDslamFlowDhcpPPPoEVendorIdInsert_Type())
adGenEthernetDslamFlowDhcpPPPoEVendorIdInsert.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpPPPoEVendorIdInsert.setStatus(_A)
_AdGenEthernetDslamFlowMatchSourceMacList_Type=OctetString
_AdGenEthernetDslamFlowMatchSourceMacList_Object=MibTableColumn
adGenEthernetDslamFlowMatchSourceMacList=_AdGenEthernetDslamFlowMatchSourceMacList_Object((1,3,6,1,4,1,664,5,70,2,2,1,76),_AdGenEthernetDslamFlowMatchSourceMacList_Type())
adGenEthernetDslamFlowMatchSourceMacList.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowMatchSourceMacList.setStatus(_A)
_AdGenEthernetDslamFlowMatchSourceMacLastErrorString_Type=DisplayString
_AdGenEthernetDslamFlowMatchSourceMacLastErrorString_Object=MibTableColumn
adGenEthernetDslamFlowMatchSourceMacLastErrorString=_AdGenEthernetDslamFlowMatchSourceMacLastErrorString_Object((1,3,6,1,4,1,664,5,70,2,2,1,77),_AdGenEthernetDslamFlowMatchSourceMacLastErrorString_Type())
adGenEthernetDslamFlowMatchSourceMacLastErrorString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowMatchSourceMacLastErrorString.setStatus(_A)
class _AdGenEthernetDslamFlowMatchNonIp_Type(TruthValue):defaultValue=2
_AdGenEthernetDslamFlowMatchNonIp_Type.__name__=_j
_AdGenEthernetDslamFlowMatchNonIp_Object=MibTableColumn
adGenEthernetDslamFlowMatchNonIp=_AdGenEthernetDslamFlowMatchNonIp_Object((1,3,6,1,4,1,664,5,70,2,2,1,78),_AdGenEthernetDslamFlowMatchNonIp_Type())
adGenEthernetDslamFlowMatchNonIp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowMatchNonIp.setStatus(_A)
_AdGenEthernetDslamFlowIndexNextTable_Object=MibTable
adGenEthernetDslamFlowIndexNextTable=_AdGenEthernetDslamFlowIndexNextTable_Object((1,3,6,1,4,1,664,5,70,2,3))
if mibBuilder.loadTexts:adGenEthernetDslamFlowIndexNextTable.setStatus(_A)
_AdGenEthernetDslamFlowIndexNextEntry_Object=MibTableRow
adGenEthernetDslamFlowIndexNextEntry=_AdGenEthernetDslamFlowIndexNextEntry_Object((1,3,6,1,4,1,664,5,70,2,3,1))
adGenEthernetDslamFlowIndexNextEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:adGenEthernetDslamFlowIndexNextEntry.setStatus(_A)
_AdGenEthernetDslamFlowIndexNext_Type=Integer32
_AdGenEthernetDslamFlowIndexNext_Object=MibTableColumn
adGenEthernetDslamFlowIndexNext=_AdGenEthernetDslamFlowIndexNext_Object((1,3,6,1,4,1,664,5,70,2,3,1,1),_AdGenEthernetDslamFlowIndexNext_Type())
adGenEthernetDslamFlowIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowIndexNext.setStatus(_A)
_AdGenEthernetDslamFlowProfilesTable_Object=MibTable
adGenEthernetDslamFlowProfilesTable=_AdGenEthernetDslamFlowProfilesTable_Object((1,3,6,1,4,1,664,5,70,2,4))
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfilesTable.setStatus(_A)
_AdGenEthernetDslamFlowProfilesEntry_Object=MibTableRow
adGenEthernetDslamFlowProfilesEntry=_AdGenEthernetDslamFlowProfilesEntry_Object((1,3,6,1,4,1,664,5,70,2,4,1))
adGenEthernetDslamFlowProfilesEntry.setIndexNames((0,_I,_J),(0,_K,_y))
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfilesEntry.setStatus(_A)
_AdGenEthernetDslamFlowProfileIndex_Type=Integer32
_AdGenEthernetDslamFlowProfileIndex_Object=MibTableColumn
adGenEthernetDslamFlowProfileIndex=_AdGenEthernetDslamFlowProfileIndex_Object((1,3,6,1,4,1,664,5,70,2,4,1,1),_AdGenEthernetDslamFlowProfileIndex_Type())
adGenEthernetDslamFlowProfileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileIndex.setStatus(_A)
class _AdGenEthernetDslamFlowProfileAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenEthernetDslamFlowProfileAlias_Type.__name__=_H
_AdGenEthernetDslamFlowProfileAlias_Object=MibTableColumn
adGenEthernetDslamFlowProfileAlias=_AdGenEthernetDslamFlowProfileAlias_Object((1,3,6,1,4,1,664,5,70,2,4,1,2),_AdGenEthernetDslamFlowProfileAlias_Type())
adGenEthernetDslamFlowProfileAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileAlias.setStatus(_A)
class _AdGenEthernetDslamFlowProfileCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_AdGenEthernetDslamFlowProfileCIR_Type.__name__=_C
_AdGenEthernetDslamFlowProfileCIR_Object=MibTableColumn
adGenEthernetDslamFlowProfileCIR=_AdGenEthernetDslamFlowProfileCIR_Object((1,3,6,1,4,1,664,5,70,2,4,1,3),_AdGenEthernetDslamFlowProfileCIR_Type())
adGenEthernetDslamFlowProfileCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileCIR.setStatus(_A)
class _AdGenEthernetDslamFlowProfileCBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_AdGenEthernetDslamFlowProfileCBS_Type.__name__=_C
_AdGenEthernetDslamFlowProfileCBS_Object=MibTableColumn
adGenEthernetDslamFlowProfileCBS=_AdGenEthernetDslamFlowProfileCBS_Object((1,3,6,1,4,1,664,5,70,2,4,1,4),_AdGenEthernetDslamFlowProfileCBS_Type())
adGenEthernetDslamFlowProfileCBS.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileCBS.setStatus(_A)
class _AdGenEthernetDslamFlowProfileEIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_AdGenEthernetDslamFlowProfileEIR_Type.__name__=_C
_AdGenEthernetDslamFlowProfileEIR_Object=MibTableColumn
adGenEthernetDslamFlowProfileEIR=_AdGenEthernetDslamFlowProfileEIR_Object((1,3,6,1,4,1,664,5,70,2,4,1,5),_AdGenEthernetDslamFlowProfileEIR_Type())
adGenEthernetDslamFlowProfileEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileEIR.setStatus(_A)
class _AdGenEthernetDslamFlowProfileEBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_AdGenEthernetDslamFlowProfileEBS_Type.__name__=_C
_AdGenEthernetDslamFlowProfileEBS_Object=MibTableColumn
adGenEthernetDslamFlowProfileEBS=_AdGenEthernetDslamFlowProfileEBS_Object((1,3,6,1,4,1,664,5,70,2,4,1,6),_AdGenEthernetDslamFlowProfileEBS_Type())
adGenEthernetDslamFlowProfileEBS.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileEBS.setStatus(_A)
_AdGenEthernetDslamFlowProfileLastErrorString_Type=DisplayString
_AdGenEthernetDslamFlowProfileLastErrorString_Object=MibTableColumn
adGenEthernetDslamFlowProfileLastErrorString=_AdGenEthernetDslamFlowProfileLastErrorString_Object((1,3,6,1,4,1,664,5,70,2,4,1,7),_AdGenEthernetDslamFlowProfileLastErrorString_Type())
adGenEthernetDslamFlowProfileLastErrorString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileLastErrorString.setStatus(_A)
_AdGenEthernetDslamFlowProfileRowStatus_Type=RowStatus
_AdGenEthernetDslamFlowProfileRowStatus_Object=MibTableColumn
adGenEthernetDslamFlowProfileRowStatus=_AdGenEthernetDslamFlowProfileRowStatus_Object((1,3,6,1,4,1,664,5,70,2,4,1,8),_AdGenEthernetDslamFlowProfileRowStatus_Type())
adGenEthernetDslamFlowProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileRowStatus.setStatus(_A)
class _AdGenEthernetDslamFlowProfileActualCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_AdGenEthernetDslamFlowProfileActualCIR_Type.__name__=_C
_AdGenEthernetDslamFlowProfileActualCIR_Object=MibTableColumn
adGenEthernetDslamFlowProfileActualCIR=_AdGenEthernetDslamFlowProfileActualCIR_Object((1,3,6,1,4,1,664,5,70,2,4,1,9),_AdGenEthernetDslamFlowProfileActualCIR_Type())
adGenEthernetDslamFlowProfileActualCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileActualCIR.setStatus(_A)
class _AdGenEthernetDslamFlowProfileActualCBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_AdGenEthernetDslamFlowProfileActualCBS_Type.__name__=_C
_AdGenEthernetDslamFlowProfileActualCBS_Object=MibTableColumn
adGenEthernetDslamFlowProfileActualCBS=_AdGenEthernetDslamFlowProfileActualCBS_Object((1,3,6,1,4,1,664,5,70,2,4,1,10),_AdGenEthernetDslamFlowProfileActualCBS_Type())
adGenEthernetDslamFlowProfileActualCBS.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileActualCBS.setStatus(_A)
class _AdGenEthernetDslamFlowProfileActualEIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_AdGenEthernetDslamFlowProfileActualEIR_Type.__name__=_C
_AdGenEthernetDslamFlowProfileActualEIR_Object=MibTableColumn
adGenEthernetDslamFlowProfileActualEIR=_AdGenEthernetDslamFlowProfileActualEIR_Object((1,3,6,1,4,1,664,5,70,2,4,1,11),_AdGenEthernetDslamFlowProfileActualEIR_Type())
adGenEthernetDslamFlowProfileActualEIR.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileActualEIR.setStatus(_A)
class _AdGenEthernetDslamFlowProfileActualEBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_AdGenEthernetDslamFlowProfileActualEBS_Type.__name__=_C
_AdGenEthernetDslamFlowProfileActualEBS_Object=MibTableColumn
adGenEthernetDslamFlowProfileActualEBS=_AdGenEthernetDslamFlowProfileActualEBS_Object((1,3,6,1,4,1,664,5,70,2,4,1,12),_AdGenEthernetDslamFlowProfileActualEBS_Type())
adGenEthernetDslamFlowProfileActualEBS.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileActualEBS.setStatus(_A)
_AdGenEthernetDslamFlowNameLookupTable_Object=MibTable
adGenEthernetDslamFlowNameLookupTable=_AdGenEthernetDslamFlowNameLookupTable_Object((1,3,6,1,4,1,664,5,70,2,5))
if mibBuilder.loadTexts:adGenEthernetDslamFlowNameLookupTable.setStatus(_A)
_AdGenEthernetDslamFlowNameLookupEntry_Object=MibTableRow
adGenEthernetDslamFlowNameLookupEntry=_AdGenEthernetDslamFlowNameLookupEntry_Object((1,3,6,1,4,1,664,5,70,2,5,1))
adGenEthernetDslamFlowNameLookupEntry.setIndexNames((0,_I,_J),(1,_K,_z))
if mibBuilder.loadTexts:adGenEthernetDslamFlowNameLookupEntry.setStatus(_A)
class _AdGenEthernetDslamFlowNameLookupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenEthernetDslamFlowNameLookupName_Type.__name__=_H
_AdGenEthernetDslamFlowNameLookupName_Object=MibTableColumn
adGenEthernetDslamFlowNameLookupName=_AdGenEthernetDslamFlowNameLookupName_Object((1,3,6,1,4,1,664,5,70,2,5,1,1),_AdGenEthernetDslamFlowNameLookupName_Type())
adGenEthernetDslamFlowNameLookupName.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenEthernetDslamFlowNameLookupName.setStatus(_A)
_AdGenEthernetDslamFlowNameLookupIndex_Type=Integer32
_AdGenEthernetDslamFlowNameLookupIndex_Object=MibTableColumn
adGenEthernetDslamFlowNameLookupIndex=_AdGenEthernetDslamFlowNameLookupIndex_Object((1,3,6,1,4,1,664,5,70,2,5,1,2),_AdGenEthernetDslamFlowNameLookupIndex_Type())
adGenEthernetDslamFlowNameLookupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowNameLookupIndex.setStatus(_A)
_AdGenEthernetDslamFlowShaperTable_Object=MibTable
adGenEthernetDslamFlowShaperTable=_AdGenEthernetDslamFlowShaperTable_Object((1,3,6,1,4,1,664,5,70,2,6))
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperTable.setStatus(_A)
_AdGenEthernetDslamFlowShaperEntry_Object=MibTableRow
adGenEthernetDslamFlowShaperEntry=_AdGenEthernetDslamFlowShaperEntry_Object((1,3,6,1,4,1,664,5,70,2,6,1))
adGenEthernetDslamFlowShaperEntry.setIndexNames((0,_h,_i),(0,_K,_A0),(0,_K,_A1))
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperEntry.setStatus(_A)
_AdGenEthernetDslamFlowShaperInterfaceLogicalIndex_Type=Integer32
_AdGenEthernetDslamFlowShaperInterfaceLogicalIndex_Object=MibTableColumn
adGenEthernetDslamFlowShaperInterfaceLogicalIndex=_AdGenEthernetDslamFlowShaperInterfaceLogicalIndex_Object((1,3,6,1,4,1,664,5,70,2,6,1,1),_AdGenEthernetDslamFlowShaperInterfaceLogicalIndex_Type())
adGenEthernetDslamFlowShaperInterfaceLogicalIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperInterfaceLogicalIndex.setStatus(_A)
_AdGenEthernetDslamFlowShaperPrioritySet_Type=Integer32
_AdGenEthernetDslamFlowShaperPrioritySet_Object=MibTableColumn
adGenEthernetDslamFlowShaperPrioritySet=_AdGenEthernetDslamFlowShaperPrioritySet_Object((1,3,6,1,4,1,664,5,70,2,6,1,2),_AdGenEthernetDslamFlowShaperPrioritySet_Type())
adGenEthernetDslamFlowShaperPrioritySet.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperPrioritySet.setStatus(_A)
_AdGenEthernetDslamFlowShaperRate_Type=Integer32
_AdGenEthernetDslamFlowShaperRate_Object=MibTableColumn
adGenEthernetDslamFlowShaperRate=_AdGenEthernetDslamFlowShaperRate_Object((1,3,6,1,4,1,664,5,70,2,6,1,3),_AdGenEthernetDslamFlowShaperRate_Type())
adGenEthernetDslamFlowShaperRate.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperRate.setStatus(_A)
_AdGenEthernetDslamFlowShaperRowStatus_Type=RowStatus
_AdGenEthernetDslamFlowShaperRowStatus_Object=MibTableColumn
adGenEthernetDslamFlowShaperRowStatus=_AdGenEthernetDslamFlowShaperRowStatus_Object((1,3,6,1,4,1,664,5,70,2,6,1,4),_AdGenEthernetDslamFlowShaperRowStatus_Type())
adGenEthernetDslamFlowShaperRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperRowStatus.setStatus(_A)
_AdGenEthernetDslamFlowShaperLastErrorString_Type=DisplayString
_AdGenEthernetDslamFlowShaperLastErrorString_Object=MibTableColumn
adGenEthernetDslamFlowShaperLastErrorString=_AdGenEthernetDslamFlowShaperLastErrorString_Object((1,3,6,1,4,1,664,5,70,2,6,1,5),_AdGenEthernetDslamFlowShaperLastErrorString_Type())
adGenEthernetDslamFlowShaperLastErrorString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperLastErrorString.setStatus(_A)
class _AdGenEthernetDslamFlowShaperAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenEthernetDslamFlowShaperAlias_Type.__name__=_H
_AdGenEthernetDslamFlowShaperAlias_Object=MibTableColumn
adGenEthernetDslamFlowShaperAlias=_AdGenEthernetDslamFlowShaperAlias_Object((1,3,6,1,4,1,664,5,70,2,6,1,6),_AdGenEthernetDslamFlowShaperAlias_Type())
adGenEthernetDslamFlowShaperAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperAlias.setStatus(_A)
class _AdGenEthernetDslamFlowShaperOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('shaperNotRunning',1),('shaperRunning',2)))
_AdGenEthernetDslamFlowShaperOperationalStatus_Type.__name__=_C
_AdGenEthernetDslamFlowShaperOperationalStatus_Object=MibTableColumn
adGenEthernetDslamFlowShaperOperationalStatus=_AdGenEthernetDslamFlowShaperOperationalStatus_Object((1,3,6,1,4,1,664,5,70,2,6,1,7),_AdGenEthernetDslamFlowShaperOperationalStatus_Type())
adGenEthernetDslamFlowShaperOperationalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperOperationalStatus.setStatus(_A)
_AdGenEthernetDslamFlowShaperBurstSize_Type=Integer32
_AdGenEthernetDslamFlowShaperBurstSize_Object=MibTableColumn
adGenEthernetDslamFlowShaperBurstSize=_AdGenEthernetDslamFlowShaperBurstSize_Object((1,3,6,1,4,1,664,5,70,2,6,1,8),_AdGenEthernetDslamFlowShaperBurstSize_Type())
adGenEthernetDslamFlowShaperBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperBurstSize.setStatus(_A)
_AdGenEthernetDslamFlowShaperFixedRate_Type=Integer32
_AdGenEthernetDslamFlowShaperFixedRate_Object=MibTableColumn
adGenEthernetDslamFlowShaperFixedRate=_AdGenEthernetDslamFlowShaperFixedRate_Object((1,3,6,1,4,1,664,5,70,2,6,1,9),_AdGenEthernetDslamFlowShaperFixedRate_Type())
adGenEthernetDslamFlowShaperFixedRate.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperFixedRate.setStatus(_A)
_AdGenEthernetDslamFlowShaperAssuredRate_Type=Integer32
_AdGenEthernetDslamFlowShaperAssuredRate_Object=MibTableColumn
adGenEthernetDslamFlowShaperAssuredRate=_AdGenEthernetDslamFlowShaperAssuredRate_Object((1,3,6,1,4,1,664,5,70,2,6,1,10),_AdGenEthernetDslamFlowShaperAssuredRate_Type())
adGenEthernetDslamFlowShaperAssuredRate.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperAssuredRate.setStatus(_A)
class _AdGenEthernetDslamFlowShaperDownstreamMinRate_Type(Integer32):defaultValue=0
_AdGenEthernetDslamFlowShaperDownstreamMinRate_Type.__name__=_C
_AdGenEthernetDslamFlowShaperDownstreamMinRate_Object=MibTableColumn
adGenEthernetDslamFlowShaperDownstreamMinRate=_AdGenEthernetDslamFlowShaperDownstreamMinRate_Object((1,3,6,1,4,1,664,5,70,2,6,1,11),_AdGenEthernetDslamFlowShaperDownstreamMinRate_Type())
adGenEthernetDslamFlowShaperDownstreamMinRate.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperDownstreamMinRate.setStatus(_A)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperDownstreamMinRate.setUnits('kbps')
_AdGenSubscriberAccessStaticIpTable_Object=MibTable
adGenSubscriberAccessStaticIpTable=_AdGenSubscriberAccessStaticIpTable_Object((1,3,6,1,4,1,664,5,70,2,7))
if mibBuilder.loadTexts:adGenSubscriberAccessStaticIpTable.setStatus(_A)
_AdGenSubscriberAccessStaticIpEntry_Object=MibTableRow
adGenSubscriberAccessStaticIpEntry=_AdGenSubscriberAccessStaticIpEntry_Object((1,3,6,1,4,1,664,5,70,2,7,1))
adGenSubscriberAccessStaticIpEntry.setIndexNames((0,_I,_J),(0,_K,_k),(0,_K,_A2))
if mibBuilder.loadTexts:adGenSubscriberAccessStaticIpEntry.setStatus(_A)
_AdGenSubscriberAccessStaticIpAddress_Type=IpAddress
_AdGenSubscriberAccessStaticIpAddress_Object=MibTableColumn
adGenSubscriberAccessStaticIpAddress=_AdGenSubscriberAccessStaticIpAddress_Object((1,3,6,1,4,1,664,5,70,2,7,1,1),_AdGenSubscriberAccessStaticIpAddress_Type())
adGenSubscriberAccessStaticIpAddress.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenSubscriberAccessStaticIpAddress.setStatus(_A)
_AdGenSubscriberAccessStaticIpMacAddress_Type=PhysAddress
_AdGenSubscriberAccessStaticIpMacAddress_Object=MibTableColumn
adGenSubscriberAccessStaticIpMacAddress=_AdGenSubscriberAccessStaticIpMacAddress_Object((1,3,6,1,4,1,664,5,70,2,7,1,2),_AdGenSubscriberAccessStaticIpMacAddress_Type())
adGenSubscriberAccessStaticIpMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubscriberAccessStaticIpMacAddress.setStatus(_A)
_AdGenSubscriberAccessStaticIpGatewayIp_Type=IpAddress
_AdGenSubscriberAccessStaticIpGatewayIp_Object=MibTableColumn
adGenSubscriberAccessStaticIpGatewayIp=_AdGenSubscriberAccessStaticIpGatewayIp_Object((1,3,6,1,4,1,664,5,70,2,7,1,3),_AdGenSubscriberAccessStaticIpGatewayIp_Type())
adGenSubscriberAccessStaticIpGatewayIp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubscriberAccessStaticIpGatewayIp.setStatus(_A)
_AdGenSubscriberAccessStaticIpGatewayMac_Type=PhysAddress
_AdGenSubscriberAccessStaticIpGatewayMac_Object=MibTableColumn
adGenSubscriberAccessStaticIpGatewayMac=_AdGenSubscriberAccessStaticIpGatewayMac_Object((1,3,6,1,4,1,664,5,70,2,7,1,4),_AdGenSubscriberAccessStaticIpGatewayMac_Type())
adGenSubscriberAccessStaticIpGatewayMac.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubscriberAccessStaticIpGatewayMac.setStatus(_A)
_AdGenSubscriberAccessStaticIpLastErrorString_Type=DisplayString
_AdGenSubscriberAccessStaticIpLastErrorString_Object=MibTableColumn
adGenSubscriberAccessStaticIpLastErrorString=_AdGenSubscriberAccessStaticIpLastErrorString_Object((1,3,6,1,4,1,664,5,70,2,7,1,5),_AdGenSubscriberAccessStaticIpLastErrorString_Type())
adGenSubscriberAccessStaticIpLastErrorString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSubscriberAccessStaticIpLastErrorString.setStatus(_A)
_AdGenSubscriberAccessStaticIpRowStatus_Type=RowStatus
_AdGenSubscriberAccessStaticIpRowStatus_Object=MibTableColumn
adGenSubscriberAccessStaticIpRowStatus=_AdGenSubscriberAccessStaticIpRowStatus_Object((1,3,6,1,4,1,664,5,70,2,7,1,6),_AdGenSubscriberAccessStaticIpRowStatus_Type())
adGenSubscriberAccessStaticIpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubscriberAccessStaticIpRowStatus.setStatus(_A)
_AdGenEthernetDslamFlowProfilesIndexNextTable_Object=MibTable
adGenEthernetDslamFlowProfilesIndexNextTable=_AdGenEthernetDslamFlowProfilesIndexNextTable_Object((1,3,6,1,4,1,664,5,70,2,8))
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfilesIndexNextTable.setStatus(_A)
_AdGenEthernetDslamFlowProfilesIndexNextEntry_Object=MibTableRow
adGenEthernetDslamFlowProfilesIndexNextEntry=_AdGenEthernetDslamFlowProfilesIndexNextEntry_Object((1,3,6,1,4,1,664,5,70,2,8,1))
adGenEthernetDslamFlowProfilesIndexNextEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfilesIndexNextEntry.setStatus(_A)
_AdGenEthernetDslamFlowProfilesIndexNext_Type=Integer32
_AdGenEthernetDslamFlowProfilesIndexNext_Object=MibTableColumn
adGenEthernetDslamFlowProfilesIndexNext=_AdGenEthernetDslamFlowProfilesIndexNext_Object((1,3,6,1,4,1,664,5,70,2,8,1,1),_AdGenEthernetDslamFlowProfilesIndexNext_Type())
adGenEthernetDslamFlowProfilesIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfilesIndexNext.setStatus(_A)
_AdGenEthernetDslamFlowProfilesLookupTable_Object=MibTable
adGenEthernetDslamFlowProfilesLookupTable=_AdGenEthernetDslamFlowProfilesLookupTable_Object((1,3,6,1,4,1,664,5,70,2,9))
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfilesLookupTable.setStatus(_A)
_AdGenEthernetDslamFlowProfilesLookupEntry_Object=MibTableRow
adGenEthernetDslamFlowProfilesLookupEntry=_AdGenEthernetDslamFlowProfilesLookupEntry_Object((1,3,6,1,4,1,664,5,70,2,9,1))
adGenEthernetDslamFlowProfilesLookupEntry.setIndexNames((0,_I,_J),(1,_K,_A3))
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfilesLookupEntry.setStatus(_A)
class _AdGenEthernetDslamFlowProfileLookupAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenEthernetDslamFlowProfileLookupAlias_Type.__name__=_H
_AdGenEthernetDslamFlowProfileLookupAlias_Object=MibTableColumn
adGenEthernetDslamFlowProfileLookupAlias=_AdGenEthernetDslamFlowProfileLookupAlias_Object((1,3,6,1,4,1,664,5,70,2,9,1,1),_AdGenEthernetDslamFlowProfileLookupAlias_Type())
adGenEthernetDslamFlowProfileLookupAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileLookupAlias.setStatus(_A)
_AdGenEthernetDslamFlowProfileLookupIndex_Type=Integer32
_AdGenEthernetDslamFlowProfileLookupIndex_Object=MibTableColumn
adGenEthernetDslamFlowProfileLookupIndex=_AdGenEthernetDslamFlowProfileLookupIndex_Object((1,3,6,1,4,1,664,5,70,2,9,1,2),_AdGenEthernetDslamFlowProfileLookupIndex_Type())
adGenEthernetDslamFlowProfileLookupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowProfileLookupIndex.setStatus(_A)
_AdGenEthernetDslamFlowShaperLookupTable_Object=MibTable
adGenEthernetDslamFlowShaperLookupTable=_AdGenEthernetDslamFlowShaperLookupTable_Object((1,3,6,1,4,1,664,5,70,2,10))
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperLookupTable.setStatus(_A)
_AdGenEthernetDslamFlowShaperLookupEntry_Object=MibTableRow
adGenEthernetDslamFlowShaperLookupEntry=_AdGenEthernetDslamFlowShaperLookupEntry_Object((1,3,6,1,4,1,664,5,70,2,10,1))
adGenEthernetDslamFlowShaperLookupEntry.setIndexNames((0,_I,_J),(1,_K,_A4))
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperLookupEntry.setStatus(_A)
class _AdGenEthernetDslamFlowShaperLookupAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenEthernetDslamFlowShaperLookupAlias_Type.__name__=_H
_AdGenEthernetDslamFlowShaperLookupAlias_Object=MibTableColumn
adGenEthernetDslamFlowShaperLookupAlias=_AdGenEthernetDslamFlowShaperLookupAlias_Object((1,3,6,1,4,1,664,5,70,2,10,1,1),_AdGenEthernetDslamFlowShaperLookupAlias_Type())
adGenEthernetDslamFlowShaperLookupAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperLookupAlias.setStatus(_A)
_AdGenEthernetDslamFlowShaperLookupIfIndex_Type=Integer32
_AdGenEthernetDslamFlowShaperLookupIfIndex_Object=MibTableColumn
adGenEthernetDslamFlowShaperLookupIfIndex=_AdGenEthernetDslamFlowShaperLookupIfIndex_Object((1,3,6,1,4,1,664,5,70,2,10,1,2),_AdGenEthernetDslamFlowShaperLookupIfIndex_Type())
adGenEthernetDslamFlowShaperLookupIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperLookupIfIndex.setStatus(_A)
_AdGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex_Type=Integer32
_AdGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex_Object=MibTableColumn
adGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex=_AdGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex_Object((1,3,6,1,4,1,664,5,70,2,10,1,3),_AdGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex_Type())
adGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex.setStatus(_A)
_AdGenEthernetDslamFlowShaperLookupPrioritySet_Type=Integer32
_AdGenEthernetDslamFlowShaperLookupPrioritySet_Object=MibTableColumn
adGenEthernetDslamFlowShaperLookupPrioritySet=_AdGenEthernetDslamFlowShaperLookupPrioritySet_Object((1,3,6,1,4,1,664,5,70,2,10,1,4),_AdGenEthernetDslamFlowShaperLookupPrioritySet_Type())
adGenEthernetDslamFlowShaperLookupPrioritySet.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperLookupPrioritySet.setStatus(_A)
_AdGenEthernetDslamFlowRev2Table_Object=MibTable
adGenEthernetDslamFlowRev2Table=_AdGenEthernetDslamFlowRev2Table_Object((1,3,6,1,4,1,664,5,70,2,11))
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2Table.setStatus(_A)
_AdGenEthernetDslamFlowRev2Entry_Object=MibTableRow
adGenEthernetDslamFlowRev2Entry=_AdGenEthernetDslamFlowRev2Entry_Object((1,3,6,1,4,1,664,5,70,2,11,1))
adGenEthernetDslamFlowRev2Entry.setIndexNames((0,_I,_J),(0,_K,_A5))
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2Entry.setStatus(_A)
_AdGenEthernetDslamFlowRev2Index_Type=Integer32
_AdGenEthernetDslamFlowRev2Index_Object=MibTableColumn
adGenEthernetDslamFlowRev2Index=_AdGenEthernetDslamFlowRev2Index_Object((1,3,6,1,4,1,664,5,70,2,11,1,1),_AdGenEthernetDslamFlowRev2Index_Type())
adGenEthernetDslamFlowRev2Index.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2Index.setStatus(_A)
class _AdGenEthernetDslamFlowRev2Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenEthernetDslamFlowRev2Name_Type.__name__=_H
_AdGenEthernetDslamFlowRev2Name_Object=MibTableColumn
adGenEthernetDslamFlowRev2Name=_AdGenEthernetDslamFlowRev2Name_Object((1,3,6,1,4,1,664,5,70,2,11,1,2),_AdGenEthernetDslamFlowRev2Name_Type())
adGenEthernetDslamFlowRev2Name.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2Name.setStatus(_A)
class _AdGenEthernetDslamFlowRev2TrafficDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_m,1),(_n,2),(_o,3)))
_AdGenEthernetDslamFlowRev2TrafficDirection_Type.__name__=_C
_AdGenEthernetDslamFlowRev2TrafficDirection_Object=MibTableColumn
adGenEthernetDslamFlowRev2TrafficDirection=_AdGenEthernetDslamFlowRev2TrafficDirection_Object((1,3,6,1,4,1,664,5,70,2,11,1,3),_AdGenEthernetDslamFlowRev2TrafficDirection_Type())
adGenEthernetDslamFlowRev2TrafficDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2TrafficDirection.setStatus(_A)
class _AdGenEthernetDslamFlowRev2NetworkSTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_AdGenEthernetDslamFlowRev2NetworkSTag_Type.__name__=_C
_AdGenEthernetDslamFlowRev2NetworkSTag_Object=MibTableColumn
adGenEthernetDslamFlowRev2NetworkSTag=_AdGenEthernetDslamFlowRev2NetworkSTag_Object((1,3,6,1,4,1,664,5,70,2,11,1,4),_AdGenEthernetDslamFlowRev2NetworkSTag_Type())
adGenEthernetDslamFlowRev2NetworkSTag.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2NetworkSTag.setStatus(_A)
class _AdGenEthernetDslamFlowRev2NetworkCTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4096))
_AdGenEthernetDslamFlowRev2NetworkCTag_Type.__name__=_C
_AdGenEthernetDslamFlowRev2NetworkCTag_Object=MibTableColumn
adGenEthernetDslamFlowRev2NetworkCTag=_AdGenEthernetDslamFlowRev2NetworkCTag_Object((1,3,6,1,4,1,664,5,70,2,11,1,5),_AdGenEthernetDslamFlowRev2NetworkCTag_Type())
adGenEthernetDslamFlowRev2NetworkCTag.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2NetworkCTag.setStatus(_A)
class _AdGenEthernetDslamFlowRev2CEVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4097))
_AdGenEthernetDslamFlowRev2CEVlan_Type.__name__=_C
_AdGenEthernetDslamFlowRev2CEVlan_Object=MibTableColumn
adGenEthernetDslamFlowRev2CEVlan=_AdGenEthernetDslamFlowRev2CEVlan_Object((1,3,6,1,4,1,664,5,70,2,11,1,6),_AdGenEthernetDslamFlowRev2CEVlan_Type())
adGenEthernetDslamFlowRev2CEVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2CEVlan.setStatus(_A)
_AdGenEthernetDslamFlowRev2DownstreamForwardingMode_Type=Integer32
_AdGenEthernetDslamFlowRev2DownstreamForwardingMode_Object=MibTableColumn
adGenEthernetDslamFlowRev2DownstreamForwardingMode=_AdGenEthernetDslamFlowRev2DownstreamForwardingMode_Object((1,3,6,1,4,1,664,5,70,2,11,1,7),_AdGenEthernetDslamFlowRev2DownstreamForwardingMode_Type())
adGenEthernetDslamFlowRev2DownstreamForwardingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2DownstreamForwardingMode.setStatus(_A)
class _AdGenEthernetDslamFlowRev2DownstreamPbitMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_AdGenEthernetDslamFlowRev2DownstreamPbitMethod_Type.__name__=_C
_AdGenEthernetDslamFlowRev2DownstreamPbitMethod_Object=MibTableColumn
adGenEthernetDslamFlowRev2DownstreamPbitMethod=_AdGenEthernetDslamFlowRev2DownstreamPbitMethod_Object((1,3,6,1,4,1,664,5,70,2,11,1,8),_AdGenEthernetDslamFlowRev2DownstreamPbitMethod_Type())
adGenEthernetDslamFlowRev2DownstreamPbitMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2DownstreamPbitMethod.setStatus(_A)
class _AdGenEthernetDslamFlowRev2DownstreamPbitMarking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenEthernetDslamFlowRev2DownstreamPbitMarking_Type.__name__=_C
_AdGenEthernetDslamFlowRev2DownstreamPbitMarking_Object=MibTableColumn
adGenEthernetDslamFlowRev2DownstreamPbitMarking=_AdGenEthernetDslamFlowRev2DownstreamPbitMarking_Object((1,3,6,1,4,1,664,5,70,2,11,1,9),_AdGenEthernetDslamFlowRev2DownstreamPbitMarking_Type())
adGenEthernetDslamFlowRev2DownstreamPbitMarking.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2DownstreamPbitMarking.setStatus(_A)
_AdGenEthernetDslamFlowRev2DownstreamPbitMapping_Type=Integer32
_AdGenEthernetDslamFlowRev2DownstreamPbitMapping_Object=MibTableColumn
adGenEthernetDslamFlowRev2DownstreamPbitMapping=_AdGenEthernetDslamFlowRev2DownstreamPbitMapping_Object((1,3,6,1,4,1,664,5,70,2,11,1,10),_AdGenEthernetDslamFlowRev2DownstreamPbitMapping_Type())
adGenEthernetDslamFlowRev2DownstreamPbitMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2DownstreamPbitMapping.setStatus(_A)
class _AdGenEthernetDslamFlowRev2NetworkIngressPbit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenEthernetDslamFlowRev2NetworkIngressPbit_Type.__name__=_C
_AdGenEthernetDslamFlowRev2NetworkIngressPbit_Object=MibTableColumn
adGenEthernetDslamFlowRev2NetworkIngressPbit=_AdGenEthernetDslamFlowRev2NetworkIngressPbit_Object((1,3,6,1,4,1,664,5,70,2,11,1,11),_AdGenEthernetDslamFlowRev2NetworkIngressPbit_Type())
adGenEthernetDslamFlowRev2NetworkIngressPbit.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2NetworkIngressPbit.setStatus(_A)
_AdGenEthernetDslamFlowRev2NetworkIngressEtherType_Type=Integer32
_AdGenEthernetDslamFlowRev2NetworkIngressEtherType_Object=MibTableColumn
adGenEthernetDslamFlowRev2NetworkIngressEtherType=_AdGenEthernetDslamFlowRev2NetworkIngressEtherType_Object((1,3,6,1,4,1,664,5,70,2,11,1,12),_AdGenEthernetDslamFlowRev2NetworkIngressEtherType_Type())
adGenEthernetDslamFlowRev2NetworkIngressEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2NetworkIngressEtherType.setStatus(_A)
class _AdGenEthernetDslamFlowRev2NetworkIngressDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_AdGenEthernetDslamFlowRev2NetworkIngressDSCP_Type.__name__=_C
_AdGenEthernetDslamFlowRev2NetworkIngressDSCP_Object=MibTableColumn
adGenEthernetDslamFlowRev2NetworkIngressDSCP=_AdGenEthernetDslamFlowRev2NetworkIngressDSCP_Object((1,3,6,1,4,1,664,5,70,2,11,1,13),_AdGenEthernetDslamFlowRev2NetworkIngressDSCP_Type())
adGenEthernetDslamFlowRev2NetworkIngressDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2NetworkIngressDSCP.setStatus(_A)
_AdGenEthernetDslamFlowRev2NetworkIngressIPProtocolID_Type=Integer32
_AdGenEthernetDslamFlowRev2NetworkIngressIPProtocolID_Object=MibTableColumn
adGenEthernetDslamFlowRev2NetworkIngressIPProtocolID=_AdGenEthernetDslamFlowRev2NetworkIngressIPProtocolID_Object((1,3,6,1,4,1,664,5,70,2,11,1,14),_AdGenEthernetDslamFlowRev2NetworkIngressIPProtocolID_Type())
adGenEthernetDslamFlowRev2NetworkIngressIPProtocolID.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2NetworkIngressIPProtocolID.setStatus(_A)
_AdGenEthernetDslamFlowRev2UpstreamForwardingMode_Type=Integer32
_AdGenEthernetDslamFlowRev2UpstreamForwardingMode_Object=MibTableColumn
adGenEthernetDslamFlowRev2UpstreamForwardingMode=_AdGenEthernetDslamFlowRev2UpstreamForwardingMode_Object((1,3,6,1,4,1,664,5,70,2,11,1,15),_AdGenEthernetDslamFlowRev2UpstreamForwardingMode_Type())
adGenEthernetDslamFlowRev2UpstreamForwardingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2UpstreamForwardingMode.setStatus(_A)
class _AdGenEthernetDslamFlowRev2UpstreamSTagPbitMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMethod_Type.__name__=_C
_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMethod_Object=MibTableColumn
adGenEthernetDslamFlowRev2UpstreamSTagPbitMethod=_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMethod_Object((1,3,6,1,4,1,664,5,70,2,11,1,16),_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMethod_Type())
adGenEthernetDslamFlowRev2UpstreamSTagPbitMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2UpstreamSTagPbitMethod.setStatus(_A)
class _AdGenEthernetDslamFlowRev2UpstreamSTagPbitMarking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMarking_Type.__name__=_C
_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMarking_Object=MibTableColumn
adGenEthernetDslamFlowRev2UpstreamSTagPbitMarking=_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMarking_Object((1,3,6,1,4,1,664,5,70,2,11,1,17),_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMarking_Type())
adGenEthernetDslamFlowRev2UpstreamSTagPbitMarking.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2UpstreamSTagPbitMarking.setStatus(_A)
_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMapping_Type=Integer32
_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMapping_Object=MibTableColumn
adGenEthernetDslamFlowRev2UpstreamSTagPbitMapping=_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMapping_Object((1,3,6,1,4,1,664,5,70,2,11,1,18),_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMapping_Type())
adGenEthernetDslamFlowRev2UpstreamSTagPbitMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2UpstreamSTagPbitMapping.setStatus(_A)
class _AdGenEthernetDslamFlowRev2UpstreamCTagPbitMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMethod_Type.__name__=_C
_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMethod_Object=MibTableColumn
adGenEthernetDslamFlowRev2UpstreamCTagPbitMethod=_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMethod_Object((1,3,6,1,4,1,664,5,70,2,11,1,19),_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMethod_Type())
adGenEthernetDslamFlowRev2UpstreamCTagPbitMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2UpstreamCTagPbitMethod.setStatus(_A)
class _AdGenEthernetDslamFlowRev2UpstreamCTagPbitMarking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMarking_Type.__name__=_C
_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMarking_Object=MibTableColumn
adGenEthernetDslamFlowRev2UpstreamCTagPbitMarking=_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMarking_Object((1,3,6,1,4,1,664,5,70,2,11,1,20),_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMarking_Type())
adGenEthernetDslamFlowRev2UpstreamCTagPbitMarking.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2UpstreamCTagPbitMarking.setStatus(_A)
_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMapping_Type=Integer32
_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMapping_Object=MibTableColumn
adGenEthernetDslamFlowRev2UpstreamCTagPbitMapping=_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMapping_Object((1,3,6,1,4,1,664,5,70,2,11,1,21),_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMapping_Type())
adGenEthernetDslamFlowRev2UpstreamCTagPbitMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2UpstreamCTagPbitMapping.setStatus(_A)
class _AdGenEthernetDslamFlowRev2CustomerIngressPbit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenEthernetDslamFlowRev2CustomerIngressPbit_Type.__name__=_C
_AdGenEthernetDslamFlowRev2CustomerIngressPbit_Object=MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressPbit=_AdGenEthernetDslamFlowRev2CustomerIngressPbit_Object((1,3,6,1,4,1,664,5,70,2,11,1,22),_AdGenEthernetDslamFlowRev2CustomerIngressPbit_Type())
adGenEthernetDslamFlowRev2CustomerIngressPbit.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2CustomerIngressPbit.setStatus(_A)
_AdGenEthernetDslamFlowRev2CustomerIngressEtherType_Type=Integer32
_AdGenEthernetDslamFlowRev2CustomerIngressEtherType_Object=MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressEtherType=_AdGenEthernetDslamFlowRev2CustomerIngressEtherType_Object((1,3,6,1,4,1,664,5,70,2,11,1,23),_AdGenEthernetDslamFlowRev2CustomerIngressEtherType_Type())
adGenEthernetDslamFlowRev2CustomerIngressEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2CustomerIngressEtherType.setStatus(_A)
class _AdGenEthernetDslamFlowRev2CustomerIngressDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_AdGenEthernetDslamFlowRev2CustomerIngressDSCP_Type.__name__=_C
_AdGenEthernetDslamFlowRev2CustomerIngressDSCP_Object=MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressDSCP=_AdGenEthernetDslamFlowRev2CustomerIngressDSCP_Object((1,3,6,1,4,1,664,5,70,2,11,1,24),_AdGenEthernetDslamFlowRev2CustomerIngressDSCP_Type())
adGenEthernetDslamFlowRev2CustomerIngressDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2CustomerIngressDSCP.setStatus(_A)
_AdGenEthernetDslamFlowRev2CustomerIngressIPProtocolID_Type=Integer32
_AdGenEthernetDslamFlowRev2CustomerIngressIPProtocolID_Object=MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressIPProtocolID=_AdGenEthernetDslamFlowRev2CustomerIngressIPProtocolID_Object((1,3,6,1,4,1,664,5,70,2,11,1,25),_AdGenEthernetDslamFlowRev2CustomerIngressIPProtocolID_Type())
adGenEthernetDslamFlowRev2CustomerIngressIPProtocolID.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2CustomerIngressIPProtocolID.setStatus(_A)
class _AdGenEthernetDslamFlowRev2CustomerIngressBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowRev2CustomerIngressBroadcast_Type.__name__=_C
_AdGenEthernetDslamFlowRev2CustomerIngressBroadcast_Object=MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressBroadcast=_AdGenEthernetDslamFlowRev2CustomerIngressBroadcast_Object((1,3,6,1,4,1,664,5,70,2,11,1,26),_AdGenEthernetDslamFlowRev2CustomerIngressBroadcast_Type())
adGenEthernetDslamFlowRev2CustomerIngressBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2CustomerIngressBroadcast.setStatus(_A)
class _AdGenEthernetDslamFlowRev2CustomerIngressMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowRev2CustomerIngressMulticast_Type.__name__=_C
_AdGenEthernetDslamFlowRev2CustomerIngressMulticast_Object=MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressMulticast=_AdGenEthernetDslamFlowRev2CustomerIngressMulticast_Object((1,3,6,1,4,1,664,5,70,2,11,1,27),_AdGenEthernetDslamFlowRev2CustomerIngressMulticast_Type())
adGenEthernetDslamFlowRev2CustomerIngressMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2CustomerIngressMulticast.setStatus(_A)
class _AdGenEthernetDslamFlowRev2CustomerIngressUnicast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowRev2CustomerIngressUnicast_Type.__name__=_C
_AdGenEthernetDslamFlowRev2CustomerIngressUnicast_Object=MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressUnicast=_AdGenEthernetDslamFlowRev2CustomerIngressUnicast_Object((1,3,6,1,4,1,664,5,70,2,11,1,28),_AdGenEthernetDslamFlowRev2CustomerIngressUnicast_Type())
adGenEthernetDslamFlowRev2CustomerIngressUnicast.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2CustomerIngressUnicast.setStatus(_A)
_AdGenEthernetDslamFlowRev2CustomerIngressPolicer_Type=Integer32
_AdGenEthernetDslamFlowRev2CustomerIngressPolicer_Object=MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressPolicer=_AdGenEthernetDslamFlowRev2CustomerIngressPolicer_Object((1,3,6,1,4,1,664,5,70,2,11,1,29),_AdGenEthernetDslamFlowRev2CustomerIngressPolicer_Type())
adGenEthernetDslamFlowRev2CustomerIngressPolicer.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2CustomerIngressPolicer.setStatus(_A)
class _AdGenEthernetDslamFlowRev2EncapsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('ipoe',1),('pppoe',2),('pppoa',3),(_E,4),('atmoe',5),(_p,6),(_q,7),(_r,8)))
_AdGenEthernetDslamFlowRev2EncapsMode_Type.__name__=_C
_AdGenEthernetDslamFlowRev2EncapsMode_Object=MibTableColumn
adGenEthernetDslamFlowRev2EncapsMode=_AdGenEthernetDslamFlowRev2EncapsMode_Object((1,3,6,1,4,1,664,5,70,2,11,1,30),_AdGenEthernetDslamFlowRev2EncapsMode_Type())
adGenEthernetDslamFlowRev2EncapsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2EncapsMode.setStatus(_A)
class _AdGenEthernetDslamFlowRev2ManualAddrAging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_AdGenEthernetDslamFlowRev2ManualAddrAging_Type.__name__=_C
_AdGenEthernetDslamFlowRev2ManualAddrAging_Object=MibTableColumn
adGenEthernetDslamFlowRev2ManualAddrAging=_AdGenEthernetDslamFlowRev2ManualAddrAging_Object((1,3,6,1,4,1,664,5,70,2,11,1,31),_AdGenEthernetDslamFlowRev2ManualAddrAging_Type())
adGenEthernetDslamFlowRev2ManualAddrAging.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2ManualAddrAging.setStatus(_A)
class _AdGenEthernetDslamFlowRev2IntermedAgent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowRev2IntermedAgent_Type.__name__=_C
_AdGenEthernetDslamFlowRev2IntermedAgent_Object=MibTableColumn
adGenEthernetDslamFlowRev2IntermedAgent=_AdGenEthernetDslamFlowRev2IntermedAgent_Object((1,3,6,1,4,1,664,5,70,2,11,1,32),_AdGenEthernetDslamFlowRev2IntermedAgent_Type())
adGenEthernetDslamFlowRev2IntermedAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2IntermedAgent.setStatus(_A)
class _AdGenEthernetDslamFlowRev2DhcpRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3),(_L,4),(_T,5)))
_AdGenEthernetDslamFlowRev2DhcpRelay_Type.__name__=_C
_AdGenEthernetDslamFlowRev2DhcpRelay_Object=MibTableColumn
adGenEthernetDslamFlowRev2DhcpRelay=_AdGenEthernetDslamFlowRev2DhcpRelay_Object((1,3,6,1,4,1,664,5,70,2,11,1,33),_AdGenEthernetDslamFlowRev2DhcpRelay_Type())
adGenEthernetDslamFlowRev2DhcpRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2DhcpRelay.setStatus(_A)
class _AdGenEthernetDslamFlowRev2Option82Insert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowRev2Option82Insert_Type.__name__=_C
_AdGenEthernetDslamFlowRev2Option82Insert_Object=MibTableColumn
adGenEthernetDslamFlowRev2Option82Insert=_AdGenEthernetDslamFlowRev2Option82Insert_Object((1,3,6,1,4,1,664,5,70,2,11,1,34),_AdGenEthernetDslamFlowRev2Option82Insert_Type())
adGenEthernetDslamFlowRev2Option82Insert.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2Option82Insert.setStatus(_A)
class _AdGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lease',1),('fixed',2),(_E,3)))
_AdGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod_Type.__name__=_C
_AdGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod_Object=MibTableColumn
adGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod=_AdGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod_Object((1,3,6,1,4,1,664,5,70,2,11,1,35),_AdGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod_Type())
adGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod.setStatus(_A)
class _AdGenEthernetDslamFlowRev2IgmpProcessing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,1),(_s,2),(_t,3),(_a,4),(_E,5),(_L,6),(_u,7)))
_AdGenEthernetDslamFlowRev2IgmpProcessing_Type.__name__=_C
_AdGenEthernetDslamFlowRev2IgmpProcessing_Object=MibTableColumn
adGenEthernetDslamFlowRev2IgmpProcessing=_AdGenEthernetDslamFlowRev2IgmpProcessing_Object((1,3,6,1,4,1,664,5,70,2,11,1,36),_AdGenEthernetDslamFlowRev2IgmpProcessing_Type())
adGenEthernetDslamFlowRev2IgmpProcessing.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2IgmpProcessing.setStatus(_A)
class _AdGenEthernetDslamFlowRev2IgmpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('v1',1),('v2',2),('v3',3),(_E,4)))
_AdGenEthernetDslamFlowRev2IgmpVersion_Type.__name__=_C
_AdGenEthernetDslamFlowRev2IgmpVersion_Object=MibTableColumn
adGenEthernetDslamFlowRev2IgmpVersion=_AdGenEthernetDslamFlowRev2IgmpVersion_Object((1,3,6,1,4,1,664,5,70,2,11,1,37),_AdGenEthernetDslamFlowRev2IgmpVersion_Type())
adGenEthernetDslamFlowRev2IgmpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2IgmpVersion.setStatus(_A)
class _AdGenEthernetDslamFlowRev2LastMemberQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,65535))
_AdGenEthernetDslamFlowRev2LastMemberQueryInterval_Type.__name__=_C
_AdGenEthernetDslamFlowRev2LastMemberQueryInterval_Object=MibTableColumn
adGenEthernetDslamFlowRev2LastMemberQueryInterval=_AdGenEthernetDslamFlowRev2LastMemberQueryInterval_Object((1,3,6,1,4,1,664,5,70,2,11,1,38),_AdGenEthernetDslamFlowRev2LastMemberQueryInterval_Type())
adGenEthernetDslamFlowRev2LastMemberQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2LastMemberQueryInterval.setStatus(_A)
class _AdGenEthernetDslamFlowRev2LastMemberQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenEthernetDslamFlowRev2LastMemberQueryCount_Type.__name__=_C
_AdGenEthernetDslamFlowRev2LastMemberQueryCount_Object=MibTableColumn
adGenEthernetDslamFlowRev2LastMemberQueryCount=_AdGenEthernetDslamFlowRev2LastMemberQueryCount_Object((1,3,6,1,4,1,664,5,70,2,11,1,39),_AdGenEthernetDslamFlowRev2LastMemberQueryCount_Type())
adGenEthernetDslamFlowRev2LastMemberQueryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2LastMemberQueryCount.setStatus(_A)
class _AdGenEthernetDslamFlowRev2ImmediateLeave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowRev2ImmediateLeave_Type.__name__=_C
_AdGenEthernetDslamFlowRev2ImmediateLeave_Object=MibTableColumn
adGenEthernetDslamFlowRev2ImmediateLeave=_AdGenEthernetDslamFlowRev2ImmediateLeave_Object((1,3,6,1,4,1,664,5,70,2,11,1,40),_AdGenEthernetDslamFlowRev2ImmediateLeave_Type())
adGenEthernetDslamFlowRev2ImmediateLeave.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2ImmediateLeave.setStatus(_A)
_AdGenEthernetDslamFlowRev2MaxAllowedMcastGroups_Type=Integer32
_AdGenEthernetDslamFlowRev2MaxAllowedMcastGroups_Object=MibTableColumn
adGenEthernetDslamFlowRev2MaxAllowedMcastGroups=_AdGenEthernetDslamFlowRev2MaxAllowedMcastGroups_Object((1,3,6,1,4,1,664,5,70,2,11,1,41),_AdGenEthernetDslamFlowRev2MaxAllowedMcastGroups_Type())
adGenEthernetDslamFlowRev2MaxAllowedMcastGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2MaxAllowedMcastGroups.setStatus(_A)
class _AdGenEthernetDslamFlowRev2DhcpPPPoERemoteId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowRev2DhcpPPPoERemoteId_Type.__name__=_C
_AdGenEthernetDslamFlowRev2DhcpPPPoERemoteId_Object=MibTableColumn
adGenEthernetDslamFlowRev2DhcpPPPoERemoteId=_AdGenEthernetDslamFlowRev2DhcpPPPoERemoteId_Object((1,3,6,1,4,1,664,5,70,2,11,1,42),_AdGenEthernetDslamFlowRev2DhcpPPPoERemoteId_Type())
adGenEthernetDslamFlowRev2DhcpPPPoERemoteId.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2DhcpPPPoERemoteId.setStatus(_A)
class _AdGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_AdGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics_Type.__name__=_C
_AdGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics_Object=MibTableColumn
adGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics=_AdGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics_Object((1,3,6,1,4,1,664,5,70,2,11,1,43),_AdGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics_Type())
adGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics.setStatus(_A)
class _AdGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AdGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat_Type.__name__=_H
_AdGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat_Object=MibTableColumn
adGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat=_AdGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat_Object((1,3,6,1,4,1,664,5,70,2,11,1,44),_AdGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat_Type())
adGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat.setStatus(_A)
_AdGenEthernetDslamFlowRev2PPPoASessionTimeout_Type=Integer32
_AdGenEthernetDslamFlowRev2PPPoASessionTimeout_Object=MibTableColumn
adGenEthernetDslamFlowRev2PPPoASessionTimeout=_AdGenEthernetDslamFlowRev2PPPoASessionTimeout_Object((1,3,6,1,4,1,664,5,70,2,11,1,45),_AdGenEthernetDslamFlowRev2PPPoASessionTimeout_Type())
adGenEthernetDslamFlowRev2PPPoASessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2PPPoASessionTimeout.setStatus(_A)
_AdGenEthernetDslamFlowRev2InterfaceIfIndex_Type=Integer32
_AdGenEthernetDslamFlowRev2InterfaceIfIndex_Object=MibTableColumn
adGenEthernetDslamFlowRev2InterfaceIfIndex=_AdGenEthernetDslamFlowRev2InterfaceIfIndex_Object((1,3,6,1,4,1,664,5,70,2,11,1,46),_AdGenEthernetDslamFlowRev2InterfaceIfIndex_Type())
adGenEthernetDslamFlowRev2InterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2InterfaceIfIndex.setStatus(_A)
_AdGenEthernetDslamFlowRev2InterfaceLogicalIndex_Type=Integer32
_AdGenEthernetDslamFlowRev2InterfaceLogicalIndex_Object=MibTableColumn
adGenEthernetDslamFlowRev2InterfaceLogicalIndex=_AdGenEthernetDslamFlowRev2InterfaceLogicalIndex_Object((1,3,6,1,4,1,664,5,70,2,11,1,47),_AdGenEthernetDslamFlowRev2InterfaceLogicalIndex_Type())
adGenEthernetDslamFlowRev2InterfaceLogicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2InterfaceLogicalIndex.setStatus(_A)
_AdGenEthernetDslamFlowRev2LastErrorString_Type=DisplayString
_AdGenEthernetDslamFlowRev2LastErrorString_Object=MibTableColumn
adGenEthernetDslamFlowRev2LastErrorString=_AdGenEthernetDslamFlowRev2LastErrorString_Object((1,3,6,1,4,1,664,5,70,2,11,1,48),_AdGenEthernetDslamFlowRev2LastErrorString_Type())
adGenEthernetDslamFlowRev2LastErrorString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2LastErrorString.setStatus(_A)
_AdGenEthernetDslamFlowRev2RowStatus_Type=RowStatus
_AdGenEthernetDslamFlowRev2RowStatus_Object=MibTableColumn
adGenEthernetDslamFlowRev2RowStatus=_AdGenEthernetDslamFlowRev2RowStatus_Object((1,3,6,1,4,1,664,5,70,2,11,1,49),_AdGenEthernetDslamFlowRev2RowStatus_Type())
adGenEthernetDslamFlowRev2RowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2RowStatus.setStatus(_A)
_AdGenEthernetDslamFlowRev2NetworkIngressPolicer_Type=Integer32
_AdGenEthernetDslamFlowRev2NetworkIngressPolicer_Object=MibTableColumn
adGenEthernetDslamFlowRev2NetworkIngressPolicer=_AdGenEthernetDslamFlowRev2NetworkIngressPolicer_Object((1,3,6,1,4,1,664,5,70,2,11,1,50),_AdGenEthernetDslamFlowRev2NetworkIngressPolicer_Type())
adGenEthernetDslamFlowRev2NetworkIngressPolicer.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2NetworkIngressPolicer.setStatus(_A)
class _AdGenEthernetDslamFlowRev2UpstreamDiscard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_AdGenEthernetDslamFlowRev2UpstreamDiscard_Type.__name__=_C
_AdGenEthernetDslamFlowRev2UpstreamDiscard_Object=MibTableColumn
adGenEthernetDslamFlowRev2UpstreamDiscard=_AdGenEthernetDslamFlowRev2UpstreamDiscard_Object((1,3,6,1,4,1,664,5,70,2,11,1,51),_AdGenEthernetDslamFlowRev2UpstreamDiscard_Type())
adGenEthernetDslamFlowRev2UpstreamDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2UpstreamDiscard.setStatus(_A)
_AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth_Type=Integer32
_AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth_Object=MibTableColumn
adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth=_AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth_Object((1,3,6,1,4,1,664,5,70,2,11,1,53),_AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth_Type())
adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth.setStatus(_A)
class _AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable_Type.__name__=_C
_AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable_Object=MibTableColumn
adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable=_AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable_Object((1,3,6,1,4,1,664,5,70,2,11,1,54),_AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable_Type())
adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable.setStatus(_A)
class _AdGenEthernetDslamFlowRev2ProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenEthernetDslamFlowRev2ProfileName_Type.__name__=_H
_AdGenEthernetDslamFlowRev2ProfileName_Object=MibTableColumn
adGenEthernetDslamFlowRev2ProfileName=_AdGenEthernetDslamFlowRev2ProfileName_Object((1,3,6,1,4,1,664,5,70,2,11,1,55),_AdGenEthernetDslamFlowRev2ProfileName_Type())
adGenEthernetDslamFlowRev2ProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2ProfileName.setStatus(_A)
class _AdGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_AdGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable_Type.__name__=_C
_AdGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable_Object=MibTableColumn
adGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable=_AdGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable_Object((1,3,6,1,4,1,664,5,70,2,11,1,56),_AdGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable_Type())
adGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable.setStatus(_A)
_AdGenEthernetDslamFlowRev2NetworkIngressDSCPList_Type=DisplayString
_AdGenEthernetDslamFlowRev2NetworkIngressDSCPList_Object=MibTableColumn
adGenEthernetDslamFlowRev2NetworkIngressDSCPList=_AdGenEthernetDslamFlowRev2NetworkIngressDSCPList_Object((1,3,6,1,4,1,664,5,70,2,11,1,57),_AdGenEthernetDslamFlowRev2NetworkIngressDSCPList_Type())
adGenEthernetDslamFlowRev2NetworkIngressDSCPList.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2NetworkIngressDSCPList.setStatus(_A)
_AdGenEthernetDslamFlowRev2CustomerIngressDSCPList_Type=DisplayString
_AdGenEthernetDslamFlowRev2CustomerIngressDSCPList_Object=MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressDSCPList=_AdGenEthernetDslamFlowRev2CustomerIngressDSCPList_Object((1,3,6,1,4,1,664,5,70,2,11,1,58),_AdGenEthernetDslamFlowRev2CustomerIngressDSCPList_Type())
adGenEthernetDslamFlowRev2CustomerIngressDSCPList.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2CustomerIngressDSCPList.setStatus(_A)
_AdGenEthernetDslamFlowRev2IgmpRouterIP_Type=IpAddress
_AdGenEthernetDslamFlowRev2IgmpRouterIP_Object=MibTableColumn
adGenEthernetDslamFlowRev2IgmpRouterIP=_AdGenEthernetDslamFlowRev2IgmpRouterIP_Object((1,3,6,1,4,1,664,5,70,2,11,1,59),_AdGenEthernetDslamFlowRev2IgmpRouterIP_Type())
adGenEthernetDslamFlowRev2IgmpRouterIP.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2IgmpRouterIP.setStatus(_A)
class _AdGenEthernetDslamFlowRev2ActivationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_v,1),(_w,2),(_x,3),('error',4)))
_AdGenEthernetDslamFlowRev2ActivationStatus_Type.__name__=_C
_AdGenEthernetDslamFlowRev2ActivationStatus_Object=MibTableColumn
adGenEthernetDslamFlowRev2ActivationStatus=_AdGenEthernetDslamFlowRev2ActivationStatus_Object((1,3,6,1,4,1,664,5,70,2,11,1,60),_AdGenEthernetDslamFlowRev2ActivationStatus_Type())
adGenEthernetDslamFlowRev2ActivationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2ActivationStatus.setStatus(_A)
class _AdGenEthernetDslamFlowRev2ARPProcessing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_a,2),(_L,3)))
_AdGenEthernetDslamFlowRev2ARPProcessing_Type.__name__=_C
_AdGenEthernetDslamFlowRev2ARPProcessing_Object=MibTableColumn
adGenEthernetDslamFlowRev2ARPProcessing=_AdGenEthernetDslamFlowRev2ARPProcessing_Object((1,3,6,1,4,1,664,5,70,2,11,1,61),_AdGenEthernetDslamFlowRev2ARPProcessing_Type())
adGenEthernetDslamFlowRev2ARPProcessing.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2ARPProcessing.setStatus(_A)
class _AdGenEthernetDslamFlowRev2PPPoEProcessing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3),(_L,4)))
_AdGenEthernetDslamFlowRev2PPPoEProcessing_Type.__name__=_C
_AdGenEthernetDslamFlowRev2PPPoEProcessing_Object=MibTableColumn
adGenEthernetDslamFlowRev2PPPoEProcessing=_AdGenEthernetDslamFlowRev2PPPoEProcessing_Object((1,3,6,1,4,1,664,5,70,2,11,1,62),_AdGenEthernetDslamFlowRev2PPPoEProcessing_Type())
adGenEthernetDslamFlowRev2PPPoEProcessing.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2PPPoEProcessing.setStatus(_A)
_AdGenEthernetDslamFlowRev2SubscriberIpRowCreateError_Type=DisplayString
_AdGenEthernetDslamFlowRev2SubscriberIpRowCreateError_Object=MibTableColumn
adGenEthernetDslamFlowRev2SubscriberIpRowCreateError=_AdGenEthernetDslamFlowRev2SubscriberIpRowCreateError_Object((1,3,6,1,4,1,664,5,70,2,11,1,63),_AdGenEthernetDslamFlowRev2SubscriberIpRowCreateError_Type())
adGenEthernetDslamFlowRev2SubscriberIpRowCreateError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2SubscriberIpRowCreateError.setStatus(_A)
_AdGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber_Type=Integer32
_AdGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber_Object=MibTableColumn
adGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber=_AdGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber_Object((1,3,6,1,4,1,664,5,70,2,11,1,64),_AdGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber_Type())
adGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber.setStatus(_A)
class _AdGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AdGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat_Type.__name__=_H
_AdGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat_Object=MibTableColumn
adGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat=_AdGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat_Object((1,3,6,1,4,1,664,5,70,2,11,1,65),_AdGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat_Type())
adGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat.setStatus(_A)
class _AdGenEthernetDslamFlowRev2EvcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_AdGenEthernetDslamFlowRev2EvcName_Type.__name__=_H
_AdGenEthernetDslamFlowRev2EvcName_Object=MibTableColumn
adGenEthernetDslamFlowRev2EvcName=_AdGenEthernetDslamFlowRev2EvcName_Object((1,3,6,1,4,1,664,5,70,2,11,1,66),_AdGenEthernetDslamFlowRev2EvcName_Type())
adGenEthernetDslamFlowRev2EvcName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2EvcName.setStatus(_A)
class _AdGenEthernetDslamFlowRev2EvcRoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_AdGenEthernetDslamFlowRev2EvcRoot_Type.__name__=_C
_AdGenEthernetDslamFlowRev2EvcRoot_Object=MibTableColumn
adGenEthernetDslamFlowRev2EvcRoot=_AdGenEthernetDslamFlowRev2EvcRoot_Object((1,3,6,1,4,1,664,5,70,2,11,1,67),_AdGenEthernetDslamFlowRev2EvcRoot_Type())
adGenEthernetDslamFlowRev2EvcRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2EvcRoot.setStatus(_A)
class _AdGenEthernetDslamFlowRev2Dhcpv6Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_b,1),(_N,2),(_L,3),(_T,4),(_c,5)))
_AdGenEthernetDslamFlowRev2Dhcpv6Mode_Type.__name__=_C
_AdGenEthernetDslamFlowRev2Dhcpv6Mode_Object=MibTableColumn
adGenEthernetDslamFlowRev2Dhcpv6Mode=_AdGenEthernetDslamFlowRev2Dhcpv6Mode_Object((1,3,6,1,4,1,664,5,70,2,11,1,68),_AdGenEthernetDslamFlowRev2Dhcpv6Mode_Type())
adGenEthernetDslamFlowRev2Dhcpv6Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2Dhcpv6Mode.setStatus(_A)
class _AdGenEthernetDslamFlowRev2Dhcpv6RelayAgent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_c,3)))
_AdGenEthernetDslamFlowRev2Dhcpv6RelayAgent_Type.__name__=_C
_AdGenEthernetDslamFlowRev2Dhcpv6RelayAgent_Object=MibTableColumn
adGenEthernetDslamFlowRev2Dhcpv6RelayAgent=_AdGenEthernetDslamFlowRev2Dhcpv6RelayAgent_Object((1,3,6,1,4,1,664,5,70,2,11,1,69),_AdGenEthernetDslamFlowRev2Dhcpv6RelayAgent_Type())
adGenEthernetDslamFlowRev2Dhcpv6RelayAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2Dhcpv6RelayAgent.setStatus(_A)
class _AdGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AdGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted_Type.__name__=_C
_AdGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted_Object=MibTableColumn
adGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted=_AdGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted_Object((1,3,6,1,4,1,664,5,70,2,11,1,70),_AdGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted_Type())
adGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted.setStatus(_A)
class _AdGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AdGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat_Type.__name__=_H
_AdGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat_Object=MibTableColumn
adGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat=_AdGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat_Object((1,3,6,1,4,1,664,5,70,2,11,1,71),_AdGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat_Type())
adGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat.setStatus(_A)
class _AdGenEthernetDslamFlowRev2DownstreamQosMapProfile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenEthernetDslamFlowRev2DownstreamQosMapProfile_Type.__name__=_H
_AdGenEthernetDslamFlowRev2DownstreamQosMapProfile_Object=MibTableColumn
adGenEthernetDslamFlowRev2DownstreamQosMapProfile=_AdGenEthernetDslamFlowRev2DownstreamQosMapProfile_Object((1,3,6,1,4,1,664,5,70,2,11,1,72),_AdGenEthernetDslamFlowRev2DownstreamQosMapProfile_Type())
adGenEthernetDslamFlowRev2DownstreamQosMapProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2DownstreamQosMapProfile.setStatus(_A)
class _AdGenEthernetDslamFlowRev2Dhcpv6CurrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),(_N,2),(_L,3),(_T,4)))
_AdGenEthernetDslamFlowRev2Dhcpv6CurrMode_Type.__name__=_C
_AdGenEthernetDslamFlowRev2Dhcpv6CurrMode_Object=MibTableColumn
adGenEthernetDslamFlowRev2Dhcpv6CurrMode=_AdGenEthernetDslamFlowRev2Dhcpv6CurrMode_Object((1,3,6,1,4,1,664,5,70,2,11,1,73),_AdGenEthernetDslamFlowRev2Dhcpv6CurrMode_Type())
adGenEthernetDslamFlowRev2Dhcpv6CurrMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2Dhcpv6CurrMode.setStatus(_A)
_AdGenEthernetDslamFlowRev2MatchSourceMacList_Type=OctetString
_AdGenEthernetDslamFlowRev2MatchSourceMacList_Object=MibTableColumn
adGenEthernetDslamFlowRev2MatchSourceMacList=_AdGenEthernetDslamFlowRev2MatchSourceMacList_Object((1,3,6,1,4,1,664,5,70,2,11,1,74),_AdGenEthernetDslamFlowRev2MatchSourceMacList_Type())
adGenEthernetDslamFlowRev2MatchSourceMacList.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2MatchSourceMacList.setStatus(_A)
_AdGenEthernetDslamFlowRev2MatchSourceMacLastErrorString_Type=DisplayString
_AdGenEthernetDslamFlowRev2MatchSourceMacLastErrorString_Object=MibTableColumn
adGenEthernetDslamFlowRev2MatchSourceMacLastErrorString=_AdGenEthernetDslamFlowRev2MatchSourceMacLastErrorString_Object((1,3,6,1,4,1,664,5,70,2,11,1,75),_AdGenEthernetDslamFlowRev2MatchSourceMacLastErrorString_Type())
adGenEthernetDslamFlowRev2MatchSourceMacLastErrorString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2MatchSourceMacLastErrorString.setStatus(_A)
class _AdGenEthernetDslamFlowRev2MatchNonIp_Type(TruthValue):defaultValue=2
_AdGenEthernetDslamFlowRev2MatchNonIp_Type.__name__=_j
_AdGenEthernetDslamFlowRev2MatchNonIp_Object=MibTableColumn
adGenEthernetDslamFlowRev2MatchNonIp=_AdGenEthernetDslamFlowRev2MatchNonIp_Object((1,3,6,1,4,1,664,5,70,2,11,1,76),_AdGenEthernetDslamFlowRev2MatchNonIp_Type())
adGenEthernetDslamFlowRev2MatchNonIp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2MatchNonIp.setStatus(_A)
_AdGenEthernetDslamFlowRev2NameLookupTable_Object=MibTable
adGenEthernetDslamFlowRev2NameLookupTable=_AdGenEthernetDslamFlowRev2NameLookupTable_Object((1,3,6,1,4,1,664,5,70,2,12))
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2NameLookupTable.setStatus(_A)
_AdGenEthernetDslamFlowRev2NameLookupEntry_Object=MibTableRow
adGenEthernetDslamFlowRev2NameLookupEntry=_AdGenEthernetDslamFlowRev2NameLookupEntry_Object((1,3,6,1,4,1,664,5,70,2,12,1))
adGenEthernetDslamFlowRev2NameLookupEntry.setIndexNames((0,_I,_J),(1,_K,_A6))
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2NameLookupEntry.setStatus(_A)
class _AdGenEthernetDslamFlowRev2NameLookupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenEthernetDslamFlowRev2NameLookupName_Type.__name__=_H
_AdGenEthernetDslamFlowRev2NameLookupName_Object=MibTableColumn
adGenEthernetDslamFlowRev2NameLookupName=_AdGenEthernetDslamFlowRev2NameLookupName_Object((1,3,6,1,4,1,664,5,70,2,12,1,1),_AdGenEthernetDslamFlowRev2NameLookupName_Type())
adGenEthernetDslamFlowRev2NameLookupName.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2NameLookupName.setStatus(_A)
_AdGenEthernetDslamFlowRev2NameLookupIndex_Type=Integer32
_AdGenEthernetDslamFlowRev2NameLookupIndex_Object=MibTableColumn
adGenEthernetDslamFlowRev2NameLookupIndex=_AdGenEthernetDslamFlowRev2NameLookupIndex_Object((1,3,6,1,4,1,664,5,70,2,12,1,2),_AdGenEthernetDslamFlowRev2NameLookupIndex_Type())
adGenEthernetDslamFlowRev2NameLookupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2NameLookupIndex.setStatus(_A)
_AdGenEthernetDslamFlowRev2IndexNextTable_Object=MibTable
adGenEthernetDslamFlowRev2IndexNextTable=_AdGenEthernetDslamFlowRev2IndexNextTable_Object((1,3,6,1,4,1,664,5,70,2,13))
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2IndexNextTable.setStatus(_A)
_AdGenEthernetDslamFlowRev2IndexNextEntry_Object=MibTableRow
adGenEthernetDslamFlowRev2IndexNextEntry=_AdGenEthernetDslamFlowRev2IndexNextEntry_Object((1,3,6,1,4,1,664,5,70,2,13,1))
adGenEthernetDslamFlowRev2IndexNextEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2IndexNextEntry.setStatus(_A)
_AdGenEthernetDslamFlowRev2IndexNext_Type=Integer32
_AdGenEthernetDslamFlowRev2IndexNext_Object=MibTableColumn
adGenEthernetDslamFlowRev2IndexNext=_AdGenEthernetDslamFlowRev2IndexNext_Object((1,3,6,1,4,1,664,5,70,2,13,1,1),_AdGenEthernetDslamFlowRev2IndexNext_Type())
adGenEthernetDslamFlowRev2IndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowRev2IndexNext.setStatus(_A)
_AdGenEthernetDslamFlowQueueTable_Object=MibTable
adGenEthernetDslamFlowQueueTable=_AdGenEthernetDslamFlowQueueTable_Object((1,3,6,1,4,1,664,5,70,2,14))
if mibBuilder.loadTexts:adGenEthernetDslamFlowQueueTable.setStatus(_A)
_AdGenEthernetDslamFlowQueueTableEntry_Object=MibTableRow
adGenEthernetDslamFlowQueueTableEntry=_AdGenEthernetDslamFlowQueueTableEntry_Object((1,3,6,1,4,1,664,5,70,2,14,1))
adGenEthernetDslamFlowQueueTableEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:adGenEthernetDslamFlowQueueTableEntry.setStatus(_A)
_AdGenEthernetDslamFlowHonorsSystemPbitCosMap_Type=TruthValue
_AdGenEthernetDslamFlowHonorsSystemPbitCosMap_Object=MibTableColumn
adGenEthernetDslamFlowHonorsSystemPbitCosMap=_AdGenEthernetDslamFlowHonorsSystemPbitCosMap_Object((1,3,6,1,4,1,664,5,70,2,14,1,1),_AdGenEthernetDslamFlowHonorsSystemPbitCosMap_Type())
adGenEthernetDslamFlowHonorsSystemPbitCosMap.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowHonorsSystemPbitCosMap.setStatus(_A)
class _AdGenEthernetDslamFlowShaperQueuePriorityOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rightMostHighest',1),('leftMostHighest',2)))
_AdGenEthernetDslamFlowShaperQueuePriorityOrder_Type.__name__=_C
_AdGenEthernetDslamFlowShaperQueuePriorityOrder_Object=MibTableColumn
adGenEthernetDslamFlowShaperQueuePriorityOrder=_AdGenEthernetDslamFlowShaperQueuePriorityOrder_Object((1,3,6,1,4,1,664,5,70,2,14,1,2),_AdGenEthernetDslamFlowShaperQueuePriorityOrder_Type())
adGenEthernetDslamFlowShaperQueuePriorityOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetDslamFlowShaperQueuePriorityOrder.setStatus(_A)
_AdGenEthernetDslamFlowAlarmsPrefix_ObjectIdentity=ObjectIdentity
adGenEthernetDslamFlowAlarmsPrefix=_AdGenEthernetDslamFlowAlarmsPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,70,2,15))
_AdGenEthernetDslamFlowAlarms_ObjectIdentity=ObjectIdentity
adGenEthernetDslamFlowAlarms=_AdGenEthernetDslamFlowAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,70,2,15,0))
_AdGenEthernetDslamFlowScalarTable_Object=MibTable
adGenEthernetDslamFlowScalarTable=_AdGenEthernetDslamFlowScalarTable_Object((1,3,6,1,4,1,664,5,70,2,16))
if mibBuilder.loadTexts:adGenEthernetDslamFlowScalarTable.setStatus(_A)
_AdGenEthernetDslamFlowScalarTableEntry_Object=MibTableRow
adGenEthernetDslamFlowScalarTableEntry=_AdGenEthernetDslamFlowScalarTableEntry_Object((1,3,6,1,4,1,664,5,70,2,16,1))
adGenEthernetDslamFlowScalarTableEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:adGenEthernetDslamFlowScalarTableEntry.setStatus(_A)
_AdGenEthernetFlowMatchSourceMacMaxAddresses_Type=Integer32
_AdGenEthernetFlowMatchSourceMacMaxAddresses_Object=MibTableColumn
adGenEthernetFlowMatchSourceMacMaxAddresses=_AdGenEthernetFlowMatchSourceMacMaxAddresses_Object((1,3,6,1,4,1,664,5,70,2,16,1,1),_AdGenEthernetFlowMatchSourceMacMaxAddresses_Type())
adGenEthernetFlowMatchSourceMacMaxAddresses.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenEthernetFlowMatchSourceMacMaxAddresses.setStatus(_A)
_AdGenEthernetDslamFlowLoggingTable_Object=MibTable
adGenEthernetDslamFlowLoggingTable=_AdGenEthernetDslamFlowLoggingTable_Object((1,3,6,1,4,1,664,5,70,2,17))
if mibBuilder.loadTexts:adGenEthernetDslamFlowLoggingTable.setStatus(_A)
_AdGenEthernetDslamFlowLoggingEntry_Object=MibTableRow
adGenEthernetDslamFlowLoggingEntry=_AdGenEthernetDslamFlowLoggingEntry_Object((1,3,6,1,4,1,664,5,70,2,17,1))
adGenEthernetDslamFlowLoggingEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:adGenEthernetDslamFlowLoggingEntry.setStatus(_A)
class _AdGenEthernetDslamFlowDhcpPppoeEventDebug_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AdGenEthernetDslamFlowDhcpPppoeEventDebug_Type.__name__=_C
_AdGenEthernetDslamFlowDhcpPppoeEventDebug_Object=MibTableColumn
adGenEthernetDslamFlowDhcpPppoeEventDebug=_AdGenEthernetDslamFlowDhcpPppoeEventDebug_Object((1,3,6,1,4,1,664,5,70,2,17,1,1),_AdGenEthernetDslamFlowDhcpPppoeEventDebug_Type())
adGenEthernetDslamFlowDhcpPppoeEventDebug.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenEthernetDslamFlowDhcpPppoeEventDebug.setStatus(_A)
adGenEthernetDslamFlowDuplicateMacDetectedClr=NotificationType((1,3,6,1,4,1,664,5,70,2,15,0,1))
adGenEthernetDslamFlowDuplicateMacDetectedClr.setObjects(*((_U,_V),(_Y,_Z),(_I,_J),(_d,_e),(_W,_X),(_f,_g)))
if mibBuilder.loadTexts:adGenEthernetDslamFlowDuplicateMacDetectedClr.setStatus(_A)
adGenEthernetDslamFlowDuplicateMacDetectedAct=NotificationType((1,3,6,1,4,1,664,5,70,2,15,0,2))
adGenEthernetDslamFlowDuplicateMacDetectedAct.setObjects(*((_U,_V),(_Y,_Z),(_I,_J),(_d,_e),(_W,_X),(_f,_g)))
if mibBuilder.loadTexts:adGenEthernetDslamFlowDuplicateMacDetectedAct.setStatus(_A)
adGenEthernetDslamFlowMacAllocationAlarmClr=NotificationType((1,3,6,1,4,1,664,5,70,2,15,0,3))
adGenEthernetDslamFlowMacAllocationAlarmClr.setObjects(*((_U,_V),(_Y,_Z),(_I,_J),(_W,_X)))
if mibBuilder.loadTexts:adGenEthernetDslamFlowMacAllocationAlarmClr.setStatus(_A)
adGenEthernetDslamFlowMacAllocationAlarmAct=NotificationType((1,3,6,1,4,1,664,5,70,2,15,0,4))
adGenEthernetDslamFlowMacAllocationAlarmAct.setObjects(*((_U,_V),(_Y,_Z),(_I,_J),(_W,_X)))
if mibBuilder.loadTexts:adGenEthernetDslamFlowMacAllocationAlarmAct.setStatus(_A)
mibBuilder.exportSymbols(_K,**{'adGenEthernetInterfaceTable':adGenEthernetInterfaceTable,'adGenEthernetInterfaceEntry':adGenEthernetInterfaceEntry,_l:adGenEthernetInterfaceLogicalIndex,'adGenEthernetInterfaceMaxMACAddresses':adGenEthernetInterfaceMaxMACAddresses,'adGenEthernetInterfaceFlowList':adGenEthernetInterfaceFlowList,'adGenEthernetInterfaceSourceAuthentication':adGenEthernetInterfaceSourceAuthentication,'adGenEthernetInterfaceType':adGenEthernetInterfaceType,'adGenEthernetInterfaceTypeSpecific':adGenEthernetInterfaceTypeSpecific,'adGenEthernetDslamFlowTable':adGenEthernetDslamFlowTable,'adGenEthernetDslamFlowEntry':adGenEthernetDslamFlowEntry,_k:adGenEthernetDslamFlowIndex,'adGenEthernetDslamFlowName':adGenEthernetDslamFlowName,'adGenEthernetDslamFlowTrafficDirection':adGenEthernetDslamFlowTrafficDirection,'adGenEthernetDslamFlowNetworkSTag':adGenEthernetDslamFlowNetworkSTag,'adGenEthernetDslamFlowNetworkCTag':adGenEthernetDslamFlowNetworkCTag,'adGenEthernetDslamFlowCEVlan':adGenEthernetDslamFlowCEVlan,'adGenEthernetDslamFlowDownstreamForwardingMode':adGenEthernetDslamFlowDownstreamForwardingMode,'adGenEthernetDslamFlowDownstreamPbitMethod':adGenEthernetDslamFlowDownstreamPbitMethod,'adGenEthernetDslamFlowDownstreamPbitMarking':adGenEthernetDslamFlowDownstreamPbitMarking,'adGenEthernetDslamFlowDownstreamPbitMapping':adGenEthernetDslamFlowDownstreamPbitMapping,'adGenEthernetDslamFlowNetworkIngressPbit':adGenEthernetDslamFlowNetworkIngressPbit,'adGenEthernetDslamFlowNetworkIngressEtherType':adGenEthernetDslamFlowNetworkIngressEtherType,'adGenEthernetDslamFlowNetworkIngressDSCP':adGenEthernetDslamFlowNetworkIngressDSCP,'adGenEthernetDslamFlowNetworkIngressIPProtocolID':adGenEthernetDslamFlowNetworkIngressIPProtocolID,'adGenEthernetDslamFlowUpstreamForwardingMode':adGenEthernetDslamFlowUpstreamForwardingMode,'adGenEthernetDslamFlowUpstreamSTagPbitMethod':adGenEthernetDslamFlowUpstreamSTagPbitMethod,'adGenEthernetDslamFlowUpstreamSTagPbitMarking':adGenEthernetDslamFlowUpstreamSTagPbitMarking,'adGenEthernetDslamFlowUpstreamSTagPbitMapping':adGenEthernetDslamFlowUpstreamSTagPbitMapping,'adGenEthernetDslamFlowUpstreamCTagPbitMethod':adGenEthernetDslamFlowUpstreamCTagPbitMethod,'adGenEthernetDslamFlowUpstreamCTagPbitMarking':adGenEthernetDslamFlowUpstreamCTagPbitMarking,'adGenEthernetDslamFlowUpstreamCTagPbitMapping':adGenEthernetDslamFlowUpstreamCTagPbitMapping,'adGenEthernetDslamFlowCustomerIngressPbit':adGenEthernetDslamFlowCustomerIngressPbit,'adGenEthernetDslamFlowCustomerIngressEtherType':adGenEthernetDslamFlowCustomerIngressEtherType,'adGenEthernetDslamFlowCustomerIngressDSCP':adGenEthernetDslamFlowCustomerIngressDSCP,'adGenEthernetDslamFlowCustomerIngressIPProtocolID':adGenEthernetDslamFlowCustomerIngressIPProtocolID,'adGenEthernetDslamFlowCustomerIngressBroadcast':adGenEthernetDslamFlowCustomerIngressBroadcast,'adGenEthernetDslamFlowCustomerIngressMulticast':adGenEthernetDslamFlowCustomerIngressMulticast,'adGenEthernetDslamFlowCustomerIngressUnicast':adGenEthernetDslamFlowCustomerIngressUnicast,'adGenEthernetDslamFlowCustomerIngressPolicer':adGenEthernetDslamFlowCustomerIngressPolicer,'adGenEthernetDslamFlowEncapsMode':adGenEthernetDslamFlowEncapsMode,'adGenEthernetDslamFlowManualAddrAging':adGenEthernetDslamFlowManualAddrAging,'adGenEthernetDslamFlowIntermedAgent':adGenEthernetDslamFlowIntermedAgent,'adGenEthernetDslamFlowDhcpRelay':adGenEthernetDslamFlowDhcpRelay,'adGenEthernetDslamFlowOption82Insert':adGenEthernetDslamFlowOption82Insert,'adGenEthernetDslamFlowLearnedIpAddrAgingMethod':adGenEthernetDslamFlowLearnedIpAddrAgingMethod,'adGenEthernetDslamFlowIgmpProcessing':adGenEthernetDslamFlowIgmpProcessing,'adGenEthernetDslamFlowIgmpVersion':adGenEthernetDslamFlowIgmpVersion,'adGenEthernetDslamFlowLastMemberQueryInterval':adGenEthernetDslamFlowLastMemberQueryInterval,'adGenEthernetDslamFlowLastMemberQueryCount':adGenEthernetDslamFlowLastMemberQueryCount,'adGenEthernetDslamFlowImmediateLeave':adGenEthernetDslamFlowImmediateLeave,'adGenEthernetDslamFlowMaxAllowedMcastGroups':adGenEthernetDslamFlowMaxAllowedMcastGroups,'adGenEthernetDslamFlowDhcpPPPoERemoteId':adGenEthernetDslamFlowDhcpPPPoERemoteId,'adGenEthernetDslamFlowDhcpPPPoELoopCharacteristics':adGenEthernetDslamFlowDhcpPPPoELoopCharacteristics,'adGenEthernetDslamFlowDhcpPPPoECircuitIdFormat':adGenEthernetDslamFlowDhcpPPPoECircuitIdFormat,'adGenEthernetDslamFlowPPPoASessionTimeout':adGenEthernetDslamFlowPPPoASessionTimeout,'adGenEthernetDslamFlowInterfaceIfIndex':adGenEthernetDslamFlowInterfaceIfIndex,'adGenEthernetDslamFlowInterfaceLogicalIndex':adGenEthernetDslamFlowInterfaceLogicalIndex,'adGenEthernetDslamFlowLastErrorString':adGenEthernetDslamFlowLastErrorString,'adGenEthernetDslamFlowRowStatus':adGenEthernetDslamFlowRowStatus,'adGenEthernetDslamFlowNetworkIngressPolicer':adGenEthernetDslamFlowNetworkIngressPolicer,'adGenEthernetDslamFlowUpstreamDiscard':adGenEthernetDslamFlowUpstreamDiscard,'adGenEthernetDslamFlowMaxAllowedMulticastBandwidth':adGenEthernetDslamFlowMaxAllowedMulticastBandwidth,'adGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable':adGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable,'adGenEthernetDslamFlowProfileName':adGenEthernetDslamFlowProfileName,'adGenEthernetDslamFlowMaxAllowedMcastGroupsEnable':adGenEthernetDslamFlowMaxAllowedMcastGroupsEnable,'adGenEthernetDslamFlowNetworkIngressDSCPList':adGenEthernetDslamFlowNetworkIngressDSCPList,'adGenEthernetDslamFlowCustomerIngressDSCPList':adGenEthernetDslamFlowCustomerIngressDSCPList,'adGenEthernetDslamFlowIgmpRouterIP':adGenEthernetDslamFlowIgmpRouterIP,'adGenEthernetDslamFlowActivationStatus':adGenEthernetDslamFlowActivationStatus,'adGenEthernetDslamFlowARPProcessing':adGenEthernetDslamFlowARPProcessing,'adGenEthernetDslamFlowPPPoEProcessing':adGenEthernetDslamFlowPPPoEProcessing,'adGenEthernetDslamFlowSubscriberIpRowCreateError':adGenEthernetDslamFlowSubscriberIpRowCreateError,'adGenEthernetDslamFlowDhcpPPPoEVendorNumber':adGenEthernetDslamFlowDhcpPPPoEVendorNumber,'adGenEthernetDslamFlowDhcpPPPoEVendorIdFormat':adGenEthernetDslamFlowDhcpPPPoEVendorIdFormat,'adGenEthernetDslamFlowEvcName':adGenEthernetDslamFlowEvcName,'adGenEthernetDslamFlowEvcRoot':adGenEthernetDslamFlowEvcRoot,'adGenEthernetDslamFlowDhcpv6Mode':adGenEthernetDslamFlowDhcpv6Mode,'adGenEthernetDslamFlowDhcpv6RelayAgent':adGenEthernetDslamFlowDhcpv6RelayAgent,'adGenEthernetDslamFlowDhcpv6RelayAgentTrusted':adGenEthernetDslamFlowDhcpv6RelayAgentTrusted,'adGenEthernetDslamFlowDhcpPPPoERemoteIdFormat':adGenEthernetDslamFlowDhcpPPPoERemoteIdFormat,'adGenEthernetDslamFlowDownstreamQosMapProfile':adGenEthernetDslamFlowDownstreamQosMapProfile,'adGenEthernetDslamFlowUpstreamChannel':adGenEthernetDslamFlowUpstreamChannel,'adGenEthernetDslamFlowDhcpv6CurrMode':adGenEthernetDslamFlowDhcpv6CurrMode,'adGenEthernetDslamFlowDhcpPPPoEVendorIdInsert':adGenEthernetDslamFlowDhcpPPPoEVendorIdInsert,'adGenEthernetDslamFlowMatchSourceMacList':adGenEthernetDslamFlowMatchSourceMacList,'adGenEthernetDslamFlowMatchSourceMacLastErrorString':adGenEthernetDslamFlowMatchSourceMacLastErrorString,'adGenEthernetDslamFlowMatchNonIp':adGenEthernetDslamFlowMatchNonIp,'adGenEthernetDslamFlowIndexNextTable':adGenEthernetDslamFlowIndexNextTable,'adGenEthernetDslamFlowIndexNextEntry':adGenEthernetDslamFlowIndexNextEntry,'adGenEthernetDslamFlowIndexNext':adGenEthernetDslamFlowIndexNext,'adGenEthernetDslamFlowProfilesTable':adGenEthernetDslamFlowProfilesTable,'adGenEthernetDslamFlowProfilesEntry':adGenEthernetDslamFlowProfilesEntry,_y:adGenEthernetDslamFlowProfileIndex,'adGenEthernetDslamFlowProfileAlias':adGenEthernetDslamFlowProfileAlias,'adGenEthernetDslamFlowProfileCIR':adGenEthernetDslamFlowProfileCIR,'adGenEthernetDslamFlowProfileCBS':adGenEthernetDslamFlowProfileCBS,'adGenEthernetDslamFlowProfileEIR':adGenEthernetDslamFlowProfileEIR,'adGenEthernetDslamFlowProfileEBS':adGenEthernetDslamFlowProfileEBS,'adGenEthernetDslamFlowProfileLastErrorString':adGenEthernetDslamFlowProfileLastErrorString,'adGenEthernetDslamFlowProfileRowStatus':adGenEthernetDslamFlowProfileRowStatus,'adGenEthernetDslamFlowProfileActualCIR':adGenEthernetDslamFlowProfileActualCIR,'adGenEthernetDslamFlowProfileActualCBS':adGenEthernetDslamFlowProfileActualCBS,'adGenEthernetDslamFlowProfileActualEIR':adGenEthernetDslamFlowProfileActualEIR,'adGenEthernetDslamFlowProfileActualEBS':adGenEthernetDslamFlowProfileActualEBS,'adGenEthernetDslamFlowNameLookupTable':adGenEthernetDslamFlowNameLookupTable,'adGenEthernetDslamFlowNameLookupEntry':adGenEthernetDslamFlowNameLookupEntry,_z:adGenEthernetDslamFlowNameLookupName,'adGenEthernetDslamFlowNameLookupIndex':adGenEthernetDslamFlowNameLookupIndex,'adGenEthernetDslamFlowShaperTable':adGenEthernetDslamFlowShaperTable,'adGenEthernetDslamFlowShaperEntry':adGenEthernetDslamFlowShaperEntry,_A0:adGenEthernetDslamFlowShaperInterfaceLogicalIndex,_A1:adGenEthernetDslamFlowShaperPrioritySet,'adGenEthernetDslamFlowShaperRate':adGenEthernetDslamFlowShaperRate,'adGenEthernetDslamFlowShaperRowStatus':adGenEthernetDslamFlowShaperRowStatus,'adGenEthernetDslamFlowShaperLastErrorString':adGenEthernetDslamFlowShaperLastErrorString,'adGenEthernetDslamFlowShaperAlias':adGenEthernetDslamFlowShaperAlias,'adGenEthernetDslamFlowShaperOperationalStatus':adGenEthernetDslamFlowShaperOperationalStatus,'adGenEthernetDslamFlowShaperBurstSize':adGenEthernetDslamFlowShaperBurstSize,'adGenEthernetDslamFlowShaperFixedRate':adGenEthernetDslamFlowShaperFixedRate,'adGenEthernetDslamFlowShaperAssuredRate':adGenEthernetDslamFlowShaperAssuredRate,'adGenEthernetDslamFlowShaperDownstreamMinRate':adGenEthernetDslamFlowShaperDownstreamMinRate,'adGenSubscriberAccessStaticIpTable':adGenSubscriberAccessStaticIpTable,'adGenSubscriberAccessStaticIpEntry':adGenSubscriberAccessStaticIpEntry,_A2:adGenSubscriberAccessStaticIpAddress,'adGenSubscriberAccessStaticIpMacAddress':adGenSubscriberAccessStaticIpMacAddress,'adGenSubscriberAccessStaticIpGatewayIp':adGenSubscriberAccessStaticIpGatewayIp,'adGenSubscriberAccessStaticIpGatewayMac':adGenSubscriberAccessStaticIpGatewayMac,'adGenSubscriberAccessStaticIpLastErrorString':adGenSubscriberAccessStaticIpLastErrorString,'adGenSubscriberAccessStaticIpRowStatus':adGenSubscriberAccessStaticIpRowStatus,'adGenEthernetDslamFlowProfilesIndexNextTable':adGenEthernetDslamFlowProfilesIndexNextTable,'adGenEthernetDslamFlowProfilesIndexNextEntry':adGenEthernetDslamFlowProfilesIndexNextEntry,'adGenEthernetDslamFlowProfilesIndexNext':adGenEthernetDslamFlowProfilesIndexNext,'adGenEthernetDslamFlowProfilesLookupTable':adGenEthernetDslamFlowProfilesLookupTable,'adGenEthernetDslamFlowProfilesLookupEntry':adGenEthernetDslamFlowProfilesLookupEntry,_A3:adGenEthernetDslamFlowProfileLookupAlias,'adGenEthernetDslamFlowProfileLookupIndex':adGenEthernetDslamFlowProfileLookupIndex,'adGenEthernetDslamFlowShaperLookupTable':adGenEthernetDslamFlowShaperLookupTable,'adGenEthernetDslamFlowShaperLookupEntry':adGenEthernetDslamFlowShaperLookupEntry,_A4:adGenEthernetDslamFlowShaperLookupAlias,'adGenEthernetDslamFlowShaperLookupIfIndex':adGenEthernetDslamFlowShaperLookupIfIndex,'adGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex':adGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex,'adGenEthernetDslamFlowShaperLookupPrioritySet':adGenEthernetDslamFlowShaperLookupPrioritySet,'adGenEthernetDslamFlowRev2Table':adGenEthernetDslamFlowRev2Table,'adGenEthernetDslamFlowRev2Entry':adGenEthernetDslamFlowRev2Entry,_A5:adGenEthernetDslamFlowRev2Index,'adGenEthernetDslamFlowRev2Name':adGenEthernetDslamFlowRev2Name,'adGenEthernetDslamFlowRev2TrafficDirection':adGenEthernetDslamFlowRev2TrafficDirection,'adGenEthernetDslamFlowRev2NetworkSTag':adGenEthernetDslamFlowRev2NetworkSTag,'adGenEthernetDslamFlowRev2NetworkCTag':adGenEthernetDslamFlowRev2NetworkCTag,'adGenEthernetDslamFlowRev2CEVlan':adGenEthernetDslamFlowRev2CEVlan,'adGenEthernetDslamFlowRev2DownstreamForwardingMode':adGenEthernetDslamFlowRev2DownstreamForwardingMode,'adGenEthernetDslamFlowRev2DownstreamPbitMethod':adGenEthernetDslamFlowRev2DownstreamPbitMethod,'adGenEthernetDslamFlowRev2DownstreamPbitMarking':adGenEthernetDslamFlowRev2DownstreamPbitMarking,'adGenEthernetDslamFlowRev2DownstreamPbitMapping':adGenEthernetDslamFlowRev2DownstreamPbitMapping,'adGenEthernetDslamFlowRev2NetworkIngressPbit':adGenEthernetDslamFlowRev2NetworkIngressPbit,'adGenEthernetDslamFlowRev2NetworkIngressEtherType':adGenEthernetDslamFlowRev2NetworkIngressEtherType,'adGenEthernetDslamFlowRev2NetworkIngressDSCP':adGenEthernetDslamFlowRev2NetworkIngressDSCP,'adGenEthernetDslamFlowRev2NetworkIngressIPProtocolID':adGenEthernetDslamFlowRev2NetworkIngressIPProtocolID,'adGenEthernetDslamFlowRev2UpstreamForwardingMode':adGenEthernetDslamFlowRev2UpstreamForwardingMode,'adGenEthernetDslamFlowRev2UpstreamSTagPbitMethod':adGenEthernetDslamFlowRev2UpstreamSTagPbitMethod,'adGenEthernetDslamFlowRev2UpstreamSTagPbitMarking':adGenEthernetDslamFlowRev2UpstreamSTagPbitMarking,'adGenEthernetDslamFlowRev2UpstreamSTagPbitMapping':adGenEthernetDslamFlowRev2UpstreamSTagPbitMapping,'adGenEthernetDslamFlowRev2UpstreamCTagPbitMethod':adGenEthernetDslamFlowRev2UpstreamCTagPbitMethod,'adGenEthernetDslamFlowRev2UpstreamCTagPbitMarking':adGenEthernetDslamFlowRev2UpstreamCTagPbitMarking,'adGenEthernetDslamFlowRev2UpstreamCTagPbitMapping':adGenEthernetDslamFlowRev2UpstreamCTagPbitMapping,'adGenEthernetDslamFlowRev2CustomerIngressPbit':adGenEthernetDslamFlowRev2CustomerIngressPbit,'adGenEthernetDslamFlowRev2CustomerIngressEtherType':adGenEthernetDslamFlowRev2CustomerIngressEtherType,'adGenEthernetDslamFlowRev2CustomerIngressDSCP':adGenEthernetDslamFlowRev2CustomerIngressDSCP,'adGenEthernetDslamFlowRev2CustomerIngressIPProtocolID':adGenEthernetDslamFlowRev2CustomerIngressIPProtocolID,'adGenEthernetDslamFlowRev2CustomerIngressBroadcast':adGenEthernetDslamFlowRev2CustomerIngressBroadcast,'adGenEthernetDslamFlowRev2CustomerIngressMulticast':adGenEthernetDslamFlowRev2CustomerIngressMulticast,'adGenEthernetDslamFlowRev2CustomerIngressUnicast':adGenEthernetDslamFlowRev2CustomerIngressUnicast,'adGenEthernetDslamFlowRev2CustomerIngressPolicer':adGenEthernetDslamFlowRev2CustomerIngressPolicer,'adGenEthernetDslamFlowRev2EncapsMode':adGenEthernetDslamFlowRev2EncapsMode,'adGenEthernetDslamFlowRev2ManualAddrAging':adGenEthernetDslamFlowRev2ManualAddrAging,'adGenEthernetDslamFlowRev2IntermedAgent':adGenEthernetDslamFlowRev2IntermedAgent,'adGenEthernetDslamFlowRev2DhcpRelay':adGenEthernetDslamFlowRev2DhcpRelay,'adGenEthernetDslamFlowRev2Option82Insert':adGenEthernetDslamFlowRev2Option82Insert,'adGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod':adGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod,'adGenEthernetDslamFlowRev2IgmpProcessing':adGenEthernetDslamFlowRev2IgmpProcessing,'adGenEthernetDslamFlowRev2IgmpVersion':adGenEthernetDslamFlowRev2IgmpVersion,'adGenEthernetDslamFlowRev2LastMemberQueryInterval':adGenEthernetDslamFlowRev2LastMemberQueryInterval,'adGenEthernetDslamFlowRev2LastMemberQueryCount':adGenEthernetDslamFlowRev2LastMemberQueryCount,'adGenEthernetDslamFlowRev2ImmediateLeave':adGenEthernetDslamFlowRev2ImmediateLeave,'adGenEthernetDslamFlowRev2MaxAllowedMcastGroups':adGenEthernetDslamFlowRev2MaxAllowedMcastGroups,'adGenEthernetDslamFlowRev2DhcpPPPoERemoteId':adGenEthernetDslamFlowRev2DhcpPPPoERemoteId,'adGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics':adGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics,'adGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat':adGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat,'adGenEthernetDslamFlowRev2PPPoASessionTimeout':adGenEthernetDslamFlowRev2PPPoASessionTimeout,'adGenEthernetDslamFlowRev2InterfaceIfIndex':adGenEthernetDslamFlowRev2InterfaceIfIndex,'adGenEthernetDslamFlowRev2InterfaceLogicalIndex':adGenEthernetDslamFlowRev2InterfaceLogicalIndex,'adGenEthernetDslamFlowRev2LastErrorString':adGenEthernetDslamFlowRev2LastErrorString,'adGenEthernetDslamFlowRev2RowStatus':adGenEthernetDslamFlowRev2RowStatus,'adGenEthernetDslamFlowRev2NetworkIngressPolicer':adGenEthernetDslamFlowRev2NetworkIngressPolicer,'adGenEthernetDslamFlowRev2UpstreamDiscard':adGenEthernetDslamFlowRev2UpstreamDiscard,'adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth':adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth,'adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable':adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable,'adGenEthernetDslamFlowRev2ProfileName':adGenEthernetDslamFlowRev2ProfileName,'adGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable':adGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable,'adGenEthernetDslamFlowRev2NetworkIngressDSCPList':adGenEthernetDslamFlowRev2NetworkIngressDSCPList,'adGenEthernetDslamFlowRev2CustomerIngressDSCPList':adGenEthernetDslamFlowRev2CustomerIngressDSCPList,'adGenEthernetDslamFlowRev2IgmpRouterIP':adGenEthernetDslamFlowRev2IgmpRouterIP,'adGenEthernetDslamFlowRev2ActivationStatus':adGenEthernetDslamFlowRev2ActivationStatus,'adGenEthernetDslamFlowRev2ARPProcessing':adGenEthernetDslamFlowRev2ARPProcessing,'adGenEthernetDslamFlowRev2PPPoEProcessing':adGenEthernetDslamFlowRev2PPPoEProcessing,'adGenEthernetDslamFlowRev2SubscriberIpRowCreateError':adGenEthernetDslamFlowRev2SubscriberIpRowCreateError,'adGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber':adGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber,'adGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat':adGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat,'adGenEthernetDslamFlowRev2EvcName':adGenEthernetDslamFlowRev2EvcName,'adGenEthernetDslamFlowRev2EvcRoot':adGenEthernetDslamFlowRev2EvcRoot,'adGenEthernetDslamFlowRev2Dhcpv6Mode':adGenEthernetDslamFlowRev2Dhcpv6Mode,'adGenEthernetDslamFlowRev2Dhcpv6RelayAgent':adGenEthernetDslamFlowRev2Dhcpv6RelayAgent,'adGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted':adGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted,'adGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat':adGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat,'adGenEthernetDslamFlowRev2DownstreamQosMapProfile':adGenEthernetDslamFlowRev2DownstreamQosMapProfile,'adGenEthernetDslamFlowRev2Dhcpv6CurrMode':adGenEthernetDslamFlowRev2Dhcpv6CurrMode,'adGenEthernetDslamFlowRev2MatchSourceMacList':adGenEthernetDslamFlowRev2MatchSourceMacList,'adGenEthernetDslamFlowRev2MatchSourceMacLastErrorString':adGenEthernetDslamFlowRev2MatchSourceMacLastErrorString,'adGenEthernetDslamFlowRev2MatchNonIp':adGenEthernetDslamFlowRev2MatchNonIp,'adGenEthernetDslamFlowRev2NameLookupTable':adGenEthernetDslamFlowRev2NameLookupTable,'adGenEthernetDslamFlowRev2NameLookupEntry':adGenEthernetDslamFlowRev2NameLookupEntry,_A6:adGenEthernetDslamFlowRev2NameLookupName,'adGenEthernetDslamFlowRev2NameLookupIndex':adGenEthernetDslamFlowRev2NameLookupIndex,'adGenEthernetDslamFlowRev2IndexNextTable':adGenEthernetDslamFlowRev2IndexNextTable,'adGenEthernetDslamFlowRev2IndexNextEntry':adGenEthernetDslamFlowRev2IndexNextEntry,'adGenEthernetDslamFlowRev2IndexNext':adGenEthernetDslamFlowRev2IndexNext,'adGenEthernetDslamFlowQueueTable':adGenEthernetDslamFlowQueueTable,'adGenEthernetDslamFlowQueueTableEntry':adGenEthernetDslamFlowQueueTableEntry,'adGenEthernetDslamFlowHonorsSystemPbitCosMap':adGenEthernetDslamFlowHonorsSystemPbitCosMap,'adGenEthernetDslamFlowShaperQueuePriorityOrder':adGenEthernetDslamFlowShaperQueuePriorityOrder,'adGenEthernetDslamFlowAlarmsPrefix':adGenEthernetDslamFlowAlarmsPrefix,'adGenEthernetDslamFlowAlarms':adGenEthernetDslamFlowAlarms,'adGenEthernetDslamFlowDuplicateMacDetectedClr':adGenEthernetDslamFlowDuplicateMacDetectedClr,'adGenEthernetDslamFlowDuplicateMacDetectedAct':adGenEthernetDslamFlowDuplicateMacDetectedAct,'adGenEthernetDslamFlowMacAllocationAlarmClr':adGenEthernetDslamFlowMacAllocationAlarmClr,'adGenEthernetDslamFlowMacAllocationAlarmAct':adGenEthernetDslamFlowMacAllocationAlarmAct,'adGenEthernetDslamFlowScalarTable':adGenEthernetDslamFlowScalarTable,'adGenEthernetDslamFlowScalarTableEntry':adGenEthernetDslamFlowScalarTableEntry,'adGenEthernetFlowMatchSourceMacMaxAddresses':adGenEthernetFlowMatchSourceMacMaxAddresses,'adGenEthernetDslamFlowLoggingTable':adGenEthernetDslamFlowLoggingTable,'adGenEthernetDslamFlowLoggingEntry':adGenEthernetDslamFlowLoggingEntry,'adGenEthernetDslamFlowDhcpPppoeEventDebug':adGenEthernetDslamFlowDhcpPppoeEventDebug,'adGenEthernetDslamFlowMIB':adGenEthernetDslamFlowMIB})