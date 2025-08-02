_O='fastpathRoutePolicyIfName'
_N='fastpathRoutePolicyIfIndex'
_M='fastpathRoutePolicyStmtAction'
_L='fastpathRoutePolicyStmtSeqNum'
_K='fastpathRoutePolicyStmtName'
_J='fastpathRoutePolicySequence'
_I='fastpathRoutePolicyStmtActionType'
_H='fastpathRoutePolicyName'
_G='Unsigned32'
_F='not-accessible'
_E='DisplayString'
_D='read-create'
_C='NETGEAR-ROUTE-POLICY-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero','ifIndex')
fastPathRouting,=mibBuilder.importSymbols('NETGEAR-ROUTING-MIB','fastPathRouting')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TruthValue')
fastPathRoutePolicy=ModuleIdentity((1,3,6,1,4,1,4526,10,2,20))
class FastpathRoutePolicyAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
class FastpathRoutePolicyStmtIpPrecedence(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('routine',0),('priority',1),('immediate',2),('flash',3),('flash-override',4),('critical',5),('internet',6),('network',7),('invalid',8)))
_FastpathRoutePolicyNameTable_Object=MibTable
fastpathRoutePolicyNameTable=_FastpathRoutePolicyNameTable_Object((1,3,6,1,4,1,4526,10,2,20,1))
if mibBuilder.loadTexts:fastpathRoutePolicyNameTable.setStatus(_A)
_FastpathRoutePolicyNameEntry_Object=MibTableRow
fastpathRoutePolicyNameEntry=_FastpathRoutePolicyNameEntry_Object((1,3,6,1,4,1,4526,10,2,20,1,1))
fastpathRoutePolicyNameEntry.setIndexNames((0,_C,_H),(0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:fastpathRoutePolicyNameEntry.setStatus(_A)
class _FastpathRoutePolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FastpathRoutePolicyName_Type.__name__=_E
_FastpathRoutePolicyName_Object=MibTableColumn
fastpathRoutePolicyName=_FastpathRoutePolicyName_Object((1,3,6,1,4,1,4526,10,2,20,1,1,1),_FastpathRoutePolicyName_Type())
fastpathRoutePolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:fastpathRoutePolicyName.setStatus(_A)
_FastpathRoutePolicyStmtActionType_Type=FastpathRoutePolicyAction
_FastpathRoutePolicyStmtActionType_Object=MibTableColumn
fastpathRoutePolicyStmtActionType=_FastpathRoutePolicyStmtActionType_Object((1,3,6,1,4,1,4526,10,2,20,1,1,2),_FastpathRoutePolicyStmtActionType_Type())
fastpathRoutePolicyStmtActionType.setMaxAccess(_D)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtActionType.setStatus(_A)
class _FastpathRoutePolicySequence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FastpathRoutePolicySequence_Type.__name__=_G
_FastpathRoutePolicySequence_Object=MibTableColumn
fastpathRoutePolicySequence=_FastpathRoutePolicySequence_Object((1,3,6,1,4,1,4526,10,2,20,1,1,3),_FastpathRoutePolicySequence_Type())
fastpathRoutePolicySequence.setMaxAccess(_D)
if mibBuilder.loadTexts:fastpathRoutePolicySequence.setStatus(_A)
_FastpathRoutePolicyNameRowStatus_Type=RowStatus
_FastpathRoutePolicyNameRowStatus_Object=MibTableColumn
fastpathRoutePolicyNameRowStatus=_FastpathRoutePolicyNameRowStatus_Object((1,3,6,1,4,1,4526,10,2,20,1,1,4),_FastpathRoutePolicyNameRowStatus_Type())
fastpathRoutePolicyNameRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fastpathRoutePolicyNameRowStatus.setStatus(_A)
_FastpathRoutePolicyStamentTable_Object=MibTable
fastpathRoutePolicyStamentTable=_FastpathRoutePolicyStamentTable_Object((1,3,6,1,4,1,4526,10,2,20,2))
if mibBuilder.loadTexts:fastpathRoutePolicyStamentTable.setStatus(_A)
_FastpathRoutePolicyStatementEntry_Object=MibTableRow
fastpathRoutePolicyStatementEntry=_FastpathRoutePolicyStatementEntry_Object((1,3,6,1,4,1,4526,10,2,20,2,1))
fastpathRoutePolicyStatementEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:fastpathRoutePolicyStatementEntry.setStatus(_A)
class _FastpathRoutePolicyStmtName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_FastpathRoutePolicyStmtName_Type.__name__=_E
_FastpathRoutePolicyStmtName_Object=MibTableColumn
fastpathRoutePolicyStmtName=_FastpathRoutePolicyStmtName_Object((1,3,6,1,4,1,4526,10,2,20,2,1,1),_FastpathRoutePolicyStmtName_Type())
fastpathRoutePolicyStmtName.setMaxAccess(_F)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtName.setStatus(_A)
_FastpathRoutePolicyStmtSeqNum_Type=Unsigned32
_FastpathRoutePolicyStmtSeqNum_Object=MibTableColumn
fastpathRoutePolicyStmtSeqNum=_FastpathRoutePolicyStmtSeqNum_Object((1,3,6,1,4,1,4526,10,2,20,2,1,2),_FastpathRoutePolicyStmtSeqNum_Type())
fastpathRoutePolicyStmtSeqNum.setMaxAccess(_F)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtSeqNum.setStatus(_A)
_FastpathRoutePolicyStmtAction_Type=FastpathRoutePolicyAction
_FastpathRoutePolicyStmtAction_Object=MibTableColumn
fastpathRoutePolicyStmtAction=_FastpathRoutePolicyStmtAction_Object((1,3,6,1,4,1,4526,10,2,20,2,1,3),_FastpathRoutePolicyStmtAction_Type())
fastpathRoutePolicyStmtAction.setMaxAccess(_F)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtAction.setStatus(_A)
_FastpathRoutePolicyStmtMatchIpv4AclList_Type=DisplayString
_FastpathRoutePolicyStmtMatchIpv4AclList_Object=MibTableColumn
fastpathRoutePolicyStmtMatchIpv4AclList=_FastpathRoutePolicyStmtMatchIpv4AclList_Object((1,3,6,1,4,1,4526,10,2,20,2,1,4),_FastpathRoutePolicyStmtMatchIpv4AclList_Type())
fastpathRoutePolicyStmtMatchIpv4AclList.setMaxAccess(_B)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtMatchIpv4AclList.setStatus(_A)
_FastpathRoutePolicyStmtMatchIpv4AclDelList_Type=DisplayString
_FastpathRoutePolicyStmtMatchIpv4AclDelList_Object=MibTableColumn
fastpathRoutePolicyStmtMatchIpv4AclDelList=_FastpathRoutePolicyStmtMatchIpv4AclDelList_Object((1,3,6,1,4,1,4526,10,2,20,2,1,5),_FastpathRoutePolicyStmtMatchIpv4AclDelList_Type())
fastpathRoutePolicyStmtMatchIpv4AclDelList.setMaxAccess(_B)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtMatchIpv4AclDelList.setStatus(_A)
_FastpathRoutePolicyStmtMatchMacAclList_Type=DisplayString
_FastpathRoutePolicyStmtMatchMacAclList_Object=MibTableColumn
fastpathRoutePolicyStmtMatchMacAclList=_FastpathRoutePolicyStmtMatchMacAclList_Object((1,3,6,1,4,1,4526,10,2,20,2,1,6),_FastpathRoutePolicyStmtMatchMacAclList_Type())
fastpathRoutePolicyStmtMatchMacAclList.setMaxAccess(_B)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtMatchMacAclList.setStatus(_A)
_FastpathRoutePolicyStmtMatchMacAclDelList_Type=DisplayString
_FastpathRoutePolicyStmtMatchMacAclDelList_Object=MibTableColumn
fastpathRoutePolicyStmtMatchMacAclDelList=_FastpathRoutePolicyStmtMatchMacAclDelList_Object((1,3,6,1,4,1,4526,10,2,20,2,1,7),_FastpathRoutePolicyStmtMatchMacAclDelList_Type())
fastpathRoutePolicyStmtMatchMacAclDelList.setMaxAccess(_B)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtMatchMacAclDelList.setStatus(_A)
_FastpathRoutePolicyStmtMatchPacketLengthRangeMin_Type=Unsigned32
_FastpathRoutePolicyStmtMatchPacketLengthRangeMin_Object=MibTableColumn
fastpathRoutePolicyStmtMatchPacketLengthRangeMin=_FastpathRoutePolicyStmtMatchPacketLengthRangeMin_Object((1,3,6,1,4,1,4526,10,2,20,2,1,8),_FastpathRoutePolicyStmtMatchPacketLengthRangeMin_Type())
fastpathRoutePolicyStmtMatchPacketLengthRangeMin.setMaxAccess(_B)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtMatchPacketLengthRangeMin.setStatus(_A)
_FastpathRoutePolicyStmtMatchPacketLengthRangeMax_Type=Unsigned32
_FastpathRoutePolicyStmtMatchPacketLengthRangeMax_Object=MibTableColumn
fastpathRoutePolicyStmtMatchPacketLengthRangeMax=_FastpathRoutePolicyStmtMatchPacketLengthRangeMax_Object((1,3,6,1,4,1,4526,10,2,20,2,1,9),_FastpathRoutePolicyStmtMatchPacketLengthRangeMax_Type())
fastpathRoutePolicyStmtMatchPacketLengthRangeMax.setMaxAccess(_B)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtMatchPacketLengthRangeMax.setStatus(_A)
_FastpathRoutePolicyStmtSetIpNextHopList_Type=DisplayString
_FastpathRoutePolicyStmtSetIpNextHopList_Object=MibTableColumn
fastpathRoutePolicyStmtSetIpNextHopList=_FastpathRoutePolicyStmtSetIpNextHopList_Object((1,3,6,1,4,1,4526,10,2,20,2,1,10),_FastpathRoutePolicyStmtSetIpNextHopList_Type())
fastpathRoutePolicyStmtSetIpNextHopList.setMaxAccess(_B)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtSetIpNextHopList.setStatus(_A)
_FastpathRoutePolicyStmtSetIpNextHopDelList_Type=DisplayString
_FastpathRoutePolicyStmtSetIpNextHopDelList_Object=MibTableColumn
fastpathRoutePolicyStmtSetIpNextHopDelList=_FastpathRoutePolicyStmtSetIpNextHopDelList_Object((1,3,6,1,4,1,4526,10,2,20,2,1,11),_FastpathRoutePolicyStmtSetIpNextHopDelList_Type())
fastpathRoutePolicyStmtSetIpNextHopDelList.setMaxAccess(_B)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtSetIpNextHopDelList.setStatus(_A)
_FastpathRoutePolicyStmtSetDefaultIpNextHopList_Type=DisplayString
_FastpathRoutePolicyStmtSetDefaultIpNextHopList_Object=MibTableColumn
fastpathRoutePolicyStmtSetDefaultIpNextHopList=_FastpathRoutePolicyStmtSetDefaultIpNextHopList_Object((1,3,6,1,4,1,4526,10,2,20,2,1,12),_FastpathRoutePolicyStmtSetDefaultIpNextHopList_Type())
fastpathRoutePolicyStmtSetDefaultIpNextHopList.setMaxAccess(_B)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtSetDefaultIpNextHopList.setStatus(_A)
_FastpathRoutePolicyStmtSetDefaultIpNextHopDelList_Type=DisplayString
_FastpathRoutePolicyStmtSetDefaultIpNextHopDelList_Object=MibTableColumn
fastpathRoutePolicyStmtSetDefaultIpNextHopDelList=_FastpathRoutePolicyStmtSetDefaultIpNextHopDelList_Object((1,3,6,1,4,1,4526,10,2,20,2,1,13),_FastpathRoutePolicyStmtSetDefaultIpNextHopDelList_Type())
fastpathRoutePolicyStmtSetDefaultIpNextHopDelList.setMaxAccess(_B)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtSetDefaultIpNextHopDelList.setStatus(_A)
_FastpathRoutePolicyStmtSetIpPrecedence_Type=FastpathRoutePolicyStmtIpPrecedence
_FastpathRoutePolicyStmtSetIpPrecedence_Object=MibTableColumn
fastpathRoutePolicyStmtSetIpPrecedence=_FastpathRoutePolicyStmtSetIpPrecedence_Object((1,3,6,1,4,1,4526,10,2,20,2,1,14),_FastpathRoutePolicyStmtSetIpPrecedence_Type())
fastpathRoutePolicyStmtSetIpPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtSetIpPrecedence.setStatus(_A)
_FastpathRoutePolicyStmtSetIntfNull0_Type=TruthValue
_FastpathRoutePolicyStmtSetIntfNull0_Object=MibTableColumn
fastpathRoutePolicyStmtSetIntfNull0=_FastpathRoutePolicyStmtSetIntfNull0_Object((1,3,6,1,4,1,4526,10,2,20,2,1,15),_FastpathRoutePolicyStmtSetIntfNull0_Type())
fastpathRoutePolicyStmtSetIntfNull0.setMaxAccess(_B)
if mibBuilder.loadTexts:fastpathRoutePolicyStmtSetIntfNull0.setStatus(_A)
_FastpathRoutePolicyIfTable_Object=MibTable
fastpathRoutePolicyIfTable=_FastpathRoutePolicyIfTable_Object((1,3,6,1,4,1,4526,10,2,20,3))
if mibBuilder.loadTexts:fastpathRoutePolicyIfTable.setStatus(_A)
_FastpathRoutePolicyIfEntry_Object=MibTableRow
fastpathRoutePolicyIfEntry=_FastpathRoutePolicyIfEntry_Object((1,3,6,1,4,1,4526,10,2,20,3,1))
fastpathRoutePolicyIfEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:fastpathRoutePolicyIfEntry.setStatus(_A)
_FastpathRoutePolicyIfIndex_Type=InterfaceIndex
_FastpathRoutePolicyIfIndex_Object=MibTableColumn
fastpathRoutePolicyIfIndex=_FastpathRoutePolicyIfIndex_Object((1,3,6,1,4,1,4526,10,2,20,3,1,1),_FastpathRoutePolicyIfIndex_Type())
fastpathRoutePolicyIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fastpathRoutePolicyIfIndex.setStatus(_A)
class _FastpathRoutePolicyIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_FastpathRoutePolicyIfName_Type.__name__=_E
_FastpathRoutePolicyIfName_Object=MibTableColumn
fastpathRoutePolicyIfName=_FastpathRoutePolicyIfName_Object((1,3,6,1,4,1,4526,10,2,20,3,1,2),_FastpathRoutePolicyIfName_Type())
fastpathRoutePolicyIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:fastpathRoutePolicyIfName.setStatus(_A)
_FastpathRoutePolicyIfRowStatus_Type=RowStatus
_FastpathRoutePolicyIfRowStatus_Object=MibTableColumn
fastpathRoutePolicyIfRowStatus=_FastpathRoutePolicyIfRowStatus_Object((1,3,6,1,4,1,4526,10,2,20,3,1,3),_FastpathRoutePolicyIfRowStatus_Type())
fastpathRoutePolicyIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fastpathRoutePolicyIfRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FastpathRoutePolicyAction':FastpathRoutePolicyAction,'FastpathRoutePolicyStmtIpPrecedence':FastpathRoutePolicyStmtIpPrecedence,'fastPathRoutePolicy':fastPathRoutePolicy,'fastpathRoutePolicyNameTable':fastpathRoutePolicyNameTable,'fastpathRoutePolicyNameEntry':fastpathRoutePolicyNameEntry,_H:fastpathRoutePolicyName,_I:fastpathRoutePolicyStmtActionType,_J:fastpathRoutePolicySequence,'fastpathRoutePolicyNameRowStatus':fastpathRoutePolicyNameRowStatus,'fastpathRoutePolicyStamentTable':fastpathRoutePolicyStamentTable,'fastpathRoutePolicyStatementEntry':fastpathRoutePolicyStatementEntry,_K:fastpathRoutePolicyStmtName,_L:fastpathRoutePolicyStmtSeqNum,_M:fastpathRoutePolicyStmtAction,'fastpathRoutePolicyStmtMatchIpv4AclList':fastpathRoutePolicyStmtMatchIpv4AclList,'fastpathRoutePolicyStmtMatchIpv4AclDelList':fastpathRoutePolicyStmtMatchIpv4AclDelList,'fastpathRoutePolicyStmtMatchMacAclList':fastpathRoutePolicyStmtMatchMacAclList,'fastpathRoutePolicyStmtMatchMacAclDelList':fastpathRoutePolicyStmtMatchMacAclDelList,'fastpathRoutePolicyStmtMatchPacketLengthRangeMin':fastpathRoutePolicyStmtMatchPacketLengthRangeMin,'fastpathRoutePolicyStmtMatchPacketLengthRangeMax':fastpathRoutePolicyStmtMatchPacketLengthRangeMax,'fastpathRoutePolicyStmtSetIpNextHopList':fastpathRoutePolicyStmtSetIpNextHopList,'fastpathRoutePolicyStmtSetIpNextHopDelList':fastpathRoutePolicyStmtSetIpNextHopDelList,'fastpathRoutePolicyStmtSetDefaultIpNextHopList':fastpathRoutePolicyStmtSetDefaultIpNextHopList,'fastpathRoutePolicyStmtSetDefaultIpNextHopDelList':fastpathRoutePolicyStmtSetDefaultIpNextHopDelList,'fastpathRoutePolicyStmtSetIpPrecedence':fastpathRoutePolicyStmtSetIpPrecedence,'fastpathRoutePolicyStmtSetIntfNull0':fastpathRoutePolicyStmtSetIntfNull0,'fastpathRoutePolicyIfTable':fastpathRoutePolicyIfTable,'fastpathRoutePolicyIfEntry':fastpathRoutePolicyIfEntry,_N:fastpathRoutePolicyIfIndex,_O:fastpathRoutePolicyIfName,'fastpathRoutePolicyIfRowStatus':fastpathRoutePolicyIfRowStatus})