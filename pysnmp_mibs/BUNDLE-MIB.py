_m='nnlinkUpTrap'
_l='nnlinkDownTrap'
_k='nnbundleUpTrap'
_j='nnbundleDownTrap'
_i='nnlinkDownCause'
_h='nnbundleDownCause'
_g='l1-failures'
_f='admin-down'
_e='admin-delete'
_d='nnloopbackIfId'
_c='nntrackIntfId'
_b='nnbundleLinkT1Num'
_a='nnlinkDescrInfo'
_Z='nnlinkNameInfo'
_Y='nnlinkContactInfo'
_X='nnlinkCircuitId'
_W='nnlinkBundleName'
_V='nnlinkCt3Num'
_U='nnlinkType'
_T='nnlinkNum'
_S='nnbundleDescrInfo'
_R='nnbundleContactInfo'
_Q='nnbundleNameStr'
_P='down'
_O='OctetString'
_N='disable'
_M='enable'
_L='not-accessible'
_K='nnbundleId'
_J='TruthValue'
_I='read-write'
_H='read-only'
_G='seconds'
_F='accessible-for-notify'
_E='DisplayString'
_D='Integer32'
_C='BUNDLE-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntEnterpriseDataTasmanMgmt,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention',_J)
nnbundleMib=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,1,13))
if mibBuilder.loadTexts:nnbundleMib.setRevisions(('1999-04-23 00:00',))
_NnbundleTable_Object=MibTable
nnbundleTable=_NnbundleTable_Object((1,3,6,1,4,1,562,73,1,1,1,13,1))
if mibBuilder.loadTexts:nnbundleTable.setStatus(_A)
_NnbundleTableEntry_Object=MibTableRow
nnbundleTableEntry=_NnbundleTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1))
nnbundleTableEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:nnbundleTableEntry.setStatus(_A)
_NnbundleId_Type=Integer32
_NnbundleId_Object=MibTableColumn
nnbundleId=_NnbundleId_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,1),_NnbundleId_Type())
nnbundleId.setMaxAccess(_L)
if mibBuilder.loadTexts:nnbundleId.setStatus(_A)
class _NnbundleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NnbundleName_Type.__name__=_E
_NnbundleName_Object=MibTableColumn
nnbundleName=_NnbundleName_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,2),_NnbundleName_Type())
nnbundleName.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleName.setStatus(_A)
class _NnbundleContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_NnbundleContact_Type.__name__=_E
_NnbundleContact_Object=MibTableColumn
nnbundleContact=_NnbundleContact_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,3),_NnbundleContact_Type())
nnbundleContact.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleContact.setStatus(_A)
class _NnbundleDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,76))
_NnbundleDescr_Type.__name__=_E
_NnbundleDescr_Object=MibTableColumn
nnbundleDescr=_NnbundleDescr_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,4),_NnbundleDescr_Type())
nnbundleDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDescr.setStatus(_A)
class _NnbundleEncapsulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noEncap',1),('ppp',2),('hdlc',3),('frameRelay',4)))
_NnbundleEncapsulation_Type.__name__=_D
_NnbundleEncapsulation_Object=MibTableColumn
nnbundleEncapsulation=_NnbundleEncapsulation_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,5),_NnbundleEncapsulation_Type())
nnbundleEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleEncapsulation.setStatus(_A)
class _NnbundleDropEs_Type(Integer32):defaultValue=0
_NnbundleDropEs_Type.__name__=_D
_NnbundleDropEs_Object=MibTableColumn
nnbundleDropEs=_NnbundleDropEs_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,6),_NnbundleDropEs_Type())
nnbundleDropEs.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDropEs.setStatus(_A)
if mibBuilder.loadTexts:nnbundleDropEs.setUnits(_G)
class _NnbundleDropSes_Type(Integer32):defaultValue=0
_NnbundleDropSes_Type.__name__=_D
_NnbundleDropSes_Object=MibTableColumn
nnbundleDropSes=_NnbundleDropSes_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,7),_NnbundleDropSes_Type())
nnbundleDropSes.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDropSes.setStatus(_A)
if mibBuilder.loadTexts:nnbundleDropSes.setUnits(_G)
class _NnbundleDropUas_Type(Integer32):defaultValue=0
_NnbundleDropUas_Type.__name__=_D
_NnbundleDropUas_Object=MibTableColumn
nnbundleDropUas=_NnbundleDropUas_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,8),_NnbundleDropUas_Type())
nnbundleDropUas.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDropUas.setStatus(_A)
if mibBuilder.loadTexts:nnbundleDropUas.setUnits(_G)
class _NnbundleDropEev_Type(Integer32):defaultValue=0
_NnbundleDropEev_Type.__name__=_D
_NnbundleDropEev_Object=MibTableColumn
nnbundleDropEev=_NnbundleDropEev_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,9),_NnbundleDropEev_Type())
nnbundleDropEev.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDropEev.setStatus(_A)
if mibBuilder.loadTexts:nnbundleDropEev.setUnits(_G)
class _NnbundleDropBes_Type(Integer32):defaultValue=0
_NnbundleDropBes_Type.__name__=_D
_NnbundleDropBes_Object=MibTableColumn
nnbundleDropBes=_NnbundleDropBes_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,10),_NnbundleDropBes_Type())
nnbundleDropBes.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDropBes.setStatus(_A)
if mibBuilder.loadTexts:nnbundleDropBes.setUnits(_G)
class _NnbundleDropBbe_Type(Integer32):defaultValue=0
_NnbundleDropBbe_Type.__name__=_D
_NnbundleDropBbe_Object=MibTableColumn
nnbundleDropBbe=_NnbundleDropBbe_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,11),_NnbundleDropBbe_Type())
nnbundleDropBbe.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDropBbe.setStatus(_A)
if mibBuilder.loadTexts:nnbundleDropBbe.setUnits(_G)
class _NnbundleDropLofc_Type(Integer32):defaultValue=0
_NnbundleDropLofc_Type.__name__=_D
_NnbundleDropLofc_Object=MibTableColumn
nnbundleDropLofc=_NnbundleDropLofc_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,12),_NnbundleDropLofc_Type())
nnbundleDropLofc.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDropLofc.setStatus(_A)
if mibBuilder.loadTexts:nnbundleDropLofc.setUnits(_G)
class _NnbundleDropBpv_Type(Integer32):defaultValue=0
_NnbundleDropBpv_Type.__name__=_D
_NnbundleDropBpv_Object=MibTableColumn
nnbundleDropBpv=_NnbundleDropBpv_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,13),_NnbundleDropBpv_Type())
nnbundleDropBpv.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDropBpv.setStatus(_A)
if mibBuilder.loadTexts:nnbundleDropBpv.setUnits(_G)
class _NnbundleDropCss_Type(Integer32):defaultValue=0
_NnbundleDropCss_Type.__name__=_D
_NnbundleDropCss_Object=MibTableColumn
nnbundleDropCss=_NnbundleDropCss_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,14),_NnbundleDropCss_Type())
nnbundleDropCss.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDropCss.setStatus(_A)
if mibBuilder.loadTexts:nnbundleDropCss.setUnits(_G)
class _NnbundleDropOof_Type(Integer32):defaultValue=0
_NnbundleDropOof_Type.__name__=_D
_NnbundleDropOof_Object=MibTableColumn
nnbundleDropOof=_NnbundleDropOof_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,15),_NnbundleDropOof_Type())
nnbundleDropOof.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDropOof.setStatus(_A)
if mibBuilder.loadTexts:nnbundleDropOof.setUnits(_G)
class _NnbundleDropCrc_Type(Integer32):defaultValue=0
_NnbundleDropCrc_Type.__name__=_D
_NnbundleDropCrc_Object=MibTableColumn
nnbundleDropCrc=_NnbundleDropCrc_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,16),_NnbundleDropCrc_Type())
nnbundleDropCrc.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDropCrc.setStatus(_A)
if mibBuilder.loadTexts:nnbundleDropCrc.setUnits(_G)
_NnbundleIpAddr_Type=IpAddress
_NnbundleIpAddr_Object=MibTableColumn
nnbundleIpAddr=_NnbundleIpAddr_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,17),_NnbundleIpAddr_Type())
nnbundleIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleIpAddr.setStatus(_A)
_NnbundleSubnetMask_Type=IpAddress
_NnbundleSubnetMask_Object=MibTableColumn
nnbundleSubnetMask=_NnbundleSubnetMask_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,18),_NnbundleSubnetMask_Type())
nnbundleSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleSubnetMask.setStatus(_A)
_NnbundleSrcForwardingAddrPrimary_Type=IpAddress
_NnbundleSrcForwardingAddrPrimary_Object=MibTableColumn
nnbundleSrcForwardingAddrPrimary=_NnbundleSrcForwardingAddrPrimary_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,19),_NnbundleSrcForwardingAddrPrimary_Type())
nnbundleSrcForwardingAddrPrimary.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleSrcForwardingAddrPrimary.setStatus(_A)
_NnbundleSrcForwardingAddrSecondary_Type=IpAddress
_NnbundleSrcForwardingAddrSecondary_Object=MibTableColumn
nnbundleSrcForwardingAddrSecondary=_NnbundleSrcForwardingAddrSecondary_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,20),_NnbundleSrcForwardingAddrSecondary_Type())
nnbundleSrcForwardingAddrSecondary.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleSrcForwardingAddrSecondary.setStatus(_A)
class _NnbundleRestoreMethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('automatic',2)))
_NnbundleRestoreMethod_Type.__name__=_D
_NnbundleRestoreMethod_Object=MibTableColumn
nnbundleRestoreMethod=_NnbundleRestoreMethod_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,21),_NnbundleRestoreMethod_Type())
nnbundleRestoreMethod.setMaxAccess(_I)
if mibBuilder.loadTexts:nnbundleRestoreMethod.setStatus(_A)
class _NnbundleLinkRestoralTime_Type(Integer32):defaultValue=120
_NnbundleLinkRestoralTime_Type.__name__=_D
_NnbundleLinkRestoralTime_Object=MibTableColumn
nnbundleLinkRestoralTime=_NnbundleLinkRestoralTime_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,22),_NnbundleLinkRestoralTime_Type())
nnbundleLinkRestoralTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleLinkRestoralTime.setStatus(_A)
if mibBuilder.loadTexts:nnbundleLinkRestoralTime.setUnits(_G)
class _NnbundleStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_NnbundleStatus_Type.__name__=_D
_NnbundleStatus_Object=MibTableColumn
nnbundleStatus=_NnbundleStatus_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,23),_NnbundleStatus_Type())
nnbundleStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:nnbundleStatus.setStatus(_A)
class _NnbundleLinkRestore_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_NnbundleLinkRestore_Type.__name__=_O
_NnbundleLinkRestore_Object=MibTableColumn
nnbundleLinkRestore=_NnbundleLinkRestore_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,24),_NnbundleLinkRestore_Type())
nnbundleLinkRestore.setMaxAccess(_I)
if mibBuilder.loadTexts:nnbundleLinkRestore.setStatus(_A)
_NnbundleNoOfLinks_Type=Integer32
_NnbundleNoOfLinks_Object=MibTableColumn
nnbundleNoOfLinks=_NnbundleNoOfLinks_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,25),_NnbundleNoOfLinks_Type())
nnbundleNoOfLinks.setMaxAccess(_H)
if mibBuilder.loadTexts:nnbundleNoOfLinks.setStatus(_A)
_NnbundleTotalBw_Type=Integer32
_NnbundleTotalBw_Object=MibTableColumn
nnbundleTotalBw=_NnbundleTotalBw_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,26),_NnbundleTotalBw_Type())
nnbundleTotalBw.setMaxAccess(_H)
if mibBuilder.loadTexts:nnbundleTotalBw.setStatus(_A)
if mibBuilder.loadTexts:nnbundleTotalBw.setUnits('kbps')
_NnbundleRowStatus_Type=RowStatus
_NnbundleRowStatus_Object=MibTableColumn
nnbundleRowStatus=_NnbundleRowStatus_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,27),_NnbundleRowStatus_Type())
nnbundleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleRowStatus.setStatus(_A)
class _NnbundleIpUnnumbered_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NnbundleIpUnnumbered_Type.__name__=_E
_NnbundleIpUnnumbered_Object=MibTableColumn
nnbundleIpUnnumbered=_NnbundleIpUnnumbered_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,28),_NnbundleIpUnnumbered_Type())
nnbundleIpUnnumbered.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleIpUnnumbered.setStatus(_A)
class _NnbundleIpMulticast_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noMcast',0),('pass',1),('block',2),('ospfrip2',3)))
_NnbundleIpMulticast_Type.__name__=_D
_NnbundleIpMulticast_Object=MibTableColumn
nnbundleIpMulticast=_NnbundleIpMulticast_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,29),_NnbundleIpMulticast_Type())
nnbundleIpMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleIpMulticast.setStatus(_A)
class _NnbundleDirectedBcast_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_M,1)))
_NnbundleDirectedBcast_Type.__name__=_D
_NnbundleDirectedBcast_Object=MibTableColumn
nnbundleDirectedBcast=_NnbundleDirectedBcast_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,30),_NnbundleDirectedBcast_Type())
nnbundleDirectedBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleDirectedBcast.setStatus(_A)
class _NnbundleIcmpUnreachable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_M,1)))
_NnbundleIcmpUnreachable_Type.__name__=_D
_NnbundleIcmpUnreachable_Object=MibTableColumn
nnbundleIcmpUnreachable=_NnbundleIcmpUnreachable_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,31),_NnbundleIcmpUnreachable_Type())
nnbundleIcmpUnreachable.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleIcmpUnreachable.setStatus(_A)
class _NnbundleIcmpRedirect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_M,1)))
_NnbundleIcmpRedirect_Type.__name__=_D
_NnbundleIcmpRedirect_Object=MibTableColumn
nnbundleIcmpRedirect=_NnbundleIcmpRedirect_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,32),_NnbundleIcmpRedirect_Type())
nnbundleIcmpRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleIcmpRedirect.setStatus(_A)
_NnbundleClearCounters_Type=Integer32
_NnbundleClearCounters_Object=MibTableColumn
nnbundleClearCounters=_NnbundleClearCounters_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,33),_NnbundleClearCounters_Type())
nnbundleClearCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleClearCounters.setStatus(_A)
class _NnbundleTrackHoldDownTimer_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NnbundleTrackHoldDownTimer_Type.__name__=_D
_NnbundleTrackHoldDownTimer_Object=MibTableColumn
nnbundleTrackHoldDownTimer=_NnbundleTrackHoldDownTimer_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,34),_NnbundleTrackHoldDownTimer_Type())
nnbundleTrackHoldDownTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleTrackHoldDownTimer.setStatus(_A)
_NnbundleDropPackets_Type=Counter32
_NnbundleDropPackets_Object=MibTableColumn
nnbundleDropPackets=_NnbundleDropPackets_Object((1,3,6,1,4,1,562,73,1,1,1,13,1,1,35),_NnbundleDropPackets_Type())
nnbundleDropPackets.setMaxAccess(_H)
if mibBuilder.loadTexts:nnbundleDropPackets.setStatus(_A)
_NnbundleLinkTable_Object=MibTable
nnbundleLinkTable=_NnbundleLinkTable_Object((1,3,6,1,4,1,562,73,1,1,1,13,2))
if mibBuilder.loadTexts:nnbundleLinkTable.setStatus(_A)
_NnbundleLinkEntry_Object=MibTableRow
nnbundleLinkEntry=_NnbundleLinkEntry_Object((1,3,6,1,4,1,562,73,1,1,1,13,2,1))
nnbundleLinkEntry.setIndexNames((0,_C,_K),(0,_C,_b))
if mibBuilder.loadTexts:nnbundleLinkEntry.setStatus(_A)
_NnbundleLinkT1Num_Type=Integer32
_NnbundleLinkT1Num_Object=MibTableColumn
nnbundleLinkT1Num=_NnbundleLinkT1Num_Object((1,3,6,1,4,1,562,73,1,1,1,13,2,1,1),_NnbundleLinkT1Num_Type())
nnbundleLinkT1Num.setMaxAccess(_L)
if mibBuilder.loadTexts:nnbundleLinkT1Num.setStatus(_A)
class _NnbundleLinkTimeSlots_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_NnbundleLinkTimeSlots_Type.__name__=_O
_NnbundleLinkTimeSlots_Object=MibTableColumn
nnbundleLinkTimeSlots=_NnbundleLinkTimeSlots_Object((1,3,6,1,4,1,562,73,1,1,1,13,2,1,2),_NnbundleLinkTimeSlots_Type())
nnbundleLinkTimeSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleLinkTimeSlots.setStatus(_A)
class _NnbundleLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('ct3',1),('t1',2),('e1',3),('hssi',4),('t3',5),('v35',6),('ft1',7),('fe1',8),('x21',9),('s530',10),('s530A',11),('s449',12),('s232',13)))
_NnbundleLinkType_Type.__name__=_D
_NnbundleLinkType_Object=MibTableColumn
nnbundleLinkType=_NnbundleLinkType_Object((1,3,6,1,4,1,562,73,1,1,1,13,2,1,3),_NnbundleLinkType_Type())
nnbundleLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleLinkType.setStatus(_A)
class _NnbundleLinkSpeed_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('kbps56',1),('kbps64',2),('notApplicable',3)))
_NnbundleLinkSpeed_Type.__name__=_D
_NnbundleLinkSpeed_Object=MibTableColumn
nnbundleLinkSpeed=_NnbundleLinkSpeed_Object((1,3,6,1,4,1,562,73,1,1,1,13,2,1,4),_NnbundleLinkSpeed_Type())
nnbundleLinkSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleLinkSpeed.setStatus(_A)
class _NnbundleLinkInvertedData_Type(TruthValue):defaultValue=2
_NnbundleLinkInvertedData_Type.__name__=_J
_NnbundleLinkInvertedData_Object=MibTableColumn
nnbundleLinkInvertedData=_NnbundleLinkInvertedData_Object((1,3,6,1,4,1,562,73,1,1,1,13,2,1,5),_NnbundleLinkInvertedData_Type())
nnbundleLinkInvertedData.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleLinkInvertedData.setStatus(_A)
class _NnbundleLinkPhysIfNum_Type(Integer32):defaultValue=0
_NnbundleLinkPhysIfNum_Type.__name__=_D
_NnbundleLinkPhysIfNum_Object=MibTableColumn
nnbundleLinkPhysIfNum=_NnbundleLinkPhysIfNum_Object((1,3,6,1,4,1,562,73,1,1,1,13,2,1,6),_NnbundleLinkPhysIfNum_Type())
nnbundleLinkPhysIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleLinkPhysIfNum.setStatus(_A)
_NnbundleLinkDiffDelay_Type=Integer32
_NnbundleLinkDiffDelay_Object=MibTableColumn
nnbundleLinkDiffDelay=_NnbundleLinkDiffDelay_Object((1,3,6,1,4,1,562,73,1,1,1,13,2,1,7),_NnbundleLinkDiffDelay_Type())
nnbundleLinkDiffDelay.setMaxAccess(_H)
if mibBuilder.loadTexts:nnbundleLinkDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:nnbundleLinkDiffDelay.setUnits('milli-seconds')
_NnbundleLinkBw_Type=Integer32
_NnbundleLinkBw_Object=MibTableColumn
nnbundleLinkBw=_NnbundleLinkBw_Object((1,3,6,1,4,1,562,73,1,1,1,13,2,1,8),_NnbundleLinkBw_Type())
nnbundleLinkBw.setMaxAccess(_H)
if mibBuilder.loadTexts:nnbundleLinkBw.setStatus(_A)
if mibBuilder.loadTexts:nnbundleLinkBw.setUnits('kbps')
class _NnbundleLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_P,2)))
_NnbundleLinkStatus_Type.__name__=_D
_NnbundleLinkStatus_Object=MibTableColumn
nnbundleLinkStatus=_NnbundleLinkStatus_Object((1,3,6,1,4,1,562,73,1,1,1,13,2,1,9),_NnbundleLinkStatus_Type())
nnbundleLinkStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:nnbundleLinkStatus.setStatus(_A)
_NnbundleLinkRowStatus_Type=RowStatus
_NnbundleLinkRowStatus_Object=MibTableColumn
nnbundleLinkRowStatus=_NnbundleLinkRowStatus_Object((1,3,6,1,4,1,562,73,1,1,1,13,2,1,10),_NnbundleLinkRowStatus_Type())
nnbundleLinkRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nnbundleLinkRowStatus.setStatus(_A)
_NnbundleTrackTable_Object=MibTable
nnbundleTrackTable=_NnbundleTrackTable_Object((1,3,6,1,4,1,562,73,1,1,1,13,3))
if mibBuilder.loadTexts:nnbundleTrackTable.setStatus(_A)
_NnbundleTrackEntry_Object=MibTableRow
nnbundleTrackEntry=_NnbundleTrackEntry_Object((1,3,6,1,4,1,562,73,1,1,1,13,3,1))
nnbundleTrackEntry.setIndexNames((0,_C,_K),(0,_C,_c))
if mibBuilder.loadTexts:nnbundleTrackEntry.setStatus(_A)
_NntrackIntfId_Type=Integer32
_NntrackIntfId_Object=MibTableColumn
nntrackIntfId=_NntrackIntfId_Object((1,3,6,1,4,1,562,73,1,1,1,13,3,1,1),_NntrackIntfId_Type())
nntrackIntfId.setMaxAccess(_L)
if mibBuilder.loadTexts:nntrackIntfId.setStatus(_A)
class _NntrackIntfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NntrackIntfName_Type.__name__=_E
_NntrackIntfName_Object=MibTableColumn
nntrackIntfName=_NntrackIntfName_Object((1,3,6,1,4,1,562,73,1,1,1,13,3,1,2),_NntrackIntfName_Type())
nntrackIntfName.setMaxAccess(_B)
if mibBuilder.loadTexts:nntrackIntfName.setStatus(_A)
class _NntrackIntfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_P,2)))
_NntrackIntfStatus_Type.__name__=_D
_NntrackIntfStatus_Object=MibTableColumn
nntrackIntfStatus=_NntrackIntfStatus_Object((1,3,6,1,4,1,562,73,1,1,1,13,3,1,3),_NntrackIntfStatus_Type())
nntrackIntfStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:nntrackIntfStatus.setStatus(_A)
_NntrackIntfRowStatus_Type=RowStatus
_NntrackIntfRowStatus_Object=MibTableColumn
nntrackIntfRowStatus=_NntrackIntfRowStatus_Object((1,3,6,1,4,1,562,73,1,1,1,13,3,1,4),_NntrackIntfRowStatus_Type())
nntrackIntfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nntrackIntfRowStatus.setStatus(_A)
_NnloopbackIfTable_Object=MibTable
nnloopbackIfTable=_NnloopbackIfTable_Object((1,3,6,1,4,1,562,73,1,1,1,13,4))
if mibBuilder.loadTexts:nnloopbackIfTable.setStatus(_A)
_NnloopbackIfTableEntry_Object=MibTableRow
nnloopbackIfTableEntry=_NnloopbackIfTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,13,4,1))
nnloopbackIfTableEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:nnloopbackIfTableEntry.setStatus(_A)
_NnloopbackIfId_Type=Integer32
_NnloopbackIfId_Object=MibTableColumn
nnloopbackIfId=_NnloopbackIfId_Object((1,3,6,1,4,1,562,73,1,1,1,13,4,1,1),_NnloopbackIfId_Type())
nnloopbackIfId.setMaxAccess(_L)
if mibBuilder.loadTexts:nnloopbackIfId.setStatus(_A)
class _NnloopbackIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NnloopbackIfName_Type.__name__=_E
_NnloopbackIfName_Object=MibTableColumn
nnloopbackIfName=_NnloopbackIfName_Object((1,3,6,1,4,1,562,73,1,1,1,13,4,1,2),_NnloopbackIfName_Type())
nnloopbackIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:nnloopbackIfName.setStatus(_A)
_NnloopbackIfIpAddr_Type=IpAddress
_NnloopbackIfIpAddr_Object=MibTableColumn
nnloopbackIfIpAddr=_NnloopbackIfIpAddr_Object((1,3,6,1,4,1,562,73,1,1,1,13,4,1,3),_NnloopbackIfIpAddr_Type())
nnloopbackIfIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnloopbackIfIpAddr.setStatus(_A)
_NnloopbackIfSubnetMask_Type=IpAddress
_NnloopbackIfSubnetMask_Object=MibTableColumn
nnloopbackIfSubnetMask=_NnloopbackIfSubnetMask_Object((1,3,6,1,4,1,562,73,1,1,1,13,4,1,4),_NnloopbackIfSubnetMask_Type())
nnloopbackIfSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:nnloopbackIfSubnetMask.setStatus(_A)
class _NnloopbackIfStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_P,2)))
_NnloopbackIfStatus_Type.__name__=_D
_NnloopbackIfStatus_Object=MibTableColumn
nnloopbackIfStatus=_NnloopbackIfStatus_Object((1,3,6,1,4,1,562,73,1,1,1,13,4,1,5),_NnloopbackIfStatus_Type())
nnloopbackIfStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:nnloopbackIfStatus.setStatus(_A)
_NnloopbackIfRowStatus_Type=RowStatus
_NnloopbackIfRowStatus_Object=MibTableColumn
nnloopbackIfRowStatus=_NnloopbackIfRowStatus_Object((1,3,6,1,4,1,562,73,1,1,1,13,4,1,6),_NnloopbackIfRowStatus_Type())
nnloopbackIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nnloopbackIfRowStatus.setStatus(_A)
_NnbundleTraps_ObjectIdentity=ObjectIdentity
nnbundleTraps=_NnbundleTraps_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,13,5))
_NnbundleNotifications_ObjectIdentity=ObjectIdentity
nnbundleNotifications=_NnbundleNotifications_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,13,5,0))
_NnbundleTrapVariables_ObjectIdentity=ObjectIdentity
nnbundleTrapVariables=_NnbundleTrapVariables_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,13,5,1))
class _NnbundleNameStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NnbundleNameStr_Type.__name__=_E
_NnbundleNameStr_Object=MibScalar
nnbundleNameStr=_NnbundleNameStr_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,1),_NnbundleNameStr_Type())
nnbundleNameStr.setMaxAccess(_F)
if mibBuilder.loadTexts:nnbundleNameStr.setStatus(_A)
class _NnbundleDownCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3),('l2-negotiation-fail',4),('bcp-negotiation-fail',5),('l3-negotiation-fail',6),('bundle-track-down',7)))
_NnbundleDownCause_Type.__name__=_D
_NnbundleDownCause_Object=MibScalar
nnbundleDownCause=_NnbundleDownCause_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,2),_NnbundleDownCause_Type())
nnbundleDownCause.setMaxAccess(_F)
if mibBuilder.loadTexts:nnbundleDownCause.setStatus(_A)
class _NnbundleContactInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_NnbundleContactInfo_Type.__name__=_E
_NnbundleContactInfo_Object=MibScalar
nnbundleContactInfo=_NnbundleContactInfo_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,3),_NnbundleContactInfo_Type())
nnbundleContactInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:nnbundleContactInfo.setStatus(_A)
class _NnbundleDescrInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_NnbundleDescrInfo_Type.__name__=_E
_NnbundleDescrInfo_Object=MibScalar
nnbundleDescrInfo=_NnbundleDescrInfo_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,4),_NnbundleDescrInfo_Type())
nnbundleDescrInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:nnbundleDescrInfo.setStatus(_A)
class _NnlinkNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_NnlinkNum_Type.__name__=_E
_NnlinkNum_Object=MibScalar
nnlinkNum=_NnlinkNum_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,5),_NnlinkNum_Type())
nnlinkNum.setMaxAccess(_F)
if mibBuilder.loadTexts:nnlinkNum.setStatus(_A)
class _NnlinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('t1',1),('t1-within-ct3',2),('e1',3),('e1-within-ce3',4),('t3',5),('hssi',6),('v35',7),('ft1',8),('fe1',9),('x21',10),('s530',11),('s530A',12),('s449',13),('s232',14)))
_NnlinkType_Type.__name__=_D
_NnlinkType_Object=MibScalar
nnlinkType=_NnlinkType_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,6),_NnlinkType_Type())
nnlinkType.setMaxAccess(_F)
if mibBuilder.loadTexts:nnlinkType.setStatus(_A)
class _NnlinkCt3Num_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_NnlinkCt3Num_Type.__name__=_E
_NnlinkCt3Num_Object=MibScalar
nnlinkCt3Num=_NnlinkCt3Num_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,7),_NnlinkCt3Num_Type())
nnlinkCt3Num.setMaxAccess(_F)
if mibBuilder.loadTexts:nnlinkCt3Num.setStatus(_A)
class _NnlinkDownCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_e,1),(_f,2),('drop-config',3),('diffdelay',4),(_g,5)))
_NnlinkDownCause_Type.__name__=_D
_NnlinkDownCause_Object=MibScalar
nnlinkDownCause=_NnlinkDownCause_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,8),_NnlinkDownCause_Type())
nnlinkDownCause.setMaxAccess(_F)
if mibBuilder.loadTexts:nnlinkDownCause.setStatus(_A)
class _NnlinkBundleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_NnlinkBundleName_Type.__name__=_E
_NnlinkBundleName_Object=MibScalar
nnlinkBundleName=_NnlinkBundleName_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,9),_NnlinkBundleName_Type())
nnlinkBundleName.setMaxAccess(_F)
if mibBuilder.loadTexts:nnlinkBundleName.setStatus(_A)
class _NnlinkCircuitId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NnlinkCircuitId_Type.__name__=_E
_NnlinkCircuitId_Object=MibScalar
nnlinkCircuitId=_NnlinkCircuitId_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,10),_NnlinkCircuitId_Type())
nnlinkCircuitId.setMaxAccess(_F)
if mibBuilder.loadTexts:nnlinkCircuitId.setStatus(_A)
class _NnlinkContactInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NnlinkContactInfo_Type.__name__=_E
_NnlinkContactInfo_Object=MibScalar
nnlinkContactInfo=_NnlinkContactInfo_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,11),_NnlinkContactInfo_Type())
nnlinkContactInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:nnlinkContactInfo.setStatus(_A)
class _NnlinkNameInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NnlinkNameInfo_Type.__name__=_E
_NnlinkNameInfo_Object=MibScalar
nnlinkNameInfo=_NnlinkNameInfo_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,12),_NnlinkNameInfo_Type())
nnlinkNameInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:nnlinkNameInfo.setStatus(_A)
class _NnlinkDescrInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_NnlinkDescrInfo_Type.__name__=_E
_NnlinkDescrInfo_Object=MibScalar
nnlinkDescrInfo=_NnlinkDescrInfo_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,1,13),_NnlinkDescrInfo_Type())
nnlinkDescrInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:nnlinkDescrInfo.setStatus(_A)
class _NnenableBundleUpDownNotification_Type(TruthValue):defaultValue=1
_NnenableBundleUpDownNotification_Type.__name__=_J
_NnenableBundleUpDownNotification_Object=MibScalar
nnenableBundleUpDownNotification=_NnenableBundleUpDownNotification_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,2),_NnenableBundleUpDownNotification_Type())
nnenableBundleUpDownNotification.setMaxAccess(_I)
if mibBuilder.loadTexts:nnenableBundleUpDownNotification.setStatus(_A)
class _NnenableLinkUpDownNotification_Type(TruthValue):defaultValue=1
_NnenableLinkUpDownNotification_Type.__name__=_J
_NnenableLinkUpDownNotification_Object=MibScalar
nnenableLinkUpDownNotification=_NnenableLinkUpDownNotification_Object((1,3,6,1,4,1,562,73,1,1,1,13,5,3),_NnenableLinkUpDownNotification_Type())
nnenableLinkUpDownNotification.setMaxAccess(_I)
if mibBuilder.loadTexts:nnenableLinkUpDownNotification.setStatus(_A)
nnbundleDownTrap=NotificationType((1,3,6,1,4,1,562,73,1,1,1,13,5,0,1))
nnbundleDownTrap.setObjects(*((_C,_Q),(_C,_h),(_C,_R),(_C,_S)))
if mibBuilder.loadTexts:nnbundleDownTrap.setStatus(_A)
nnbundleUpTrap=NotificationType((1,3,6,1,4,1,562,73,1,1,1,13,5,0,2))
nnbundleUpTrap.setObjects(*((_C,_Q),(_C,_R),(_C,_S)))
if mibBuilder.loadTexts:nnbundleUpTrap.setStatus(_A)
nnlinkDownTrap=NotificationType((1,3,6,1,4,1,562,73,1,1,1,13,5,0,3))
nnlinkDownTrap.setObjects(*((_C,_T),(_C,_U),(_C,_V),(_C,_i),(_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_C,_a)))
if mibBuilder.loadTexts:nnlinkDownTrap.setStatus(_A)
nnlinkUpTrap=NotificationType((1,3,6,1,4,1,562,73,1,1,1,13,5,0,4))
nnlinkUpTrap.setObjects(*((_C,_T),(_C,_U),(_C,_V),(_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_C,_a)))
if mibBuilder.loadTexts:nnlinkUpTrap.setStatus(_A)
nnbundleNotificationGroup=NotificationGroup((1,3,6,1,4,1,562,73,1,1,1,13,6))
nnbundleNotificationGroup.setObjects(*((_C,_j),(_C,_k),(_C,_l),(_C,_m)))
if mibBuilder.loadTexts:nnbundleNotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nnbundleMib':nnbundleMib,'nnbundleTable':nnbundleTable,'nnbundleTableEntry':nnbundleTableEntry,_K:nnbundleId,'nnbundleName':nnbundleName,'nnbundleContact':nnbundleContact,'nnbundleDescr':nnbundleDescr,'nnbundleEncapsulation':nnbundleEncapsulation,'nnbundleDropEs':nnbundleDropEs,'nnbundleDropSes':nnbundleDropSes,'nnbundleDropUas':nnbundleDropUas,'nnbundleDropEev':nnbundleDropEev,'nnbundleDropBes':nnbundleDropBes,'nnbundleDropBbe':nnbundleDropBbe,'nnbundleDropLofc':nnbundleDropLofc,'nnbundleDropBpv':nnbundleDropBpv,'nnbundleDropCss':nnbundleDropCss,'nnbundleDropOof':nnbundleDropOof,'nnbundleDropCrc':nnbundleDropCrc,'nnbundleIpAddr':nnbundleIpAddr,'nnbundleSubnetMask':nnbundleSubnetMask,'nnbundleSrcForwardingAddrPrimary':nnbundleSrcForwardingAddrPrimary,'nnbundleSrcForwardingAddrSecondary':nnbundleSrcForwardingAddrSecondary,'nnbundleRestoreMethod':nnbundleRestoreMethod,'nnbundleLinkRestoralTime':nnbundleLinkRestoralTime,'nnbundleStatus':nnbundleStatus,'nnbundleLinkRestore':nnbundleLinkRestore,'nnbundleNoOfLinks':nnbundleNoOfLinks,'nnbundleTotalBw':nnbundleTotalBw,'nnbundleRowStatus':nnbundleRowStatus,'nnbundleIpUnnumbered':nnbundleIpUnnumbered,'nnbundleIpMulticast':nnbundleIpMulticast,'nnbundleDirectedBcast':nnbundleDirectedBcast,'nnbundleIcmpUnreachable':nnbundleIcmpUnreachable,'nnbundleIcmpRedirect':nnbundleIcmpRedirect,'nnbundleClearCounters':nnbundleClearCounters,'nnbundleTrackHoldDownTimer':nnbundleTrackHoldDownTimer,'nnbundleDropPackets':nnbundleDropPackets,'nnbundleLinkTable':nnbundleLinkTable,'nnbundleLinkEntry':nnbundleLinkEntry,_b:nnbundleLinkT1Num,'nnbundleLinkTimeSlots':nnbundleLinkTimeSlots,'nnbundleLinkType':nnbundleLinkType,'nnbundleLinkSpeed':nnbundleLinkSpeed,'nnbundleLinkInvertedData':nnbundleLinkInvertedData,'nnbundleLinkPhysIfNum':nnbundleLinkPhysIfNum,'nnbundleLinkDiffDelay':nnbundleLinkDiffDelay,'nnbundleLinkBw':nnbundleLinkBw,'nnbundleLinkStatus':nnbundleLinkStatus,'nnbundleLinkRowStatus':nnbundleLinkRowStatus,'nnbundleTrackTable':nnbundleTrackTable,'nnbundleTrackEntry':nnbundleTrackEntry,_c:nntrackIntfId,'nntrackIntfName':nntrackIntfName,'nntrackIntfStatus':nntrackIntfStatus,'nntrackIntfRowStatus':nntrackIntfRowStatus,'nnloopbackIfTable':nnloopbackIfTable,'nnloopbackIfTableEntry':nnloopbackIfTableEntry,_d:nnloopbackIfId,'nnloopbackIfName':nnloopbackIfName,'nnloopbackIfIpAddr':nnloopbackIfIpAddr,'nnloopbackIfSubnetMask':nnloopbackIfSubnetMask,'nnloopbackIfStatus':nnloopbackIfStatus,'nnloopbackIfRowStatus':nnloopbackIfRowStatus,'nnbundleTraps':nnbundleTraps,'nnbundleNotifications':nnbundleNotifications,_j:nnbundleDownTrap,_k:nnbundleUpTrap,_l:nnlinkDownTrap,_m:nnlinkUpTrap,'nnbundleTrapVariables':nnbundleTrapVariables,_Q:nnbundleNameStr,_h:nnbundleDownCause,_R:nnbundleContactInfo,_S:nnbundleDescrInfo,_T:nnlinkNum,_U:nnlinkType,_V:nnlinkCt3Num,_i:nnlinkDownCause,_W:nnlinkBundleName,_X:nnlinkCircuitId,_Y:nnlinkContactInfo,_Z:nnlinkNameInfo,_a:nnlinkDescrInfo,'nnenableBundleUpDownNotification':nnenableBundleUpDownNotification,'nnenableLinkUpDownNotification':nnenableLinkUpDownNotification,'nnbundleNotificationGroup':nnbundleNotificationGroup})