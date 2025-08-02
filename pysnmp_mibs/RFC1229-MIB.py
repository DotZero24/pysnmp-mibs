_J='ifExtnsRcvAddress'
_I='ifExtnsRcvAddrIfIndex'
_H='read-write'
_G='ifExtnsTestIfIndex'
_F='ifExtnsIfIndex'
_E='DisplayString'
_D='Integer32'
_C='RFC1229-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_IfExtensions_ObjectIdentity=ObjectIdentity
ifExtensions=_IfExtensions_ObjectIdentity((1,3,6,1,3,6))
_IfExtnsTable_Object=MibTable
ifExtnsTable=_IfExtnsTable_Object((1,3,6,1,3,6,1))
if mibBuilder.loadTexts:ifExtnsTable.setStatus(_A)
_IfExtnsEntry_Object=MibTableRow
ifExtnsEntry=_IfExtnsEntry_Object((1,3,6,1,3,6,1,1))
ifExtnsEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:ifExtnsEntry.setStatus(_A)
_IfExtnsIfIndex_Type=Integer32
_IfExtnsIfIndex_Object=MibTableColumn
ifExtnsIfIndex=_IfExtnsIfIndex_Object((1,3,6,1,3,6,1,1,1),_IfExtnsIfIndex_Type())
ifExtnsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsIfIndex.setStatus(_A)
_IfExtnsChipSet_Type=ObjectIdentifier
_IfExtnsChipSet_Object=MibTableColumn
ifExtnsChipSet=_IfExtnsChipSet_Object((1,3,6,1,3,6,1,1,2),_IfExtnsChipSet_Type())
ifExtnsChipSet.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsChipSet.setStatus(_A)
class _IfExtnsRevWare_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IfExtnsRevWare_Type.__name__=_E
_IfExtnsRevWare_Object=MibTableColumn
ifExtnsRevWare=_IfExtnsRevWare_Object((1,3,6,1,3,6,1,1,3),_IfExtnsRevWare_Type())
ifExtnsRevWare.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsRevWare.setStatus(_A)
_IfExtnsMulticastsTransmittedOks_Type=Counter32
_IfExtnsMulticastsTransmittedOks_Object=MibTableColumn
ifExtnsMulticastsTransmittedOks=_IfExtnsMulticastsTransmittedOks_Object((1,3,6,1,3,6,1,1,4),_IfExtnsMulticastsTransmittedOks_Type())
ifExtnsMulticastsTransmittedOks.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsMulticastsTransmittedOks.setStatus(_A)
_IfExtnsBroadcastsTransmittedOks_Type=Counter32
_IfExtnsBroadcastsTransmittedOks_Object=MibTableColumn
ifExtnsBroadcastsTransmittedOks=_IfExtnsBroadcastsTransmittedOks_Object((1,3,6,1,3,6,1,1,5),_IfExtnsBroadcastsTransmittedOks_Type())
ifExtnsBroadcastsTransmittedOks.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsBroadcastsTransmittedOks.setStatus(_A)
_IfExtnsMulticastsReceivedOks_Type=Counter32
_IfExtnsMulticastsReceivedOks_Object=MibTableColumn
ifExtnsMulticastsReceivedOks=_IfExtnsMulticastsReceivedOks_Object((1,3,6,1,3,6,1,1,6),_IfExtnsMulticastsReceivedOks_Type())
ifExtnsMulticastsReceivedOks.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsMulticastsReceivedOks.setStatus(_A)
_IfExtnsBroadcastsReceivedOks_Type=Counter32
_IfExtnsBroadcastsReceivedOks_Object=MibTableColumn
ifExtnsBroadcastsReceivedOks=_IfExtnsBroadcastsReceivedOks_Object((1,3,6,1,3,6,1,1,7),_IfExtnsBroadcastsReceivedOks_Type())
ifExtnsBroadcastsReceivedOks.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsBroadcastsReceivedOks.setStatus(_A)
class _IfExtnsPromiscuous_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_IfExtnsPromiscuous_Type.__name__=_D
_IfExtnsPromiscuous_Object=MibTableColumn
ifExtnsPromiscuous=_IfExtnsPromiscuous_Object((1,3,6,1,3,6,1,1,8),_IfExtnsPromiscuous_Type())
ifExtnsPromiscuous.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsPromiscuous.setStatus(_A)
_IfExtnsTestTable_Object=MibTable
ifExtnsTestTable=_IfExtnsTestTable_Object((1,3,6,1,3,6,2))
if mibBuilder.loadTexts:ifExtnsTestTable.setStatus(_A)
_IfExtnsTestEntry_Object=MibTableRow
ifExtnsTestEntry=_IfExtnsTestEntry_Object((1,3,6,1,3,6,2,1))
ifExtnsTestEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:ifExtnsTestEntry.setStatus(_A)
_IfExtnsTestIfIndex_Type=Integer32
_IfExtnsTestIfIndex_Object=MibTableColumn
ifExtnsTestIfIndex=_IfExtnsTestIfIndex_Object((1,3,6,1,3,6,2,1,1),_IfExtnsTestIfIndex_Type())
ifExtnsTestIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsTestIfIndex.setStatus(_A)
_IfExtnsTestCommunity_Type=OctetString
_IfExtnsTestCommunity_Object=MibTableColumn
ifExtnsTestCommunity=_IfExtnsTestCommunity_Object((1,3,6,1,3,6,2,1,2),_IfExtnsTestCommunity_Type())
ifExtnsTestCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsTestCommunity.setStatus(_A)
_IfExtnsTestRequestId_Type=Integer32
_IfExtnsTestRequestId_Object=MibTableColumn
ifExtnsTestRequestId=_IfExtnsTestRequestId_Object((1,3,6,1,3,6,2,1,3),_IfExtnsTestRequestId_Type())
ifExtnsTestRequestId.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsTestRequestId.setStatus(_A)
_IfExtnsTestType_Type=ObjectIdentifier
_IfExtnsTestType_Object=MibTableColumn
ifExtnsTestType=_IfExtnsTestType_Object((1,3,6,1,3,6,2,1,4),_IfExtnsTestType_Type())
ifExtnsTestType.setMaxAccess(_H)
if mibBuilder.loadTexts:ifExtnsTestType.setStatus(_A)
class _IfExtnsTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('success',2),('inProgress',3),('notSupported',4),('unAbleToRun',5),('aborted',6),('failed',7)))
_IfExtnsTestResult_Type.__name__=_D
_IfExtnsTestResult_Object=MibTableColumn
ifExtnsTestResult=_IfExtnsTestResult_Object((1,3,6,1,3,6,2,1,5),_IfExtnsTestResult_Type())
ifExtnsTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsTestResult.setStatus(_A)
_IfExtnsTestCode_Type=ObjectIdentifier
_IfExtnsTestCode_Object=MibTableColumn
ifExtnsTestCode=_IfExtnsTestCode_Object((1,3,6,1,3,6,2,1,6),_IfExtnsTestCode_Type())
ifExtnsTestCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsTestCode.setStatus(_A)
_IfExtnsRcvAddrTable_Object=MibTable
ifExtnsRcvAddrTable=_IfExtnsRcvAddrTable_Object((1,3,6,1,3,6,3))
if mibBuilder.loadTexts:ifExtnsRcvAddrTable.setStatus(_A)
_IfExtnsRcvAddrEntry_Object=MibTableRow
ifExtnsRcvAddrEntry=_IfExtnsRcvAddrEntry_Object((1,3,6,1,3,6,3,1))
ifExtnsRcvAddrEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:ifExtnsRcvAddrEntry.setStatus(_A)
_IfExtnsRcvAddrIfIndex_Type=Integer32
_IfExtnsRcvAddrIfIndex_Object=MibTableColumn
ifExtnsRcvAddrIfIndex=_IfExtnsRcvAddrIfIndex_Object((1,3,6,1,3,6,3,1,1),_IfExtnsRcvAddrIfIndex_Type())
ifExtnsRcvAddrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsRcvAddrIfIndex.setStatus(_A)
_IfExtnsRcvAddress_Type=PhysAddress
_IfExtnsRcvAddress_Object=MibTableColumn
ifExtnsRcvAddress=_IfExtnsRcvAddress_Object((1,3,6,1,3,6,3,1,2),_IfExtnsRcvAddress_Type())
ifExtnsRcvAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtnsRcvAddress.setStatus(_A)
class _IfExtnsRcvAddrStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('invalid',2),('volatile',3),('nonVolatile',4)))
_IfExtnsRcvAddrStatus_Type.__name__=_D
_IfExtnsRcvAddrStatus_Object=MibTableColumn
ifExtnsRcvAddrStatus=_IfExtnsRcvAddrStatus_Object((1,3,6,1,3,6,3,1,3),_IfExtnsRcvAddrStatus_Type())
ifExtnsRcvAddrStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:ifExtnsRcvAddrStatus.setStatus(_A)
_WellKnownTests_ObjectIdentity=ObjectIdentity
wellKnownTests=_WellKnownTests_ObjectIdentity((1,3,6,1,3,6,4))
_TestFullDuplexLoopBack_ObjectIdentity=ObjectIdentity
testFullDuplexLoopBack=_TestFullDuplexLoopBack_ObjectIdentity((1,3,6,1,3,6,4,1))
mibBuilder.exportSymbols(_C,**{'ifExtensions':ifExtensions,'ifExtnsTable':ifExtnsTable,'ifExtnsEntry':ifExtnsEntry,_F:ifExtnsIfIndex,'ifExtnsChipSet':ifExtnsChipSet,'ifExtnsRevWare':ifExtnsRevWare,'ifExtnsMulticastsTransmittedOks':ifExtnsMulticastsTransmittedOks,'ifExtnsBroadcastsTransmittedOks':ifExtnsBroadcastsTransmittedOks,'ifExtnsMulticastsReceivedOks':ifExtnsMulticastsReceivedOks,'ifExtnsBroadcastsReceivedOks':ifExtnsBroadcastsReceivedOks,'ifExtnsPromiscuous':ifExtnsPromiscuous,'ifExtnsTestTable':ifExtnsTestTable,'ifExtnsTestEntry':ifExtnsTestEntry,_G:ifExtnsTestIfIndex,'ifExtnsTestCommunity':ifExtnsTestCommunity,'ifExtnsTestRequestId':ifExtnsTestRequestId,'ifExtnsTestType':ifExtnsTestType,'ifExtnsTestResult':ifExtnsTestResult,'ifExtnsTestCode':ifExtnsTestCode,'ifExtnsRcvAddrTable':ifExtnsRcvAddrTable,'ifExtnsRcvAddrEntry':ifExtnsRcvAddrEntry,_I:ifExtnsRcvAddrIfIndex,_J:ifExtnsRcvAddress,'ifExtnsRcvAddrStatus':ifExtnsRcvAddrStatus,'wellKnownTests':wellKnownTests,'testFullDuplexLoopBack':testFullDuplexLoopBack})