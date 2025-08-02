_R='extremeQosCapabilitiesEntry'
_Q='read-write'
_P='deprecated'
_O='ffffffff'
_N='00000000'
_M='extremeQosRuleIndex'
_L='DisplayString'
_K='Counter64'
_J='OwnerString'
_I='any'
_H='EXTREME-PBQOS-MIB'
_G='OctetString'
_F='read-only'
_E='IpAddress'
_D='L4Port'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
L4Port,PortList,extremeAgent=mibBuilder.importSymbols('EXTREME-BASE-MIB',_D,'PortList','extremeAgent')
ifEntry,=mibBuilder.importSymbols('IF-MIB','ifEntry')
OwnerString,=mibBuilder.importSymbols('RMON-MIB',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32',_K,'Gauge32',_C,_E,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','RowStatus','TextualConvention','TruthValue')
extremeQosPolicy=ModuleIdentity((1,3,6,1,4,1,1916,1,7))
_ExtremeNextAvailableQosRuleIndex_Type=Integer32
_ExtremeNextAvailableQosRuleIndex_Object=MibScalar
extremeNextAvailableQosRuleIndex=_ExtremeNextAvailableQosRuleIndex_Object((1,3,6,1,4,1,1916,1,7,1),_ExtremeNextAvailableQosRuleIndex_Type())
extremeNextAvailableQosRuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeNextAvailableQosRuleIndex.setStatus(_A)
_ExtremeQosRuleTable_Object=MibTable
extremeQosRuleTable=_ExtremeQosRuleTable_Object((1,3,6,1,4,1,1916,1,7,2))
if mibBuilder.loadTexts:extremeQosRuleTable.setStatus(_A)
_ExtremeQosRuleEntry_Object=MibTableRow
extremeQosRuleEntry=_ExtremeQosRuleEntry_Object((1,3,6,1,4,1,1916,1,7,2,1))
extremeQosRuleEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:extremeQosRuleEntry.setStatus(_A)
_ExtremeQosRuleIndex_Type=Integer32
_ExtremeQosRuleIndex_Object=MibTableColumn
extremeQosRuleIndex=_ExtremeQosRuleIndex_Object((1,3,6,1,4,1,1916,1,7,2,1,1),_ExtremeQosRuleIndex_Type())
extremeQosRuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleIndex.setStatus(_A)
class _ExtremeQosRuleScope_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('signaled',2),('inband',3)))
_ExtremeQosRuleScope_Type.__name__=_C
_ExtremeQosRuleScope_Object=MibTableColumn
extremeQosRuleScope=_ExtremeQosRuleScope_Object((1,3,6,1,4,1,1916,1,7,2,1,2),_ExtremeQosRuleScope_Type())
extremeQosRuleScope.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleScope.setStatus(_A)
class _ExtremeQosRuleDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('forward',2),('backward',3)))
_ExtremeQosRuleDirection_Type.__name__=_C
_ExtremeQosRuleDirection_Object=MibTableColumn
extremeQosRuleDirection=_ExtremeQosRuleDirection_Object((1,3,6,1,4,1,1916,1,7,2,1,3),_ExtremeQosRuleDirection_Type())
extremeQosRuleDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleDirection.setStatus(_A)
class _ExtremeQosRuleInPort_Type(Integer32):defaultValue=0
_ExtremeQosRuleInPort_Type.__name__=_C
_ExtremeQosRuleInPort_Object=MibTableColumn
extremeQosRuleInPort=_ExtremeQosRuleInPort_Object((1,3,6,1,4,1,1916,1,7,2,1,4),_ExtremeQosRuleInPort_Type())
extremeQosRuleInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleInPort.setStatus(_A)
_ExtremeQosRuleInPortMask_Type=PortList
_ExtremeQosRuleInPortMask_Object=MibTableColumn
extremeQosRuleInPortMask=_ExtremeQosRuleInPortMask_Object((1,3,6,1,4,1,1916,1,7,2,1,5),_ExtremeQosRuleInPortMask_Type())
extremeQosRuleInPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleInPortMask.setStatus(_A)
class _ExtremeQosRuleDestAddrStart_Type(IpAddress):defaultHexValue=_N
_ExtremeQosRuleDestAddrStart_Type.__name__=_E
_ExtremeQosRuleDestAddrStart_Object=MibTableColumn
extremeQosRuleDestAddrStart=_ExtremeQosRuleDestAddrStart_Object((1,3,6,1,4,1,1916,1,7,2,1,6),_ExtremeQosRuleDestAddrStart_Type())
extremeQosRuleDestAddrStart.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleDestAddrStart.setStatus(_A)
class _ExtremeQosRuleDestAddrEnd_Type(IpAddress):defaultHexValue=_O
_ExtremeQosRuleDestAddrEnd_Type.__name__=_E
_ExtremeQosRuleDestAddrEnd_Object=MibTableColumn
extremeQosRuleDestAddrEnd=_ExtremeQosRuleDestAddrEnd_Object((1,3,6,1,4,1,1916,1,7,2,1,7),_ExtremeQosRuleDestAddrEnd_Type())
extremeQosRuleDestAddrEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleDestAddrEnd.setStatus(_A)
class _ExtremeQosRuleSrcAddrStart_Type(IpAddress):defaultHexValue=_N
_ExtremeQosRuleSrcAddrStart_Type.__name__=_E
_ExtremeQosRuleSrcAddrStart_Object=MibTableColumn
extremeQosRuleSrcAddrStart=_ExtremeQosRuleSrcAddrStart_Object((1,3,6,1,4,1,1916,1,7,2,1,8),_ExtremeQosRuleSrcAddrStart_Type())
extremeQosRuleSrcAddrStart.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleSrcAddrStart.setStatus(_A)
class _ExtremeQosRuleSrcAddrEnd_Type(IpAddress):defaultHexValue=_O
_ExtremeQosRuleSrcAddrEnd_Type.__name__=_E
_ExtremeQosRuleSrcAddrEnd_Object=MibTableColumn
extremeQosRuleSrcAddrEnd=_ExtremeQosRuleSrcAddrEnd_Object((1,3,6,1,4,1,1916,1,7,2,1,9),_ExtremeQosRuleSrcAddrEnd_Type())
extremeQosRuleSrcAddrEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleSrcAddrEnd.setStatus(_A)
class _ExtremeQosRuleProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),('udp',2),('tcp',3),('other',4),('tcpPermitEstablished',5),('icmp',6)))
_ExtremeQosRuleProtocol_Type.__name__=_C
_ExtremeQosRuleProtocol_Object=MibTableColumn
extremeQosRuleProtocol=_ExtremeQosRuleProtocol_Object((1,3,6,1,4,1,1916,1,7,2,1,10),_ExtremeQosRuleProtocol_Type())
extremeQosRuleProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleProtocol.setStatus(_A)
class _ExtremeQosRuleDestL4PortStart_Type(L4Port):defaultValue=0
_ExtremeQosRuleDestL4PortStart_Type.__name__=_D
_ExtremeQosRuleDestL4PortStart_Object=MibTableColumn
extremeQosRuleDestL4PortStart=_ExtremeQosRuleDestL4PortStart_Object((1,3,6,1,4,1,1916,1,7,2,1,11),_ExtremeQosRuleDestL4PortStart_Type())
extremeQosRuleDestL4PortStart.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleDestL4PortStart.setStatus(_A)
class _ExtremeQosRuleSourceL4PortStart_Type(L4Port):defaultValue=0
_ExtremeQosRuleSourceL4PortStart_Type.__name__=_D
_ExtremeQosRuleSourceL4PortStart_Object=MibTableColumn
extremeQosRuleSourceL4PortStart=_ExtremeQosRuleSourceL4PortStart_Object((1,3,6,1,4,1,1916,1,7,2,1,12),_ExtremeQosRuleSourceL4PortStart_Type())
extremeQosRuleSourceL4PortStart.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleSourceL4PortStart.setStatus(_A)
class _ExtremeQosRuleTosMask_Type(OctetString):defaultHexValue='00';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_ExtremeQosRuleTosMask_Type.__name__=_G
_ExtremeQosRuleTosMask_Object=MibTableColumn
extremeQosRuleTosMask=_ExtremeQosRuleTosMask_Object((1,3,6,1,4,1,1916,1,7,2,1,13),_ExtremeQosRuleTosMask_Type())
extremeQosRuleTosMask.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleTosMask.setStatus(_P)
class _ExtremeQosRuleTosMatch_Type(OctetString):defaultHexValue='00';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_ExtremeQosRuleTosMatch_Type.__name__=_G
_ExtremeQosRuleTosMatch_Object=MibTableColumn
extremeQosRuleTosMatch=_ExtremeQosRuleTosMatch_Object((1,3,6,1,4,1,1916,1,7,2,1,14),_ExtremeQosRuleTosMatch_Type())
extremeQosRuleTosMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleTosMatch.setStatus(_P)
class _ExtremeQosRuleQosProfileIndex_Type(Integer32):defaultValue=1
_ExtremeQosRuleQosProfileIndex_Type.__name__=_C
_ExtremeQosRuleQosProfileIndex_Object=MibTableColumn
extremeQosRuleQosProfileIndex=_ExtremeQosRuleQosProfileIndex_Object((1,3,6,1,4,1,1916,1,7,2,1,15),_ExtremeQosRuleQosProfileIndex_Type())
extremeQosRuleQosProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleQosProfileIndex.setStatus(_A)
class _ExtremeQosRuleOwner_Type(OwnerString):subtypeSpec=OwnerString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeQosRuleOwner_Type.__name__=_J
_ExtremeQosRuleOwner_Object=MibTableColumn
extremeQosRuleOwner=_ExtremeQosRuleOwner_Object((1,3,6,1,4,1,1916,1,7,2,1,16),_ExtremeQosRuleOwner_Type())
extremeQosRuleOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleOwner.setStatus(_A)
_ExtremeQosRuleRowStatus_Type=RowStatus
_ExtremeQosRuleRowStatus_Object=MibTableColumn
extremeQosRuleRowStatus=_ExtremeQosRuleRowStatus_Object((1,3,6,1,4,1,1916,1,7,2,1,17),_ExtremeQosRuleRowStatus_Type())
extremeQosRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleRowStatus.setStatus(_A)
class _ExtremeQosRuleDestL4PortEnd_Type(L4Port):defaultValue=0
_ExtremeQosRuleDestL4PortEnd_Type.__name__=_D
_ExtremeQosRuleDestL4PortEnd_Object=MibTableColumn
extremeQosRuleDestL4PortEnd=_ExtremeQosRuleDestL4PortEnd_Object((1,3,6,1,4,1,1916,1,7,2,1,18),_ExtremeQosRuleDestL4PortEnd_Type())
extremeQosRuleDestL4PortEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleDestL4PortEnd.setStatus(_A)
class _ExtremeQosRuleSourceL4PortEnd_Type(L4Port):defaultValue=0
_ExtremeQosRuleSourceL4PortEnd_Type.__name__=_D
_ExtremeQosRuleSourceL4PortEnd_Object=MibTableColumn
extremeQosRuleSourceL4PortEnd=_ExtremeQosRuleSourceL4PortEnd_Object((1,3,6,1,4,1,1916,1,7,2,1,19),_ExtremeQosRuleSourceL4PortEnd_Type())
extremeQosRuleSourceL4PortEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleSourceL4PortEnd.setStatus(_A)
class _ExtremeQosRulePrecedence_Type(Integer32):defaultValue=0
_ExtremeQosRulePrecedence_Type.__name__=_C
_ExtremeQosRulePrecedence_Object=MibTableColumn
extremeQosRulePrecedence=_ExtremeQosRulePrecedence_Object((1,3,6,1,4,1,1916,1,7,2,1,20),_ExtremeQosRulePrecedence_Type())
extremeQosRulePrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRulePrecedence.setStatus(_A)
class _ExtremeQosRuleCounter_Type(Counter64):defaultValue=0
_ExtremeQosRuleCounter_Type.__name__=_K
_ExtremeQosRuleCounter_Object=MibTableColumn
extremeQosRuleCounter=_ExtremeQosRuleCounter_Object((1,3,6,1,4,1,1916,1,7,2,1,21),_ExtremeQosRuleCounter_Type())
extremeQosRuleCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeQosRuleCounter.setStatus(_A)
class _ExtremeQosRuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeQosRuleName_Type.__name__=_L
_ExtremeQosRuleName_Object=MibTableColumn
extremeQosRuleName=_ExtremeQosRuleName_Object((1,3,6,1,4,1,1916,1,7,2,1,22),_ExtremeQosRuleName_Type())
extremeQosRuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeQosRuleName.setStatus(_A)
_ExtremeQosCapabilitiesTable_Object=MibTable
extremeQosCapabilitiesTable=_ExtremeQosCapabilitiesTable_Object((1,3,6,1,4,1,1916,1,7,3))
if mibBuilder.loadTexts:extremeQosCapabilitiesTable.setStatus(_A)
_ExtremeQosCapabilitiesEntry_Object=MibTableRow
extremeQosCapabilitiesEntry=_ExtremeQosCapabilitiesEntry_Object((1,3,6,1,4,1,1916,1,7,3,1))
if mibBuilder.loadTexts:extremeQosCapabilitiesEntry.setStatus(_A)
_ExtremeQosCapMarkIpTosCapable_Type=TruthValue
_ExtremeQosCapMarkIpTosCapable_Object=MibTableColumn
extremeQosCapMarkIpTosCapable=_ExtremeQosCapMarkIpTosCapable_Object((1,3,6,1,4,1,1916,1,7,3,1,1),_ExtremeQosCapMarkIpTosCapable_Type())
extremeQosCapMarkIpTosCapable.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeQosCapMarkIpTosCapable.setStatus(_A)
_ExtremeQosCapMatchIpTosCapable_Type=TruthValue
_ExtremeQosCapMatchIpTosCapable_Object=MibTableColumn
extremeQosCapMatchIpTosCapable=_ExtremeQosCapMatchIpTosCapable_Object((1,3,6,1,4,1,1916,1,7,3,1,2),_ExtremeQosCapMatchIpTosCapable_Type())
extremeQosCapMatchIpTosCapable.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeQosCapMatchIpTosCapable.setStatus(_A)
_ExtremeQosClearIPFdb_Type=TruthValue
_ExtremeQosClearIPFdb_Object=MibScalar
extremeQosClearIPFdb=_ExtremeQosClearIPFdb_Object((1,3,6,1,4,1,1916,1,7,4),_ExtremeQosClearIPFdb_Type())
extremeQosClearIPFdb.setMaxAccess(_Q)
if mibBuilder.loadTexts:extremeQosClearIPFdb.setStatus(_A)
_ExtremeQosClearFdb_Type=TruthValue
_ExtremeQosClearFdb_Object=MibScalar
extremeQosClearFdb=_ExtremeQosClearFdb_Object((1,3,6,1,4,1,1916,1,7,5),_ExtremeQosClearFdb_Type())
extremeQosClearFdb.setMaxAccess(_Q)
if mibBuilder.loadTexts:extremeQosClearFdb.setStatus(_A)
ifEntry.registerAugmentions((_H,_R))
extremeQosCapabilitiesEntry.setIndexNames(*ifEntry.getIndexNames())
mibBuilder.exportSymbols(_H,**{'extremeQosPolicy':extremeQosPolicy,'extremeNextAvailableQosRuleIndex':extremeNextAvailableQosRuleIndex,'extremeQosRuleTable':extremeQosRuleTable,'extremeQosRuleEntry':extremeQosRuleEntry,_M:extremeQosRuleIndex,'extremeQosRuleScope':extremeQosRuleScope,'extremeQosRuleDirection':extremeQosRuleDirection,'extremeQosRuleInPort':extremeQosRuleInPort,'extremeQosRuleInPortMask':extremeQosRuleInPortMask,'extremeQosRuleDestAddrStart':extremeQosRuleDestAddrStart,'extremeQosRuleDestAddrEnd':extremeQosRuleDestAddrEnd,'extremeQosRuleSrcAddrStart':extremeQosRuleSrcAddrStart,'extremeQosRuleSrcAddrEnd':extremeQosRuleSrcAddrEnd,'extremeQosRuleProtocol':extremeQosRuleProtocol,'extremeQosRuleDestL4PortStart':extremeQosRuleDestL4PortStart,'extremeQosRuleSourceL4PortStart':extremeQosRuleSourceL4PortStart,'extremeQosRuleTosMask':extremeQosRuleTosMask,'extremeQosRuleTosMatch':extremeQosRuleTosMatch,'extremeQosRuleQosProfileIndex':extremeQosRuleQosProfileIndex,'extremeQosRuleOwner':extremeQosRuleOwner,'extremeQosRuleRowStatus':extremeQosRuleRowStatus,'extremeQosRuleDestL4PortEnd':extremeQosRuleDestL4PortEnd,'extremeQosRuleSourceL4PortEnd':extremeQosRuleSourceL4PortEnd,'extremeQosRulePrecedence':extremeQosRulePrecedence,'extremeQosRuleCounter':extremeQosRuleCounter,'extremeQosRuleName':extremeQosRuleName,'extremeQosCapabilitiesTable':extremeQosCapabilitiesTable,_R:extremeQosCapabilitiesEntry,'extremeQosCapMarkIpTosCapable':extremeQosCapMarkIpTosCapable,'extremeQosCapMatchIpTosCapable':extremeQosCapMatchIpTosCapable,'extremeQosClearIPFdb':extremeQosClearIPFdb,'extremeQosClearFdb':extremeQosClearFdb})