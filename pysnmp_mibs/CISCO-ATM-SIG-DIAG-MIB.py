_z='ciscoSigFailMIBGroup'
_y='ciscoSigFailGeneralGroup'
_x='csfDtlLinkType'
_w='csfDtlPortId'
_v='csfDtlNodeId'
_u='csfRecordTimeStamp'
_t='csfRecordCrankBackPortId'
_s='csfRecordCrankBackSucceedingNodeId'
_r='csfRecordCrankBackNodeId'
_q='csfRecordCrankBackTransitType'
_p='csfRecordCalledPartySubAddress'
_o='csfRecordCalledParty'
_n='csfRecordCallingPartySubAddress'
_m='csfRecordCallingParty'
_l='csfRecordDiags'
_k='csfRecordCause'
_j='csfRecordOutInterface'
_i='csfRecordInInterface'
_h='csfRecordServiceCategory'
_g='csfRecordConnIndicator'
_f='csfRecordConnCastType'
_e='csfRecordConnKind'
_d='csfRecordScope'
_c='csfFilterRowStatus'
_b='csfFilterNumMatches'
_a='csfFilterPurge'
_Z='csfFilterAgeTimeout'
_Y='csfFilterMaxRecords'
_X='csfFilterCalledPartyMask'
_W='csfFilterCalledParty'
_V='csfFilterCallingPartyMask'
_U='csfFilterCallingParty'
_T='csfFilterCause'
_S='csfFilterOutInterface'
_R='csfFilterInInterface'
_Q='csfFilterServiceCategory'
_P='csfFilterConnCastType'
_O='csfFilterConnKind'
_N='csfFilterScope'
_M='csfFilterControl'
_L='csfDtlEntryIndex'
_K='csfRecordIndex'
_J='AtmAddr'
_I='not-accessible'
_H='InterfaceIndexOrZero'
_G='csfFilterIndex'
_F='OctetString'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='CISCO-ATM-SIG-DIAG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('CISCO-TC',_H)
PnniNodeId,PnniPortId,ServiceCategory=mibBuilder.importSymbols('PNNI-MIB','PnniNodeId','PnniPortId','ServiceCategory')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
ciscoAtmSigDiagMIB=ModuleIdentity((1,3,6,1,4,1,9,9,78))
if mibBuilder.loadTexts:ciscoAtmSigDiagMIB.setRevisions(('1997-07-28 00:00',))
class AtmAddr(TextualConvention,OctetString):status=_A;displayHint='1x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8),ValueSizeConstraint(20,20))
_CiscoSigFailMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSigFailMIBObjects=_CiscoSigFailMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,78,1))
_CsfBaseGroup_ObjectIdentity=ObjectIdentity
csfBaseGroup=_CsfBaseGroup_ObjectIdentity((1,3,6,1,4,1,9,9,78,1,1))
class _CsfFilterControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CsfFilterControl_Type.__name__=_D
_CsfFilterControl_Object=MibScalar
csfFilterControl=_CsfFilterControl_Object((1,3,6,1,4,1,9,9,78,1,1,1),_CsfFilterControl_Type())
csfFilterControl.setMaxAccess('read-write')
if mibBuilder.loadTexts:csfFilterControl.setStatus(_A)
_CsfFilterGroup_ObjectIdentity=ObjectIdentity
csfFilterGroup=_CsfFilterGroup_ObjectIdentity((1,3,6,1,4,1,9,9,78,1,2))
_CsfFilterTable_Object=MibTable
csfFilterTable=_CsfFilterTable_Object((1,3,6,1,4,1,9,9,78,1,2,1))
if mibBuilder.loadTexts:csfFilterTable.setStatus(_A)
_CsfFilterEntry_Object=MibTableRow
csfFilterEntry=_CsfFilterEntry_Object((1,3,6,1,4,1,9,9,78,1,2,1,1))
csfFilterEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:csfFilterEntry.setStatus(_A)
class _CsfFilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_CsfFilterIndex_Type.__name__=_D
_CsfFilterIndex_Object=MibTableColumn
csfFilterIndex=_CsfFilterIndex_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,1),_CsfFilterIndex_Type())
csfFilterIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:csfFilterIndex.setStatus(_A)
class _CsfFilterScope_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('localRejects',1),('remoteRejects',2),('allRejects',3)))
_CsfFilterScope_Type.__name__=_D
_CsfFilterScope_Object=MibTableColumn
csfFilterScope=_CsfFilterScope_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,2),_CsfFilterScope_Type())
csfFilterScope.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterScope.setStatus(_A)
class _CsfFilterConnKind_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CsfFilterConnKind_Type.__name__=_F
_CsfFilterConnKind_Object=MibTableColumn
csfFilterConnKind=_CsfFilterConnKind_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,3),_CsfFilterConnKind_Type())
csfFilterConnKind.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterConnKind.setStatus(_A)
class _CsfFilterConnCastType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CsfFilterConnCastType_Type.__name__=_F
_CsfFilterConnCastType_Object=MibTableColumn
csfFilterConnCastType=_CsfFilterConnCastType_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,4),_CsfFilterConnCastType_Type())
csfFilterConnCastType.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterConnCastType.setStatus(_A)
class _CsfFilterServiceCategory_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CsfFilterServiceCategory_Type.__name__=_F
_CsfFilterServiceCategory_Object=MibTableColumn
csfFilterServiceCategory=_CsfFilterServiceCategory_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,5),_CsfFilterServiceCategory_Type())
csfFilterServiceCategory.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterServiceCategory.setStatus(_A)
class _CsfFilterInInterface_Type(InterfaceIndexOrZero):defaultValue=0
_CsfFilterInInterface_Type.__name__=_H
_CsfFilterInInterface_Object=MibTableColumn
csfFilterInInterface=_CsfFilterInInterface_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,6),_CsfFilterInInterface_Type())
csfFilterInInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterInInterface.setStatus(_A)
class _CsfFilterOutInterface_Type(InterfaceIndexOrZero):defaultValue=0
_CsfFilterOutInterface_Type.__name__=_H
_CsfFilterOutInterface_Object=MibTableColumn
csfFilterOutInterface=_CsfFilterOutInterface_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,7),_CsfFilterOutInterface_Type())
csfFilterOutInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterOutInterface.setStatus(_A)
class _CsfFilterCause_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CsfFilterCause_Type.__name__=_D
_CsfFilterCause_Object=MibTableColumn
csfFilterCause=_CsfFilterCause_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,8),_CsfFilterCause_Type())
csfFilterCause.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterCause.setStatus(_A)
class _CsfFilterCallingParty_Type(AtmAddr):defaultValue=OctetString('')
_CsfFilterCallingParty_Type.__name__=_J
_CsfFilterCallingParty_Object=MibTableColumn
csfFilterCallingParty=_CsfFilterCallingParty_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,9),_CsfFilterCallingParty_Type())
csfFilterCallingParty.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterCallingParty.setStatus(_A)
class _CsfFilterCallingPartyMask_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CsfFilterCallingPartyMask_Type.__name__=_F
_CsfFilterCallingPartyMask_Object=MibTableColumn
csfFilterCallingPartyMask=_CsfFilterCallingPartyMask_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,10),_CsfFilterCallingPartyMask_Type())
csfFilterCallingPartyMask.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterCallingPartyMask.setStatus(_A)
class _CsfFilterCalledParty_Type(AtmAddr):defaultValue=OctetString('')
_CsfFilterCalledParty_Type.__name__=_J
_CsfFilterCalledParty_Object=MibTableColumn
csfFilterCalledParty=_CsfFilterCalledParty_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,11),_CsfFilterCalledParty_Type())
csfFilterCalledParty.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterCalledParty.setStatus(_A)
class _CsfFilterCalledPartyMask_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CsfFilterCalledPartyMask_Type.__name__=_F
_CsfFilterCalledPartyMask_Object=MibTableColumn
csfFilterCalledPartyMask=_CsfFilterCalledPartyMask_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,12),_CsfFilterCalledPartyMask_Type())
csfFilterCalledPartyMask.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterCalledPartyMask.setStatus(_A)
class _CsfFilterMaxRecords_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,214783647))
_CsfFilterMaxRecords_Type.__name__=_D
_CsfFilterMaxRecords_Object=MibTableColumn
csfFilterMaxRecords=_CsfFilterMaxRecords_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,13),_CsfFilterMaxRecords_Type())
csfFilterMaxRecords.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterMaxRecords.setStatus(_A)
class _CsfFilterAgeTimeout_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_CsfFilterAgeTimeout_Type.__name__=_D
_CsfFilterAgeTimeout_Object=MibTableColumn
csfFilterAgeTimeout=_CsfFilterAgeTimeout_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,14),_CsfFilterAgeTimeout_Type())
csfFilterAgeTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterAgeTimeout.setStatus(_A)
if mibBuilder.loadTexts:csfFilterAgeTimeout.setUnits('seconds')
class _CsfFilterPurge_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('purge',1),('noop',2)))
_CsfFilterPurge_Type.__name__=_D
_CsfFilterPurge_Object=MibTableColumn
csfFilterPurge=_CsfFilterPurge_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,15),_CsfFilterPurge_Type())
csfFilterPurge.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterPurge.setStatus(_A)
_CsfFilterNumMatches_Type=Counter32
_CsfFilterNumMatches_Object=MibTableColumn
csfFilterNumMatches=_CsfFilterNumMatches_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,16),_CsfFilterNumMatches_Type())
csfFilterNumMatches.setMaxAccess(_C)
if mibBuilder.loadTexts:csfFilterNumMatches.setStatus(_A)
_CsfFilterRowStatus_Type=RowStatus
_CsfFilterRowStatus_Object=MibTableColumn
csfFilterRowStatus=_CsfFilterRowStatus_Object((1,3,6,1,4,1,9,9,78,1,2,1,1,17),_CsfFilterRowStatus_Type())
csfFilterRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:csfFilterRowStatus.setStatus(_A)
_CsfRecordGroup_ObjectIdentity=ObjectIdentity
csfRecordGroup=_CsfRecordGroup_ObjectIdentity((1,3,6,1,4,1,9,9,78,1,3))
_CsfRecordTable_Object=MibTable
csfRecordTable=_CsfRecordTable_Object((1,3,6,1,4,1,9,9,78,1,3,1))
if mibBuilder.loadTexts:csfRecordTable.setStatus(_A)
_CsfRecordEntry_Object=MibTableRow
csfRecordEntry=_CsfRecordEntry_Object((1,3,6,1,4,1,9,9,78,1,3,1,1))
csfRecordEntry.setIndexNames((0,_B,_G),(0,_B,_K))
if mibBuilder.loadTexts:csfRecordEntry.setStatus(_A)
class _CsfRecordIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CsfRecordIndex_Type.__name__=_D
_CsfRecordIndex_Object=MibTableColumn
csfRecordIndex=_CsfRecordIndex_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,1),_CsfRecordIndex_Type())
csfRecordIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:csfRecordIndex.setStatus(_A)
class _CsfRecordScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('localReject',1),('remoteReject',2)))
_CsfRecordScope_Type.__name__=_D
_CsfRecordScope_Object=MibTableColumn
csfRecordScope=_CsfRecordScope_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,2),_CsfRecordScope_Type())
csfRecordScope.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordScope.setStatus(_A)
class _CsfRecordConnKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('softPvcc',1),('softPvpc',2),('switchedVcc',3),('switchedVpc',4)))
_CsfRecordConnKind_Type.__name__=_D
_CsfRecordConnKind_Object=MibTableColumn
csfRecordConnKind=_CsfRecordConnKind_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,3),_CsfRecordConnKind_Type())
csfRecordConnKind.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordConnKind.setStatus(_A)
class _CsfRecordConnCastType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('p2p',1),('p2mp',2)))
_CsfRecordConnCastType_Type.__name__=_D
_CsfRecordConnCastType_Object=MibTableColumn
csfRecordConnCastType=_CsfRecordConnCastType_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,4),_CsfRecordConnCastType_Type())
csfRecordConnCastType.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordConnCastType.setStatus(_A)
class _CsfRecordConnIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('addPartyReject',1),('setupReject',2)))
_CsfRecordConnIndicator_Type.__name__=_D
_CsfRecordConnIndicator_Object=MibTableColumn
csfRecordConnIndicator=_CsfRecordConnIndicator_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,5),_CsfRecordConnIndicator_Type())
csfRecordConnIndicator.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordConnIndicator.setStatus(_A)
_CsfRecordServiceCategory_Type=ServiceCategory
_CsfRecordServiceCategory_Object=MibTableColumn
csfRecordServiceCategory=_CsfRecordServiceCategory_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,6),_CsfRecordServiceCategory_Type())
csfRecordServiceCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordServiceCategory.setStatus(_A)
class _CsfRecordInInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CsfRecordInInterface_Type.__name__=_D
_CsfRecordInInterface_Object=MibTableColumn
csfRecordInInterface=_CsfRecordInInterface_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,7),_CsfRecordInInterface_Type())
csfRecordInInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordInInterface.setStatus(_A)
_CsfRecordOutInterface_Type=InterfaceIndexOrZero
_CsfRecordOutInterface_Object=MibTableColumn
csfRecordOutInterface=_CsfRecordOutInterface_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,8),_CsfRecordOutInterface_Type())
csfRecordOutInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordOutInterface.setStatus(_A)
class _CsfRecordCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CsfRecordCause_Type.__name__=_D
_CsfRecordCause_Object=MibTableColumn
csfRecordCause=_CsfRecordCause_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,9),_CsfRecordCause_Type())
csfRecordCause.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordCause.setStatus(_A)
class _CsfRecordDiags_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CsfRecordDiags_Type.__name__=_F
_CsfRecordDiags_Object=MibTableColumn
csfRecordDiags=_CsfRecordDiags_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,10),_CsfRecordDiags_Type())
csfRecordDiags.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordDiags.setStatus(_A)
_CsfRecordCallingParty_Type=AtmAddr
_CsfRecordCallingParty_Object=MibTableColumn
csfRecordCallingParty=_CsfRecordCallingParty_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,11),_CsfRecordCallingParty_Type())
csfRecordCallingParty.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordCallingParty.setStatus(_A)
_CsfRecordCallingPartySubAddress_Type=AtmAddr
_CsfRecordCallingPartySubAddress_Object=MibTableColumn
csfRecordCallingPartySubAddress=_CsfRecordCallingPartySubAddress_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,12),_CsfRecordCallingPartySubAddress_Type())
csfRecordCallingPartySubAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordCallingPartySubAddress.setStatus(_A)
_CsfRecordCalledParty_Type=AtmAddr
_CsfRecordCalledParty_Object=MibTableColumn
csfRecordCalledParty=_CsfRecordCalledParty_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,13),_CsfRecordCalledParty_Type())
csfRecordCalledParty.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordCalledParty.setStatus(_A)
_CsfRecordCalledPartySubAddress_Type=AtmAddr
_CsfRecordCalledPartySubAddress_Object=MibTableColumn
csfRecordCalledPartySubAddress=_CsfRecordCalledPartySubAddress_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,14),_CsfRecordCalledPartySubAddress_Type())
csfRecordCalledPartySubAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordCalledPartySubAddress.setStatus(_A)
class _CsfRecordCrankBackTransitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('blockedIncomingPort',1),('blockedNode',2),('blockedLink',3),('noCrankBack',4)))
_CsfRecordCrankBackTransitType_Type.__name__=_D
_CsfRecordCrankBackTransitType_Object=MibTableColumn
csfRecordCrankBackTransitType=_CsfRecordCrankBackTransitType_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,15),_CsfRecordCrankBackTransitType_Type())
csfRecordCrankBackTransitType.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordCrankBackTransitType.setStatus(_A)
_CsfRecordCrankBackNodeId_Type=PnniNodeId
_CsfRecordCrankBackNodeId_Object=MibTableColumn
csfRecordCrankBackNodeId=_CsfRecordCrankBackNodeId_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,16),_CsfRecordCrankBackNodeId_Type())
csfRecordCrankBackNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordCrankBackNodeId.setStatus(_A)
_CsfRecordCrankBackPortId_Type=PnniPortId
_CsfRecordCrankBackPortId_Object=MibTableColumn
csfRecordCrankBackPortId=_CsfRecordCrankBackPortId_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,17),_CsfRecordCrankBackPortId_Type())
csfRecordCrankBackPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordCrankBackPortId.setStatus(_A)
_CsfRecordCrankBackSucceedingNodeId_Type=PnniNodeId
_CsfRecordCrankBackSucceedingNodeId_Object=MibTableColumn
csfRecordCrankBackSucceedingNodeId=_CsfRecordCrankBackSucceedingNodeId_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,18),_CsfRecordCrankBackSucceedingNodeId_Type())
csfRecordCrankBackSucceedingNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordCrankBackSucceedingNodeId.setStatus(_A)
_CsfRecordTimeStamp_Type=TimeStamp
_CsfRecordTimeStamp_Object=MibTableColumn
csfRecordTimeStamp=_CsfRecordTimeStamp_Object((1,3,6,1,4,1,9,9,78,1,3,1,1,19),_CsfRecordTimeStamp_Type())
csfRecordTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:csfRecordTimeStamp.setStatus(_A)
_CsfDtlTable_Object=MibTable
csfDtlTable=_CsfDtlTable_Object((1,3,6,1,4,1,9,9,78,1,3,2))
if mibBuilder.loadTexts:csfDtlTable.setStatus(_A)
_CsfDtlEntry_Object=MibTableRow
csfDtlEntry=_CsfDtlEntry_Object((1,3,6,1,4,1,9,9,78,1,3,2,1))
csfDtlEntry.setIndexNames((0,_B,_G),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:csfDtlEntry.setStatus(_A)
class _CsfDtlEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_CsfDtlEntryIndex_Type.__name__=_D
_CsfDtlEntryIndex_Object=MibTableColumn
csfDtlEntryIndex=_CsfDtlEntryIndex_Object((1,3,6,1,4,1,9,9,78,1,3,2,1,1),_CsfDtlEntryIndex_Type())
csfDtlEntryIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:csfDtlEntryIndex.setStatus(_A)
_CsfDtlNodeId_Type=PnniNodeId
_CsfDtlNodeId_Object=MibTableColumn
csfDtlNodeId=_CsfDtlNodeId_Object((1,3,6,1,4,1,9,9,78,1,3,2,1,2),_CsfDtlNodeId_Type())
csfDtlNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:csfDtlNodeId.setStatus(_A)
_CsfDtlPortId_Type=PnniPortId
_CsfDtlPortId_Object=MibTableColumn
csfDtlPortId=_CsfDtlPortId_Object((1,3,6,1,4,1,9,9,78,1,3,2,1,3),_CsfDtlPortId_Type())
csfDtlPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:csfDtlPortId.setStatus(_A)
class _CsfDtlLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('invalid',1),('horizontal',2),('uplink',3),('last',4)))
_CsfDtlLinkType_Type.__name__=_D
_CsfDtlLinkType_Object=MibTableColumn
csfDtlLinkType=_CsfDtlLinkType_Object((1,3,6,1,4,1,9,9,78,1,3,2,1,4),_CsfDtlLinkType_Type())
csfDtlLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:csfDtlLinkType.setStatus(_A)
_CiscoSigFailMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSigFailMIBConformance=_CiscoSigFailMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,78,3))
_CiscoSigFailMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSigFailMIBCompliances=_CiscoSigFailMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,78,3,1))
_CiscoSigFailMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSigFailMIBGroups=_CiscoSigFailMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,78,3,2))
ciscoSigFailGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,9,78,3,2,1))
ciscoSigFailGeneralGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:ciscoSigFailGeneralGroup.setStatus(_A)
ciscoSigFailMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,78,3,2,2))
ciscoSigFailMIBGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:ciscoSigFailMIBGroup.setStatus(_A)
ciscoSigFailMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,78,3,1,1))
ciscoSigFailMIBCompliance.setObjects(*((_B,_y),(_B,_z)))
if mibBuilder.loadTexts:ciscoSigFailMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_J:AtmAddr,'ciscoAtmSigDiagMIB':ciscoAtmSigDiagMIB,'ciscoSigFailMIBObjects':ciscoSigFailMIBObjects,'csfBaseGroup':csfBaseGroup,_M:csfFilterControl,'csfFilterGroup':csfFilterGroup,'csfFilterTable':csfFilterTable,'csfFilterEntry':csfFilterEntry,_G:csfFilterIndex,_N:csfFilterScope,_O:csfFilterConnKind,_P:csfFilterConnCastType,_Q:csfFilterServiceCategory,_R:csfFilterInInterface,_S:csfFilterOutInterface,_T:csfFilterCause,_U:csfFilterCallingParty,_V:csfFilterCallingPartyMask,_W:csfFilterCalledParty,_X:csfFilterCalledPartyMask,_Y:csfFilterMaxRecords,_Z:csfFilterAgeTimeout,_a:csfFilterPurge,_b:csfFilterNumMatches,_c:csfFilterRowStatus,'csfRecordGroup':csfRecordGroup,'csfRecordTable':csfRecordTable,'csfRecordEntry':csfRecordEntry,_K:csfRecordIndex,_d:csfRecordScope,_e:csfRecordConnKind,_f:csfRecordConnCastType,_g:csfRecordConnIndicator,_h:csfRecordServiceCategory,_i:csfRecordInInterface,_j:csfRecordOutInterface,_k:csfRecordCause,_l:csfRecordDiags,_m:csfRecordCallingParty,_n:csfRecordCallingPartySubAddress,_o:csfRecordCalledParty,_p:csfRecordCalledPartySubAddress,_q:csfRecordCrankBackTransitType,_r:csfRecordCrankBackNodeId,_t:csfRecordCrankBackPortId,_s:csfRecordCrankBackSucceedingNodeId,_u:csfRecordTimeStamp,'csfDtlTable':csfDtlTable,'csfDtlEntry':csfDtlEntry,_L:csfDtlEntryIndex,_v:csfDtlNodeId,_w:csfDtlPortId,_x:csfDtlLinkType,'ciscoSigFailMIBConformance':ciscoSigFailMIBConformance,'ciscoSigFailMIBCompliances':ciscoSigFailMIBCompliances,'ciscoSigFailMIBCompliance':ciscoSigFailMIBCompliance,'ciscoSigFailMIBGroups':ciscoSigFailMIBGroups,_y:ciscoSigFailGeneralGroup,_z:ciscoSigFailMIBGroup})