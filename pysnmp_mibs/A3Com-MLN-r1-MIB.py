_Q='a3mlnPStatIndex'
_P='a3mlnMemPort'
_O='a3mlnMemGrpPort'
_N='a3mlnGrpPort'
_M='ignore'
_L='otherMedia'
_K='groupPort'
_J='a3mlnPindex'
_I='fddi'
_H='tokenRing'
_G='ethernet'
_F='DisplayString'
_E='read-write'
_D='A3Com-MLN-r1-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_BrouterMIB_ObjectIdentity=ObjectIdentity
brouterMIB=_BrouterMIB_ObjectIdentity((1,3,6,1,4,1,43,2))
_A3ComMLN_ObjectIdentity=ObjectIdentity
a3ComMLN=_A3ComMLN_ObjectIdentity((1,3,6,1,4,1,43,2,23))
_A3mlnMaxPorts_Type=Integer32
_A3mlnMaxPorts_Object=MibScalar
a3mlnMaxPorts=_A3mlnMaxPorts_Object((1,3,6,1,4,1,43,2,23,1),_A3mlnMaxPorts_Type())
a3mlnMaxPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnMaxPorts.setStatus(_A)
_A3mlnMaxPhyPorts_Type=Integer32
_A3mlnMaxPhyPorts_Object=MibScalar
a3mlnMaxPhyPorts=_A3mlnMaxPhyPorts_Object((1,3,6,1,4,1,43,2,23,2),_A3mlnMaxPhyPorts_Type())
a3mlnMaxPhyPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnMaxPhyPorts.setStatus(_A)
_A3mlnCCSsaveErr_Type=Integer32
_A3mlnCCSsaveErr_Object=MibScalar
a3mlnCCSsaveErr=_A3mlnCCSsaveErr_Object((1,3,6,1,4,1,43,2,23,3),_A3mlnCCSsaveErr_Type())
a3mlnCCSsaveErr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnCCSsaveErr.setStatus(_A)
_A3mlnCCSdelErr_Type=Integer32
_A3mlnCCSdelErr_Object=MibScalar
a3mlnCCSdelErr=_A3mlnCCSdelErr_Object((1,3,6,1,4,1,43,2,23,4),_A3mlnCCSdelErr_Type())
a3mlnCCSdelErr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnCCSdelErr.setStatus(_A)
class _A3mlnSetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('setNoErr',1),('setErr',2),('setWarning',3)))
_A3mlnSetStatus_Type.__name__=_C
_A3mlnSetStatus_Object=MibScalar
a3mlnSetStatus=_A3mlnSetStatus_Object((1,3,6,1,4,1,43,2,23,5),_A3mlnSetStatus_Type())
a3mlnSetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnSetStatus.setStatus(_A)
class _A3mlnSetMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_A3mlnSetMsg_Type.__name__=_F
_A3mlnSetMsg_Object=MibScalar
a3mlnSetMsg=_A3mlnSetMsg_Object((1,3,6,1,4,1,43,2,23,6),_A3mlnSetMsg_Type())
a3mlnSetMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnSetMsg.setStatus(_A)
_A3mlnPortTable_Object=MibTable
a3mlnPortTable=_A3mlnPortTable_Object((1,3,6,1,4,1,43,2,23,7))
if mibBuilder.loadTexts:a3mlnPortTable.setStatus(_A)
_A3mlnPortEntry_Object=MibTableRow
a3mlnPortEntry=_A3mlnPortEntry_Object((1,3,6,1,4,1,43,2,23,7,1))
a3mlnPortEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:a3mlnPortEntry.setStatus(_A)
_A3mlnPindex_Type=Integer32
_A3mlnPindex_Object=MibTableColumn
a3mlnPindex=_A3mlnPindex_Object((1,3,6,1,4,1,43,2,23,7,1,1),_A3mlnPindex_Type())
a3mlnPindex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPindex.setStatus(_A)
class _A3mlnPtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ppmPort',1),(_K,2),('memberPort',3),('primaryPort',4)))
_A3mlnPtype_Type.__name__=_C
_A3mlnPtype_Object=MibTableColumn
a3mlnPtype=_A3mlnPtype_Object((1,3,6,1,4,1,43,2,23,7,1,2),_A3mlnPtype_Type())
a3mlnPtype.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPtype.setStatus(_A)
class _A3mlnPowner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_L,4)))
_A3mlnPowner_Type.__name__=_C
_A3mlnPowner_Object=MibTableColumn
a3mlnPowner=_A3mlnPowner_Object((1,3,6,1,4,1,43,2,23,7,1,3),_A3mlnPowner_Type())
a3mlnPowner.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPowner.setStatus(_A)
_A3mlnPlink_Type=Integer32
_A3mlnPlink_Object=MibTableColumn
a3mlnPlink=_A3mlnPlink_Object((1,3,6,1,4,1,43,2,23,7,1,4),_A3mlnPlink_Type())
a3mlnPlink.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPlink.setStatus(_A)
class _A3mlnPstState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forwarding',1),('blocking',2),(_M,3)))
_A3mlnPstState_Type.__name__=_C
_A3mlnPstState_Object=MibTableColumn
a3mlnPstState=_A3mlnPstState_Object((1,3,6,1,4,1,43,2,23,7,1,5),_A3mlnPstState_Type())
a3mlnPstState.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPstState.setStatus(_A)
class _A3mlnPtbState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('learn',1),('noLearn',2),(_M,3)))
_A3mlnPtbState_Type.__name__=_C
_A3mlnPtbState_Object=MibTableColumn
a3mlnPtbState=_A3mlnPtbState_Object((1,3,6,1,4,1,43,2,23,7,1,6),_A3mlnPtbState_Type())
a3mlnPtbState.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPtbState.setStatus(_A)
_A3mlnPgrpPrimaryPort_Type=Integer32
_A3mlnPgrpPrimaryPort_Object=MibTableColumn
a3mlnPgrpPrimaryPort=_A3mlnPgrpPrimaryPort_Object((1,3,6,1,4,1,43,2,23,7,1,7),_A3mlnPgrpPrimaryPort_Type())
a3mlnPgrpPrimaryPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPgrpPrimaryPort.setStatus(_A)
_A3mlnPgrpSrcAdrPort_Type=Integer32
_A3mlnPgrpSrcAdrPort_Object=MibTableColumn
a3mlnPgrpSrcAdrPort=_A3mlnPgrpSrcAdrPort_Object((1,3,6,1,4,1,43,2,23,7,1,8),_A3mlnPgrpSrcAdrPort_Type())
a3mlnPgrpSrcAdrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPgrpSrcAdrPort.setStatus(_A)
class _A3mlnPgrpSrcAdrMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mediaMAC',1),('mediaOther',2)))
_A3mlnPgrpSrcAdrMedia_Type.__name__=_C
_A3mlnPgrpSrcAdrMedia_Object=MibTableColumn
a3mlnPgrpSrcAdrMedia=_A3mlnPgrpSrcAdrMedia_Object((1,3,6,1,4,1,43,2,23,7,1,9),_A3mlnPgrpSrcAdrMedia_Type())
a3mlnPgrpSrcAdrMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPgrpSrcAdrMedia.setStatus(_A)
_A3mlnPgrpSrcAdrValue_Type=PhysAddress
_A3mlnPgrpSrcAdrValue_Object=MibTableColumn
a3mlnPgrpSrcAdrValue=_A3mlnPgrpSrcAdrValue_Object((1,3,6,1,4,1,43,2,23,7,1,10),_A3mlnPgrpSrcAdrValue_Type())
a3mlnPgrpSrcAdrValue.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPgrpSrcAdrValue.setStatus(_A)
class _A3mlnPgrpDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_A3mlnPgrpDescription_Type.__name__=_F
_A3mlnPgrpDescription_Object=MibTableColumn
a3mlnPgrpDescription=_A3mlnPgrpDescription_Object((1,3,6,1,4,1,43,2,23,7,1,11),_A3mlnPgrpDescription_Type())
a3mlnPgrpDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPgrpDescription.setStatus(_A)
_A3mlnGroupTable_Object=MibTable
a3mlnGroupTable=_A3mlnGroupTable_Object((1,3,6,1,4,1,43,2,23,8))
if mibBuilder.loadTexts:a3mlnGroupTable.setStatus(_A)
_A3mlnGroupEntry_Object=MibTableRow
a3mlnGroupEntry=_A3mlnGroupEntry_Object((1,3,6,1,4,1,43,2,23,8,1))
a3mlnGroupEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:a3mlnGroupEntry.setStatus(_A)
_A3mlnGrpPort_Type=Integer32
_A3mlnGrpPort_Object=MibTableColumn
a3mlnGrpPort=_A3mlnGrpPort_Object((1,3,6,1,4,1,43,2,23,8,1,1),_A3mlnGrpPort_Type())
a3mlnGrpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnGrpPort.setStatus(_A)
class _A3mlnGrpPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_K,2))
_A3mlnGrpPortType_Type.__name__=_C
_A3mlnGrpPortType_Object=MibTableColumn
a3mlnGrpPortType=_A3mlnGrpPortType_Object((1,3,6,1,4,1,43,2,23,8,1,2),_A3mlnGrpPortType_Type())
a3mlnGrpPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnGrpPortType.setStatus(_A)
class _A3mlnGrpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_A3mlnGrpPortState_Type.__name__=_C
_A3mlnGrpPortState_Object=MibTableColumn
a3mlnGrpPortState=_A3mlnGrpPortState_Object((1,3,6,1,4,1,43,2,23,8,1,3),_A3mlnGrpPortState_Type())
a3mlnGrpPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnGrpPortState.setStatus(_A)
_A3mlnGrpPrimaryPort_Type=Integer32
_A3mlnGrpPrimaryPort_Object=MibTableColumn
a3mlnGrpPrimaryPort=_A3mlnGrpPrimaryPort_Object((1,3,6,1,4,1,43,2,23,8,1,4),_A3mlnGrpPrimaryPort_Type())
a3mlnGrpPrimaryPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnGrpPrimaryPort.setStatus(_A)
class _A3mlnGrpOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_A3mlnGrpOwner_Type.__name__=_C
_A3mlnGrpOwner_Object=MibTableColumn
a3mlnGrpOwner=_A3mlnGrpOwner_Object((1,3,6,1,4,1,43,2,23,8,1,5),_A3mlnGrpOwner_Type())
a3mlnGrpOwner.setMaxAccess(_E)
if mibBuilder.loadTexts:a3mlnGrpOwner.setStatus(_A)
_A3mlnGrpMemberCount_Type=Integer32
_A3mlnGrpMemberCount_Object=MibTableColumn
a3mlnGrpMemberCount=_A3mlnGrpMemberCount_Object((1,3,6,1,4,1,43,2,23,8,1,6),_A3mlnGrpMemberCount_Type())
a3mlnGrpMemberCount.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnGrpMemberCount.setStatus(_A)
_A3mlnGrpFirstMember_Type=Integer32
_A3mlnGrpFirstMember_Object=MibTableColumn
a3mlnGrpFirstMember=_A3mlnGrpFirstMember_Object((1,3,6,1,4,1,43,2,23,8,1,7),_A3mlnGrpFirstMember_Type())
a3mlnGrpFirstMember.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnGrpFirstMember.setStatus(_A)
class _A3mlnGrpDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_A3mlnGrpDescription_Type.__name__=_F
_A3mlnGrpDescription_Object=MibTableColumn
a3mlnGrpDescription=_A3mlnGrpDescription_Object((1,3,6,1,4,1,43,2,23,8,1,8),_A3mlnGrpDescription_Type())
a3mlnGrpDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:a3mlnGrpDescription.setStatus(_A)
_A3mlnGrpEntryStatus_Type=RowStatus
_A3mlnGrpEntryStatus_Object=MibTableColumn
a3mlnGrpEntryStatus=_A3mlnGrpEntryStatus_Object((1,3,6,1,4,1,43,2,23,8,1,9),_A3mlnGrpEntryStatus_Type())
a3mlnGrpEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:a3mlnGrpEntryStatus.setStatus(_A)
_A3mlnMemberTable_Object=MibTable
a3mlnMemberTable=_A3mlnMemberTable_Object((1,3,6,1,4,1,43,2,23,9))
if mibBuilder.loadTexts:a3mlnMemberTable.setStatus(_A)
_A3mlnMemberEntry_Object=MibTableRow
a3mlnMemberEntry=_A3mlnMemberEntry_Object((1,3,6,1,4,1,43,2,23,9,1))
a3mlnMemberEntry.setIndexNames((0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:a3mlnMemberEntry.setStatus(_A)
_A3mlnMemGrpPort_Type=Integer32
_A3mlnMemGrpPort_Object=MibTableColumn
a3mlnMemGrpPort=_A3mlnMemGrpPort_Object((1,3,6,1,4,1,43,2,23,9,1,1),_A3mlnMemGrpPort_Type())
a3mlnMemGrpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnMemGrpPort.setStatus(_A)
_A3mlnMemPort_Type=Integer32
_A3mlnMemPort_Object=MibTableColumn
a3mlnMemPort=_A3mlnMemPort_Object((1,3,6,1,4,1,43,2,23,9,1,2),_A3mlnMemPort_Type())
a3mlnMemPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnMemPort.setStatus(_A)
class _A3mlnMemOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_L,4)))
_A3mlnMemOwner_Type.__name__=_C
_A3mlnMemOwner_Object=MibTableColumn
a3mlnMemOwner=_A3mlnMemOwner_Object((1,3,6,1,4,1,43,2,23,9,1,3),_A3mlnMemOwner_Type())
a3mlnMemOwner.setMaxAccess(_E)
if mibBuilder.loadTexts:a3mlnMemOwner.setStatus(_A)
_A3mlnMemEntryStatus_Type=RowStatus
_A3mlnMemEntryStatus_Object=MibTableColumn
a3mlnMemEntryStatus=_A3mlnMemEntryStatus_Object((1,3,6,1,4,1,43,2,23,9,1,4),_A3mlnMemEntryStatus_Type())
a3mlnMemEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:a3mlnMemEntryStatus.setStatus(_A)
_A3mlnStatistics_ObjectIdentity=ObjectIdentity
a3mlnStatistics=_A3mlnStatistics_ObjectIdentity((1,3,6,1,4,1,43,2,23,10))
_A3mlnStatSelGrpPort_Type=Integer32
_A3mlnStatSelGrpPort_Object=MibScalar
a3mlnStatSelGrpPort=_A3mlnStatSelGrpPort_Object((1,3,6,1,4,1,43,2,23,10,1),_A3mlnStatSelGrpPort_Type())
a3mlnStatSelGrpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnStatSelGrpPort.setStatus(_A)
_A3mlnStatSelMacAdr_Type=Integer32
_A3mlnStatSelMacAdr_Object=MibScalar
a3mlnStatSelMacAdr=_A3mlnStatSelMacAdr_Object((1,3,6,1,4,1,43,2,23,10,2),_A3mlnStatSelMacAdr_Type())
a3mlnStatSelMacAdr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnStatSelMacAdr.setStatus(_A)
_A3mlnPortStatTable_Object=MibTable
a3mlnPortStatTable=_A3mlnPortStatTable_Object((1,3,6,1,4,1,43,2,23,10,3))
if mibBuilder.loadTexts:a3mlnPortStatTable.setStatus(_A)
_A3mlnPortStatEntry_Object=MibTableRow
a3mlnPortStatEntry=_A3mlnPortStatEntry_Object((1,3,6,1,4,1,43,2,23,10,3,1))
a3mlnPortStatEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:a3mlnPortStatEntry.setStatus(_A)
_A3mlnPStatIndex_Type=Integer32
_A3mlnPStatIndex_Object=MibTableColumn
a3mlnPStatIndex=_A3mlnPStatIndex_Object((1,3,6,1,4,1,43,2,23,10,3,1,1),_A3mlnPStatIndex_Type())
a3mlnPStatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPStatIndex.setStatus(_A)
_A3mlnPStatRcvd_Type=Integer32
_A3mlnPStatRcvd_Object=MibTableColumn
a3mlnPStatRcvd=_A3mlnPStatRcvd_Object((1,3,6,1,4,1,43,2,23,10,3,1,2),_A3mlnPStatRcvd_Type())
a3mlnPStatRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPStatRcvd.setStatus(_A)
_A3mlnPStatXmit_Type=Integer32
_A3mlnPStatXmit_Object=MibTableColumn
a3mlnPStatXmit=_A3mlnPStatXmit_Object((1,3,6,1,4,1,43,2,23,10,3,1,3),_A3mlnPStatXmit_Type())
a3mlnPStatXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPStatXmit.setStatus(_A)
_A3mlnPStatStaMoveFrom_Type=Integer32
_A3mlnPStatStaMoveFrom_Object=MibTableColumn
a3mlnPStatStaMoveFrom=_A3mlnPStatStaMoveFrom_Object((1,3,6,1,4,1,43,2,23,10,3,1,4),_A3mlnPStatStaMoveFrom_Type())
a3mlnPStatStaMoveFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPStatStaMoveFrom.setStatus(_A)
_A3mlnPStatStaMoveTo_Type=Integer32
_A3mlnPStatStaMoveTo_Object=MibTableColumn
a3mlnPStatStaMoveTo=_A3mlnPStatStaMoveTo_Object((1,3,6,1,4,1,43,2,23,10,3,1,5),_A3mlnPStatStaMoveTo_Type())
a3mlnPStatStaMoveTo.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPStatStaMoveTo.setStatus(_A)
_A3mlnPStatSTAchange_Type=Integer32
_A3mlnPStatSTAchange_Object=MibTableColumn
a3mlnPStatSTAchange=_A3mlnPStatSTAchange_Object((1,3,6,1,4,1,43,2,23,10,3,1,6),_A3mlnPStatSTAchange_Type())
a3mlnPStatSTAchange.setMaxAccess(_B)
if mibBuilder.loadTexts:a3mlnPStatSTAchange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'RowStatus':RowStatus,'a3Com':a3Com,'brouterMIB':brouterMIB,'a3ComMLN':a3ComMLN,'a3mlnMaxPorts':a3mlnMaxPorts,'a3mlnMaxPhyPorts':a3mlnMaxPhyPorts,'a3mlnCCSsaveErr':a3mlnCCSsaveErr,'a3mlnCCSdelErr':a3mlnCCSdelErr,'a3mlnSetStatus':a3mlnSetStatus,'a3mlnSetMsg':a3mlnSetMsg,'a3mlnPortTable':a3mlnPortTable,'a3mlnPortEntry':a3mlnPortEntry,_J:a3mlnPindex,'a3mlnPtype':a3mlnPtype,'a3mlnPowner':a3mlnPowner,'a3mlnPlink':a3mlnPlink,'a3mlnPstState':a3mlnPstState,'a3mlnPtbState':a3mlnPtbState,'a3mlnPgrpPrimaryPort':a3mlnPgrpPrimaryPort,'a3mlnPgrpSrcAdrPort':a3mlnPgrpSrcAdrPort,'a3mlnPgrpSrcAdrMedia':a3mlnPgrpSrcAdrMedia,'a3mlnPgrpSrcAdrValue':a3mlnPgrpSrcAdrValue,'a3mlnPgrpDescription':a3mlnPgrpDescription,'a3mlnGroupTable':a3mlnGroupTable,'a3mlnGroupEntry':a3mlnGroupEntry,_N:a3mlnGrpPort,'a3mlnGrpPortType':a3mlnGrpPortType,'a3mlnGrpPortState':a3mlnGrpPortState,'a3mlnGrpPrimaryPort':a3mlnGrpPrimaryPort,'a3mlnGrpOwner':a3mlnGrpOwner,'a3mlnGrpMemberCount':a3mlnGrpMemberCount,'a3mlnGrpFirstMember':a3mlnGrpFirstMember,'a3mlnGrpDescription':a3mlnGrpDescription,'a3mlnGrpEntryStatus':a3mlnGrpEntryStatus,'a3mlnMemberTable':a3mlnMemberTable,'a3mlnMemberEntry':a3mlnMemberEntry,_O:a3mlnMemGrpPort,_P:a3mlnMemPort,'a3mlnMemOwner':a3mlnMemOwner,'a3mlnMemEntryStatus':a3mlnMemEntryStatus,'a3mlnStatistics':a3mlnStatistics,'a3mlnStatSelGrpPort':a3mlnStatSelGrpPort,'a3mlnStatSelMacAdr':a3mlnStatSelMacAdr,'a3mlnPortStatTable':a3mlnPortStatTable,'a3mlnPortStatEntry':a3mlnPortStatEntry,_Q:a3mlnPStatIndex,'a3mlnPStatRcvd':a3mlnPStatRcvd,'a3mlnPStatXmit':a3mlnPStatXmit,'a3mlnPStatStaMoveFrom':a3mlnPStatStaMoveFrom,'a3mlnPStatStaMoveTo':a3mlnPStatStaMoveTo,'a3mlnPStatSTAchange':a3mlnPStatSTAchange})