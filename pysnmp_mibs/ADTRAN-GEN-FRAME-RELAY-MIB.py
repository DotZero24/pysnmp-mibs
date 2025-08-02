_i='adGenFrPVCDayIntervalNumber'
_h='adGenFrPVCIntervalNumber'
_g='adGenFrLinkBundleId'
_f='adGenFrLinkIfIndex'
_e='adGenFrLinkGroupIfIndex'
_d='adGenFrGroupDayIntervalNumber'
_c='adGenFrGroupIntervalNumber'
_b='TruthValue'
_a='DisplayString'
_Z='adGenSlotInfoIndex'
_Y='ADTRAN-GENSLOT-MIB'
_X='adGenFrPVCState'
_W='adGenFrPVCIfIndex'
_V='adGenFrGroupLmiStatus'
_U='testing'
_T='ifOperStatus'
_S='reset'
_R='down'
_Q='up'
_P='InetAddressType'
_O='sysName'
_N='SNMPv2-MIB'
_M='adTAeSCUTrapAlarmLevel'
_L='ADTRAN-TAeSCUEXT1-MIB'
_K='adTrapInformSeqNum'
_J='ADTRAN-GENTRAPINFORM-MIB'
_I='not-accessible'
_H='adGenFrPVCDLCIIndex'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='read-create'
_C='ADTRAN-GEN-FRAME-RELAY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortTrapIdentifier,=mibBuilder.importSymbols('ADTRAN-GENPORT-MIB','adGenPortTrapIdentifier')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_Y,_Z)
adTrapInformSeqNum,=mibBuilder.importSymbols(_J,_K)
adGenFrameRelay,adGenFrameRelayID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenFrameRelay','adGenFrameRelayID')
adTAeSCUTrapAlarmLevel,=mibBuilder.importSymbols(_L,_M)
InterfaceIndex,ifIndex,ifOperStatus=mibBuilder.importSymbols(_F,'InterfaceIndex',_G,_T)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_P)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_N,_O)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_a,'PhysAddress','RowStatus','TextualConvention',_b)
adGenFrameRelayMib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,29,1))
if mibBuilder.loadTexts:adGenFrameRelayMib.setRevisions(('2010-09-09 00:00','2010-09-02 00:00','2010-06-25 00:00','2010-05-03 00:00','2010-04-30 00:00','2010-03-29 00:00','2010-03-24 00:00'))
_AdGenFrameRelayMIBObjects_ObjectIdentity=ObjectIdentity
adGenFrameRelayMIBObjects=_AdGenFrameRelayMIBObjects_ObjectIdentity((1,3,6,1,4,1,664,5,70,29,1))
_AdGenFrGroup_ObjectIdentity=ObjectIdentity
adGenFrGroup=_AdGenFrGroup_ObjectIdentity((1,3,6,1,4,1,664,5,70,29,1,1))
_AdGenFrGroupTable_Object=MibTable
adGenFrGroupTable=_AdGenFrGroupTable_Object((1,3,6,1,4,1,664,5,70,29,1,1,2))
if mibBuilder.loadTexts:adGenFrGroupTable.setStatus(_A)
_AdGenFrGroupEntry_Object=MibTableRow
adGenFrGroupEntry=_AdGenFrGroupEntry_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1))
adGenFrGroupEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenFrGroupEntry.setStatus(_A)
_AdGenFrGroupRowStatus_Type=RowStatus
_AdGenFrGroupRowStatus_Object=MibTableColumn
adGenFrGroupRowStatus=_AdGenFrGroupRowStatus_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,1),_AdGenFrGroupRowStatus_Type())
adGenFrGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrGroupRowStatus.setStatus(_A)
_AdGenFrGroupStatusString_Type=DisplayString
_AdGenFrGroupStatusString_Object=MibTableColumn
adGenFrGroupStatusString=_AdGenFrGroupStatusString_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,2),_AdGenFrGroupStatusString_Type())
adGenFrGroupStatusString.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupStatusString.setStatus(_A)
class _AdGenFrGroupAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_U,3)))
_AdGenFrGroupAdminStatus_Type.__name__=_E
_AdGenFrGroupAdminStatus_Object=MibTableColumn
adGenFrGroupAdminStatus=_AdGenFrGroupAdminStatus_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,3),_AdGenFrGroupAdminStatus_Type())
adGenFrGroupAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrGroupAdminStatus.setStatus(_A)
class _AdGenFrGroupLmiType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('none',1),('ansi617d1994',3)))
_AdGenFrGroupLmiType_Type.__name__=_E
_AdGenFrGroupLmiType_Object=MibTableColumn
adGenFrGroupLmiType=_AdGenFrGroupLmiType_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,5),_AdGenFrGroupLmiType_Type())
adGenFrGroupLmiType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrGroupLmiType.setStatus(_A)
class _AdGenFrGroupLmiStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_AdGenFrGroupLmiStatus_Type.__name__=_E
_AdGenFrGroupLmiStatus_Object=MibTableColumn
adGenFrGroupLmiStatus=_AdGenFrGroupLmiStatus_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,6),_AdGenFrGroupLmiStatus_Type())
adGenFrGroupLmiStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupLmiStatus.setStatus(_A)
_AdGenFrGroupLmiEnquiryIn_Type=Counter32
_AdGenFrGroupLmiEnquiryIn_Object=MibTableColumn
adGenFrGroupLmiEnquiryIn=_AdGenFrGroupLmiEnquiryIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,7),_AdGenFrGroupLmiEnquiryIn_Type())
adGenFrGroupLmiEnquiryIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupLmiEnquiryIn.setStatus(_A)
_AdGenFrGroupLmiEnquiryOut_Type=Counter32
_AdGenFrGroupLmiEnquiryOut_Object=MibTableColumn
adGenFrGroupLmiEnquiryOut=_AdGenFrGroupLmiEnquiryOut_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,8),_AdGenFrGroupLmiEnquiryOut_Type())
adGenFrGroupLmiEnquiryOut.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupLmiEnquiryOut.setStatus(_A)
_AdGenFrGroupLmiStatusIn_Type=Counter32
_AdGenFrGroupLmiStatusIn_Object=MibTableColumn
adGenFrGroupLmiStatusIn=_AdGenFrGroupLmiStatusIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,9),_AdGenFrGroupLmiStatusIn_Type())
adGenFrGroupLmiStatusIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupLmiStatusIn.setStatus(_A)
_AdGenFrGroupLmiStatusOut_Type=Counter32
_AdGenFrGroupLmiStatusOut_Object=MibTableColumn
adGenFrGroupLmiStatusOut=_AdGenFrGroupLmiStatusOut_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,10),_AdGenFrGroupLmiStatusOut_Type())
adGenFrGroupLmiStatusOut.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupLmiStatusOut.setStatus(_A)
_AdGenFrGroupLmiInvalidIn_Type=Counter32
_AdGenFrGroupLmiInvalidIn_Object=MibTableColumn
adGenFrGroupLmiInvalidIn=_AdGenFrGroupLmiInvalidIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,11),_AdGenFrGroupLmiInvalidIn_Type())
adGenFrGroupLmiInvalidIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupLmiInvalidIn.setStatus(_A)
_AdGenFrGroupLmiStatusEnqTimeouts_Type=Counter32
_AdGenFrGroupLmiStatusEnqTimeouts_Object=MibTableColumn
adGenFrGroupLmiStatusEnqTimeouts=_AdGenFrGroupLmiStatusEnqTimeouts_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,12),_AdGenFrGroupLmiStatusEnqTimeouts_Type())
adGenFrGroupLmiStatusEnqTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupLmiStatusEnqTimeouts.setStatus(_A)
_AdGenFrGroupLmiStatusTimeouts_Type=Counter32
_AdGenFrGroupLmiStatusTimeouts_Object=MibTableColumn
adGenFrGroupLmiStatusTimeouts=_AdGenFrGroupLmiStatusTimeouts_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,13),_AdGenFrGroupLmiStatusTimeouts_Type())
adGenFrGroupLmiStatusTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupLmiStatusTimeouts.setStatus(_A)
class _AdGenFrGroupClearCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_S,1))
_AdGenFrGroupClearCounters_Type.__name__=_E
_AdGenFrGroupClearCounters_Object=MibTableColumn
adGenFrGroupClearCounters=_AdGenFrGroupClearCounters_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,14),_AdGenFrGroupClearCounters_Type())
adGenFrGroupClearCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrGroupClearCounters.setStatus(_A)
class _AdGenFrGroupClearPmHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_S,1))
_AdGenFrGroupClearPmHistory_Type.__name__=_E
_AdGenFrGroupClearPmHistory_Object=MibTableColumn
adGenFrGroupClearPmHistory=_AdGenFrGroupClearPmHistory_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,15),_AdGenFrGroupClearPmHistory_Type())
adGenFrGroupClearPmHistory.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrGroupClearPmHistory.setStatus(_A)
_AdGenFrGroupLinkLastCreateError_Type=DisplayString
_AdGenFrGroupLinkLastCreateError_Object=MibTableColumn
adGenFrGroupLinkLastCreateError=_AdGenFrGroupLinkLastCreateError_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,16),_AdGenFrGroupLinkLastCreateError_Type())
adGenFrGroupLinkLastCreateError.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupLinkLastCreateError.setStatus(_A)
_AdGenFrGroupPvcLastCreateError_Type=DisplayString
_AdGenFrGroupPvcLastCreateError_Object=MibTableColumn
adGenFrGroupPvcLastCreateError=_AdGenFrGroupPvcLastCreateError_Object((1,3,6,1,4,1,664,5,70,29,1,1,2,1,17),_AdGenFrGroupPvcLastCreateError_Type())
adGenFrGroupPvcLastCreateError.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupPvcLastCreateError.setStatus(_A)
_AdGenFrGroupCurrentTable_Object=MibTable
adGenFrGroupCurrentTable=_AdGenFrGroupCurrentTable_Object((1,3,6,1,4,1,664,5,70,29,1,1,3))
if mibBuilder.loadTexts:adGenFrGroupCurrentTable.setStatus(_A)
_AdGenFrGroupCurrentEntry_Object=MibTableRow
adGenFrGroupCurrentEntry=_AdGenFrGroupCurrentEntry_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1))
adGenFrGroupCurrentEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenFrGroupCurrentEntry.setStatus(_A)
_AdGenFrGroupCurrentInOctets_Type=Counter32
_AdGenFrGroupCurrentInOctets_Object=MibTableColumn
adGenFrGroupCurrentInOctets=_AdGenFrGroupCurrentInOctets_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,1),_AdGenFrGroupCurrentInOctets_Type())
adGenFrGroupCurrentInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentInOctets.setStatus(_A)
_AdGenFrGroupCurrentInPkts_Type=Counter32
_AdGenFrGroupCurrentInPkts_Object=MibTableColumn
adGenFrGroupCurrentInPkts=_AdGenFrGroupCurrentInPkts_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,2),_AdGenFrGroupCurrentInPkts_Type())
adGenFrGroupCurrentInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentInPkts.setStatus(_A)
_AdGenFrGroupCurrentInDiscards_Type=Counter32
_AdGenFrGroupCurrentInDiscards_Object=MibTableColumn
adGenFrGroupCurrentInDiscards=_AdGenFrGroupCurrentInDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,3),_AdGenFrGroupCurrentInDiscards_Type())
adGenFrGroupCurrentInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentInDiscards.setStatus(_A)
_AdGenFrGroupCurrentInErrors_Type=Counter32
_AdGenFrGroupCurrentInErrors_Object=MibTableColumn
adGenFrGroupCurrentInErrors=_AdGenFrGroupCurrentInErrors_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,4),_AdGenFrGroupCurrentInErrors_Type())
adGenFrGroupCurrentInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentInErrors.setStatus(_A)
_AdGenFrGroupCurrentOutOctets_Type=Counter32
_AdGenFrGroupCurrentOutOctets_Object=MibTableColumn
adGenFrGroupCurrentOutOctets=_AdGenFrGroupCurrentOutOctets_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,5),_AdGenFrGroupCurrentOutOctets_Type())
adGenFrGroupCurrentOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentOutOctets.setStatus(_A)
_AdGenFrGroupCurrentOutPkts_Type=Counter32
_AdGenFrGroupCurrentOutPkts_Object=MibTableColumn
adGenFrGroupCurrentOutPkts=_AdGenFrGroupCurrentOutPkts_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,6),_AdGenFrGroupCurrentOutPkts_Type())
adGenFrGroupCurrentOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentOutPkts.setStatus(_A)
_AdGenFrGroupCurrentOutDiscards_Type=Counter32
_AdGenFrGroupCurrentOutDiscards_Object=MibTableColumn
adGenFrGroupCurrentOutDiscards=_AdGenFrGroupCurrentOutDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,7),_AdGenFrGroupCurrentOutDiscards_Type())
adGenFrGroupCurrentOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentOutDiscards.setStatus(_A)
_AdGenFrGroupCurrentOutErrors_Type=Counter32
_AdGenFrGroupCurrentOutErrors_Object=MibTableColumn
adGenFrGroupCurrentOutErrors=_AdGenFrGroupCurrentOutErrors_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,8),_AdGenFrGroupCurrentOutErrors_Type())
adGenFrGroupCurrentOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentOutErrors.setStatus(_A)
_AdGenFrGroupCurrentLmiEnquiryIn_Type=Counter32
_AdGenFrGroupCurrentLmiEnquiryIn_Object=MibTableColumn
adGenFrGroupCurrentLmiEnquiryIn=_AdGenFrGroupCurrentLmiEnquiryIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,9),_AdGenFrGroupCurrentLmiEnquiryIn_Type())
adGenFrGroupCurrentLmiEnquiryIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentLmiEnquiryIn.setStatus(_A)
_AdGenFrGroupCurrentLmiEnquiryOut_Type=Counter32
_AdGenFrGroupCurrentLmiEnquiryOut_Object=MibTableColumn
adGenFrGroupCurrentLmiEnquiryOut=_AdGenFrGroupCurrentLmiEnquiryOut_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,10),_AdGenFrGroupCurrentLmiEnquiryOut_Type())
adGenFrGroupCurrentLmiEnquiryOut.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentLmiEnquiryOut.setStatus(_A)
_AdGenFrGroupCurrentLmiStatusIn_Type=Counter32
_AdGenFrGroupCurrentLmiStatusIn_Object=MibTableColumn
adGenFrGroupCurrentLmiStatusIn=_AdGenFrGroupCurrentLmiStatusIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,11),_AdGenFrGroupCurrentLmiStatusIn_Type())
adGenFrGroupCurrentLmiStatusIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentLmiStatusIn.setStatus(_A)
_AdGenFrGroupCurrentLmiStatusOut_Type=Counter32
_AdGenFrGroupCurrentLmiStatusOut_Object=MibTableColumn
adGenFrGroupCurrentLmiStatusOut=_AdGenFrGroupCurrentLmiStatusOut_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,12),_AdGenFrGroupCurrentLmiStatusOut_Type())
adGenFrGroupCurrentLmiStatusOut.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentLmiStatusOut.setStatus(_A)
_AdGenFrGroupCurrentLmiInvalidIn_Type=Counter32
_AdGenFrGroupCurrentLmiInvalidIn_Object=MibTableColumn
adGenFrGroupCurrentLmiInvalidIn=_AdGenFrGroupCurrentLmiInvalidIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,13),_AdGenFrGroupCurrentLmiInvalidIn_Type())
adGenFrGroupCurrentLmiInvalidIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentLmiInvalidIn.setStatus(_A)
_AdGenFrGroupCurrentLmiStatusEnqTimeouts_Type=Counter32
_AdGenFrGroupCurrentLmiStatusEnqTimeouts_Object=MibTableColumn
adGenFrGroupCurrentLmiStatusEnqTimeouts=_AdGenFrGroupCurrentLmiStatusEnqTimeouts_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,14),_AdGenFrGroupCurrentLmiStatusEnqTimeouts_Type())
adGenFrGroupCurrentLmiStatusEnqTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentLmiStatusEnqTimeouts.setStatus(_A)
_AdGenFrGroupCurrentLmiStatusTimeouts_Type=Counter32
_AdGenFrGroupCurrentLmiStatusTimeouts_Object=MibTableColumn
adGenFrGroupCurrentLmiStatusTimeouts=_AdGenFrGroupCurrentLmiStatusTimeouts_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,15),_AdGenFrGroupCurrentLmiStatusTimeouts_Type())
adGenFrGroupCurrentLmiStatusTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentLmiStatusTimeouts.setStatus(_A)
_AdGenFrGroupCurrentNetworkInactive_Type=Counter32
_AdGenFrGroupCurrentNetworkInactive_Object=MibTableColumn
adGenFrGroupCurrentNetworkInactive=_AdGenFrGroupCurrentNetworkInactive_Object((1,3,6,1,4,1,664,5,70,29,1,1,3,1,16),_AdGenFrGroupCurrentNetworkInactive_Type())
adGenFrGroupCurrentNetworkInactive.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupCurrentNetworkInactive.setStatus(_A)
_AdGenFrGroupIntervalTable_Object=MibTable
adGenFrGroupIntervalTable=_AdGenFrGroupIntervalTable_Object((1,3,6,1,4,1,664,5,70,29,1,1,4))
if mibBuilder.loadTexts:adGenFrGroupIntervalTable.setStatus(_A)
_AdGenFrGroupIntervalEntry_Object=MibTableRow
adGenFrGroupIntervalEntry=_AdGenFrGroupIntervalEntry_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1))
adGenFrGroupIntervalEntry.setIndexNames((0,_F,_G),(0,_C,_c))
if mibBuilder.loadTexts:adGenFrGroupIntervalEntry.setStatus(_A)
class _AdGenFrGroupIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AdGenFrGroupIntervalNumber_Type.__name__=_E
_AdGenFrGroupIntervalNumber_Object=MibTableColumn
adGenFrGroupIntervalNumber=_AdGenFrGroupIntervalNumber_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,1),_AdGenFrGroupIntervalNumber_Type())
adGenFrGroupIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenFrGroupIntervalNumber.setStatus(_A)
_AdGenFrGroupIntervalTimeStamp_Type=DisplayString
_AdGenFrGroupIntervalTimeStamp_Object=MibTableColumn
adGenFrGroupIntervalTimeStamp=_AdGenFrGroupIntervalTimeStamp_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,2),_AdGenFrGroupIntervalTimeStamp_Type())
adGenFrGroupIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalTimeStamp.setStatus(_A)
_AdGenFrGroupIntervalInOctets_Type=Counter32
_AdGenFrGroupIntervalInOctets_Object=MibTableColumn
adGenFrGroupIntervalInOctets=_AdGenFrGroupIntervalInOctets_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,3),_AdGenFrGroupIntervalInOctets_Type())
adGenFrGroupIntervalInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalInOctets.setStatus(_A)
_AdGenFrGroupIntervalInPkts_Type=Counter32
_AdGenFrGroupIntervalInPkts_Object=MibTableColumn
adGenFrGroupIntervalInPkts=_AdGenFrGroupIntervalInPkts_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,4),_AdGenFrGroupIntervalInPkts_Type())
adGenFrGroupIntervalInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalInPkts.setStatus(_A)
_AdGenFrGroupIntervalInDiscards_Type=Counter32
_AdGenFrGroupIntervalInDiscards_Object=MibTableColumn
adGenFrGroupIntervalInDiscards=_AdGenFrGroupIntervalInDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,5),_AdGenFrGroupIntervalInDiscards_Type())
adGenFrGroupIntervalInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalInDiscards.setStatus(_A)
_AdGenFrGroupIntervalInErrors_Type=Counter32
_AdGenFrGroupIntervalInErrors_Object=MibTableColumn
adGenFrGroupIntervalInErrors=_AdGenFrGroupIntervalInErrors_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,6),_AdGenFrGroupIntervalInErrors_Type())
adGenFrGroupIntervalInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalInErrors.setStatus(_A)
_AdGenFrGroupIntervalOutOctets_Type=Counter32
_AdGenFrGroupIntervalOutOctets_Object=MibTableColumn
adGenFrGroupIntervalOutOctets=_AdGenFrGroupIntervalOutOctets_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,7),_AdGenFrGroupIntervalOutOctets_Type())
adGenFrGroupIntervalOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalOutOctets.setStatus(_A)
_AdGenFrGroupIntervalOutPkts_Type=Counter32
_AdGenFrGroupIntervalOutPkts_Object=MibTableColumn
adGenFrGroupIntervalOutPkts=_AdGenFrGroupIntervalOutPkts_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,8),_AdGenFrGroupIntervalOutPkts_Type())
adGenFrGroupIntervalOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalOutPkts.setStatus(_A)
_AdGenFrGroupIntervalOutDiscards_Type=Counter32
_AdGenFrGroupIntervalOutDiscards_Object=MibTableColumn
adGenFrGroupIntervalOutDiscards=_AdGenFrGroupIntervalOutDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,9),_AdGenFrGroupIntervalOutDiscards_Type())
adGenFrGroupIntervalOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalOutDiscards.setStatus(_A)
_AdGenFrGroupIntervalOutErrors_Type=Counter32
_AdGenFrGroupIntervalOutErrors_Object=MibTableColumn
adGenFrGroupIntervalOutErrors=_AdGenFrGroupIntervalOutErrors_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,10),_AdGenFrGroupIntervalOutErrors_Type())
adGenFrGroupIntervalOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalOutErrors.setStatus(_A)
_AdGenFrGroupIntervalLmiEnquiryIn_Type=Counter32
_AdGenFrGroupIntervalLmiEnquiryIn_Object=MibTableColumn
adGenFrGroupIntervalLmiEnquiryIn=_AdGenFrGroupIntervalLmiEnquiryIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,11),_AdGenFrGroupIntervalLmiEnquiryIn_Type())
adGenFrGroupIntervalLmiEnquiryIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalLmiEnquiryIn.setStatus(_A)
_AdGenFrGroupIntervalLmiEnquiryOut_Type=Counter32
_AdGenFrGroupIntervalLmiEnquiryOut_Object=MibTableColumn
adGenFrGroupIntervalLmiEnquiryOut=_AdGenFrGroupIntervalLmiEnquiryOut_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,12),_AdGenFrGroupIntervalLmiEnquiryOut_Type())
adGenFrGroupIntervalLmiEnquiryOut.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalLmiEnquiryOut.setStatus(_A)
_AdGenFrGroupIntervalLmiStatusIn_Type=Counter32
_AdGenFrGroupIntervalLmiStatusIn_Object=MibTableColumn
adGenFrGroupIntervalLmiStatusIn=_AdGenFrGroupIntervalLmiStatusIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,13),_AdGenFrGroupIntervalLmiStatusIn_Type())
adGenFrGroupIntervalLmiStatusIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalLmiStatusIn.setStatus(_A)
_AdGenFrGroupIntervalLmiStatusOut_Type=Counter32
_AdGenFrGroupIntervalLmiStatusOut_Object=MibTableColumn
adGenFrGroupIntervalLmiStatusOut=_AdGenFrGroupIntervalLmiStatusOut_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,14),_AdGenFrGroupIntervalLmiStatusOut_Type())
adGenFrGroupIntervalLmiStatusOut.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalLmiStatusOut.setStatus(_A)
_AdGenFrGroupIntervalLmiInvalidIn_Type=Counter32
_AdGenFrGroupIntervalLmiInvalidIn_Object=MibTableColumn
adGenFrGroupIntervalLmiInvalidIn=_AdGenFrGroupIntervalLmiInvalidIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,15),_AdGenFrGroupIntervalLmiInvalidIn_Type())
adGenFrGroupIntervalLmiInvalidIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalLmiInvalidIn.setStatus(_A)
_AdGenFrGroupIntervalLmiStatusEnqTimeouts_Type=Counter32
_AdGenFrGroupIntervalLmiStatusEnqTimeouts_Object=MibTableColumn
adGenFrGroupIntervalLmiStatusEnqTimeouts=_AdGenFrGroupIntervalLmiStatusEnqTimeouts_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,16),_AdGenFrGroupIntervalLmiStatusEnqTimeouts_Type())
adGenFrGroupIntervalLmiStatusEnqTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalLmiStatusEnqTimeouts.setStatus(_A)
_AdGenFrGroupIntervalLmiStatusTimeouts_Type=Counter32
_AdGenFrGroupIntervalLmiStatusTimeouts_Object=MibTableColumn
adGenFrGroupIntervalLmiStatusTimeouts=_AdGenFrGroupIntervalLmiStatusTimeouts_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,17),_AdGenFrGroupIntervalLmiStatusTimeouts_Type())
adGenFrGroupIntervalLmiStatusTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalLmiStatusTimeouts.setStatus(_A)
_AdGenFrGroupIntervalNetworkInactive_Type=Counter32
_AdGenFrGroupIntervalNetworkInactive_Object=MibTableColumn
adGenFrGroupIntervalNetworkInactive=_AdGenFrGroupIntervalNetworkInactive_Object((1,3,6,1,4,1,664,5,70,29,1,1,4,1,18),_AdGenFrGroupIntervalNetworkInactive_Type())
adGenFrGroupIntervalNetworkInactive.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupIntervalNetworkInactive.setStatus(_A)
_AdGenFrGroupDayCurrentTable_Object=MibTable
adGenFrGroupDayCurrentTable=_AdGenFrGroupDayCurrentTable_Object((1,3,6,1,4,1,664,5,70,29,1,1,5))
if mibBuilder.loadTexts:adGenFrGroupDayCurrentTable.setStatus(_A)
_AdGenFrGroupDayCurrentEntry_Object=MibTableRow
adGenFrGroupDayCurrentEntry=_AdGenFrGroupDayCurrentEntry_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1))
adGenFrGroupDayCurrentEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenFrGroupDayCurrentEntry.setStatus(_A)
_AdGenFrGroupDayCurrentInOctets_Type=Counter32
_AdGenFrGroupDayCurrentInOctets_Object=MibTableColumn
adGenFrGroupDayCurrentInOctets=_AdGenFrGroupDayCurrentInOctets_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,1),_AdGenFrGroupDayCurrentInOctets_Type())
adGenFrGroupDayCurrentInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentInOctets.setStatus(_A)
_AdGenFrGroupDayCurrentInPkts_Type=Counter32
_AdGenFrGroupDayCurrentInPkts_Object=MibTableColumn
adGenFrGroupDayCurrentInPkts=_AdGenFrGroupDayCurrentInPkts_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,2),_AdGenFrGroupDayCurrentInPkts_Type())
adGenFrGroupDayCurrentInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentInPkts.setStatus(_A)
_AdGenFrGroupDayCurrentInDiscards_Type=Counter32
_AdGenFrGroupDayCurrentInDiscards_Object=MibTableColumn
adGenFrGroupDayCurrentInDiscards=_AdGenFrGroupDayCurrentInDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,3),_AdGenFrGroupDayCurrentInDiscards_Type())
adGenFrGroupDayCurrentInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentInDiscards.setStatus(_A)
_AdGenFrGroupDayCurrentInErrors_Type=Counter32
_AdGenFrGroupDayCurrentInErrors_Object=MibTableColumn
adGenFrGroupDayCurrentInErrors=_AdGenFrGroupDayCurrentInErrors_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,4),_AdGenFrGroupDayCurrentInErrors_Type())
adGenFrGroupDayCurrentInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentInErrors.setStatus(_A)
_AdGenFrGroupDayCurrentOutOctets_Type=Counter32
_AdGenFrGroupDayCurrentOutOctets_Object=MibTableColumn
adGenFrGroupDayCurrentOutOctets=_AdGenFrGroupDayCurrentOutOctets_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,5),_AdGenFrGroupDayCurrentOutOctets_Type())
adGenFrGroupDayCurrentOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentOutOctets.setStatus(_A)
_AdGenFrGroupDayCurrentOutPkts_Type=Counter32
_AdGenFrGroupDayCurrentOutPkts_Object=MibTableColumn
adGenFrGroupDayCurrentOutPkts=_AdGenFrGroupDayCurrentOutPkts_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,6),_AdGenFrGroupDayCurrentOutPkts_Type())
adGenFrGroupDayCurrentOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentOutPkts.setStatus(_A)
_AdGenFrGroupDayCurrentOutDiscards_Type=Counter32
_AdGenFrGroupDayCurrentOutDiscards_Object=MibTableColumn
adGenFrGroupDayCurrentOutDiscards=_AdGenFrGroupDayCurrentOutDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,7),_AdGenFrGroupDayCurrentOutDiscards_Type())
adGenFrGroupDayCurrentOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentOutDiscards.setStatus(_A)
_AdGenFrGroupDayCurrentOutErrors_Type=Counter32
_AdGenFrGroupDayCurrentOutErrors_Object=MibTableColumn
adGenFrGroupDayCurrentOutErrors=_AdGenFrGroupDayCurrentOutErrors_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,8),_AdGenFrGroupDayCurrentOutErrors_Type())
adGenFrGroupDayCurrentOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentOutErrors.setStatus(_A)
_AdGenFrGroupDayCurrentLmiEnquiryIn_Type=Counter32
_AdGenFrGroupDayCurrentLmiEnquiryIn_Object=MibTableColumn
adGenFrGroupDayCurrentLmiEnquiryIn=_AdGenFrGroupDayCurrentLmiEnquiryIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,9),_AdGenFrGroupDayCurrentLmiEnquiryIn_Type())
adGenFrGroupDayCurrentLmiEnquiryIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentLmiEnquiryIn.setStatus(_A)
_AdGenFrGroupDayCurrentLmiEnquiryOut_Type=Counter32
_AdGenFrGroupDayCurrentLmiEnquiryOut_Object=MibTableColumn
adGenFrGroupDayCurrentLmiEnquiryOut=_AdGenFrGroupDayCurrentLmiEnquiryOut_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,10),_AdGenFrGroupDayCurrentLmiEnquiryOut_Type())
adGenFrGroupDayCurrentLmiEnquiryOut.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentLmiEnquiryOut.setStatus(_A)
_AdGenFrGroupDayCurrentLmiStatusIn_Type=Counter32
_AdGenFrGroupDayCurrentLmiStatusIn_Object=MibTableColumn
adGenFrGroupDayCurrentLmiStatusIn=_AdGenFrGroupDayCurrentLmiStatusIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,11),_AdGenFrGroupDayCurrentLmiStatusIn_Type())
adGenFrGroupDayCurrentLmiStatusIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentLmiStatusIn.setStatus(_A)
_AdGenFrGroupDayCurrentLmiStatusOut_Type=Counter32
_AdGenFrGroupDayCurrentLmiStatusOut_Object=MibTableColumn
adGenFrGroupDayCurrentLmiStatusOut=_AdGenFrGroupDayCurrentLmiStatusOut_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,12),_AdGenFrGroupDayCurrentLmiStatusOut_Type())
adGenFrGroupDayCurrentLmiStatusOut.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentLmiStatusOut.setStatus(_A)
_AdGenFrGroupDayCurrentLmiInvalidIn_Type=Counter32
_AdGenFrGroupDayCurrentLmiInvalidIn_Object=MibTableColumn
adGenFrGroupDayCurrentLmiInvalidIn=_AdGenFrGroupDayCurrentLmiInvalidIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,13),_AdGenFrGroupDayCurrentLmiInvalidIn_Type())
adGenFrGroupDayCurrentLmiInvalidIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentLmiInvalidIn.setStatus(_A)
_AdGenFrGroupDayCurrentLmiStatusEnqTimeouts_Type=Counter32
_AdGenFrGroupDayCurrentLmiStatusEnqTimeouts_Object=MibTableColumn
adGenFrGroupDayCurrentLmiStatusEnqTimeouts=_AdGenFrGroupDayCurrentLmiStatusEnqTimeouts_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,14),_AdGenFrGroupDayCurrentLmiStatusEnqTimeouts_Type())
adGenFrGroupDayCurrentLmiStatusEnqTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentLmiStatusEnqTimeouts.setStatus(_A)
_AdGenFrGroupDayCurrentLmiStatusTimeouts_Type=Counter32
_AdGenFrGroupDayCurrentLmiStatusTimeouts_Object=MibTableColumn
adGenFrGroupDayCurrentLmiStatusTimeouts=_AdGenFrGroupDayCurrentLmiStatusTimeouts_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,15),_AdGenFrGroupDayCurrentLmiStatusTimeouts_Type())
adGenFrGroupDayCurrentLmiStatusTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentLmiStatusTimeouts.setStatus(_A)
_AdGenFrGroupDayCurrentNetworkInactive_Type=Counter32
_AdGenFrGroupDayCurrentNetworkInactive_Object=MibTableColumn
adGenFrGroupDayCurrentNetworkInactive=_AdGenFrGroupDayCurrentNetworkInactive_Object((1,3,6,1,4,1,664,5,70,29,1,1,5,1,16),_AdGenFrGroupDayCurrentNetworkInactive_Type())
adGenFrGroupDayCurrentNetworkInactive.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayCurrentNetworkInactive.setStatus(_A)
_AdGenFrGroupDayIntervalTable_Object=MibTable
adGenFrGroupDayIntervalTable=_AdGenFrGroupDayIntervalTable_Object((1,3,6,1,4,1,664,5,70,29,1,1,6))
if mibBuilder.loadTexts:adGenFrGroupDayIntervalTable.setStatus(_A)
_AdGenFrGroupDayIntervalEntry_Object=MibTableRow
adGenFrGroupDayIntervalEntry=_AdGenFrGroupDayIntervalEntry_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1))
adGenFrGroupDayIntervalEntry.setIndexNames((0,_F,_G),(0,_C,_d))
if mibBuilder.loadTexts:adGenFrGroupDayIntervalEntry.setStatus(_A)
class _AdGenFrGroupDayIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AdGenFrGroupDayIntervalNumber_Type.__name__=_E
_AdGenFrGroupDayIntervalNumber_Object=MibTableColumn
adGenFrGroupDayIntervalNumber=_AdGenFrGroupDayIntervalNumber_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,1),_AdGenFrGroupDayIntervalNumber_Type())
adGenFrGroupDayIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalNumber.setStatus(_A)
_AdGenFrGroupDayIntervalTimeStamp_Type=DisplayString
_AdGenFrGroupDayIntervalTimeStamp_Object=MibTableColumn
adGenFrGroupDayIntervalTimeStamp=_AdGenFrGroupDayIntervalTimeStamp_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,2),_AdGenFrGroupDayIntervalTimeStamp_Type())
adGenFrGroupDayIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalTimeStamp.setStatus(_A)
_AdGenFrGroupDayIntervalInOctets_Type=Counter32
_AdGenFrGroupDayIntervalInOctets_Object=MibTableColumn
adGenFrGroupDayIntervalInOctets=_AdGenFrGroupDayIntervalInOctets_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,3),_AdGenFrGroupDayIntervalInOctets_Type())
adGenFrGroupDayIntervalInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalInOctets.setStatus(_A)
_AdGenFrGroupDayIntervalInPkts_Type=Counter32
_AdGenFrGroupDayIntervalInPkts_Object=MibTableColumn
adGenFrGroupDayIntervalInPkts=_AdGenFrGroupDayIntervalInPkts_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,4),_AdGenFrGroupDayIntervalInPkts_Type())
adGenFrGroupDayIntervalInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalInPkts.setStatus(_A)
_AdGenFrGroupDayIntervalInDiscards_Type=Counter32
_AdGenFrGroupDayIntervalInDiscards_Object=MibTableColumn
adGenFrGroupDayIntervalInDiscards=_AdGenFrGroupDayIntervalInDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,5),_AdGenFrGroupDayIntervalInDiscards_Type())
adGenFrGroupDayIntervalInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalInDiscards.setStatus(_A)
_AdGenFrGroupDayIntervalInErrors_Type=Counter32
_AdGenFrGroupDayIntervalInErrors_Object=MibTableColumn
adGenFrGroupDayIntervalInErrors=_AdGenFrGroupDayIntervalInErrors_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,6),_AdGenFrGroupDayIntervalInErrors_Type())
adGenFrGroupDayIntervalInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalInErrors.setStatus(_A)
_AdGenFrGroupDayIntervalOutOctets_Type=Counter32
_AdGenFrGroupDayIntervalOutOctets_Object=MibTableColumn
adGenFrGroupDayIntervalOutOctets=_AdGenFrGroupDayIntervalOutOctets_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,7),_AdGenFrGroupDayIntervalOutOctets_Type())
adGenFrGroupDayIntervalOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalOutOctets.setStatus(_A)
_AdGenFrGroupDayIntervalOutPkts_Type=Counter32
_AdGenFrGroupDayIntervalOutPkts_Object=MibTableColumn
adGenFrGroupDayIntervalOutPkts=_AdGenFrGroupDayIntervalOutPkts_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,8),_AdGenFrGroupDayIntervalOutPkts_Type())
adGenFrGroupDayIntervalOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalOutPkts.setStatus(_A)
_AdGenFrGroupDayIntervalOutDiscards_Type=Counter32
_AdGenFrGroupDayIntervalOutDiscards_Object=MibTableColumn
adGenFrGroupDayIntervalOutDiscards=_AdGenFrGroupDayIntervalOutDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,9),_AdGenFrGroupDayIntervalOutDiscards_Type())
adGenFrGroupDayIntervalOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalOutDiscards.setStatus(_A)
_AdGenFrGroupDayIntervalOutErrors_Type=Counter32
_AdGenFrGroupDayIntervalOutErrors_Object=MibTableColumn
adGenFrGroupDayIntervalOutErrors=_AdGenFrGroupDayIntervalOutErrors_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,10),_AdGenFrGroupDayIntervalOutErrors_Type())
adGenFrGroupDayIntervalOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalOutErrors.setStatus(_A)
_AdGenFrGroupDayIntervalLmiEnquiryIn_Type=Counter32
_AdGenFrGroupDayIntervalLmiEnquiryIn_Object=MibTableColumn
adGenFrGroupDayIntervalLmiEnquiryIn=_AdGenFrGroupDayIntervalLmiEnquiryIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,11),_AdGenFrGroupDayIntervalLmiEnquiryIn_Type())
adGenFrGroupDayIntervalLmiEnquiryIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalLmiEnquiryIn.setStatus(_A)
_AdGenFrGroupDayIntervalLmiEnquiryOut_Type=Counter32
_AdGenFrGroupDayIntervalLmiEnquiryOut_Object=MibTableColumn
adGenFrGroupDayIntervalLmiEnquiryOut=_AdGenFrGroupDayIntervalLmiEnquiryOut_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,12),_AdGenFrGroupDayIntervalLmiEnquiryOut_Type())
adGenFrGroupDayIntervalLmiEnquiryOut.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalLmiEnquiryOut.setStatus(_A)
_AdGenFrGroupDayIntervalLmiStatusIn_Type=Counter32
_AdGenFrGroupDayIntervalLmiStatusIn_Object=MibTableColumn
adGenFrGroupDayIntervalLmiStatusIn=_AdGenFrGroupDayIntervalLmiStatusIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,13),_AdGenFrGroupDayIntervalLmiStatusIn_Type())
adGenFrGroupDayIntervalLmiStatusIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalLmiStatusIn.setStatus(_A)
_AdGenFrGroupDayIntervalLmiStatusOut_Type=Counter32
_AdGenFrGroupDayIntervalLmiStatusOut_Object=MibTableColumn
adGenFrGroupDayIntervalLmiStatusOut=_AdGenFrGroupDayIntervalLmiStatusOut_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,14),_AdGenFrGroupDayIntervalLmiStatusOut_Type())
adGenFrGroupDayIntervalLmiStatusOut.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalLmiStatusOut.setStatus(_A)
_AdGenFrGroupDayIntervalLmiInvalidIn_Type=Counter32
_AdGenFrGroupDayIntervalLmiInvalidIn_Object=MibTableColumn
adGenFrGroupDayIntervalLmiInvalidIn=_AdGenFrGroupDayIntervalLmiInvalidIn_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,15),_AdGenFrGroupDayIntervalLmiInvalidIn_Type())
adGenFrGroupDayIntervalLmiInvalidIn.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalLmiInvalidIn.setStatus(_A)
_AdGenFrGroupDayIntervalLmiStatusEnqTimeouts_Type=Counter32
_AdGenFrGroupDayIntervalLmiStatusEnqTimeouts_Object=MibTableColumn
adGenFrGroupDayIntervalLmiStatusEnqTimeouts=_AdGenFrGroupDayIntervalLmiStatusEnqTimeouts_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,16),_AdGenFrGroupDayIntervalLmiStatusEnqTimeouts_Type())
adGenFrGroupDayIntervalLmiStatusEnqTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalLmiStatusEnqTimeouts.setStatus(_A)
_AdGenFrGroupDayIntervalLmiStatusTimeouts_Type=Counter32
_AdGenFrGroupDayIntervalLmiStatusTimeouts_Object=MibTableColumn
adGenFrGroupDayIntervalLmiStatusTimeouts=_AdGenFrGroupDayIntervalLmiStatusTimeouts_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,17),_AdGenFrGroupDayIntervalLmiStatusTimeouts_Type())
adGenFrGroupDayIntervalLmiStatusTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalLmiStatusTimeouts.setStatus(_A)
_AdGenFrGroupDayIntervalNetworkInactive_Type=Counter32
_AdGenFrGroupDayIntervalNetworkInactive_Object=MibTableColumn
adGenFrGroupDayIntervalNetworkInactive=_AdGenFrGroupDayIntervalNetworkInactive_Object((1,3,6,1,4,1,664,5,70,29,1,1,6,1,18),_AdGenFrGroupDayIntervalNetworkInactive_Type())
adGenFrGroupDayIntervalNetworkInactive.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrGroupDayIntervalNetworkInactive.setStatus(_A)
_AdGenFrLink_ObjectIdentity=ObjectIdentity
adGenFrLink=_AdGenFrLink_ObjectIdentity((1,3,6,1,4,1,664,5,70,29,1,2))
_AdGenFrLinkTable_Object=MibTable
adGenFrLinkTable=_AdGenFrLinkTable_Object((1,3,6,1,4,1,664,5,70,29,1,2,2))
if mibBuilder.loadTexts:adGenFrLinkTable.setStatus(_A)
_AdGenFrLinkEntry_Object=MibTableRow
adGenFrLinkEntry=_AdGenFrLinkEntry_Object((1,3,6,1,4,1,664,5,70,29,1,2,2,1))
adGenFrLinkEntry.setIndexNames((0,_C,_e),(0,_C,_f),(0,_C,_g))
if mibBuilder.loadTexts:adGenFrLinkEntry.setStatus(_A)
_AdGenFrLinkGroupIfIndex_Type=InterfaceIndex
_AdGenFrLinkGroupIfIndex_Object=MibTableColumn
adGenFrLinkGroupIfIndex=_AdGenFrLinkGroupIfIndex_Object((1,3,6,1,4,1,664,5,70,29,1,2,2,1,1),_AdGenFrLinkGroupIfIndex_Type())
adGenFrLinkGroupIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenFrLinkGroupIfIndex.setStatus(_A)
_AdGenFrLinkIfIndex_Type=InterfaceIndex
_AdGenFrLinkIfIndex_Object=MibTableColumn
adGenFrLinkIfIndex=_AdGenFrLinkIfIndex_Object((1,3,6,1,4,1,664,5,70,29,1,2,2,1,2),_AdGenFrLinkIfIndex_Type())
adGenFrLinkIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenFrLinkIfIndex.setStatus(_A)
class _AdGenFrLinkBundleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AdGenFrLinkBundleId_Type.__name__=_E
_AdGenFrLinkBundleId_Object=MibTableColumn
adGenFrLinkBundleId=_AdGenFrLinkBundleId_Object((1,3,6,1,4,1,664,5,70,29,1,2,2,1,3),_AdGenFrLinkBundleId_Type())
adGenFrLinkBundleId.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenFrLinkBundleId.setStatus(_A)
_AdGenFrLinkRowStatus_Type=RowStatus
_AdGenFrLinkRowStatus_Object=MibTableColumn
adGenFrLinkRowStatus=_AdGenFrLinkRowStatus_Object((1,3,6,1,4,1,664,5,70,29,1,2,2,1,4),_AdGenFrLinkRowStatus_Type())
adGenFrLinkRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrLinkRowStatus.setStatus(_A)
class _AdGenFrLinkTimeslots_Type(DisplayString):defaultValue=OctetString('1-24')
_AdGenFrLinkTimeslots_Type.__name__=_a
_AdGenFrLinkTimeslots_Object=MibTableColumn
adGenFrLinkTimeslots=_AdGenFrLinkTimeslots_Object((1,3,6,1,4,1,664,5,70,29,1,2,2,1,5),_AdGenFrLinkTimeslots_Type())
adGenFrLinkTimeslots.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrLinkTimeslots.setStatus(_A)
_AdGenFrLinkStatusString_Type=DisplayString
_AdGenFrLinkStatusString_Object=MibTableColumn
adGenFrLinkStatusString=_AdGenFrLinkStatusString_Object((1,3,6,1,4,1,664,5,70,29,1,2,2,1,7),_AdGenFrLinkStatusString_Type())
adGenFrLinkStatusString.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrLinkStatusString.setStatus(_A)
_AdGenFrPVC_ObjectIdentity=ObjectIdentity
adGenFrPVC=_AdGenFrPVC_ObjectIdentity((1,3,6,1,4,1,664,5,70,29,1,3))
_AdGenFrPVCTable_Object=MibTable
adGenFrPVCTable=_AdGenFrPVCTable_Object((1,3,6,1,4,1,664,5,70,29,1,3,4))
if mibBuilder.loadTexts:adGenFrPVCTable.setStatus(_A)
_AdGenFrPVCEntry_Object=MibTableRow
adGenFrPVCEntry=_AdGenFrPVCEntry_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1))
adGenFrPVCEntry.setIndexNames((0,_F,_G),(0,_C,_H))
if mibBuilder.loadTexts:adGenFrPVCEntry.setStatus(_A)
_AdGenFrPVCIfIndex_Type=InterfaceIndex
_AdGenFrPVCIfIndex_Object=MibTableColumn
adGenFrPVCIfIndex=_AdGenFrPVCIfIndex_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,1),_AdGenFrPVCIfIndex_Type())
adGenFrPVCIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIfIndex.setStatus(_A)
class _AdGenFrPVCDLCIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,991))
_AdGenFrPVCDLCIIndex_Type.__name__=_E
_AdGenFrPVCDLCIIndex_Object=MibTableColumn
adGenFrPVCDLCIIndex=_AdGenFrPVCDLCIIndex_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,2),_AdGenFrPVCDLCIIndex_Type())
adGenFrPVCDLCIIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDLCIIndex.setStatus(_A)
_AdGenFrPVCStatusString_Type=DisplayString
_AdGenFrPVCStatusString_Object=MibTableColumn
adGenFrPVCStatusString=_AdGenFrPVCStatusString_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,3),_AdGenFrPVCStatusString_Type())
adGenFrPVCStatusString.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCStatusString.setStatus(_A)
class _AdGenFrPVCAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_U,3)))
_AdGenFrPVCAdminStatus_Type.__name__=_E
_AdGenFrPVCAdminStatus_Object=MibTableColumn
adGenFrPVCAdminStatus=_AdGenFrPVCAdminStatus_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,4),_AdGenFrPVCAdminStatus_Type())
adGenFrPVCAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCAdminStatus.setStatus(_A)
class _AdGenFrPVCState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('new',1),('none',2),('active',3),('inactive',4),('deleted',5)))
_AdGenFrPVCState_Type.__name__=_E
_AdGenFrPVCState_Object=MibTableColumn
adGenFrPVCState=_AdGenFrPVCState_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,5),_AdGenFrPVCState_Type())
adGenFrPVCState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCState.setStatus(_A)
class _AdGenFrPVCEncapsulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ipv4',1))
_AdGenFrPVCEncapsulation_Type.__name__=_E
_AdGenFrPVCEncapsulation_Object=MibTableColumn
adGenFrPVCEncapsulation=_AdGenFrPVCEncapsulation_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,6),_AdGenFrPVCEncapsulation_Type())
adGenFrPVCEncapsulation.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCEncapsulation.setStatus(_A)
class _AdGenFrPVCPrimaryPeerIpAddressType_Type(InetAddressType):defaultValue=1
_AdGenFrPVCPrimaryPeerIpAddressType_Type.__name__=_P
_AdGenFrPVCPrimaryPeerIpAddressType_Object=MibTableColumn
adGenFrPVCPrimaryPeerIpAddressType=_AdGenFrPVCPrimaryPeerIpAddressType_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,7),_AdGenFrPVCPrimaryPeerIpAddressType_Type())
adGenFrPVCPrimaryPeerIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCPrimaryPeerIpAddressType.setStatus(_A)
_AdGenFrPVCPrimaryPeerIpAddress_Type=InetAddress
_AdGenFrPVCPrimaryPeerIpAddress_Object=MibTableColumn
adGenFrPVCPrimaryPeerIpAddress=_AdGenFrPVCPrimaryPeerIpAddress_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,8),_AdGenFrPVCPrimaryPeerIpAddress_Type())
adGenFrPVCPrimaryPeerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCPrimaryPeerIpAddress.setStatus(_A)
class _AdGenFrPVCSecondaryPeerAddressType_Type(InetAddressType):defaultValue=1
_AdGenFrPVCSecondaryPeerAddressType_Type.__name__=_P
_AdGenFrPVCSecondaryPeerAddressType_Object=MibTableColumn
adGenFrPVCSecondaryPeerAddressType=_AdGenFrPVCSecondaryPeerAddressType_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,9),_AdGenFrPVCSecondaryPeerAddressType_Type())
adGenFrPVCSecondaryPeerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCSecondaryPeerAddressType.setStatus(_A)
_AdGenFrPVCSecondaryPeerIpAddress_Type=InetAddress
_AdGenFrPVCSecondaryPeerIpAddress_Object=MibTableColumn
adGenFrPVCSecondaryPeerIpAddress=_AdGenFrPVCSecondaryPeerIpAddress_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,10),_AdGenFrPVCSecondaryPeerIpAddress_Type())
adGenFrPVCSecondaryPeerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCSecondaryPeerIpAddress.setStatus(_A)
class _AdGenFrPVCPrimaryGatewayAddressType_Type(InetAddressType):defaultValue=1
_AdGenFrPVCPrimaryGatewayAddressType_Type.__name__=_P
_AdGenFrPVCPrimaryGatewayAddressType_Object=MibTableColumn
adGenFrPVCPrimaryGatewayAddressType=_AdGenFrPVCPrimaryGatewayAddressType_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,11),_AdGenFrPVCPrimaryGatewayAddressType_Type())
adGenFrPVCPrimaryGatewayAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCPrimaryGatewayAddressType.setStatus(_A)
_AdGenFrPVCPrimaryGatewayAddress_Type=InetAddress
_AdGenFrPVCPrimaryGatewayAddress_Object=MibTableColumn
adGenFrPVCPrimaryGatewayAddress=_AdGenFrPVCPrimaryGatewayAddress_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,12),_AdGenFrPVCPrimaryGatewayAddress_Type())
adGenFrPVCPrimaryGatewayAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCPrimaryGatewayAddress.setStatus(_A)
class _AdGenFrPVCInverseArpEnable_Type(TruthValue):defaultValue=1
_AdGenFrPVCInverseArpEnable_Type.__name__=_b
_AdGenFrPVCInverseArpEnable_Object=MibTableColumn
adGenFrPVCInverseArpEnable=_AdGenFrPVCInverseArpEnable_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,19),_AdGenFrPVCInverseArpEnable_Type())
adGenFrPVCInverseArpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCInverseArpEnable.setStatus(_A)
_AdGenFrPVCLearnedPrimaryPeerIpAddressType_Type=InetAddressType
_AdGenFrPVCLearnedPrimaryPeerIpAddressType_Object=MibTableColumn
adGenFrPVCLearnedPrimaryPeerIpAddressType=_AdGenFrPVCLearnedPrimaryPeerIpAddressType_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,20),_AdGenFrPVCLearnedPrimaryPeerIpAddressType_Type())
adGenFrPVCLearnedPrimaryPeerIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCLearnedPrimaryPeerIpAddressType.setStatus(_A)
_AdGenFrPVCLearnedPrimaryPeerIpAddress_Type=InetAddress
_AdGenFrPVCLearnedPrimaryPeerIpAddress_Object=MibTableColumn
adGenFrPVCLearnedPrimaryPeerIpAddress=_AdGenFrPVCLearnedPrimaryPeerIpAddress_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,21),_AdGenFrPVCLearnedPrimaryPeerIpAddress_Type())
adGenFrPVCLearnedPrimaryPeerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCLearnedPrimaryPeerIpAddress.setStatus(_A)
_AdGenFrPVCLearnedSecondaryPeerAddressType_Type=InetAddressType
_AdGenFrPVCLearnedSecondaryPeerAddressType_Object=MibTableColumn
adGenFrPVCLearnedSecondaryPeerAddressType=_AdGenFrPVCLearnedSecondaryPeerAddressType_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,22),_AdGenFrPVCLearnedSecondaryPeerAddressType_Type())
adGenFrPVCLearnedSecondaryPeerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCLearnedSecondaryPeerAddressType.setStatus(_A)
_AdGenFrPVCLearnedSecondaryPeerIpAddress_Type=InetAddress
_AdGenFrPVCLearnedSecondaryPeerIpAddress_Object=MibTableColumn
adGenFrPVCLearnedSecondaryPeerIpAddress=_AdGenFrPVCLearnedSecondaryPeerIpAddress_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,23),_AdGenFrPVCLearnedSecondaryPeerIpAddress_Type())
adGenFrPVCLearnedSecondaryPeerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCLearnedSecondaryPeerIpAddress.setStatus(_A)
class _AdGenFrPVCClearCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_S,1))
_AdGenFrPVCClearCounters_Type.__name__=_E
_AdGenFrPVCClearCounters_Object=MibTableColumn
adGenFrPVCClearCounters=_AdGenFrPVCClearCounters_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,24),_AdGenFrPVCClearCounters_Type())
adGenFrPVCClearCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCClearCounters.setStatus(_A)
class _AdGenFrPVCClearPmHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_S,1))
_AdGenFrPVCClearPmHistory_Type.__name__=_E
_AdGenFrPVCClearPmHistory_Object=MibTableColumn
adGenFrPVCClearPmHistory=_AdGenFrPVCClearPmHistory_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,25),_AdGenFrPVCClearPmHistory_Type())
adGenFrPVCClearPmHistory.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCClearPmHistory.setStatus(_A)
class _AdGenFrPVCOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Q,1),(_R,2),(_U,3),('unknown',4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_AdGenFrPVCOperStatus_Type.__name__=_E
_AdGenFrPVCOperStatus_Object=MibTableColumn
adGenFrPVCOperStatus=_AdGenFrPVCOperStatus_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,26),_AdGenFrPVCOperStatus_Type())
adGenFrPVCOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCOperStatus.setStatus(_A)
_AdGenFrPVCLastChange_Type=TimeTicks
_AdGenFrPVCLastChange_Object=MibTableColumn
adGenFrPVCLastChange=_AdGenFrPVCLastChange_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,27),_AdGenFrPVCLastChange_Type())
adGenFrPVCLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCLastChange.setStatus(_A)
_AdGenFrPVCDescription_Type=DisplayString
_AdGenFrPVCDescription_Object=MibTableColumn
adGenFrPVCDescription=_AdGenFrPVCDescription_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,28),_AdGenFrPVCDescription_Type())
adGenFrPVCDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCDescription.setStatus(_A)
class _AdGenFrPVCMtu_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(262,1600))
_AdGenFrPVCMtu_Type.__name__=_E
_AdGenFrPVCMtu_Object=MibTableColumn
adGenFrPVCMtu=_AdGenFrPVCMtu_Object((1,3,6,1,4,1,664,5,70,29,1,3,4,1,29),_AdGenFrPVCMtu_Type())
adGenFrPVCMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenFrPVCMtu.setStatus(_A)
if mibBuilder.loadTexts:adGenFrPVCMtu.setUnits('Octets')
_AdGenFrPVCCurrentTable_Object=MibTable
adGenFrPVCCurrentTable=_AdGenFrPVCCurrentTable_Object((1,3,6,1,4,1,664,5,70,29,1,3,5))
if mibBuilder.loadTexts:adGenFrPVCCurrentTable.setStatus(_A)
_AdGenFrPVCCurrentEntry_Object=MibTableRow
adGenFrPVCCurrentEntry=_AdGenFrPVCCurrentEntry_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1))
adGenFrPVCCurrentEntry.setIndexNames((0,_F,_G),(0,_C,_H))
if mibBuilder.loadTexts:adGenFrPVCCurrentEntry.setStatus(_A)
_AdGenFrPVCCurrentInOctets_Type=Counter32
_AdGenFrPVCCurrentInOctets_Object=MibTableColumn
adGenFrPVCCurrentInOctets=_AdGenFrPVCCurrentInOctets_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,1),_AdGenFrPVCCurrentInOctets_Type())
adGenFrPVCCurrentInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentInOctets.setStatus(_A)
_AdGenFrPVCCurrentInPkts_Type=Counter32
_AdGenFrPVCCurrentInPkts_Object=MibTableColumn
adGenFrPVCCurrentInPkts=_AdGenFrPVCCurrentInPkts_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,2),_AdGenFrPVCCurrentInPkts_Type())
adGenFrPVCCurrentInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentInPkts.setStatus(_A)
_AdGenFrPVCCurrentInDiscards_Type=Counter32
_AdGenFrPVCCurrentInDiscards_Object=MibTableColumn
adGenFrPVCCurrentInDiscards=_AdGenFrPVCCurrentInDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,3),_AdGenFrPVCCurrentInDiscards_Type())
adGenFrPVCCurrentInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentInDiscards.setStatus(_A)
_AdGenFrPVCCurrentOutOctets_Type=Counter32
_AdGenFrPVCCurrentOutOctets_Object=MibTableColumn
adGenFrPVCCurrentOutOctets=_AdGenFrPVCCurrentOutOctets_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,5),_AdGenFrPVCCurrentOutOctets_Type())
adGenFrPVCCurrentOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentOutOctets.setStatus(_A)
_AdGenFrPVCCurrentOutPkts_Type=Counter32
_AdGenFrPVCCurrentOutPkts_Object=MibTableColumn
adGenFrPVCCurrentOutPkts=_AdGenFrPVCCurrentOutPkts_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,6),_AdGenFrPVCCurrentOutPkts_Type())
adGenFrPVCCurrentOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentOutPkts.setStatus(_A)
_AdGenFrPVCCurrentOutDiscards_Type=Counter32
_AdGenFrPVCCurrentOutDiscards_Object=MibTableColumn
adGenFrPVCCurrentOutDiscards=_AdGenFrPVCCurrentOutDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,7),_AdGenFrPVCCurrentOutDiscards_Type())
adGenFrPVCCurrentOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentOutDiscards.setStatus(_A)
_AdGenFrPVCCurrentPktsFECN1In_Type=Counter32
_AdGenFrPVCCurrentPktsFECN1In_Object=MibTableColumn
adGenFrPVCCurrentPktsFECN1In=_AdGenFrPVCCurrentPktsFECN1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,9),_AdGenFrPVCCurrentPktsFECN1In_Type())
adGenFrPVCCurrentPktsFECN1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentPktsFECN1In.setStatus(_A)
_AdGenFrPVCCurrentPktsFECN1Out_Type=Counter32
_AdGenFrPVCCurrentPktsFECN1Out_Object=MibTableColumn
adGenFrPVCCurrentPktsFECN1Out=_AdGenFrPVCCurrentPktsFECN1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,10),_AdGenFrPVCCurrentPktsFECN1Out_Type())
adGenFrPVCCurrentPktsFECN1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentPktsFECN1Out.setStatus(_A)
_AdGenFrPVCCurrentPktsBECN1In_Type=Counter32
_AdGenFrPVCCurrentPktsBECN1In_Object=MibTableColumn
adGenFrPVCCurrentPktsBECN1In=_AdGenFrPVCCurrentPktsBECN1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,11),_AdGenFrPVCCurrentPktsBECN1In_Type())
adGenFrPVCCurrentPktsBECN1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentPktsBECN1In.setStatus(_A)
_AdGenFrPVCCurrentPktsBECN1Out_Type=Counter32
_AdGenFrPVCCurrentPktsBECN1Out_Object=MibTableColumn
adGenFrPVCCurrentPktsBECN1Out=_AdGenFrPVCCurrentPktsBECN1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,12),_AdGenFrPVCCurrentPktsBECN1Out_Type())
adGenFrPVCCurrentPktsBECN1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentPktsBECN1Out.setStatus(_A)
_AdGenFrPVCCurrentPktsDE1In_Type=Counter32
_AdGenFrPVCCurrentPktsDE1In_Object=MibTableColumn
adGenFrPVCCurrentPktsDE1In=_AdGenFrPVCCurrentPktsDE1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,13),_AdGenFrPVCCurrentPktsDE1In_Type())
adGenFrPVCCurrentPktsDE1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentPktsDE1In.setStatus(_A)
_AdGenFrPVCCurrentPktsDE1Out_Type=Counter32
_AdGenFrPVCCurrentPktsDE1Out_Object=MibTableColumn
adGenFrPVCCurrentPktsDE1Out=_AdGenFrPVCCurrentPktsDE1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,14),_AdGenFrPVCCurrentPktsDE1Out_Type())
adGenFrPVCCurrentPktsDE1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentPktsDE1Out.setStatus(_A)
_AdGenFrPVCCurrentOctetsDE1In_Type=Counter32
_AdGenFrPVCCurrentOctetsDE1In_Object=MibTableColumn
adGenFrPVCCurrentOctetsDE1In=_AdGenFrPVCCurrentOctetsDE1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,15),_AdGenFrPVCCurrentOctetsDE1In_Type())
adGenFrPVCCurrentOctetsDE1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentOctetsDE1In.setStatus(_A)
_AdGenFrPVCCurrentOctetsDE1Out_Type=Counter32
_AdGenFrPVCCurrentOctetsDE1Out_Object=MibTableColumn
adGenFrPVCCurrentOctetsDE1Out=_AdGenFrPVCCurrentOctetsDE1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,5,1,16),_AdGenFrPVCCurrentOctetsDE1Out_Type())
adGenFrPVCCurrentOctetsDE1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCCurrentOctetsDE1Out.setStatus(_A)
_AdGenFrPVCIntervalTable_Object=MibTable
adGenFrPVCIntervalTable=_AdGenFrPVCIntervalTable_Object((1,3,6,1,4,1,664,5,70,29,1,3,6))
if mibBuilder.loadTexts:adGenFrPVCIntervalTable.setStatus(_A)
_AdGenFrPVCIntervalEntry_Object=MibTableRow
adGenFrPVCIntervalEntry=_AdGenFrPVCIntervalEntry_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1))
adGenFrPVCIntervalEntry.setIndexNames((0,_F,_G),(0,_C,_H),(0,_C,_h))
if mibBuilder.loadTexts:adGenFrPVCIntervalEntry.setStatus(_A)
class _AdGenFrPVCIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AdGenFrPVCIntervalNumber_Type.__name__=_E
_AdGenFrPVCIntervalNumber_Object=MibTableColumn
adGenFrPVCIntervalNumber=_AdGenFrPVCIntervalNumber_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,1),_AdGenFrPVCIntervalNumber_Type())
adGenFrPVCIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenFrPVCIntervalNumber.setStatus(_A)
_AdGenFrPVCIntervalTimeStamp_Type=DisplayString
_AdGenFrPVCIntervalTimeStamp_Object=MibTableColumn
adGenFrPVCIntervalTimeStamp=_AdGenFrPVCIntervalTimeStamp_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,2),_AdGenFrPVCIntervalTimeStamp_Type())
adGenFrPVCIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalTimeStamp.setStatus(_A)
_AdGenFrPVCIntervalInOctets_Type=Counter32
_AdGenFrPVCIntervalInOctets_Object=MibTableColumn
adGenFrPVCIntervalInOctets=_AdGenFrPVCIntervalInOctets_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,3),_AdGenFrPVCIntervalInOctets_Type())
adGenFrPVCIntervalInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalInOctets.setStatus(_A)
_AdGenFrPVCIntervalInPkts_Type=Counter32
_AdGenFrPVCIntervalInPkts_Object=MibTableColumn
adGenFrPVCIntervalInPkts=_AdGenFrPVCIntervalInPkts_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,4),_AdGenFrPVCIntervalInPkts_Type())
adGenFrPVCIntervalInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalInPkts.setStatus(_A)
_AdGenFrPVCIntervalInDiscards_Type=Counter32
_AdGenFrPVCIntervalInDiscards_Object=MibTableColumn
adGenFrPVCIntervalInDiscards=_AdGenFrPVCIntervalInDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,5),_AdGenFrPVCIntervalInDiscards_Type())
adGenFrPVCIntervalInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalInDiscards.setStatus(_A)
_AdGenFrPVCIntervalOutOctets_Type=Counter32
_AdGenFrPVCIntervalOutOctets_Object=MibTableColumn
adGenFrPVCIntervalOutOctets=_AdGenFrPVCIntervalOutOctets_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,7),_AdGenFrPVCIntervalOutOctets_Type())
adGenFrPVCIntervalOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalOutOctets.setStatus(_A)
_AdGenFrPVCIntervalOutPkts_Type=Counter32
_AdGenFrPVCIntervalOutPkts_Object=MibTableColumn
adGenFrPVCIntervalOutPkts=_AdGenFrPVCIntervalOutPkts_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,8),_AdGenFrPVCIntervalOutPkts_Type())
adGenFrPVCIntervalOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalOutPkts.setStatus(_A)
_AdGenFrPVCIntervalOutDiscards_Type=Counter32
_AdGenFrPVCIntervalOutDiscards_Object=MibTableColumn
adGenFrPVCIntervalOutDiscards=_AdGenFrPVCIntervalOutDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,9),_AdGenFrPVCIntervalOutDiscards_Type())
adGenFrPVCIntervalOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalOutDiscards.setStatus(_A)
_AdGenFrPVCIntervalPktsFECN1In_Type=Counter32
_AdGenFrPVCIntervalPktsFECN1In_Object=MibTableColumn
adGenFrPVCIntervalPktsFECN1In=_AdGenFrPVCIntervalPktsFECN1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,11),_AdGenFrPVCIntervalPktsFECN1In_Type())
adGenFrPVCIntervalPktsFECN1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalPktsFECN1In.setStatus(_A)
_AdGenFrPVCIntervalPktsFECN1Out_Type=Counter32
_AdGenFrPVCIntervalPktsFECN1Out_Object=MibTableColumn
adGenFrPVCIntervalPktsFECN1Out=_AdGenFrPVCIntervalPktsFECN1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,12),_AdGenFrPVCIntervalPktsFECN1Out_Type())
adGenFrPVCIntervalPktsFECN1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalPktsFECN1Out.setStatus(_A)
_AdGenFrPVCIntervalPktsBECN1In_Type=Counter32
_AdGenFrPVCIntervalPktsBECN1In_Object=MibTableColumn
adGenFrPVCIntervalPktsBECN1In=_AdGenFrPVCIntervalPktsBECN1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,13),_AdGenFrPVCIntervalPktsBECN1In_Type())
adGenFrPVCIntervalPktsBECN1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalPktsBECN1In.setStatus(_A)
_AdGenFrPVCIntervalPktsBECN1Out_Type=Counter32
_AdGenFrPVCIntervalPktsBECN1Out_Object=MibTableColumn
adGenFrPVCIntervalPktsBECN1Out=_AdGenFrPVCIntervalPktsBECN1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,14),_AdGenFrPVCIntervalPktsBECN1Out_Type())
adGenFrPVCIntervalPktsBECN1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalPktsBECN1Out.setStatus(_A)
_AdGenFrPVCIntervalPktsDE1In_Type=Counter32
_AdGenFrPVCIntervalPktsDE1In_Object=MibTableColumn
adGenFrPVCIntervalPktsDE1In=_AdGenFrPVCIntervalPktsDE1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,15),_AdGenFrPVCIntervalPktsDE1In_Type())
adGenFrPVCIntervalPktsDE1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalPktsDE1In.setStatus(_A)
_AdGenFrPVCIntervalPktsDE1Out_Type=Counter32
_AdGenFrPVCIntervalPktsDE1Out_Object=MibTableColumn
adGenFrPVCIntervalPktsDE1Out=_AdGenFrPVCIntervalPktsDE1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,16),_AdGenFrPVCIntervalPktsDE1Out_Type())
adGenFrPVCIntervalPktsDE1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalPktsDE1Out.setStatus(_A)
_AdGenFrPVCIntervalOctetsDE1In_Type=Counter32
_AdGenFrPVCIntervalOctetsDE1In_Object=MibTableColumn
adGenFrPVCIntervalOctetsDE1In=_AdGenFrPVCIntervalOctetsDE1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,17),_AdGenFrPVCIntervalOctetsDE1In_Type())
adGenFrPVCIntervalOctetsDE1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalOctetsDE1In.setStatus(_A)
_AdGenFrPVCIntervalOctetsDE1Out_Type=Counter32
_AdGenFrPVCIntervalOctetsDE1Out_Object=MibTableColumn
adGenFrPVCIntervalOctetsDE1Out=_AdGenFrPVCIntervalOctetsDE1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,6,1,18),_AdGenFrPVCIntervalOctetsDE1Out_Type())
adGenFrPVCIntervalOctetsDE1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCIntervalOctetsDE1Out.setStatus(_A)
_AdGenFrPVCDayCurrentTable_Object=MibTable
adGenFrPVCDayCurrentTable=_AdGenFrPVCDayCurrentTable_Object((1,3,6,1,4,1,664,5,70,29,1,3,7))
if mibBuilder.loadTexts:adGenFrPVCDayCurrentTable.setStatus(_A)
_AdGenFrPVCDayCurrentEntry_Object=MibTableRow
adGenFrPVCDayCurrentEntry=_AdGenFrPVCDayCurrentEntry_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1))
adGenFrPVCDayCurrentEntry.setIndexNames((0,_F,_G),(0,_C,_H))
if mibBuilder.loadTexts:adGenFrPVCDayCurrentEntry.setStatus(_A)
_AdGenFrPVCDayCurrentInOctets_Type=Counter32
_AdGenFrPVCDayCurrentInOctets_Object=MibTableColumn
adGenFrPVCDayCurrentInOctets=_AdGenFrPVCDayCurrentInOctets_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,1),_AdGenFrPVCDayCurrentInOctets_Type())
adGenFrPVCDayCurrentInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentInOctets.setStatus(_A)
_AdGenFrPVCDayCurrentInPkts_Type=Counter32
_AdGenFrPVCDayCurrentInPkts_Object=MibTableColumn
adGenFrPVCDayCurrentInPkts=_AdGenFrPVCDayCurrentInPkts_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,2),_AdGenFrPVCDayCurrentInPkts_Type())
adGenFrPVCDayCurrentInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentInPkts.setStatus(_A)
_AdGenFrPVCDayCurrentInDiscards_Type=Counter32
_AdGenFrPVCDayCurrentInDiscards_Object=MibTableColumn
adGenFrPVCDayCurrentInDiscards=_AdGenFrPVCDayCurrentInDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,3),_AdGenFrPVCDayCurrentInDiscards_Type())
adGenFrPVCDayCurrentInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentInDiscards.setStatus(_A)
_AdGenFrPVCDayCurrentOutOctets_Type=Counter32
_AdGenFrPVCDayCurrentOutOctets_Object=MibTableColumn
adGenFrPVCDayCurrentOutOctets=_AdGenFrPVCDayCurrentOutOctets_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,5),_AdGenFrPVCDayCurrentOutOctets_Type())
adGenFrPVCDayCurrentOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentOutOctets.setStatus(_A)
_AdGenFrPVCDayCurrentOutPkts_Type=Counter32
_AdGenFrPVCDayCurrentOutPkts_Object=MibTableColumn
adGenFrPVCDayCurrentOutPkts=_AdGenFrPVCDayCurrentOutPkts_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,6),_AdGenFrPVCDayCurrentOutPkts_Type())
adGenFrPVCDayCurrentOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentOutPkts.setStatus(_A)
_AdGenFrPVCDayCurrentOutDiscards_Type=Counter32
_AdGenFrPVCDayCurrentOutDiscards_Object=MibTableColumn
adGenFrPVCDayCurrentOutDiscards=_AdGenFrPVCDayCurrentOutDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,7),_AdGenFrPVCDayCurrentOutDiscards_Type())
adGenFrPVCDayCurrentOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentOutDiscards.setStatus(_A)
_AdGenFrPVCDayCurrentPktsFECN1In_Type=Counter32
_AdGenFrPVCDayCurrentPktsFECN1In_Object=MibTableColumn
adGenFrPVCDayCurrentPktsFECN1In=_AdGenFrPVCDayCurrentPktsFECN1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,9),_AdGenFrPVCDayCurrentPktsFECN1In_Type())
adGenFrPVCDayCurrentPktsFECN1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentPktsFECN1In.setStatus(_A)
_AdGenFrPVCDayCurrentPktsFECN1Out_Type=Counter32
_AdGenFrPVCDayCurrentPktsFECN1Out_Object=MibTableColumn
adGenFrPVCDayCurrentPktsFECN1Out=_AdGenFrPVCDayCurrentPktsFECN1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,10),_AdGenFrPVCDayCurrentPktsFECN1Out_Type())
adGenFrPVCDayCurrentPktsFECN1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentPktsFECN1Out.setStatus(_A)
_AdGenFrPVCDayCurrentPktsBECN1In_Type=Counter32
_AdGenFrPVCDayCurrentPktsBECN1In_Object=MibTableColumn
adGenFrPVCDayCurrentPktsBECN1In=_AdGenFrPVCDayCurrentPktsBECN1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,11),_AdGenFrPVCDayCurrentPktsBECN1In_Type())
adGenFrPVCDayCurrentPktsBECN1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentPktsBECN1In.setStatus(_A)
_AdGenFrPVCDayCurrentPktsBECN1Out_Type=Counter32
_AdGenFrPVCDayCurrentPktsBECN1Out_Object=MibTableColumn
adGenFrPVCDayCurrentPktsBECN1Out=_AdGenFrPVCDayCurrentPktsBECN1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,12),_AdGenFrPVCDayCurrentPktsBECN1Out_Type())
adGenFrPVCDayCurrentPktsBECN1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentPktsBECN1Out.setStatus(_A)
_AdGenFrPVCDayCurrentPktsDE1In_Type=Counter32
_AdGenFrPVCDayCurrentPktsDE1In_Object=MibTableColumn
adGenFrPVCDayCurrentPktsDE1In=_AdGenFrPVCDayCurrentPktsDE1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,13),_AdGenFrPVCDayCurrentPktsDE1In_Type())
adGenFrPVCDayCurrentPktsDE1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentPktsDE1In.setStatus(_A)
_AdGenFrPVCDayCurrentPktsDE1Out_Type=Counter32
_AdGenFrPVCDayCurrentPktsDE1Out_Object=MibTableColumn
adGenFrPVCDayCurrentPktsDE1Out=_AdGenFrPVCDayCurrentPktsDE1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,14),_AdGenFrPVCDayCurrentPktsDE1Out_Type())
adGenFrPVCDayCurrentPktsDE1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentPktsDE1Out.setStatus(_A)
_AdGenFrPVCDayCurrentOctetsDE1In_Type=Counter32
_AdGenFrPVCDayCurrentOctetsDE1In_Object=MibTableColumn
adGenFrPVCDayCurrentOctetsDE1In=_AdGenFrPVCDayCurrentOctetsDE1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,15),_AdGenFrPVCDayCurrentOctetsDE1In_Type())
adGenFrPVCDayCurrentOctetsDE1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentOctetsDE1In.setStatus(_A)
_AdGenFrPVCDayCurrentOctetsDE1Out_Type=Counter32
_AdGenFrPVCDayCurrentOctetsDE1Out_Object=MibTableColumn
adGenFrPVCDayCurrentOctetsDE1Out=_AdGenFrPVCDayCurrentOctetsDE1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,7,1,16),_AdGenFrPVCDayCurrentOctetsDE1Out_Type())
adGenFrPVCDayCurrentOctetsDE1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayCurrentOctetsDE1Out.setStatus(_A)
_AdGenFrPVCDayIntervalTable_Object=MibTable
adGenFrPVCDayIntervalTable=_AdGenFrPVCDayIntervalTable_Object((1,3,6,1,4,1,664,5,70,29,1,3,8))
if mibBuilder.loadTexts:adGenFrPVCDayIntervalTable.setStatus(_A)
_AdGenFrPVCDayIntervalEntry_Object=MibTableRow
adGenFrPVCDayIntervalEntry=_AdGenFrPVCDayIntervalEntry_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1))
adGenFrPVCDayIntervalEntry.setIndexNames((0,_F,_G),(0,_C,_H),(0,_C,_i))
if mibBuilder.loadTexts:adGenFrPVCDayIntervalEntry.setStatus(_A)
class _AdGenFrPVCDayIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AdGenFrPVCDayIntervalNumber_Type.__name__=_E
_AdGenFrPVCDayIntervalNumber_Object=MibTableColumn
adGenFrPVCDayIntervalNumber=_AdGenFrPVCDayIntervalNumber_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,1),_AdGenFrPVCDayIntervalNumber_Type())
adGenFrPVCDayIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalNumber.setStatus(_A)
_AdGenFrPVCDayIntervalTimeStamp_Type=DisplayString
_AdGenFrPVCDayIntervalTimeStamp_Object=MibTableColumn
adGenFrPVCDayIntervalTimeStamp=_AdGenFrPVCDayIntervalTimeStamp_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,2),_AdGenFrPVCDayIntervalTimeStamp_Type())
adGenFrPVCDayIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalTimeStamp.setStatus(_A)
_AdGenFrPVCDayIntervalInOctets_Type=Counter32
_AdGenFrPVCDayIntervalInOctets_Object=MibTableColumn
adGenFrPVCDayIntervalInOctets=_AdGenFrPVCDayIntervalInOctets_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,3),_AdGenFrPVCDayIntervalInOctets_Type())
adGenFrPVCDayIntervalInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalInOctets.setStatus(_A)
_AdGenFrPVCDayIntervalInPkts_Type=Counter32
_AdGenFrPVCDayIntervalInPkts_Object=MibTableColumn
adGenFrPVCDayIntervalInPkts=_AdGenFrPVCDayIntervalInPkts_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,4),_AdGenFrPVCDayIntervalInPkts_Type())
adGenFrPVCDayIntervalInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalInPkts.setStatus(_A)
_AdGenFrPVCDayIntervalInDiscards_Type=Counter32
_AdGenFrPVCDayIntervalInDiscards_Object=MibTableColumn
adGenFrPVCDayIntervalInDiscards=_AdGenFrPVCDayIntervalInDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,5),_AdGenFrPVCDayIntervalInDiscards_Type())
adGenFrPVCDayIntervalInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalInDiscards.setStatus(_A)
_AdGenFrPVCDayIntervalOutOctets_Type=Counter32
_AdGenFrPVCDayIntervalOutOctets_Object=MibTableColumn
adGenFrPVCDayIntervalOutOctets=_AdGenFrPVCDayIntervalOutOctets_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,7),_AdGenFrPVCDayIntervalOutOctets_Type())
adGenFrPVCDayIntervalOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalOutOctets.setStatus(_A)
_AdGenFrPVCDayIntervalOutPkts_Type=Counter32
_AdGenFrPVCDayIntervalOutPkts_Object=MibTableColumn
adGenFrPVCDayIntervalOutPkts=_AdGenFrPVCDayIntervalOutPkts_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,8),_AdGenFrPVCDayIntervalOutPkts_Type())
adGenFrPVCDayIntervalOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalOutPkts.setStatus(_A)
_AdGenFrPVCDayIntervalOutDiscards_Type=Counter32
_AdGenFrPVCDayIntervalOutDiscards_Object=MibTableColumn
adGenFrPVCDayIntervalOutDiscards=_AdGenFrPVCDayIntervalOutDiscards_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,9),_AdGenFrPVCDayIntervalOutDiscards_Type())
adGenFrPVCDayIntervalOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalOutDiscards.setStatus(_A)
_AdGenFrPVCDayIntervalPktsFECN1In_Type=Counter32
_AdGenFrPVCDayIntervalPktsFECN1In_Object=MibTableColumn
adGenFrPVCDayIntervalPktsFECN1In=_AdGenFrPVCDayIntervalPktsFECN1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,11),_AdGenFrPVCDayIntervalPktsFECN1In_Type())
adGenFrPVCDayIntervalPktsFECN1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalPktsFECN1In.setStatus(_A)
_AdGenFrPVCDayIntervalPktsFECN1Out_Type=Counter32
_AdGenFrPVCDayIntervalPktsFECN1Out_Object=MibTableColumn
adGenFrPVCDayIntervalPktsFECN1Out=_AdGenFrPVCDayIntervalPktsFECN1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,12),_AdGenFrPVCDayIntervalPktsFECN1Out_Type())
adGenFrPVCDayIntervalPktsFECN1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalPktsFECN1Out.setStatus(_A)
_AdGenFrPVCDayIntervalPktsBECN1In_Type=Counter32
_AdGenFrPVCDayIntervalPktsBECN1In_Object=MibTableColumn
adGenFrPVCDayIntervalPktsBECN1In=_AdGenFrPVCDayIntervalPktsBECN1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,13),_AdGenFrPVCDayIntervalPktsBECN1In_Type())
adGenFrPVCDayIntervalPktsBECN1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalPktsBECN1In.setStatus(_A)
_AdGenFrPVCDayIntervalPktsBECN1Out_Type=Counter32
_AdGenFrPVCDayIntervalPktsBECN1Out_Object=MibTableColumn
adGenFrPVCDayIntervalPktsBECN1Out=_AdGenFrPVCDayIntervalPktsBECN1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,14),_AdGenFrPVCDayIntervalPktsBECN1Out_Type())
adGenFrPVCDayIntervalPktsBECN1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalPktsBECN1Out.setStatus(_A)
_AdGenFrPVCDayIntervalPktsDE1In_Type=Counter32
_AdGenFrPVCDayIntervalPktsDE1In_Object=MibTableColumn
adGenFrPVCDayIntervalPktsDE1In=_AdGenFrPVCDayIntervalPktsDE1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,15),_AdGenFrPVCDayIntervalPktsDE1In_Type())
adGenFrPVCDayIntervalPktsDE1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalPktsDE1In.setStatus(_A)
_AdGenFrPVCDayIntervalPktsDE1Out_Type=Counter32
_AdGenFrPVCDayIntervalPktsDE1Out_Object=MibTableColumn
adGenFrPVCDayIntervalPktsDE1Out=_AdGenFrPVCDayIntervalPktsDE1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,16),_AdGenFrPVCDayIntervalPktsDE1Out_Type())
adGenFrPVCDayIntervalPktsDE1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalPktsDE1Out.setStatus(_A)
_AdGenFrPVCDayIntervalOctetsDE1In_Type=Counter32
_AdGenFrPVCDayIntervalOctetsDE1In_Object=MibTableColumn
adGenFrPVCDayIntervalOctetsDE1In=_AdGenFrPVCDayIntervalOctetsDE1In_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,17),_AdGenFrPVCDayIntervalOctetsDE1In_Type())
adGenFrPVCDayIntervalOctetsDE1In.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalOctetsDE1In.setStatus(_A)
_AdGenFrPVCDayIntervalOctetsDE1Out_Type=Counter32
_AdGenFrPVCDayIntervalOctetsDE1Out_Object=MibTableColumn
adGenFrPVCDayIntervalOctetsDE1Out=_AdGenFrPVCDayIntervalOctetsDE1Out_Object((1,3,6,1,4,1,664,5,70,29,1,3,8,1,18),_AdGenFrPVCDayIntervalOctetsDE1Out_Type())
adGenFrPVCDayIntervalOctetsDE1Out.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrPVCDayIntervalOctetsDE1Out.setStatus(_A)
_AdGenFrSlot_ObjectIdentity=ObjectIdentity
adGenFrSlot=_AdGenFrSlot_ObjectIdentity((1,3,6,1,4,1,664,5,70,29,1,4))
_AdGenFrSlotTable_Object=MibTable
adGenFrSlotTable=_AdGenFrSlotTable_Object((1,3,6,1,4,1,664,5,70,29,1,4,1))
if mibBuilder.loadTexts:adGenFrSlotTable.setStatus(_A)
_AdGenFrSlotEntry_Object=MibTableRow
adGenFrSlotEntry=_AdGenFrSlotEntry_Object((1,3,6,1,4,1,664,5,70,29,1,4,1,1))
adGenFrSlotEntry.setIndexNames((0,_Y,_Z))
if mibBuilder.loadTexts:adGenFrSlotEntry.setStatus(_A)
_AdGenFrSlotGroupLastCreateError_Type=DisplayString
_AdGenFrSlotGroupLastCreateError_Object=MibTableColumn
adGenFrSlotGroupLastCreateError=_AdGenFrSlotGroupLastCreateError_Object((1,3,6,1,4,1,664,5,70,29,1,4,1,1,1),_AdGenFrSlotGroupLastCreateError_Type())
adGenFrSlotGroupLastCreateError.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrSlotGroupLastCreateError.setStatus(_A)
_AdGenFrSlotPVCMaxNumber_Type=Unsigned32
_AdGenFrSlotPVCMaxNumber_Object=MibTableColumn
adGenFrSlotPVCMaxNumber=_AdGenFrSlotPVCMaxNumber_Object((1,3,6,1,4,1,664,5,70,29,1,4,1,1,2),_AdGenFrSlotPVCMaxNumber_Type())
adGenFrSlotPVCMaxNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrSlotPVCMaxNumber.setStatus(_A)
_AdGenFrSlotPVCCurrentNumber_Type=Unsigned32
_AdGenFrSlotPVCCurrentNumber_Object=MibTableColumn
adGenFrSlotPVCCurrentNumber=_AdGenFrSlotPVCCurrentNumber_Object((1,3,6,1,4,1,664,5,70,29,1,4,1,1,3),_AdGenFrSlotPVCCurrentNumber_Type())
adGenFrSlotPVCCurrentNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenFrSlotPVCCurrentNumber.setStatus(_A)
_AdGenFrAlarmsPrefix_ObjectIdentity=ObjectIdentity
adGenFrAlarmsPrefix=_AdGenFrAlarmsPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,70,29,2))
_AdGenFrAlarms_ObjectIdentity=ObjectIdentity
adGenFrAlarms=_AdGenFrAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,70,29,2,0))
adGenFrGroupDownAlarmClr=NotificationType((1,3,6,1,4,1,664,5,70,29,2,0,1))
adGenFrGroupDownAlarmClr.setObjects(*((_J,_K),(_N,_O),(_F,_G),(_F,_T),(_L,_M),(_C,_V)))
if mibBuilder.loadTexts:adGenFrGroupDownAlarmClr.setStatus(_A)
adGenFrGroupDownAlarmAct=NotificationType((1,3,6,1,4,1,664,5,70,29,2,0,2))
adGenFrGroupDownAlarmAct.setObjects(*((_J,_K),(_N,_O),(_F,_G),(_F,_T),(_L,_M),(_C,_V)))
if mibBuilder.loadTexts:adGenFrGroupDownAlarmAct.setStatus(_A)
adGenFrDlciDownAlarmClr=NotificationType((1,3,6,1,4,1,664,5,70,29,2,0,3))
adGenFrDlciDownAlarmClr.setObjects(*((_J,_K),(_N,_O),(_C,_W),(_C,_H),(_L,_M),(_C,_X)))
if mibBuilder.loadTexts:adGenFrDlciDownAlarmClr.setStatus(_A)
adGenFrDlciDownAlarmAct=NotificationType((1,3,6,1,4,1,664,5,70,29,2,0,4))
adGenFrDlciDownAlarmAct.setObjects(*((_J,_K),(_N,_O),(_C,_W),(_C,_H),(_L,_M),(_C,_X)))
if mibBuilder.loadTexts:adGenFrDlciDownAlarmAct.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'adGenFrameRelayMIBObjects':adGenFrameRelayMIBObjects,'adGenFrGroup':adGenFrGroup,'adGenFrGroupTable':adGenFrGroupTable,'adGenFrGroupEntry':adGenFrGroupEntry,'adGenFrGroupRowStatus':adGenFrGroupRowStatus,'adGenFrGroupStatusString':adGenFrGroupStatusString,'adGenFrGroupAdminStatus':adGenFrGroupAdminStatus,'adGenFrGroupLmiType':adGenFrGroupLmiType,_V:adGenFrGroupLmiStatus,'adGenFrGroupLmiEnquiryIn':adGenFrGroupLmiEnquiryIn,'adGenFrGroupLmiEnquiryOut':adGenFrGroupLmiEnquiryOut,'adGenFrGroupLmiStatusIn':adGenFrGroupLmiStatusIn,'adGenFrGroupLmiStatusOut':adGenFrGroupLmiStatusOut,'adGenFrGroupLmiInvalidIn':adGenFrGroupLmiInvalidIn,'adGenFrGroupLmiStatusEnqTimeouts':adGenFrGroupLmiStatusEnqTimeouts,'adGenFrGroupLmiStatusTimeouts':adGenFrGroupLmiStatusTimeouts,'adGenFrGroupClearCounters':adGenFrGroupClearCounters,'adGenFrGroupClearPmHistory':adGenFrGroupClearPmHistory,'adGenFrGroupLinkLastCreateError':adGenFrGroupLinkLastCreateError,'adGenFrGroupPvcLastCreateError':adGenFrGroupPvcLastCreateError,'adGenFrGroupCurrentTable':adGenFrGroupCurrentTable,'adGenFrGroupCurrentEntry':adGenFrGroupCurrentEntry,'adGenFrGroupCurrentInOctets':adGenFrGroupCurrentInOctets,'adGenFrGroupCurrentInPkts':adGenFrGroupCurrentInPkts,'adGenFrGroupCurrentInDiscards':adGenFrGroupCurrentInDiscards,'adGenFrGroupCurrentInErrors':adGenFrGroupCurrentInErrors,'adGenFrGroupCurrentOutOctets':adGenFrGroupCurrentOutOctets,'adGenFrGroupCurrentOutPkts':adGenFrGroupCurrentOutPkts,'adGenFrGroupCurrentOutDiscards':adGenFrGroupCurrentOutDiscards,'adGenFrGroupCurrentOutErrors':adGenFrGroupCurrentOutErrors,'adGenFrGroupCurrentLmiEnquiryIn':adGenFrGroupCurrentLmiEnquiryIn,'adGenFrGroupCurrentLmiEnquiryOut':adGenFrGroupCurrentLmiEnquiryOut,'adGenFrGroupCurrentLmiStatusIn':adGenFrGroupCurrentLmiStatusIn,'adGenFrGroupCurrentLmiStatusOut':adGenFrGroupCurrentLmiStatusOut,'adGenFrGroupCurrentLmiInvalidIn':adGenFrGroupCurrentLmiInvalidIn,'adGenFrGroupCurrentLmiStatusEnqTimeouts':adGenFrGroupCurrentLmiStatusEnqTimeouts,'adGenFrGroupCurrentLmiStatusTimeouts':adGenFrGroupCurrentLmiStatusTimeouts,'adGenFrGroupCurrentNetworkInactive':adGenFrGroupCurrentNetworkInactive,'adGenFrGroupIntervalTable':adGenFrGroupIntervalTable,'adGenFrGroupIntervalEntry':adGenFrGroupIntervalEntry,_c:adGenFrGroupIntervalNumber,'adGenFrGroupIntervalTimeStamp':adGenFrGroupIntervalTimeStamp,'adGenFrGroupIntervalInOctets':adGenFrGroupIntervalInOctets,'adGenFrGroupIntervalInPkts':adGenFrGroupIntervalInPkts,'adGenFrGroupIntervalInDiscards':adGenFrGroupIntervalInDiscards,'adGenFrGroupIntervalInErrors':adGenFrGroupIntervalInErrors,'adGenFrGroupIntervalOutOctets':adGenFrGroupIntervalOutOctets,'adGenFrGroupIntervalOutPkts':adGenFrGroupIntervalOutPkts,'adGenFrGroupIntervalOutDiscards':adGenFrGroupIntervalOutDiscards,'adGenFrGroupIntervalOutErrors':adGenFrGroupIntervalOutErrors,'adGenFrGroupIntervalLmiEnquiryIn':adGenFrGroupIntervalLmiEnquiryIn,'adGenFrGroupIntervalLmiEnquiryOut':adGenFrGroupIntervalLmiEnquiryOut,'adGenFrGroupIntervalLmiStatusIn':adGenFrGroupIntervalLmiStatusIn,'adGenFrGroupIntervalLmiStatusOut':adGenFrGroupIntervalLmiStatusOut,'adGenFrGroupIntervalLmiInvalidIn':adGenFrGroupIntervalLmiInvalidIn,'adGenFrGroupIntervalLmiStatusEnqTimeouts':adGenFrGroupIntervalLmiStatusEnqTimeouts,'adGenFrGroupIntervalLmiStatusTimeouts':adGenFrGroupIntervalLmiStatusTimeouts,'adGenFrGroupIntervalNetworkInactive':adGenFrGroupIntervalNetworkInactive,'adGenFrGroupDayCurrentTable':adGenFrGroupDayCurrentTable,'adGenFrGroupDayCurrentEntry':adGenFrGroupDayCurrentEntry,'adGenFrGroupDayCurrentInOctets':adGenFrGroupDayCurrentInOctets,'adGenFrGroupDayCurrentInPkts':adGenFrGroupDayCurrentInPkts,'adGenFrGroupDayCurrentInDiscards':adGenFrGroupDayCurrentInDiscards,'adGenFrGroupDayCurrentInErrors':adGenFrGroupDayCurrentInErrors,'adGenFrGroupDayCurrentOutOctets':adGenFrGroupDayCurrentOutOctets,'adGenFrGroupDayCurrentOutPkts':adGenFrGroupDayCurrentOutPkts,'adGenFrGroupDayCurrentOutDiscards':adGenFrGroupDayCurrentOutDiscards,'adGenFrGroupDayCurrentOutErrors':adGenFrGroupDayCurrentOutErrors,'adGenFrGroupDayCurrentLmiEnquiryIn':adGenFrGroupDayCurrentLmiEnquiryIn,'adGenFrGroupDayCurrentLmiEnquiryOut':adGenFrGroupDayCurrentLmiEnquiryOut,'adGenFrGroupDayCurrentLmiStatusIn':adGenFrGroupDayCurrentLmiStatusIn,'adGenFrGroupDayCurrentLmiStatusOut':adGenFrGroupDayCurrentLmiStatusOut,'adGenFrGroupDayCurrentLmiInvalidIn':adGenFrGroupDayCurrentLmiInvalidIn,'adGenFrGroupDayCurrentLmiStatusEnqTimeouts':adGenFrGroupDayCurrentLmiStatusEnqTimeouts,'adGenFrGroupDayCurrentLmiStatusTimeouts':adGenFrGroupDayCurrentLmiStatusTimeouts,'adGenFrGroupDayCurrentNetworkInactive':adGenFrGroupDayCurrentNetworkInactive,'adGenFrGroupDayIntervalTable':adGenFrGroupDayIntervalTable,'adGenFrGroupDayIntervalEntry':adGenFrGroupDayIntervalEntry,_d:adGenFrGroupDayIntervalNumber,'adGenFrGroupDayIntervalTimeStamp':adGenFrGroupDayIntervalTimeStamp,'adGenFrGroupDayIntervalInOctets':adGenFrGroupDayIntervalInOctets,'adGenFrGroupDayIntervalInPkts':adGenFrGroupDayIntervalInPkts,'adGenFrGroupDayIntervalInDiscards':adGenFrGroupDayIntervalInDiscards,'adGenFrGroupDayIntervalInErrors':adGenFrGroupDayIntervalInErrors,'adGenFrGroupDayIntervalOutOctets':adGenFrGroupDayIntervalOutOctets,'adGenFrGroupDayIntervalOutPkts':adGenFrGroupDayIntervalOutPkts,'adGenFrGroupDayIntervalOutDiscards':adGenFrGroupDayIntervalOutDiscards,'adGenFrGroupDayIntervalOutErrors':adGenFrGroupDayIntervalOutErrors,'adGenFrGroupDayIntervalLmiEnquiryIn':adGenFrGroupDayIntervalLmiEnquiryIn,'adGenFrGroupDayIntervalLmiEnquiryOut':adGenFrGroupDayIntervalLmiEnquiryOut,'adGenFrGroupDayIntervalLmiStatusIn':adGenFrGroupDayIntervalLmiStatusIn,'adGenFrGroupDayIntervalLmiStatusOut':adGenFrGroupDayIntervalLmiStatusOut,'adGenFrGroupDayIntervalLmiInvalidIn':adGenFrGroupDayIntervalLmiInvalidIn,'adGenFrGroupDayIntervalLmiStatusEnqTimeouts':adGenFrGroupDayIntervalLmiStatusEnqTimeouts,'adGenFrGroupDayIntervalLmiStatusTimeouts':adGenFrGroupDayIntervalLmiStatusTimeouts,'adGenFrGroupDayIntervalNetworkInactive':adGenFrGroupDayIntervalNetworkInactive,'adGenFrLink':adGenFrLink,'adGenFrLinkTable':adGenFrLinkTable,'adGenFrLinkEntry':adGenFrLinkEntry,_e:adGenFrLinkGroupIfIndex,_f:adGenFrLinkIfIndex,_g:adGenFrLinkBundleId,'adGenFrLinkRowStatus':adGenFrLinkRowStatus,'adGenFrLinkTimeslots':adGenFrLinkTimeslots,'adGenFrLinkStatusString':adGenFrLinkStatusString,'adGenFrPVC':adGenFrPVC,'adGenFrPVCTable':adGenFrPVCTable,'adGenFrPVCEntry':adGenFrPVCEntry,_W:adGenFrPVCIfIndex,_H:adGenFrPVCDLCIIndex,'adGenFrPVCStatusString':adGenFrPVCStatusString,'adGenFrPVCAdminStatus':adGenFrPVCAdminStatus,_X:adGenFrPVCState,'adGenFrPVCEncapsulation':adGenFrPVCEncapsulation,'adGenFrPVCPrimaryPeerIpAddressType':adGenFrPVCPrimaryPeerIpAddressType,'adGenFrPVCPrimaryPeerIpAddress':adGenFrPVCPrimaryPeerIpAddress,'adGenFrPVCSecondaryPeerAddressType':adGenFrPVCSecondaryPeerAddressType,'adGenFrPVCSecondaryPeerIpAddress':adGenFrPVCSecondaryPeerIpAddress,'adGenFrPVCPrimaryGatewayAddressType':adGenFrPVCPrimaryGatewayAddressType,'adGenFrPVCPrimaryGatewayAddress':adGenFrPVCPrimaryGatewayAddress,'adGenFrPVCInverseArpEnable':adGenFrPVCInverseArpEnable,'adGenFrPVCLearnedPrimaryPeerIpAddressType':adGenFrPVCLearnedPrimaryPeerIpAddressType,'adGenFrPVCLearnedPrimaryPeerIpAddress':adGenFrPVCLearnedPrimaryPeerIpAddress,'adGenFrPVCLearnedSecondaryPeerAddressType':adGenFrPVCLearnedSecondaryPeerAddressType,'adGenFrPVCLearnedSecondaryPeerIpAddress':adGenFrPVCLearnedSecondaryPeerIpAddress,'adGenFrPVCClearCounters':adGenFrPVCClearCounters,'adGenFrPVCClearPmHistory':adGenFrPVCClearPmHistory,'adGenFrPVCOperStatus':adGenFrPVCOperStatus,'adGenFrPVCLastChange':adGenFrPVCLastChange,'adGenFrPVCDescription':adGenFrPVCDescription,'adGenFrPVCMtu':adGenFrPVCMtu,'adGenFrPVCCurrentTable':adGenFrPVCCurrentTable,'adGenFrPVCCurrentEntry':adGenFrPVCCurrentEntry,'adGenFrPVCCurrentInOctets':adGenFrPVCCurrentInOctets,'adGenFrPVCCurrentInPkts':adGenFrPVCCurrentInPkts,'adGenFrPVCCurrentInDiscards':adGenFrPVCCurrentInDiscards,'adGenFrPVCCurrentOutOctets':adGenFrPVCCurrentOutOctets,'adGenFrPVCCurrentOutPkts':adGenFrPVCCurrentOutPkts,'adGenFrPVCCurrentOutDiscards':adGenFrPVCCurrentOutDiscards,'adGenFrPVCCurrentPktsFECN1In':adGenFrPVCCurrentPktsFECN1In,'adGenFrPVCCurrentPktsFECN1Out':adGenFrPVCCurrentPktsFECN1Out,'adGenFrPVCCurrentPktsBECN1In':adGenFrPVCCurrentPktsBECN1In,'adGenFrPVCCurrentPktsBECN1Out':adGenFrPVCCurrentPktsBECN1Out,'adGenFrPVCCurrentPktsDE1In':adGenFrPVCCurrentPktsDE1In,'adGenFrPVCCurrentPktsDE1Out':adGenFrPVCCurrentPktsDE1Out,'adGenFrPVCCurrentOctetsDE1In':adGenFrPVCCurrentOctetsDE1In,'adGenFrPVCCurrentOctetsDE1Out':adGenFrPVCCurrentOctetsDE1Out,'adGenFrPVCIntervalTable':adGenFrPVCIntervalTable,'adGenFrPVCIntervalEntry':adGenFrPVCIntervalEntry,_h:adGenFrPVCIntervalNumber,'adGenFrPVCIntervalTimeStamp':adGenFrPVCIntervalTimeStamp,'adGenFrPVCIntervalInOctets':adGenFrPVCIntervalInOctets,'adGenFrPVCIntervalInPkts':adGenFrPVCIntervalInPkts,'adGenFrPVCIntervalInDiscards':adGenFrPVCIntervalInDiscards,'adGenFrPVCIntervalOutOctets':adGenFrPVCIntervalOutOctets,'adGenFrPVCIntervalOutPkts':adGenFrPVCIntervalOutPkts,'adGenFrPVCIntervalOutDiscards':adGenFrPVCIntervalOutDiscards,'adGenFrPVCIntervalPktsFECN1In':adGenFrPVCIntervalPktsFECN1In,'adGenFrPVCIntervalPktsFECN1Out':adGenFrPVCIntervalPktsFECN1Out,'adGenFrPVCIntervalPktsBECN1In':adGenFrPVCIntervalPktsBECN1In,'adGenFrPVCIntervalPktsBECN1Out':adGenFrPVCIntervalPktsBECN1Out,'adGenFrPVCIntervalPktsDE1In':adGenFrPVCIntervalPktsDE1In,'adGenFrPVCIntervalPktsDE1Out':adGenFrPVCIntervalPktsDE1Out,'adGenFrPVCIntervalOctetsDE1In':adGenFrPVCIntervalOctetsDE1In,'adGenFrPVCIntervalOctetsDE1Out':adGenFrPVCIntervalOctetsDE1Out,'adGenFrPVCDayCurrentTable':adGenFrPVCDayCurrentTable,'adGenFrPVCDayCurrentEntry':adGenFrPVCDayCurrentEntry,'adGenFrPVCDayCurrentInOctets':adGenFrPVCDayCurrentInOctets,'adGenFrPVCDayCurrentInPkts':adGenFrPVCDayCurrentInPkts,'adGenFrPVCDayCurrentInDiscards':adGenFrPVCDayCurrentInDiscards,'adGenFrPVCDayCurrentOutOctets':adGenFrPVCDayCurrentOutOctets,'adGenFrPVCDayCurrentOutPkts':adGenFrPVCDayCurrentOutPkts,'adGenFrPVCDayCurrentOutDiscards':adGenFrPVCDayCurrentOutDiscards,'adGenFrPVCDayCurrentPktsFECN1In':adGenFrPVCDayCurrentPktsFECN1In,'adGenFrPVCDayCurrentPktsFECN1Out':adGenFrPVCDayCurrentPktsFECN1Out,'adGenFrPVCDayCurrentPktsBECN1In':adGenFrPVCDayCurrentPktsBECN1In,'adGenFrPVCDayCurrentPktsBECN1Out':adGenFrPVCDayCurrentPktsBECN1Out,'adGenFrPVCDayCurrentPktsDE1In':adGenFrPVCDayCurrentPktsDE1In,'adGenFrPVCDayCurrentPktsDE1Out':adGenFrPVCDayCurrentPktsDE1Out,'adGenFrPVCDayCurrentOctetsDE1In':adGenFrPVCDayCurrentOctetsDE1In,'adGenFrPVCDayCurrentOctetsDE1Out':adGenFrPVCDayCurrentOctetsDE1Out,'adGenFrPVCDayIntervalTable':adGenFrPVCDayIntervalTable,'adGenFrPVCDayIntervalEntry':adGenFrPVCDayIntervalEntry,_i:adGenFrPVCDayIntervalNumber,'adGenFrPVCDayIntervalTimeStamp':adGenFrPVCDayIntervalTimeStamp,'adGenFrPVCDayIntervalInOctets':adGenFrPVCDayIntervalInOctets,'adGenFrPVCDayIntervalInPkts':adGenFrPVCDayIntervalInPkts,'adGenFrPVCDayIntervalInDiscards':adGenFrPVCDayIntervalInDiscards,'adGenFrPVCDayIntervalOutOctets':adGenFrPVCDayIntervalOutOctets,'adGenFrPVCDayIntervalOutPkts':adGenFrPVCDayIntervalOutPkts,'adGenFrPVCDayIntervalOutDiscards':adGenFrPVCDayIntervalOutDiscards,'adGenFrPVCDayIntervalPktsFECN1In':adGenFrPVCDayIntervalPktsFECN1In,'adGenFrPVCDayIntervalPktsFECN1Out':adGenFrPVCDayIntervalPktsFECN1Out,'adGenFrPVCDayIntervalPktsBECN1In':adGenFrPVCDayIntervalPktsBECN1In,'adGenFrPVCDayIntervalPktsBECN1Out':adGenFrPVCDayIntervalPktsBECN1Out,'adGenFrPVCDayIntervalPktsDE1In':adGenFrPVCDayIntervalPktsDE1In,'adGenFrPVCDayIntervalPktsDE1Out':adGenFrPVCDayIntervalPktsDE1Out,'adGenFrPVCDayIntervalOctetsDE1In':adGenFrPVCDayIntervalOctetsDE1In,'adGenFrPVCDayIntervalOctetsDE1Out':adGenFrPVCDayIntervalOctetsDE1Out,'adGenFrSlot':adGenFrSlot,'adGenFrSlotTable':adGenFrSlotTable,'adGenFrSlotEntry':adGenFrSlotEntry,'adGenFrSlotGroupLastCreateError':adGenFrSlotGroupLastCreateError,'adGenFrSlotPVCMaxNumber':adGenFrSlotPVCMaxNumber,'adGenFrSlotPVCCurrentNumber':adGenFrSlotPVCCurrentNumber,'adGenFrAlarmsPrefix':adGenFrAlarmsPrefix,'adGenFrAlarms':adGenFrAlarms,'adGenFrGroupDownAlarmClr':adGenFrGroupDownAlarmClr,'adGenFrGroupDownAlarmAct':adGenFrGroupDownAlarmAct,'adGenFrDlciDownAlarmClr':adGenFrDlciDownAlarmClr,'adGenFrDlciDownAlarmAct':adGenFrDlciDownAlarmAct,'adGenFrameRelayMib':adGenFrameRelayMib})