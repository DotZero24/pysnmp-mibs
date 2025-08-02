_E='TruthValue'
_D='IpAddress'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('Dell-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_D,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_E)
_RlOpenFlow_ObjectIdentity=ObjectIdentity
rlOpenFlow=_RlOpenFlow_ObjectIdentity((1,3,6,1,4,1,89,319))
_RlOpenFlowSupported_Type=TruthValue
_RlOpenFlowSupported_Object=MibScalar
rlOpenFlowSupported=_RlOpenFlowSupported_Object((1,3,6,1,4,1,89,319,1),_RlOpenFlowSupported_Type())
rlOpenFlowSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpenFlowSupported.setStatus(_A)
class _RlOpenFlowTcpPort_Type(Integer32):defaultValue=6633
_RlOpenFlowTcpPort_Type.__name__=_C
_RlOpenFlowTcpPort_Object=MibScalar
rlOpenFlowTcpPort=_RlOpenFlowTcpPort_Object((1,3,6,1,4,1,89,319,2),_RlOpenFlowTcpPort_Type())
rlOpenFlowTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpenFlowTcpPort.setStatus(_A)
class _RlOpenFlowServerIpAddr_Type(IpAddress):defaultHexValue='00000000'
_RlOpenFlowServerIpAddr_Type.__name__=_D
_RlOpenFlowServerIpAddr_Object=MibScalar
rlOpenFlowServerIpAddr=_RlOpenFlowServerIpAddr_Object((1,3,6,1,4,1,89,319,3),_RlOpenFlowServerIpAddr_Type())
rlOpenFlowServerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpenFlowServerIpAddr.setStatus(_A)
class _RlOpenFlowProtocolType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('tcp',0),('tls',1)))
_RlOpenFlowProtocolType_Type.__name__=_C
_RlOpenFlowProtocolType_Object=MibScalar
rlOpenFlowProtocolType=_RlOpenFlowProtocolType_Object((1,3,6,1,4,1,89,319,4),_RlOpenFlowProtocolType_Type())
rlOpenFlowProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpenFlowProtocolType.setStatus(_A)
class _RlOpenFlowDefaultForwardAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forward',0),('drop',1),('toController',2)))
_RlOpenFlowDefaultForwardAction_Type.__name__=_C
_RlOpenFlowDefaultForwardAction_Object=MibScalar
rlOpenFlowDefaultForwardAction=_RlOpenFlowDefaultForwardAction_Object((1,3,6,1,4,1,89,319,5),_RlOpenFlowDefaultForwardAction_Type())
rlOpenFlowDefaultForwardAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpenFlowDefaultForwardAction.setStatus(_A)
_RlOpenFlowEnable_Type=TruthValue
_RlOpenFlowEnable_Object=MibScalar
rlOpenFlowEnable=_RlOpenFlowEnable_Object((1,3,6,1,4,1,89,319,6),_RlOpenFlowEnable_Type())
rlOpenFlowEnable.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlOpenFlowEnable.setStatus(_A)
class _RlOpenFlowEnableAfterReset_Type(TruthValue):defaultValue=2
_RlOpenFlowEnableAfterReset_Type.__name__=_E
_RlOpenFlowEnableAfterReset_Object=MibScalar
rlOpenFlowEnableAfterReset=_RlOpenFlowEnableAfterReset_Object((1,3,6,1,4,1,89,319,7),_RlOpenFlowEnableAfterReset_Type())
rlOpenFlowEnableAfterReset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpenFlowEnableAfterReset.setStatus(_A)
mibBuilder.exportSymbols('Dell-openflow-MIB',**{'rlOpenFlow':rlOpenFlow,'rlOpenFlowSupported':rlOpenFlowSupported,'rlOpenFlowTcpPort':rlOpenFlowTcpPort,'rlOpenFlowServerIpAddr':rlOpenFlowServerIpAddr,'rlOpenFlowProtocolType':rlOpenFlowProtocolType,'rlOpenFlowDefaultForwardAction':rlOpenFlowDefaultForwardAction,'rlOpenFlowEnable':rlOpenFlowEnable,'rlOpenFlowEnableAfterReset':rlOpenFlowEnableAfterReset})